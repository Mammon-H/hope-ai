import json
from pathlib import Path

class SkillEngine:

    def __init__(self):

        self.dir=Path(__file__).parent/"learned"
        self.dir.mkdir(exist_ok=True)

    def list(self):

        return [x.stem for x in self.dir.glob("*.json")]
