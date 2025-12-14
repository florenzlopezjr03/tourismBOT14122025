# Tourism Bot Setup & Usage Guide 🌍

## ✅ Setup Complete!

Your Tourism Bot has been successfully created in `/Users/TOURISM BOT2/`

### What's Been Set Up

1. **Virtual Environment** - Isolated Python environment with Mistral AI installed
2. **Three Bot Versions** - Simple, Advanced, and Demo versions
3. **Documentation** - Comprehensive guides and README files

---

## 📁 Project Files

```
TOURISM BOT2/
├── venv/                      # Virtual environment (don't modify)
├── tourism_bot.py             # Simple interactive bot (requires valid API key)
├── advanced_tourism_bot.py    # Advanced bot with menu (requires valid API key)
├── tourism_bot_demo.py        # Demo bot (works offline, no API key needed)
├── conversation_history.json  # Auto-saved conversations (generated)
├── README.md                  # Main documentation
└── SETUP_GUIDE.md             # This file
```

---

## 🚀 Quick Start

### 1. Activate Virtual Environment
```bash
source /Users/TOURISM\ BOT2/venv/bin/activate
```

You should see `(venv)` at the start of your terminal prompt.

### 2. Run the Bot

#### Option A: Demo Version (No API Key Needed)
```bash
python /Users/TOURISM\ BOT2/tourism_bot_demo.py
```

#### Option B: Interactive Bot (Requires Valid API Key)
```bash
python /Users/TOURISM\ BOT2/tourism_bot.py
```

#### Option C: Advanced Bot with Menu (Requires Valid API Key)
```bash
python /Users/TOURISM\ BOT2/advanced_tourism_bot.py
```

### 3. Deactivate Virtual Environment (When Done)
```bash
deactivate
```

---

## 🔑 API Key Configuration

The provided API key (`rTfqOg0bg33dG3wnoC2cQaDIwpVdlSAi`) appears to be invalid or expired.

### To Use a Valid API Key:

1. **Get a Mistral AI API Key:**
   - Visit https://console.mistral.ai
   - Sign up or log in
   - Generate an API key
   - Copy your API key

2. **Update the Bot Files:**

   **For `tourism_bot.py`:**
   - Open the file
   - Find line: `api_key = "rTfqOg0bg33dG3wnoC2cQaDIwpVdlSAi"`
   - Replace with: `api_key = "YOUR_ACTUAL_API_KEY"`

   **For `advanced_tourism_bot.py`:**
   - Open the file
   - Find line: `api_key = "rTfqOg0bg33dG3wnoC2cQaDIwpVdlSAi"`
   - Replace with: `api_key = "YOUR_ACTUAL_API_KEY"`

3. **Test Your API Key:**
   ```bash
   python /Users/TOURISM\ BOT2/tourism_bot.py
   ```

---

## 💡 Usage Examples

### With Demo Bot (No API Needed)
```bash
source /Users/TOURISM\ BOT2/venv/bin/activate
python /Users/TOURISM\ BOT2/tourism_bot_demo.py
```

**Example interaction:**
```
You: What are the best beach destinations?
Bot: Top beach destinations for 2025:
1. **Maldives** - Crystal clear waters, luxury resorts...
2. **Bali, Indonesia** - Affordable, vibrant culture...
3. **Cancun, Mexico** - All-inclusive resorts...

You: Tell me about Europe
Bot: Top European destinations:
1. **Italy** - Rome, Venice, Florence...
2. **Spain** - Barcelona, Madrid, Seville...
3. **France** - Paris, Provence, French Riviera...

You: quit
Bot: Thank you for chatting with me! Safe travels! 🌴✈️
```

### With Live Bot (Valid API Key Required)
```bash
source /Users/TOURISM\ BOT2/venv/bin/activate
python /Users/TOURISM\ BOT2/tourism_bot.py
```

The experience is similar, but responses come from the live Mistral AI API.

---

## 🎯 Bot Features

All versions support:

✅ **Destination Recommendations**
- Suggest travel destinations based on preferences
- Information about attractions and landmarks

✅ **Itinerary Planning**
- Create personalized travel itineraries
- Suggest activities and experiences

✅ **Travel Tips**
- Best times to visit destinations
- Local customs and cultural insights
- Budget travel recommendations

✅ **Accommodation & Dining**
- Hotel and resort recommendations
- Local restaurant and food suggestions

✅ **Practical Information**
- Visa and documentation requirements
- Safety and health information
- Packing tips and preparation

✅ **Budget Planning**
- Cost estimation for destinations
- Money-saving travel tips
- Affordable alternatives

---

## 🔄 Conversation History (Advanced Bot)

The `advanced_tourism_bot.py` automatically saves conversations to `conversation_history.json`.

### Features:
- Auto-saves after each exchange
- Load previous conversations
- View conversation history
- Clear history when starting fresh

### Example Menu:
```
============================================================
Tourism Bot Menu
============================================================
1. Chat with the bot
2. Start a new conversation
3. View conversation history
4. Clear conversation history
5. Exit
============================================================
```

---

## 🛠️ Troubleshooting

### Problem: "command not found: python"
**Solution:** Make sure virtual environment is activated
```bash
source /Users/TOURISM\ BOT2/venv/bin/activate
python --version  # Should show Python 3.14.2
```

### Problem: "API error occurred: Status 401 Unauthorized"
**Solution:** API key is invalid
- Use the demo version instead: `python tourism_bot_demo.py`
- Or get a valid API key from https://console.mistral.ai

### Problem: "ModuleNotFoundError: No module named 'mistralai'"
**Solution:** Make sure virtual environment is activated and packages are installed
```bash
source /Users/TOURISM\ BOT2/venv/bin/activate
pip list | grep mistral  # Should show mistralai
```

### Problem: Bot not responding
**Solution:** 
- Check internet connection
- Verify API key is valid
- Try the demo version first

---

## 📊 Bot Capabilities Summary

| Feature | Demo Bot | Interactive Bot | Advanced Bot |
|---------|----------|-----------------|--------------|
| Works offline | ✅ | ❌ | ❌ |
| Requires API key | ❌ | ✅ | ✅ |
| Saves conversations | ❌ | ❌ | ✅ |
| Menu interface | ❌ | ❌ | ✅ |
| AI responses | Limited | Full | Full |
| Real-time info | ❌ | ✅ | ✅ |

---

## 📚 Additional Resources

- **Mistral AI Docs:** https://docs.mistral.ai
- **Python Virtual Environments:** https://docs.python.org/3/tutorial/venv.html
- **Tourism API Integration:** Can be extended to include flight, hotel, and activity APIs

---

## 🎓 Learning Path

1. **Start with Demo Bot** - Understand the UI and features
2. **Get a Mistral API Key** - https://console.mistral.ai
3. **Run Interactive Bot** - Experience live AI responses
4. **Use Advanced Bot** - Leverage conversation history
5. **Customize & Extend** - Add more features as needed

---

## 💬 Next Steps

1. **Run the demo bot** to see it in action:
   ```bash
   source /Users/TOURISM\ BOT2/venv/bin/activate
   python /Users/TOURISM\ BOT2/tourism_bot_demo.py
   ```

2. **Get a valid API key** from Mistral AI Console

3. **Update the bot files** with your API key

4. **Enjoy planning travels!** 🌴✈️

---

## 📞 Support Tips

- Check the README.md for additional features
- Review your conversation history to improve queries
- Experiment with different question formats
- Ask follow-up questions for more details
- Request alternatives if suggestions don't match preferences

Happy travels! 🌍
