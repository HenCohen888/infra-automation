#!/bin/bash

set -e

echo "[INFO] Hello from Nginx installation"
echo "[INFO] Running install_nginx.sh"

if command -v nginx >/dev/null 2>&1; then
    echo "[INFO] nginx already installed, nothing to do."
    exit 0
fi

echo "[INFO] nginx not found, installing..."

sudo apt update
sudo apt install -y nginx

echo "[INFO] nginx installation finishied."