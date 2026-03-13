"""
File Operations Tool
"""
from pathlib import Path

def main(operation, path, content=""):
    p = Path(path).expanduser()
    
    if operation == "read":
        return p.read_text() if p.exists() else "File not found"
    elif operation == "write":
        p.write_text(content)
        return f"Written to {path}"
    elif operation == "list":
        return "\\n".join([x.name for x in p.iterdir()]) if p.is_dir() else "Not a directory"
    else:
        return f"Unknown operation: {operation}"
