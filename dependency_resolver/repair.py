"""
HOPE Dependency Resolver v7.0
Self-healing package management
"""
import subprocess
import sys
from pathlib import Path
from typing import Dict, List, Tuple

class DependencyResolver:
    """
    Manages Python package dependencies across multiple Python versions
    """
    
    def __init__(self):
        self.compat_map = {
            "sentence-transformers": {"python": "3.11", "priority": 1},
            "chromadb": {"python": "3.11", "priority": 1},
            "torch": {"python": "3.10", "priority": 2},
            "fastapi": {"python": "3.12", "priority": 1},
            "numpy": {"python": "3.13", "priority": 1},
            "requests": {"python": "3.13", "priority": 1}
        }
    
    def resolve(self, package: str) -> Tuple[str, List[str]]:
        """
        Determine best Python version and install commands
        """
        config = self.compat_map.get(package, {"python": "3.13"})
        target_python = config["python"]
        
        python_path = f"~/.pyenv/versions/{target_python}.*/bin/python"
        
        commands = [
            f"pip install --upgrade {package}"
        ]
        
        return python_path, commands
    
    def install(self, package: str) -> bool:
        """Install a package"""
        try:
            subprocess.run(
                [sys.executable, "-m", "pip", "install", "--upgrade", package],
                check=True,
                capture_output=True,
                timeout=300
            )
            return True
        except Exception as e:
            print(f"Installation failed: {e}")
            return False
    
    def check_and_repair(self, package: str) -> bool:
        """Check if package works, repair if needed"""
        try:
            __import__(package.replace("-", "_"))
            return True
        except ImportError:
            return self.install(package)
    
    def self_repair_all(self) -> Dict[str, bool]:
        """Repair all known packages"""
        results = {}
        for package in self.compat_map.keys():
            results[package] = self.check_and_repair(package)
        return results

def get_resolver():
    return DependencyResolver()
