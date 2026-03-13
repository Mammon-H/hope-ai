"""
HOPE Agent System v7.0
Autonomous task delegation
"""

class AgentManager:
    """
    Routes tasks to specialized agents
    """
    
    def __init__(self):
        self.agents = {
            "planner": "Breaks down complex goals",
            "researcher": "Gathers information",
            "builder": "Creates files and code",
            "critic": "Reviews and improves"
        }
    
    def delegate(self, task: str) -> str:
        """Delegate task to appropriate agent"""
        task_lower = task.lower()
        
        if any(kw in task_lower for kw in ["plan", "steps", "organize", "break down"]):
            return f"[PLANNER] Creating plan for: {task}"
        
        elif any(kw in task_lower for kw in ["research", "find", "search", "look up"]):
            return f"[RESEARCHER] Researching: {task}"
        
        elif any(kw in task_lower for kw in ["create", "build", "make", "code", "write"]):
            return f"[BUILDER] Creating: {task}"
        
        elif any(kw in task_lower for kw in ["review", "check", "critique", "improve"]):
            return f"[CRITIC] Reviewing: {task}"
        
        else:
            return f"[GENERAL] Processing: {task}"
    
    def list_agents(self):
        """List available agents"""
        return self.agents

def get_agent_manager():
    return AgentManager()
