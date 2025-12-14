#!/usr/bin/env python3
"""
Tourism Bot - Enhanced Streamlit Web Application
Powered by Mistral AI with Beautiful UI and Engaging Design
"""

import streamlit as st
from mistralai import Mistral

# Page configuration
st.set_page_config(
    page_title="🌍 Tourism Bot - Your Travel Companion",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for enhanced aesthetics
st.markdown("""
    <style>
    /* Main styling */
    [data-testid="stMainBlockContainer"] {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem 1rem;
    }
    
    /* Chat messages */
    .user-message {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 15px 20px;
        border-radius: 18px;
        margin: 10px 0;
        word-wrap: break-word;
    }
    
    .bot-message {
        background: white;
        color: #262730;
        padding: 15px 20px;
        border-radius: 18px;
        margin: 10px 0;
        border-left: 5px solid #667eea;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    
    /* Header section */
    .header-container {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 60px 20px;
        border-radius: 20px;
        margin-bottom: 40px;
        text-align: center;
        box-shadow: 0 8px 20px rgba(102, 126, 234, 0.3);
    }
    
    .header-container h1 {
        font-size: 3.5em;
        margin: 0;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.2);
    }
    
    .header-container p {
        font-size: 1.4em;
        margin: 15px 0 0 0;
        opacity: 0.95;
    }
    
    /* About section styling */
    .about-card {
        background: white;
        border-radius: 15px;
        padding: 25px;
        margin: 15px 0;
        border-left: 6px solid #667eea;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
    }
    
    .feature-item {
        background: linear-gradient(135deg, #667eea10 0%, #764ba210 100%);
        padding: 18px;
        border-radius: 12px;
        margin: 12px 0;
        border-left: 4px solid #667eea;
        transition: transform 0.3s;
    }
    
    .feature-item:hover {
        transform: translateX(5px);
    }
    
    /* Button styling */
    .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%) !important;
        color: white !important;
        border: none !important;
        border-radius: 25px !important;
        padding: 12px 24px !important;
        font-weight: 500 !important;
        transition: all 0.3s !important;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 12px rgba(102, 126, 234, 0.4) !important;
    }
    
    /* Chat container */
    .chat-container {
        background: white;
        border-radius: 15px;
        padding: 25px;
        margin: 20px 0;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
    }
    
    /* Destination cards */
    .destination-btn {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 12px 15px;
        border-radius: 12px;
        border: none;
        margin: 5px;
        cursor: pointer;
        transition: all 0.3s;
    }
    
    .destination-btn:hover {
        transform: translateY(-3px);
        box-shadow: 0 6px 12px rgba(102, 126, 234, 0.4);
    }
    
    /* Footer styling */
    .footer-section {
        text-align: center;
        padding: 30px 20px;
        color: white;
        margin-top: 40px;
    }
    
    .badge {
        display: inline-block;
        background: #28a745;
        color: white;
        padding: 8px 16px;
        border-radius: 20px;
        font-size: 0.9em;
        margin: 10px 5px;
    }
    </style>
""", unsafe_allow_html=True)

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Initialize Mistral client
API_KEY = "8rJkzPuf6KRuuX90wNSShAW2RNe5B1XB"
try:
    client = Mistral(api_key=API_KEY)
except Exception as e:
    st.error(f"Failed to initialize Mistral client: {str(e)}")
    st.stop()

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
Use emojis to make responses engaging and visually appealing.
When relevant, ask follow-up questions to better understand what the user is looking for.
Format your response with clear sections, bullet points, and highlights."""

# Header Section
st.markdown("""
<div class="header-container">
    <h1>🌍 Tourism Bot</h1>
    <p>Your AI-Powered Travel Companion</p>
    <p style="font-size: 1em; margin-top: 20px; opacity: 0.9;">Explore the world with personalized recommendations and expert travel advice</p>
</div>
""", unsafe_allow_html=True)

# Sidebar - Enhanced About Section
with st.sidebar:
    st.markdown("""
    <div style="text-align: center; padding: 20px 0;">
        <h2 style="color: #667eea; font-size: 2em;">✈️ About Tourism Bot</h2>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="about-card">
        <p><strong>Welcome to Your Travel Companion!</strong></p>
        <p style="font-size: 0.95em; line-height: 1.8; color: #555;">
        Tourism Bot is an intelligent travel assistant powered by advanced AI. We help millions of travelers discover destinations, 
        plan itineraries, and get expert advice for unforgettable adventures.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<h4 style='color: #667eea; margin-top: 25px; text-align: center;'>🎯 Our Features</h4>", unsafe_allow_html=True)
    
    features = [
        ("🗺️", "Smart Discovery", "Find perfect destinations based on your interests and budget"),
        ("📋", "Plan with Ease", "Create detailed itineraries with day-by-day recommendations"),
        ("💰", "Budget Friendly", "Get money-saving tips and cost breakdowns"),
        ("🏨", "Stay & Eat", "Discover great hotels, restaurants, and local food"),
        ("🌐", "Cultural Insights", "Learn customs, traditions, and local wisdom"),
        ("📚", "Travel Essentials", "Visa info, safety tips, and travel guidelines"),
    ]
    
    for emoji, title, desc in features:
        st.markdown(f"""
        <div class="feature-item">
            <p style="margin: 0; font-weight: bold;"><span style="font-size: 1.5em;">{emoji}</span> {title}</p>
            <p style="margin: 8px 0 0 0; font-size: 0.85em; color: #666;">{desc}</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.divider()
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🗑️ Clear", use_container_width=True):
            st.session_state.messages = []
            st.rerun()
    with col2:
        if st.button("✨ New Chat", use_container_width=True):
            st.session_state.messages = []
            st.rerun()
    
    st.divider()
    
    st.markdown("<h4 style='color: #667eea; margin-top: 20px;'>🌟 Popular Destinations</h4>", unsafe_allow_html=True)
    
    destinations = [
        ("🏖️ Maldives", "Best for relaxation and water sports"),
        ("🗾 Japan", "Culture, food, and technology"),
        ("🇹🇭 Thailand", "Budget-friendly tropical paradise"),
        ("🗼 France", "Romance and artistic heritage"),
        ("🌴 Bali", "Beaches, temples, and culture"),
        ("🇮🇹 Italy", "History, art, and cuisine"),
    ]
    
    for dest, desc in destinations:
        if st.button(f"**{dest}** - {desc}", use_container_width=True):
            st.session_state.messages = []
            st.session_state.messages.append({"role": "user", "content": f"Tell me about {dest.split()[1]}"})
            st.rerun()

# Main Chat Area
st.markdown('<div class="chat-container">', unsafe_allow_html=True)

# Display chat history with enhanced styling
if st.session_state.messages:
    for message in st.session_state.messages:
        if message["role"] == "user":
            col1, col2, col3 = st.columns([0.5, 2, 0.5])
            with col2:
                st.markdown(f'<div class="user-message">👤 {message["content"]}</div>', unsafe_allow_html=True)
        else:
            col1, col2, col3 = st.columns([0.5, 2, 0.5])
            with col2:
                st.markdown(f'<div class="bot-message">🤖 {message["content"]}</div>', unsafe_allow_html=True)
else:
    st.markdown("""
    <div style="text-align: center; padding: 40px 20px; color: #999;">
        <p style="font-size: 1.2em;">👋 Welcome to Tourism Bot!</p>
        <p>Ask me about your dream destinations, plan your itinerary, or get travel tips</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# Input Section
st.markdown('<div class="chat-container">', unsafe_allow_html=True)

user_input = st.chat_input(
    "✍️ Ask me about destinations, itineraries, budgets, culture...",
    key="user_input"
)

if user_input:
    # Add user message to history
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    # Display user message
    col1, col2, col3 = st.columns([0.5, 2, 0.5])
    with col2:
        st.markdown(f'<div class="user-message">👤 {user_input}</div>', unsafe_allow_html=True)
    
    # Generate bot response
    with st.spinner("🤖 Thinking... This may take a moment..."):
        try:
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
            
            # Add to history
            st.session_state.messages.append({"role": "assistant", "content": bot_response})
            
            # Display response
            col1, col2, col3 = st.columns([0.5, 2, 0.5])
            with col2:
                st.markdown(f'<div class="bot-message">🤖 {bot_response}</div>', unsafe_allow_html=True)
            
            st.rerun()
        
        except Exception as e:
            st.error(f"❌ Error: {str(e)}")
            if st.session_state.messages and st.session_state.messages[-1]["role"] == "user":
                st.session_state.messages.pop()

st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown("""
<div class="footer-section">
    <div style="display: flex; justify-content: center; gap: 20px; flex-wrap: wrap;">
        <span class="badge">🌍 Global Reach</span>
        <span class="badge">🤖 AI-Powered</span>
        <span class="badge">24/7 Available</span>
    </div>
    <p style="margin-top: 20px; font-size: 0.9em; color: #999;">
        Tourism Bot v1.0 | Powered by Mistral AI | Messages: """ + str(len(st.session_state.messages)) + """
    </p>
    <p style="font-size: 0.85em; color: #999;">Happy travels! 🌴 ✈️ 🗺️</p>
</div>
""", unsafe_allow_html=True)
