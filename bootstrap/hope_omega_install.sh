#!/data/data/com.termux/files/usr/bin/bash
echo "🚀 HOPE OMEGA v7.0 Bootstrap"
pkg install -y python python-pip git

# Install CLI
cp ~/hope-ai/hope $PREFIX/bin/hope
chmod +x $PREFIX/bin/hope

# Install dependencies
pip install requests beautifulsoup4

echo "✅ HOPE ready! Run: hope start"
