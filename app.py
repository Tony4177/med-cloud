import streamlit as st
import random

# 1. Page Configuration
st.set_page_config(page_title="Med-Cloud Pro", layout="centered")

# 2. Premium CSS (Medical Theme - No Black, Rounded Corners)
st.markdown("""
    <style>
    /* Global Background and Text */
    .stApp { background-color: #FFFFFF; }
    p, span, label, li { color: #1E3A8A !important; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; }

    /* Centered Headline at the top */
    .top-headline {
        text-align: center; color: #1E3A8A; font-weight: bold; font-size: 26px; margin-bottom: 10px;
    }

    /* Primary Blue Button - Less Width & Rounded Corners */
    .stButton>button {
        background-color: #2563EB !important;
        color: white !important;
        border-radius: 12px !important; /* Rounded corners */
        border: none !important;
        padding: 8px 20px !important;
        font-weight: bold !important;
        width: auto !important; /* Less width */
        min-width: 120px;
        display: block;
        margin: 0 auto;
    }
    .stButton>button:hover { background-color: #1E40AF !important; }

    /* Transparent Buttons for 'Forgot ID' and 'Create Account' */
    .forgot-btn button, .create-btn button {
        background-color: transparent !important;
        color: #2563EB !important;
        border: none !important;
        text-decoration: none !important;
        font-weight: normal !important;
        padding: 0 !important;
        box-shadow: none !important;
    }

    /* Medical Input Box - Rounded with Blue Border */
    .stTextInput>div>div>input {
        background-color: #F8FAFC !important;
        color: #1E3A8A !important;
        border: 2px solid #E2E8F0 !important;
        border-radius: 12px !important; /* Rounded corners */
        padding: 10px !important;
    }
    .stTextInput>div>div>input:focus {
        border-color: #2563EB !important;
    }

    /* Custom spacing for Sign-In Interface */
    .auth-container {
        padding: 30px;
        border: 1px solid #E2E8F0;
        border-radius: 20px;
        margin-top: 20px;
    }
    
    /* Hide Streamlit components */
    header {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# Initialize Session States
if 'page' not in st.session_state: st.session_state.page = "welcome"
if 'user_id' not in st.session_state: st.session_state.user_id = None

# --- PAGE 1: WELCOME ---
if st.session_state.page == "welcome":
    st.markdown("<div class='top-headline'>Smart Healthcare Monitoring & Caretaker Escalation</div>", unsafe_allow_html=True)
    st.image("https://img.freepik.com/free-vector/health-professional-team-concept-illustration_114360-1608.jpg", use_container_width=True)

    col_a, col_b = st.columns(2)
    with col_a:
        st.markdown("**What it does:**\n* Tracks daily pill schedules.\n* Alerts caretakers if missed.")
    with col_b:
        st.markdown("**Main Advantages:**\n* Secure Unique IDs.\n* Built-in AI Doctor.")

    st.markdown("<p style='text-align: center;'>Thank you for choosing Med-Cloud!</p>", unsafe_allow_html=True)

    # Continue Button - Blue, Less width, Centered
    st.write("")
    if st.button("Continue ➔"):
        st.session_state.page = "auth"
        st.rerun()

# --- PAGE 2: AUTH (Medical Sign-In) ---
elif st.session_state.page == "auth":
    # Spacer
    st.write("")
    
    # Sign-In Layout
    with st.container():
        # Header Row: Logo on Left, Project Name next to it
        logo_col, title_col = st.columns([0.15, 0.85])
        with logo_col:
            st.image("https://cdn-icons-png.flaticon.com/512/2966/2966327.png", width=35)
        with title_col:
            st.markdown("<h2 style='margin:0; padding-top:5px; color:#1E3A8A;'>Med-Cloud Pro</h2>", unsafe_allow_html=True)
        
        st.markdown("<h3 style='margin-top:10px;'>Sign in</h3>", unsafe_allow_html=True)
        
        # ID Box (Label 'ID' removed above the box, moved to placeholder)
        st.write("")
        user_id_input = st.text_input("", placeholder="Enter your Unique ID", label_visibility="collapsed")
        
        # Forgot ID Link (Styled as button)
        st.markdown("<div class='forgot-btn'>", unsafe_allow_html=True)
        if st.button("Forgot ID?"):
            st.toast("Contact your caretaker for ID recovery.")
        st.markdown("</div>", unsafe_allow_html=True)
        
        st.write("")
        st.write("")
        
        # Bottom Actions: Create Account and Next
        # Using columns to put them on opposite sides
        col_act1, col_act2 = st.columns([1, 1])
        with col_act1:
            st.markdown("<div class='create-btn'>", unsafe_allow_html=True)
            if st.button("Create account"):
                st.session_state.user_id = f"MED-{random.randint(1000,9999)}"
                st.success(f"New ID: {st.session_state.user_id}")
            st.markdown("</div>", unsafe_allow_html=True)
            
        with col_act2:
            # Blue Next button with less width
            if st.button("Next"):
                if user_id_input:
                    st.session_state.user_id = user_id_input
                    st.session_state.page = "dashboard"
                    st.rerun()
                else:
                    st.error("Please enter ID")

    # Back to Welcome link
    st.write("")
    if st.button("← Back to Welcome", key="back_btn"):
        st.session_state.page = "welcome"
        st.rerun()
