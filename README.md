# Tourism Bot 🌍

A conversational tourism assistant powered by Mistral AI that helps you plan your next adventure!

## Features

- **Destination Recommendations**: Get suggestions for travel destinations based on your preferences
- **Itinerary Planning**: Create personalized travel itineraries
- **Travel Tips**: Learn about the best times to visit, local customs, and cultural insights
- **Accommodation & Dining**: Get recommendations for hotels, restaurants, and local cuisines
- **Budget Planning**: Tips for budget travel and cost optimization
- **Safety & Health Info**: Important information for safe and healthy travels
- **Visa & Documentation**: Help with visa requirements and travel documents

## Project Structure

```
TOURISM BOT2/
├── venv/                    # Virtual environment
├── tourism_bot.py          # Simple interactive bot
├── advanced_tourism_bot.py # Advanced bot with menu and history
├── conversation_history.json # Saved conversations (auto-generated)
└── README.md               # This file
```

## Installation

### 1. Activate Virtual Environment
```bash
source venv/bin/activate
```

### 2. Install Dependencies
The Mistral AI package is already installed in your virtual environment.

## Usage

### Option 1: Simple Interactive Bot
```bash
python tourism_bot.py
```

This starts a simple chat interface where you can directly ask questions about tourism and travel.

**Example:**
```
You: What are the best destinations for a beach vacation in 2025?
Bot: [Provides recommendations for beach destinations...]

You: Tell me about Bali
Bot: [Provides detailed information about Bali...]

You: quit
```

### Option 2: Advanced Bot with Menu
```bash
python advanced_tourism_bot.py
```

This provides a menu-based interface with additional features:
- Chat with the bot
- Start a new conversation
- View conversation history
- Clear conversation history
- Save and load conversations automatically

## API Configuration

The bot uses the Mistral AI API with the following key:
- **API Key**: `rTfqOg0bg33dG3wnoC2cQaDIwpVdlSAi`
- **Model**: `mistral-large-latest`

## Example Queries

Here are some things you can ask the Tourism Bot:

- "What are the best destinations for solo travelers?"
- "I want to visit Japan for 2 weeks in March. Create an itinerary."
- "Tell me about the street food scene in Bangkok"
- "What's the best time to visit Machu Picchu?"
- "I have a budget of $2000 for a month-long trip. Where should I go?"
- "What are visa requirements for US citizens traveling to Europe?"
- "Recommend a hidden gem destination in Southeast Asia"
- "What cultural etiquette should I know before visiting India?"

## Tips for Best Results

1. **Be Specific**: Provide details about your preferences, budget, and travel duration
2. **Ask Follow-ups**: The bot remembers the conversation context
3. **Request Alternatives**: Ask for multiple options if the first suggestion doesn't suit you
4. **Ask for Details**: Request specific information like costs, transportation, or best seasons
5. **Local Insights**: Ask for local tips and hidden gems for a unique experience

## Troubleshooting

### Connection Error
If you get an error about the API key:
- Ensure you have an active internet connection
- Verify the API key is correct
- Check that your Mistral AI account is valid

### No Response
- Try rephrasing your question
- Check your internet connection
- Make sure the virtual environment is activated

## Deactivate Virtual Environment

When you're done using the bot:
```bash
deactivate
```

## Future Enhancements

Potential features to add:
- Integration with booking APIs (flights, hotels, activities)
- Real-time pricing information
- Image gallery of destinations
- Multi-language support
- Integration with weather APIs
- Travel budget calculator
- Accessibility features

## Support

For issues or improvements, check the conversation logs or re-run with fresh context.

Enjoy planning your next adventure! ✈️🌴
