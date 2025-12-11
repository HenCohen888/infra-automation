# DevOps Infra Automation Project

## Overview
This project is a Python-based infrastructure provisioning simulator.
It allows creating virtual machine definitions, saving them to a JSON file, and automatically installing Nginx using a Bash script.
The project demonstrates modular Python design, basic automation, logging, and error handling.

This project is built as preparation for future real cloud automation using AWS and Terraform.

---

## Features
- Virtual machine simulation using a Machine class  
- User input handling and validation  
- Instances stored in JSON format  
- Automatic Nginx installation using Bash  
- Python executes Bash scripts using subprocess  
- Full logging system (console + file)  
- Error handling in Python and Bash  

## Project Structure

```
infra-automation/
│
├── configs/               # Stored VM configurations
│   └── instances.json     # Output file containing created machines
│
├── logs/                  # Logging directory
│   └── provisioning.log   # Log output from provisioning runs
│
├── scripts/               # Shell automation scripts
│   └── install_nginx.sh   # Bash script to install Nginx
│
├── src/                   # Python source code
│   ├── input_prompt.py    # User input & validation logic
│   ├── instance_io.py     # Load/save JSON configuration
│   ├── machine.py         # Machine class + install_nginx logic
│   └── __init__.py        # Module initializer
│
├── main.py                # Main program entry point
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation
```

## Setup & Installation

### Prerequisites
- Python 3.8+
- Linux / WSL environment (required for Nginx installation)
- sudo privileges
- Git installed

### Clone the repository

```bash
git clone https://github.com/HenCohen888/infra-automation.git
cd infra-automation
```


## Class Responsibilities

### Machine
- Represents a virtual machine definition
- Performs validation on:
  - Name
  - Operating system
  - CPU cores
  - RAM size
- Converts VM data to dictionary format
- Runs service installation (Nginx) via Bash script

### instance_io
- Loads existing VM configurations from JSON
- Saves updated VM configurations back to JSON
- Handles basic file I/O error conditions

### input_prompt
- Collects user input interactively
- Validates format and acceptable value ranges
- Ensures clean and user-friendly error messages

### install_nginx.sh (Bash Script)
- Checks if Nginx is already installed (idempotent)
- Installs and configures Nginx using `apt`
- Exits with proper error codes for Python error handling

## Troubleshooting

### Error: Script not found
**Cause:** Running program from the wrong directory  
**Fix:** Always run from the project root:

```bash
cd infra-automation
python3 main.py











