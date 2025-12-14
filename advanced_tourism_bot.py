#!/usr/bin/env python3
"""
Advanced Tourism Bot with conversation management
Powered by Mistral AI
"""

import json
import os
from datetime import datetime
from mistralai import Mistral

# Initialize the Mistral client
api_key = "8rJkzPuf6KRuuX90wNSShAW2RNe5B1XB"
client = Mistral(api_key=api_key)

SYSTEM_PROMPT = """You are an expert tourism assistant chatbot with deep knowledge about:
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

CONVERSATION_FILE = "conversation_history.json"


def load_conversation_history():
    """Load conversation history from file if it exists"""
    if os.path.exists(CONVERSATION_FILE):
        try:
            with open(CONVERSATION_FILE, "r") as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError):
            return []
    return []


def save_conversation_history(history):
    """Save conversation history to file"""
    try:
        with open(CONVERSATION_FILE, "w") as f:
            json.dump(history, f, indent=2)
    except IOError as e:
        print(f"Warning: Could not save conversation history: {e}")


def display_menu():
    """Display the main menu"""
    print("\n" + "=" * 60)
    print("Tourism Bot Menu")
    print("=" * 60)
    print("1. Chat with the bot")
    print("2. Start a new conversation")
    print("3. View conversation history")
    print("4. Clear conversation history")
    print("5. Exit")
    print("=" * 60)


def view_history(history):
    """Display conversation history"""
    if not history:
        print("\nNo conversation history found.")
        return

    print("\n" + "=" * 60)
    print("Conversation History")
    print("=" * 60)
    for i, message in enumerate(history):
        role = message["role"].upper()
        content = message["content"]
        print(f"\n[{i + 1}] {role}:")
        print(f"    {content[:100]}..." if len(content) > 100 else f"    {content}")


def chat_session(history):
    """Run a chat session with the bot"""
    print("\n" + "=" * 60)
    print("Chat Session")
    print("=" * 60)
    print("Type 'menu' to return to main menu\n")

    while True:
        user_input = input("You: ").strip()

        if user_input.lower() == "menu":
            break

        if not user_input:
            continue

        # Add user message to history
        history.append({"role": "user", "content": user_input})

        try:
            # Call Mistral API
            messages = [{"role": "system", "content": SYSTEM_PROMPT}] + history
            response = client.chat.complete(
                model="mistral-large-latest", messages=messages
            )

            bot_response = response.choices[0].message.content

            # Add bot response to history
            history.append({"role": "assistant", "content": bot_response})

            # Display response
            print(f"\nBot: {bot_response}\n")

            # Save history after each exchange
            save_conversation_history(history)

        except Exception as e:
            print(f"\nError: {str(e)}\n")
            history.pop()  # Remove failed user message

    return history


def main():
    """Main function to run the advanced tourism bot"""
    print("=" * 60)
    print("🌍 Welcome to Advanced Tourism Bot 🌍")
    print("=" * 60)
    print("Powered by Mistral AI\n")

    history = load_conversation_history()

    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            history = chat_session(history)
        elif choice == "2":
            history = []
            save_conversation_history(history)
            print("\n✓ Conversation history cleared. Starting fresh!\n")
            history = chat_session(history)
        elif choice == "3":
            view_history(history)
        elif choice == "4":
            confirm = input("\nAre you sure? (yes/no): ").strip().lower()
            if confirm == "yes":
                history = []
                save_conversation_history(history)
                print("✓ Conversation history cleared.\n")
        elif choice == "5":
            print(
                "\nThank you for using Tourism Bot! Safe travels! 🌴✈️\n"
            )
            break
        else:
            print("\nInvalid choice. Please try again.\n")


if __name__ == "__main__":
    main()
