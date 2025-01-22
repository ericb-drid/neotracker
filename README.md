# NeoTracker

NeoTracker is a Python-based tool designed to synchronize desktop shortcuts across multiple Windows devices, ensuring a consistent user interface wherever you work. With NeoTracker, you can define a primary directory for your shortcuts and replicate them to any number of target directories on different devices.

## Features

- Synchronizes `.lnk` shortcuts from a source directory to multiple target directories.
- Allows adding and removing of target directories via a configuration file.
- Ensures all devices have the same desktop shortcuts for a seamless user experience.

## Requirements

- Python 3.x
- Windows Operating System

## Installation

1. Clone the repository or download the `neotracker.py` file.
2. Ensure Python is installed on your system.

## Usage

1. Set up your configuration by adding target directories where shortcuts should be synchronized.
2. Run the script to synchronize shortcuts.

### Example

```python
neotracker = NeoTracker()

# Add target directories
neotracker.add_target_directory("C:/Users/User1/Desktop")
neotracker.add_target_directory("D:/Workspace/SharedDesktop")

# List current target directories
print("Current target directories:", neotracker.list_target_directories())

# Synchronize shortcuts
neotracker.synchronize_shortcuts(neotracker.list_target_directories())
```

## Configuration

The configuration is stored in a `config.json` file, which keeps track of the target directories for synchronization. You can directly edit this file or use the provided methods in the code to manage it.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Contact

For any inquiries or support, please contact the repository owner.