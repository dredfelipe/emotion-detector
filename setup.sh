#!/bin/bash
# Emotion Detection Application - Installation and Verification Script

echo "=========================================="
echo "Emotion Detection Application Setup"
echo "=========================================="
echo ""

# Navigate to project directory
cd "$(dirname "$0")" || exit

echo "📦 Installing dependencies..."
pip install -r requirements.txt

echo ""
echo "✅ Dependency installation complete!"
echo ""

echo "🧪 Running unit tests..."
python -m unittest discover -s tests -p "test_*.py" -v

echo ""
echo "=========================================="
echo "Setup Complete!"
echo "=========================================="
echo ""
echo "To start the server, run:"
echo "  python server.py"
echo ""
echo "Then visit: http://localhost:5000"
echo ""
