"""
AI Orchestrator
"""
import os

class AIRouter:
    def __init__(self):
        self.api_key = os.getenv("OPENAI_API_KEY", "")
    
    def route(self, prompt, task_type="general"):
        if not self.api_key:
            return "⚠️  API key not configured. Set OPENAI_API_KEY environment variable."
        
        # Placeholder for actual API call
        return f"[AI Response] You asked: {prompt[:50]}..."
    
    def ask(self, prompt):
        return self.route(prompt)

def route(prompt, task_type="general"):
    router = AIRouter()
    return router.route(prompt, task_type)
