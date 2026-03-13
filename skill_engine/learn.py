"""
Skill Learning Engine
"""
import json
from pathlib import Path

class SkillEngine:
    def __init__(self):
        self.skills_dir = Path(__file__).parent / "learned"
        self.skills_dir.mkdir(exist_ok=True)
        self.skills = {}
        self._load_skills()
    
    def _load_skills(self):
        for skill_file in self.skills_dir.glob("*.json"):
            with open(skill_file) as f:
                self.skills[skill_file.stem] = json.load(f)
    
    def list_skills(self):
        return list(self.skills.keys())
    
    def execute_skill(self, name):
        if name not in self.skills:
            return {"error": f"Skill '{name}' not found"}
        return {"skill": name, "status": "executed"}

def get_skill_engine():
    return SkillEngine()
