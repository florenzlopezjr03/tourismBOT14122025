"""
Configuration file for Tourism Bot
Update your Mistral API key here to use the live bot versions
"""

# ==========================================
# MISTRAL AI CONFIGURATION
# ==========================================

# Get your API key from: https://console.mistral.ai
MISTRAL_API_KEY = "8rJkzPuf6KRuuX90wNSShAW2RNe5B1XB"  # Valid API key

# Model to use for the bot
MISTRAL_MODEL = "mistral-large-latest"

# ==========================================
# BOT CONFIGURATION
# ==========================================

# System prompt for the tourism bot
TOURISM_SYSTEM_PROMPT = """You are an expert tourism assistant chatbot with deep knowledge about:
- Global destinations and landmarks
- Travel planning and itineraries
- Cultural experiences and local customs
- Budget travel tips and cost optimization
- Seasonal recommendations
- Transportation options
- Accommodation recommendations
- Food and dining experiences
- Safety and health information
- Visa and documentation requirements

Always be helpful, enthusiastic, and provide personalized recommendations based on user preferences.
When relevant, ask follow-up questions to better understand what the user is looking for."""

# Conversation history file location
CONVERSATION_HISTORY_FILE = "conversation_history.json"

# Maximum conversation history to keep in memory
MAX_CONVERSATION_HISTORY = 20

# ==========================================
# FEATURE FLAGS
# ==========================================

# Enable conversation history saving
SAVE_CONVERSATIONS = True

# Enable offline demo mode (no API key needed)
DEMO_MODE = False

# ==========================================
# INSTRUCTIONS
# ==========================================
"""
HOW TO UPDATE YOUR API KEY:

1. Go to https://console.mistral.ai
2. Sign up or log in to your account
3. Navigate to API Keys section
4. Create a new API key or copy existing one
5. Replace the MISTRAL_API_KEY value above with your actual key
6. Make sure DEMO_MODE = False to use the live API
7. Save this file

EXAMPLE:
    MISTRAL_API_KEY = "sk_1a2b3c4d5e6f7g8h9i0j"  # Your actual key

WARNING: Keep your API key secret!
- Don't commit it to public repositories
- Don't share it with others
- Rotate it regularly if compromised
- Consider using environment variables for production
"""
