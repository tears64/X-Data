# X-Data TempMail

A receive-only disposable inbox backend for X-Data.

```bash
pip install flask
export TEMPMAIL_DOMAIN=mail.example.com
export TEMPMAIL_API_TOKEN=change-me
python3 tempmail_server.py
```

The development API listens on 127.0.0.1:8080. For production, use a domain you control,
HTTPS, a trusted mail gateway/MTA, rate limits, message-size limits, and automatic expiry.
Do not configure the service as an open SMTP relay.
