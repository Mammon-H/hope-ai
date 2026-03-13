import subprocess
from pathlib import Path

class GitHubSync:

    def __init__(self):

        self.dir=Path.home()/ "hope-ai"

    def sync(self):

        subprocess.run(["git","add","."],cwd=self.dir)
        subprocess.run(["git","commit","-m","sync"],cwd=self.dir)
        subprocess.run(["git","push"],cwd=self.dir)

        return "synced"
