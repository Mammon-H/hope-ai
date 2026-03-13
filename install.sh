#!/data/data/com.termux/files/usr/bin/bash
echo "Installing HOPE OMEGA v7.0..."
pkg install -y git python
cd ~
git clone https://github.com/Mammon-H/hope-ai.git
cd hope-ai
bash bootstrap/hope_omega_install.sh
echo "✅ HOPE installed! Run: hope start"
