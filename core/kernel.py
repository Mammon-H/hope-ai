#!/usr/bin/env python3
"""
HOPE OMEGA v7.0 Kernel
"""
import sys
from pathlib import Path
HOPE_DIR = Path.home() / "hope-ai"
sys.path.insert(0, str(HOPE_DIR))

class HOPEKernel:
    VERSION = "7.0.0"
    
    def __init__(self):
        print(f"🚀 HOPE OMEGA v{self.VERSION}")
        print("Commands: ai <query> | tool | skill | sync | quit")
        self.running = True
    
    def start(self):
        while self.running:
            try:
                cmd = input("\nHOPE> ").strip()
                if cmd == "quit":
                    self.running = False
                elif cmd.startswith("ai "):
                    self._ai_query(cmd[3:])
                elif cmd == "status":
                    print("System ready")
                else:
                    print(f"Echo: {cmd}")
            except KeyboardInterrupt:
                break
        print("\nGoodbye!")
    
    def _ai_query(self, query):
        try:
            from ai_orchestrator.router import route
            print(route(query, "general"))
        except Exception as e:
            print(f"AI Error: {e}")

if __name__ == "__main__":
    kernel = HOPEKernel()
    kernel.start()
