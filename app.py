import streamlit as st
import random

# 1. Page Configuration
st.set_page_config(page_title="Med-Cloud Pro", layout="centered")

# 2. Premium CSS (Light Blue Theme & Rounded UI)
st.markdown("""
    <style>
    /* Global Background and Text */
    .stApp { background-color: #FFFFFF; }
    p, span, label, li { color: #1E3A8A !important; font-family: 'Segoe UI', sans-serif; }

    /* Centered Headline at the top */
    .top-headline {
        text-align: center; color: #1E3A8A; font-weight: bold; font-size: 26px; margin-bottom: 10px;
    }

    /* Light Blue Button - Less Width & Rounded Corners */
    .stButton>button {
        background-color: #A8C7FA !important; /* Medical Light Blue */
        color: #062E6F !important;
        border-radius: 15px !important; 
        border: none !important;
        padding: 8px 25px !important;
        font-weight: bold !important;
        width: auto !important; 
        min-width: 140px;
        display: block;
        margin: 0 auto; /* Centers the button */
    }
    .stButton>button:hover { background-color: #D1E3FF !important; }

    /* Transparent Buttons */
    .forgot-btn button, .create-btn button {
        background-color: transparent !important;
        color: #2563EB !important;
        border: none !important;
        text-align: left !important;
        padding: 0 !important;
    }

    /* Medical Input Box - Rounded */
    .stTextInput>div>div>input {
        background-color: #F0F4F9 !important;
        color: #1E3A8A !important;
        border: 1px solid #747775 !important;
        border-radius: 8px !important;
        padding: 12px !important;
    }
    
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

    # Continue Button - Light Blue & Centered in Middle
    st.write("")
    if st.button("Continue ➔"):
        st.session_state.page = "auth"
        st.rerun()

# --- PAGE 2: AUTH (Light Blue Sign-In) ---
elif st.session_state.page == "auth":
    st.write("")
    
    with st.container():
        # Header Row: Logo & Project Name
        logo_col, title_col = st.columns([0.15, 0.85])
        with logo_col:
            st.image("https://cdn-icons-png.flaticon.com/512/2966/2966327.png", width=35)
        with title_col:
            st.markdown("<h2 style='margin:0; padding-top:5px; color:#1E3A8A;'>Med-Cloud Pro</h2>", unsafe_allow_html=True)
        
        st.markdown("<h3 style='margin-top:10px;'>Sign in</h3>", unsafe_allow_html=True)
        
        # ID Box with Project Name Label and Example Placeholder
        st.markdown("<p style='margin-bottom:-10px; font-weight:bold;'>Med-Cloud ID</p>", unsafe_allow_html=True)
        user_id_input = st.text_input("", placeholder="ex: MED-1234", label_visibility="visible")
        
        # Forgot ID Link
        st.markdown("<div class='forgot-btn'>", unsafe_allow_html=True)
        if st.button("Forgot ID?"):
            st.toast("Please contact support.")
        st.markdown("</div>", unsafe_allow_html=True)
        
        st.write("")
        
        # Bottom Actions
        col_act1, col_act2 = st.columns([1, 1])
        with col_act1:
            st.markdown("<div class='create-btn'>", unsafe_allow_html=True)
            if st.button("Create account"):
                st.info("Registration MED-XXXX")
            st.markdown("</div>", unsafe_allow_html=True)
            
        with col_act2:
            # Light Blue Next button
            if st.button("Next"):
                if user_id_input:
                    st.session_state.user_id = user_id_input
                    st.session_state.page = "dashboard"
                    st.rerun()
                else:
                    st.error("Please enter ID")

    # Navigation back
    st.write("")
    if st.button("← Back", key="back_btn"):
        st.session_state.page = "welcome"
        st.rerun()
