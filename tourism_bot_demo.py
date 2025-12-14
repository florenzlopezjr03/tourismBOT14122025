#!/usr/bin/env python3
"""
Tourism Bot Demo Version (Offline Mode)
This version demonstrates the bot functionality without requiring API calls.
Replace with your valid Mistral AI API key when ready to use live features.
"""

import json
import os
from datetime import datetime

# Demo mode - replace with actual Mistral client when you have a valid API key
DEMO_MODE = True

if not DEMO_MODE:
    from mistralai import Mistral
    api_key = "YOUR_MISTRAL_API_KEY_HERE"  # Replace with valid key
    client = Mistral(api_key=api_key)


class TourismBotDemo:
    """Demo version of Tourism Bot with sample responses"""

    def __init__(self):
        self.demo_responses = {
            "beach": [
                "Top beach destinations for 2025:\n"
                "1. **Maldives** - Crystal clear waters, luxury resorts, best Dec-Mar\n"
                "2. **Bali, Indonesia** - Affordable, vibrant culture, year-round sunshine\n"
                "3. **Cancun, Mexico** - All-inclusive resorts, turquoise waters, warm climate"
            ],
            "budget": [
                "Budget-friendly destinations:\n"
                "1. **Vietnam** - Amazing food, $15-25/day possible, beautiful landscapes\n"
                "2. **Thailand** - Islands, temples, $20-30/day, friendly locals\n"
                "3. **Portugal** - European charm, affordable wine, $30-40/day"
            ],
            "europe": [
                "Top European destinations:\n"
                "1. **Italy** - Rome, Venice, Florence, amazing cuisine\n"
                "2. **Spain** - Barcelona, Madrid, Seville, beaches and culture\n"
                "3. **France** - Paris, Provence, French Riviera, romantic atmosphere"
            ],
            "asia": [
                "Popular Asian destinations:\n"
                "1. **Japan** - Tokyo, Kyoto, Mount Fuji, unique culture\n"
                "2. **Thailand** - Bangkok, Phuket, temples, tropical paradise\n"
                "3. **Vietnam** - Hanoi, Ho Chi Minh City, Ha Long Bay, authentic experience"
            ],
            "south america": [
                "South American highlights:\n"
                "1. **Peru** - Machu Picchu, Amazon, Nazca Lines\n"
                "2. **Colombia** - Coffee region, Caribbean coast, friendly people\n"
                "3. **Chile** - Atacama Desert, Patagonia, diverse landscapes"
            ],
            "africa": [
                "African destinations:\n"
                "1. **Egypt** - Pyramids, Nile River, ancient history\n"
                "2. **Tanzania** - Safari, Mount Kilimanjaro, Zanzibar\n"
                "3. **Morocco** - Marrakech, Sahara, Casablanca, blend of cultures"
            ],
            "itinerary": [
                "Here's a 7-day Thailand itinerary:\n"
                "Day 1-2: Bangkok - Grand Palace, temples, night markets\n"
                "Day 3-4: Phuket - Beaches, island hopping, snorkeling\n"
                "Day 5-7: Krabi - Rock climbing, relaxation, sunset views\n"
                "Budget: $40-60/day, mix of culture and nature"
            ],
            "visa": [
                "Visa information varies by destination:\n"
                "- Most EU countries: US/UK citizens get 90 days visa-free\n"
                "- Thailand: 30 days visa-free for many nationalities\n"
                "- Japan: 90 days visa-free for US/UK citizens\n"
                "- China: Requires advance visa (usually 30-90 days)\n"
                "Check your country's official travel site for specifics"
            ],
            "safety": [
                "General travel safety tips:\n"
                "1. Register with your embassy before traveling\n"
                "2. Keep copies of important documents\n"
                "3. Avoid walking alone at night in unfamiliar areas\n"
                "4. Use official taxis or ride-sharing apps\n"
                "5. Keep valuables hidden and use hotel safes\n"
                "6. Travel insurance is highly recommended"
            ],
            "packing": [
                "Essential packing tips:\n"
                "- Check weather for your destination\n"
                "- Pack light and versatile clothing\n"
                "- Include medications and first aid kit\n"
                "- Bring universal power adapter\n"
                "- Don't forget sunscreen and insect repellent\n"
                "- Keep important documents in carry-on\n"
                "- Leave room for souvenirs!"
            ],
        }

    def get_response(self, user_input):
        """Generate a demo response based on user input"""
        user_input = user_input.lower()

        # Check for keyword matches
        for keyword, response in self.demo_responses.items():
            if keyword in user_input:
                return response[0]

        # Default response
        return (
            "Great question! I'm a Tourism Bot powered by Mistral AI, and I can help you with:\n"
            "- Destination recommendations\n"
            "- Itinerary planning\n"
            "- Budget travel tips\n"
            "- Safety and visa information\n"
            "- Cultural insights and local recommendations\n\n"
            "Try asking about specific destinations like 'beaches', 'Europe', 'budget travel', or 'itineraries'!"
        )


def main():
    """Main function to run the tourism bot demo"""
    print("=" * 70)
    print("🌍 Welcome to Tourism Bot! (Demo Version) 🌍")
    print("=" * 70)
    print("I'm here to help you plan your next adventure!")
    print("Type 'quit' or 'exit' to end the conversation.\n")
    print("📝 NOTE: This is a demo version with sample responses.")
    print("For live AI responses, update your Mistral API key in the code.\n")

    bot = TourismBotDemo()

    while True:
        user_input = input("You: ").strip()

        if user_input.lower() in ["quit", "exit", "bye", "goodbye"]:
            print(
                "\nBot: Thank you for chatting with me! Safe travels! 🌴✈️\n"
            )
            break

        if not user_input:
            continue

        response = bot.get_response(user_input)
        print(f"\nBot: {response}\n")


if __name__ == "__main__":
    main()
