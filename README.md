# iNetHandler

Welcome to **iNetHandler**! 🎉

iNetHandler windows application designed to automatically connect your Windows device to the fastest known WiFi network nearby. With a blend of powerful libraries and `netsh` commands, iNetHandler ensures you always get the best possible internet connection with minimal effort.

## Features

- **Automatic WiFi Selection**: Scans and connects to the fastest available WiFi network.
- **Multi-threading**: Utilizes the `threading` library for efficient performance.
- **Comprehensive Network Handling**: Executes `netsh` commands to manage WiFi connections.
- **Robust Networking Libraries**: Built with `urllib3` and `requests` for network operations.

## Requirements

- Windows OS
- Python 3.6 or higher
- Required Libraries: `threading`, `os`, `sys`, `urllib3`, `requests`

## Installation

   ```bash
   git clone https://github.com/mayankkumargupta1/iNetHandler.git
   cd iNetHandler
   pip install requirements.txt
   py app.py
   ```

## How It Works
iNetHandler leverages a combination of Python libraries and Windows netsh commands to manage your WiFi connections. Here's a brief overview of the core components:

- threading: Ensures the program runs efficiently without blocking the main thread.
- os: Interacts with the operating system to execute netsh commands.
- sys: Handles system-specific parameters and functions.
- urllib3 & requests: Perform network operations, such as speed tests and connectivity checks.
- netsh commands: Manage WiFi settings and connections on Windows.

Made with ❤️ by Mayank Kumar Gupta.
