#!/usr/bin/env python3
"""
Tourism Bot - Streamlit Web Application
Powered by Mistral AI
Fixed version with proper error handling
"""

import streamlit as st
from mistralai import Mistral

# Page configuration
st.set_page_config(
    page_title="Tourism Bot 🌍",
    page_icon="🌍",
    layout="wide"
)

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []

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

# Title
st.title("🌍 Tourism Bot")
st.subheader("Your AI Travel Assistant Powered by Mistral AI")

# Sidebar
with st.sidebar:
    st.header("ℹ️ About")
    st.write("""
    Tourism Bot helps you plan your next adventure with:
    - **Destination Recommendations** - Find perfect travel destinations
    - **Itinerary Planning** - Create travel schedules
    - **Budget Travel Tips** - Save money while traveling
    - **Local Insights** - Learn about culture and customs
    - **Practical Info** - Visas, safety, transportation
    """)
    
    st.divider()
    
    if st.button("🗑️ Clear Chat", use_container_width=True):
        st.session_state.messages = []
        st.rerun()
    
    st.divider()
    
    st.subheader("💡 Try These Questions")
    example_prompts = [
        "🏖️ Best beach destinations for 2025",
        "💰 Budget travel destinations under $1000/month",
        "🗺️ 7-day Europe itinerary",
        "🍜 Best street food in Asia",
        "✈️ Visa requirements for US citizens",
        "🏨 Hidden gems in Southeast Asia",
    ]
    
    for prompt in example_prompts:
        if st.button(prompt, use_container_width=True):
            st.session_state.user_input = prompt

# Display chat history
st.divider()
for message in st.session_state.messages:
    with st.chat_message(message["role"], avatar="👤" if message["role"] == "user" else "🤖"):
        st.markdown(message["content"])

st.divider()

# Chat input
user_input = st.chat_input("Ask me about destinations, travel tips, itineraries...", key="user_input")

if user_input:
    # Add user message to history
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    # Display user message
    with st.chat_message("user", avatar="👤"):
        st.markdown(user_input)
    
    # Generate bot response
    with st.chat_message("assistant", avatar="🤖"):
        message_placeholder = st.empty()
        
        try:
            with st.spinner("Thinking..."):
                # Build messages for API
                api_messages = [{"role": "system", "content": SYSTEM_PROMPT}]
                for msg in st.session_state.messages:
                    api_messages.append({"role": msg["role"], "content": msg["content"]})
                
                # Call Mistral API
                response = client.chat.complete(
                    model="mistral-large-latest",
                    messages=api_messages
                )
                
                bot_response = response.choices[0].message.content
                
                # Display response
                message_placeholder.markdown(bot_response)
                
                # Add to history
                st.session_state.messages.append({"role": "assistant", "content": bot_response})
        
        except Exception as e:
            error_msg = f"❌ Error: {str(e)}\n\nPlease try again or contact support."
            message_placeholder.error(error_msg)
            # Remove the user message if error occurred
            if st.session_state.messages and st.session_state.messages[-1]["role"] == "user":
                st.session_state.messages.pop()

# Footer
st.divider()
col1, col2, col3 = st.columns([1, 1, 1])
with col1:
    st.caption("🌍 Tourism Bot v1.0")
with col2:
    st.caption("Powered by Mistral AI")
with col3:
    st.caption(f"Messages: {len(st.session_state.messages)}")
