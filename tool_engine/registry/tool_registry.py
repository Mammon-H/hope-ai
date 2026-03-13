from pathlib import Path
import importlib.util

class ToolRegistry:

    def __init__(self):

        self.tools={}
        self.dir=Path(__file__).parent.parent/"tools"
        self.load()

    def load(self):

        for f in self.dir.glob("*.py"):

            name=f.stem

            spec=importlib.util.spec_from_file_location(name,f)
            mod=importlib.util.module_from_spec(spec)
            spec.loader.exec_module(mod)

            if hasattr(mod,"main"):
                self.tools[name]=mod.main

    def list_tools(self):

        return list(self.tools.keys())

    def execute(self,name,**kw):

        if name not in self.tools:
            return "Tool not found"

        return self.tools[name](**kw)
