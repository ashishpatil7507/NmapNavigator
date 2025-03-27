# NmapNavigator

## About
NmapNavigator is an intuitive and visually enhanced graphical interface for the Nmap network scanning tool, designed with Tkinter. It simplifies complex network scanning tasks, allowing users to select scan types effortlessly, modify commands, and view real-time results in an organized format.

## Features
- Interactive GUI with a sleek and modern design.
- Select multiple Nmap scan types with checkboxes.
- Modify the generated Nmap command before execution.
- View real-time scan progress and results.
- Animated loading indicator while scanning.
- Restart or exit easily after a scan.

## Requirements
- Python 3.x
- Tkinter (included with standard Python installation)
- Nmap (must be installed on the system)

## Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/NmapNavigator.git
   cd NmapNavigator
   ```
2. Ensure Nmap is installed:
   - Linux:
     ```sh
     sudo apt install nmap
     ```
   - macOS:
     ```sh
     brew install nmap
     ```
   - Windows:
     Download and install from [https://nmap.org/download.html](https://nmap.org/download.html)

## Usage
1. Run the script:
   ```sh
   python nmap_gui.py
   ```
2. Enter the target IP or domain.
3. Select scan options from the list.
4. Click "Scan" to proceed.
5. Modify the command if needed in the provided input field.
6. View real-time results after execution.
7. Click "Re-Scan" to perform another scan or "Exit" to quit immediately.

## Author
Developed by **Ashish Patil**

