"""
Agent System
"""
class AgentManager:
    def __init__(self):
        self.agents = ["Planner", "Researcher", "Builder", "Critic"]
    
    def delegate(self, task):
        return f"[Agent] Processing: {task[:50]}"
    
    def list_agents(self):
        return self.agents

def get_agent_manager():
    return AgentManager()
