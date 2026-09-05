from pathlib import Path
import hashlib

def run(value):
    path = Path(value).expanduser()
    if not path.is_file():
        return {"type": "hash", "path": str(path), "error": "File not found"}
    data = path.read_bytes()
    return {
        "type": "hash",
        "path": str(path.resolve()),
        "size_bytes": len(data),
        "md5": hashlib.md5(data).hexdigest(),
        "sha1": hashlib.sha1(data).hexdigest(),
        "sha256": hashlib.sha256(data).hexdigest(),
    }


# Compatibility entry point used by the X-Data CLI.
def compute(value):
    return run(value)
