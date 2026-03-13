#!/usr/bin/env python3
import sys
from pathlib import Path

HOPE_DIR = Path.home() / "hope-ai"
sys.path.insert(0, str(HOPE_DIR))

class HOPEKernel:

    VERSION="7.0"

    def __init__(self):
        print(f"🚀 HOPE OMEGA v{self.VERSION}")
        self.running=True

    def start(self):

        while self.running:

            try:
                cmd=input("HOPE> ").strip()

                if cmd=="quit":
                    self.running=False

                elif cmd.startswith("ai "):
                    self.ai(cmd[3:])

                elif cmd=="tool":
                    self.tools()

                elif cmd=="status":
                    print("System OK")

                else:
                    print("Unknown command")

            except KeyboardInterrupt:
                break

    def ai(self,query):

        from ai_orchestrator.router import route
        print(route(query))

    def tools(self):

        from tool_engine.registry.tool_registry import ToolRegistry
        reg=ToolRegistry()

        print("Tools:")
        for t in reg.list_tools():
            print("-",t)


if __name__=="__main__":

    kernel=HOPEKernel()
    kernel.start()
