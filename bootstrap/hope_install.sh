#!/data/data/com.termux/files/usr/bin/bash

echo "Installing HOPE..."

pkg install -y git python
pip install requests beautifulsoup4

cp ~/hope-ai/hope $PREFIX/bin/hope

echo "Install complete"
echo "Run: hope start"
