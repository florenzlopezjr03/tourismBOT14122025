#!/usr/bin/env python3
"""
Tourism Bot - Streamlit Web Application
Powered by Mistral AI
"""

import streamlit as st
import json
import os
from datetime import datetime
from mistralai import Mistral

# Page configuration
st.set_page_config(
    page_title="Tourism Bot 🌍",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
    <style>
    .main {
        padding-top: 2rem;
    }
    .chat-message {
        padding: 1rem;
        margin: 0.5rem 0;
        border-radius: 0.5rem;
    }
    .user-message {
        background-color: #e3f2fd;
        text-align: right;
    }
    .bot-message {
        background-color: #f5f5f5;
    }
    </style>
""", unsafe_allow_html=True)

# Initialize Mistral client
API_KEY = "8rJkzPuf6KRuuX90wNSShAW2RNe5B1XB"
client = Mistral(api_key=API_KEY)

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

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []
if "conversation_history" not in st.session_state:
    st.session_state.conversation_history = []

# Main app
def main():
    st.title("🌍 Tourism Bot")
    st.subheader("Your AI Travel Assistant Powered by Mistral AI")
    
    # Sidebar
    with st.sidebar:
        st.header("About")
        st.write("""
        Tourism Bot is an AI-powered travel assistant that helps you:
        - Find the best destinations
        - Plan itineraries
        - Get budget travel tips
        - Learn about local customs
        - Get accommodation & dining recommendations
        - Understand visa requirements
        """)
        
        st.divider()
        
        col1, col2 = st.columns(2)
        with col1:
            if st.button("🗑️ Clear Chat", use_container_width=True):
                st.session_state.messages = []
                st.session_state.conversation_history = []
                st.rerun()
        
        with col2:
            if st.button("📝 New Chat", use_container_width=True):
                st.session_state.messages = []
                st.session_state.conversation_history = []
                st.rerun()
        
        st.divider()
        
        st.subheader("Quick Prompts")
        prompts = [
            "🏖️ Best beach destinations for 2025",
            "💰 Budget travel destinations under $1000/month",
            "🗺️ Create a 7-day Europe itinerary",
            "🍜 Best street food in Southeast Asia",
            "✈️ Visa requirements for US citizens",
            "🏨 Hidden gem destinations in Asia",
        ]
        
        for prompt in prompts:
            if st.button(prompt, use_container_width=True):
                st.session_state.user_input = prompt
    
    # Main chat area
    chat_container = st.container()
    input_container = st.container()
    
    # Display chat history
    with chat_container:
        for message in st.session_state.messages:
            if message["role"] == "user":
                with st.chat_message("user", avatar="👤"):
                    st.write(message["content"])
            else:
                with st.chat_message("assistant", avatar="🤖"):
                    st.write(message["content"])
    
    # Input area
    with input_container:
        st.divider()
        
        col1, col2 = st.columns([5, 1])
        
        with col1:
            user_input = st.chat_input(
                "Ask me about destinations, travel tips, itineraries...",
                key="chat_input"
            )
        
        with col2:
            send_button = st.button("Send", use_container_width=True, key="send_btn")
        
        # Process user input
        if user_input and send_button:
            # Add user message to chat
            st.session_state.messages.append({
                "role": "user",
                "content": user_input
            })
            st.session_state.conversation_history.append({
                "role": "user",
                "content": user_input
            })
            
            # Display user message
            with chat_container:
                with st.chat_message("user", avatar="👤"):
                    st.write(user_input)
            
            # Generate bot response
            with st.spinner("Thinking..."):
                try:
                    messages = [{"role": "system", "content": SYSTEM_PROMPT}] + st.session_state.conversation_history
                    
                    response = client.chat.complete(
                        model="mistral-large-latest",
                        messages=messages
                    )
                    
                    bot_response = response.choices[0].message.content
                    
                    # Add bot response to chat
                    st.session_state.messages.append({
                        "role": "assistant",
                        "content": bot_response
                    })
                    st.session_state.conversation_history.append({
                        "role": "assistant",
                        "content": bot_response
                    })
                    
                    # Display bot response
                    with chat_container:
                        with st.chat_message("assistant", avatar="🤖"):
                            st.write(bot_response)
                    
                    st.rerun()
                
                except Exception as e:
                    st.error(f"Error: {str(e)}")
                    st.session_state.conversation_history.pop()
                    st.session_state.messages.pop()

if __name__ == "__main__":
    main()
