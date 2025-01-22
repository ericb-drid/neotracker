import os
import shutil
import json
from pathlib import Path

class NeoTracker:
    def __init__(self, config_file='config.json'):
        self.config_file = config_file
        self.config = self.load_config()
        self.shortcut_dir = Path(self.config.get("shortcut_directory", "C:/Users/Public/Desktop"))

    def load_config(self):
        try:
            with open(self.config_file, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return {}

    def save_config(self):
        with open(self.config_file, 'w') as file:
            json.dump(self.config, file, indent=4)

    def synchronize_shortcuts(self, target_directories):
        if not self.shortcut_dir.exists():
            print(f"Shortcut directory {self.shortcut_dir} does not exist.")
            return
        
        for target in target_directories:
            target_path = Path(target)
            if not target_path.exists():
                print(f"Target directory {target_path} does not exist. Creating it.")
                target_path.mkdir(parents=True, exist_ok=True)

            for file in self.shortcut_dir.glob("*.lnk"):
                shutil.copy(file, target_path)
                print(f"Copied {file.name} to {target_path}")

    def add_target_directory(self, directory):
        if "target_directories" not in self.config:
            self.config["target_directories"] = []
        
        if directory not in self.config["target_directories"]:
            self.config["target_directories"].append(directory)
            self.save_config()
            print(f"Added {directory} to target directories.")

    def remove_target_directory(self, directory):
        if "target_directories" in self.config and directory in self.config["target_directories"]:
            self.config["target_directories"].remove(directory)
            self.save_config()
            print(f"Removed {directory} from target directories.")

    def list_target_directories(self):
        return self.config.get("target_directories", [])

if __name__ == "__main__":
    neotracker = NeoTracker()

    # Example usage
    neotracker.add_target_directory("C:/Users/User1/Desktop")
    neotracker.add_target_directory("D:/Workspace/SharedDesktop")

    print("Current target directories:", neotracker.list_target_directories())

    neotracker.synchronize_shortcuts(neotracker.list_target_directories())