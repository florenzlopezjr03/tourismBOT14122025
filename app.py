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

# Custom CSS for enhanced aesthetics with rich colors and backgrounds
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap');
    
    * {
        font-family: 'Poppins', sans-serif;
    }
    
    /* Animated main background */
    [data-testid="stMainBlockContainer"] {
        background: linear-gradient(135deg, #1a1a2e 0%, #16213e 25%, #0f3460 50%, #533483 75%, #c1121f 100%);
        background-size: 400% 400%;
        animation: gradient 15s ease infinite;
        padding: 2rem 1rem;
    }
    
    @keyframes gradient {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    
    /* Sidebar styling */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #1a1a2e 0%, #16213e 100%) !important;
    }
    
    /* Header with rich gradient */
    .header-container {
        background: linear-gradient(135deg, rgba(26, 26, 46, 0.95) 0%, rgba(22, 33, 62, 0.95) 50%, rgba(15, 52, 96, 0.95) 100%);
        color: white;
        padding: 60px 20px;
        border-radius: 20px;
        margin-bottom: 40px;
        text-align: center;
        box-shadow: 0 12px 30px rgba(193, 18, 31, 0.4);
        border: 2px solid rgba(193, 18, 31, 0.5);
    }
    
    .header-container h1 {
        font-size: 3.8em;
        margin: 0;
        text-shadow: 3px 3px 8px rgba(0, 0, 0, 0.5);
        background: linear-gradient(135deg, #ff6b6b, #ff8c42, #ffd700);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }
    
    .header-container p {
        font-size: 1.4em;
        margin: 15px 0 0 0;
        opacity: 0.95;
        color: #ffd700;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3);
    }
    
    /* Chat messages */
    .user-message {
        background: linear-gradient(135deg, #ff6b6b 0%, #ff8c42 100%);
        color: white;
        padding: 15px 20px;
        border-radius: 18px;
        margin: 10px 0;
        word-wrap: break-word;
        box-shadow: 0 6px 15px rgba(255, 107, 107, 0.3);
        border: 1px solid rgba(255, 255, 255, 0.2);
    }
    
    .bot-message {
        background: linear-gradient(135deg, #ffffff 0%, #f0f0f0 100%);
        color: #1a1a2e;
        padding: 15px 20px;
        border-radius: 18px;
        margin: 10px 0;
        border-left: 5px solid #ffd700;
        box-shadow: 0 6px 15px rgba(255, 215, 0, 0.2);
        border: 1px solid rgba(255, 215, 0, 0.3);
    }
    
    /* About section styling */
    .about-card {
        background: linear-gradient(135deg, rgba(255, 255, 255, 0.95) 0%, rgba(240, 240, 240, 0.95) 100%);
        border-radius: 15px;
        padding: 25px;
        margin: 15px 0;
        border-left: 6px solid #ff6b6b;
        box-shadow: 0 8px 20px rgba(255, 107, 107, 0.2);
        backdrop-filter: blur(10px);
    }
    
    .feature-item {
        background: linear-gradient(135deg, rgba(255, 107, 107, 0.1) 0%, rgba(255, 140, 66, 0.1) 100%);
        padding: 18px;
        border-radius: 12px;
        margin: 12px 0;
        border-left: 4px solid #ff6b6b;
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        border: 1px solid rgba(255, 107, 107, 0.2);
    }
    
    .feature-item:hover {
        transform: translateX(10px) scale(1.02);
        background: linear-gradient(135deg, rgba(255, 107, 107, 0.2) 0%, rgba(255, 140, 66, 0.2) 100%);
        box-shadow: 0 8px 20px rgba(255, 107, 107, 0.2);
    }
    
    /* Button styling */
    .stButton > button {
        background: linear-gradient(135deg, #ff6b6b 0%, #ff8c42 100%) !important;
        color: white !important;
        border: none !important;
        border-radius: 25px !important;
        padding: 12px 24px !important;
        font-weight: 600 !important;
        transition: all 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275) !important;
        box-shadow: 0 4px 15px rgba(255, 107, 107, 0.3) !important;
    }
    
    .stButton > button:hover {
        transform: translateY(-3px) scale(1.05);
        box-shadow: 0 8px 25px rgba(255, 107, 107, 0.5) !important;
    }
    
    .stButton > button:active {
        transform: translateY(-1px) scale(0.98);
    }
    
    /* Chat container */
    .chat-container {
        background: linear-gradient(135deg, rgba(255, 255, 255, 0.95) 0%, rgba(245, 245, 245, 0.95) 100%);
        border-radius: 15px;
        padding: 25px;
        margin: 20px 0;
        box-shadow: 0 8px 25px rgba(0, 0, 0, 0.15);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 215, 0, 0.2);
    }
    
    /* Footer styling */
    .footer-section {
        text-align: center;
        padding: 30px 20px;
        background: linear-gradient(135deg, rgba(26, 26, 46, 0.8) 0%, rgba(15, 52, 96, 0.8) 100%);
        color: white;
        margin-top: 40px;
        border-radius: 15px;
        border-top: 2px solid rgba(255, 215, 0, 0.3);
    }
    
    /* Badges */
    .badge {
        display: inline-block;
        background: linear-gradient(135deg, #ff6b6b 0%, #ff8c42 100%);
        color: white;
        padding: 8px 20px;
        border-radius: 20px;
        font-size: 0.9em;
        margin: 10px 5px;
        font-weight: 600;
        box-shadow: 0 4px 15px rgba(255, 107, 107, 0.3);
    }
    
    /* Headings */
    h1, h2, h3, h4, h5, h6 {
        color: #ff6b6b !important;
    }
    
    /* Welcome message */
    .welcome-box {
        background: linear-gradient(135deg, rgba(255, 107, 107, 0.1) 0%, rgba(255, 140, 66, 0.1) 100%);
        border: 2px solid rgba(255, 215, 0, 0.3);
        padding: 30px;
        border-radius: 15px;
        text-align: center;
        color: white;
    }
    
    .welcome-box p {
        font-size: 1.1em;
        margin: 10px 0;
        color: white;
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
    <p>✨ Your AI-Powered Travel Companion ✨</p>
    <p style="font-size: 1em; margin-top: 20px; opacity: 0.9; color: #fff;">Discover amazing destinations, plan unforgettable journeys, and travel like a local</p>
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
    <div class="welcome-box">
        <p style="font-size: 1.3em; margin: 0;">👋 Welcome to Tourism Bot!</p>
        <p>Ask me about your dream destinations, plan your itinerary, or get travel tips</p>
        <p style="font-size: 0.9em; margin-top: 15px; opacity: 0.9;">🌟 Try asking about beaches, budgets, culture, or your favorite destination</p>
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
