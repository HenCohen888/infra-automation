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

---

## Project Structure

infra-automation/
├── configs/
│   └── instances.json
├── logs/
│   └── provisioning.log
├── scripts/
│   └── install_nginx.sh
├── src/
│   ├── input_prompt.py
│   ├── instance_io.py
│   ├── machine.py
│   └── __init__.py
├── main.py
├── requirements.txt
└── README.md

---

## Setup & Installation

### Prerequisites
- Python 3.8+
- Ubuntu / WSL (for Nginx installation)
- Git

### Clone the repository
```bash
git clone https://github.com/HenCohen888/infra-automation.git
cd infra-automation


