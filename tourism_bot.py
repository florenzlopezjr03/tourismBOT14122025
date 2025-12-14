#!/usr/bin/env python3
"""
Tourism Bot powered by Mistral AI
A conversational bot that provides tourism recommendations and travel information
"""

from mistralai import Mistral

# Initialize the Mistral client
api_key = "8rJkzPuf6KRuuX90wNSShAW2RNe5B1XB"
client = Mistral(api_key=api_key)

# System prompt for the tourism bot
SYSTEM_PROMPT = """You are a knowledgeable and friendly tourism assistant chatbot. Your role is to:
1. Help travelers find travel destinations and provide information about them
2. Suggest tourist attractions, activities, and experiences
3. Provide travel tips, best times to visit, and local customs
4. Recommend restaurants, accommodations, and transportation options
5. Answer questions about visa requirements, travel budgets, and safety
6. Suggest itineraries based on traveler preferences and duration
7. Provide cultural insights and local recommendations

Be helpful, enthusiastic, and personalized in your responses. Ask clarifying questions when needed to provide better recommendations."""


def chat_with_bot():
    """Main function to run the tourism bot in an interactive chat mode"""
    print("=" * 60)
    print("Welcome to Tourism Bot! 🌍")
    print("=" * 60)
    print("I'm here to help you plan your next adventure!")
    print("Ask me about destinations, attractions, travel tips, and more.")
    print("Type 'quit' or 'exit' to end the conversation.\n")

    conversation_history = []

    while True:
        # Get user input
        user_input = input("You: ").strip()

        # Check for exit commands
        if user_input.lower() in ["quit", "exit", "bye", "goodbye"]:
            print("Bot: Thank you for chatting with me! Safe travels! 🌴✈️")
            break

        # Skip empty input
        if not user_input:
            continue

        # Add user message to conversation history
        conversation_history.append({"role": "user", "content": user_input})

        try:
            # Call Mistral API with conversation history
            messages = [{"role": "system", "content": SYSTEM_PROMPT}] + conversation_history
            response = client.chat.complete(
                model="mistral-large-latest",
                messages=messages,
            )

            # Extract bot response
            bot_response = response.choices[0].message.content

            # Add bot response to conversation history
            conversation_history.append({"role": "assistant", "content": bot_response})

            # Display bot response
            print(f"\nBot: {bot_response}\n")

        except Exception as e:
            print(f"\nError communicating with Mistral AI: {str(e)}")
            print("Please try again.\n")
            # Remove the failed user message from history
            conversation_history.pop()


if __name__ == "__main__":
    chat_with_bot()
