#!/bin/bash

# Tourism Bot - Quick Start Script
# This script helps you quickly run the tourism bot

echo "🌍 Tourism Bot Quick Start"
echo "=========================="
echo ""

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "❌ Virtual environment not found!"
    echo "Creating virtual environment..."
    python3 -m venv venv
    echo "✓ Virtual environment created"
fi

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

echo "✓ Virtual environment activated"
echo ""
echo "Choose which bot to run:"
echo "1. Demo Bot (works without API key)"
echo "2. Interactive Bot (requires valid API key)"
echo "3. Advanced Bot with Menu (requires valid API key)"
echo "4. Exit"
echo ""

read -p "Enter your choice (1-4): " choice

case $choice in
    1)
        echo ""
        echo "Starting Demo Bot..."
        echo "Type 'quit' to exit"
        echo ""
        python tourism_bot_demo.py
        ;;
    2)
        echo ""
        echo "Starting Interactive Bot..."
        echo "Type 'quit' to exit"
        echo ""
        python tourism_bot.py
        ;;
    3)
        echo ""
        echo "Starting Advanced Bot..."
        echo "Type 'quit' or select 'Exit' from menu"
        echo ""
        python advanced_tourism_bot.py
        ;;
    4)
        echo "Exiting..."
        deactivate
        exit 0
        ;;
    *)
        echo "Invalid choice!"
        exit 1
        ;;
esac

# Deactivate virtual environment when done
deactivate
echo ""
echo "✓ Virtual environment deactivated"
