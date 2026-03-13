from pathlib import Path

def main(operation,path,content=""):

    p=Path(path).expanduser()

    if operation=="read":
        return p.read_text()

    if operation=="write":
        p.write_text(content)
        return "written"

    if operation=="list":
        return "\n".join([x.name for x in p.iterdir()])
