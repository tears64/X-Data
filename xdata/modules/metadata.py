from pathlib import Path
import hashlib
import mimetypes

def run(value):
    path = Path(value).expanduser()
    if not path.is_file():
        return {"type": "metadata", "path": str(path), "error": "File not found"}

    data = path.read_bytes()
    return {
        "type": "metadata",
        "path": str(path.resolve()),
        "name": path.name,
        "size_bytes": len(data),
        "mime_type": mimetypes.guess_type(path.name)[0],
        "sha256": hashlib.sha256(data).hexdigest(),
        "extension": path.suffix.lower(),
    }


# Compatibility entry point used by the X-Data CLI.
def inspect(value):
    return run(value)
