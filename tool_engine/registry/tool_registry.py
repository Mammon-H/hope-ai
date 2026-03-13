"""
Tool Registry
"""
from pathlib import Path
import json

class ToolRegistry:
    def __init__(self):
        self.tools = {}
        self._load_tools()
    
    def _load_tools(self):
        # Auto-discover tools
        tools_dir = Path(__file__).parent.parent / "tools"
        if tools_dir.exists():
            for tool_file in tools_dir.glob("*.py"):
                if not tool_file.name.startswith("_"):
                    self.tools[tool_file.stem] = str(tool_file)
    
    def list_tools(self):
        return list(self.tools.keys())
    
    def execute(self, name, **kwargs):
        if name not in self.tools:
            return f"Tool '{name}' not found"
        return f"Executed {name} with {kwargs}"

def get_registry():
    return ToolRegistry()
