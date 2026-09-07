import os
import secrets
import sqlite3
import time
from email.parser import BytesParser
from email.policy import default
from flask import Flask, jsonify, request

DB = os.getenv("TEMPMAIL_DB", "tempmail.db")
DOMAIN = os.getenv("TEMPMAIL_DOMAIN", "example.com")
TTL = int(os.getenv("TEMPMAIL_TTL", "86400"))
API_TOKEN = os.getenv("TEMPMAIL_API_TOKEN", "")
INTERNAL_KEY = os.getenv("TEMPMAIL_INTERNAL_KEY", "")

app = Flask(__name__)

def db():
    c = sqlite3.connect(DB)
    c.row_factory = sqlite3.Row
    return c

def init():
    c = db()
    c.execute("CREATE TABLE IF NOT EXISTS addresses(address TEXT PRIMARY KEY, created INTEGER)")
    c.execute("""CREATE TABLE IF NOT EXISTS messages(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        address TEXT,
        sender TEXT,
        subject TEXT,
        body TEXT,
        created INTEGER
    )""")
    c.commit()
    c.close()

def cleanup():
    cutoff = int(time.time()) - TTL
    c = db()
    c.execute("DELETE FROM messages WHERE created < ?", (cutoff,))
    c.execute("DELETE FROM addresses WHERE created < ?", (cutoff,))
    c.commit()
    c.close()

@app.before_request
def guard():
    cleanup()
    if request.path.startswith("/api/") and API_TOKEN:
        if request.headers.get("Authorization") != "Bearer " + API_TOKEN:
            return jsonify({"error": "unauthorized"}), 401

@app.post("/api/addresses")
def create_address():
    for _ in range(10):
        address = secrets.token_hex(9) + "@" + DOMAIN
        try:
            c = db()
            c.execute("INSERT INTO addresses VALUES(?, ?)", (address, int(time.time())))
            c.commit()
            c.close()
            return jsonify({"address": address, "expires_in": TTL})
        except sqlite3.IntegrityError:
            pass
    return jsonify({"error": "could not create address"}), 503

@app.get("/api/messages")
def list_messages():
    address = request.args.get("address", "")
    c = db()
    rows = c.execute(
        "SELECT id,sender,subject,created FROM messages WHERE address=? ORDER BY id DESC",
        (address,)
    ).fetchall()
    c.close()
    return jsonify([dict(row) for row in rows])

@app.get("/api/messages/<int:message_id>")
def get_message(message_id):
    address = request.args.get("address", "")
    c = db()
    row = c.execute(
        "SELECT * FROM messages WHERE id=? AND address=?",
        (message_id, address)
    ).fetchone()
    c.close()
    if not row:
        return jsonify({"error": "not found"}), 404
    return jsonify(dict(row))

@app.delete("/api/addresses")
def delete_address():
    address = request.args.get("address", "")
    c = db()
    c.execute("DELETE FROM messages WHERE address=?", (address,))
    c.execute("DELETE FROM addresses WHERE address=?", (address,))
    c.commit()
    c.close()
    return jsonify({"deleted": address})

@app.post("/internal/deliver")
def deliver():
    if INTERNAL_KEY and request.headers.get("X-Internal-Key") != INTERNAL_KEY:
        return jsonify({"error": "unauthorized"}), 401

    address = request.args.get("address", "")
    msg = BytesParser(policy=default).parsebytes(request.get_data())
    body = msg.get_body(preferencelist=("plain", "html"))
    text = body.get_content() if body else ""

    c = db()
    if not c.execute("SELECT 1 FROM addresses WHERE address=?", (address,)).fetchone():
        c.close()
        return jsonify({"error": "unknown address"}), 404

    c.execute(
        "INSERT INTO messages(address,sender,subject,body,created) VALUES(?,?,?,?,?)",
        (address, msg.get("From", ""), msg.get("Subject", ""), text, int(time.time()))
    )
    c.commit()
    c.close()
    return jsonify({"accepted": True})

if __name__ == "__main__":
    init()
    app.run(host="127.0.0.1", port=int(os.getenv("TEMPMAIL_PORT", "8080")))
