#!/data/data/com.termux/files/usr/bin/bash

echo "🚀 Installing HOPE AI..."

pkg update -y
pkg upgrade -y

pkg install python git -y

echo "📦 Installing Python dependencies..."
pip install --upgrade pip

if [ -f requirements.txt ]; then
    pip install -r requirements.txt
fi

echo "✅ HOPE AI installation complete."
