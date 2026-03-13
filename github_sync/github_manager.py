"""
GitHub Manager
"""
import subprocess
from pathlib import Path

class GitHubSync:
    def __init__(self):
        self.hope_dir = Path.home() / "hope-ai"
    
    def sync(self, message=None):
        try:
            subprocess.run(["git", "add", "."], cwd=self.hope_dir, check=True)
            subprocess.run(["git", "commit", "-m", message or "HOPE sync"], 
                         cwd=self.hope_dir, check=True)
            subprocess.run(["git", "push", "origin", "main"], 
                         cwd=self.hope_dir, check=True)
            return {"success": True, "message": "Synced"}
        except Exception as e:
            return {"success": False, "message": str(e)}
    
    def get_status(self):
        return {"status": "ready"}

def get_github_sync():
    return GitHubSync()
