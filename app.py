import streamlit as st

# 1. Page Configuration
st.set_page_config(page_title="Med-Cloud Pro", layout="centered")

# 2. CSS - FINAL LOCKED DESIGN (V2.7)
st.markdown("""
    <style>
    .stApp { background-color: #FFFFFF; }
    
    /* Global Light Blue for Headers and Labels */
    h1, h2, h3, .top-headline, p, span, label, li {
        color: #1A73E8 !important;
        font-family: 'Segoe UI', sans-serif !important;
    }

    /* Next, Create Account, and Back Buttons: Light Blue Background */
    div[data-testid="stButton"] button:has(div p:contains("Next")),
    div[data-testid="stButton"] button:has(div p:contains("Create account")),
    div[data-testid="stButton"] button:has(div p:contains("Back")) {
        background-color: #1A73E8 !important;
        color: white !important;
        border-radius: 20px !important;
        border: none !important;
        padding: 6px 15px !important;
        font-weight: 500 !important;
        font-size: 14px !important;
        box-shadow: none !important;
    }

    /* Adjusting "Next" specifically for that wide/short look */
    div[data-testid="stButton"] button:has(div p:contains("Next")) {
        width: 120px !important;
        height: 32px !important;
        display: flex;
        align-items: center;
        justify-content: center;
    }

    /* ID BOX: Blinking Cursor Enabled */
    .stTextInput>div>div>input {
        background-color: #F8FAFC !important;
        color: #000000 !important;
        border: 1px solid #747775 !important;
        border-radius: 4px !important;
        padding: 12px !important;
        caret-color: #1A73E8 !important; /* Blinking blue line */
    }
    
    /* FORGOT ID: No background, Smaller letters, 1.5cm Gap */
    div[data-testid="stButton"] button:has(div p:contains("Forgot ID?")) {
        background: transparent !important;
        border: none !important;
        color: #1A73E8 !important; /* Light blue text only */
        padding: 0 !important;
        font-size: 10px !important; /* Decreased letter size */
        font-weight: 500 !important;
        box-shadow: none !important;
        width: auto !important;
        margin-top: 55px !important; /* Precise 1.5cm gap */
        text-align: left !important;
    }

    /* Stepper Styling */
    .stepper { display: flex; justify-content: center; margin-bottom: 25px; }
    .step-dot { height: 6px; width: 35px; background-color: #1A73E8; border-radius: 4px; margin: 0 4px; }
    .step-dot-off { height: 6px; width: 35px; background-color: #E2E8F0; border-radius: 4px; margin: 0 4px; }

    header {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# Session State Initialization
if 'page' not in st.session_state: st.session_state.page = "welcome"
if 'user_id' not in st.session_state: st.session_state.user_id = None

# --- PAGE 1: WELCOME ---
if st.session_state.page == "welcome":
    st.markdown("<h1 style='text-align:center;'>Smart Healthcare Monitoring</h1>", unsafe_allow_html=True)
    st.image("https://img.freepik.com/free-vector/health-professional-team-concept-illustration_114360-1608.jpg", use_container_width=True)
    if st.button("Continue ➔", key="welcome_go"):
        st.session_state.page = "auth"
        st.rerun()

# --- PAGE 2: AUTH (LOCKED) ---
elif st.session_state.page == "auth":
    st.markdown("""<div class='stepper'><div class='step-dot'></div><div class='step-dot-off'></div><div class='step-dot-off'></div></div>""", unsafe_allow_html=True)
    
    # Header: Icon and Name beside each other
    st.markdown("""
        <div style='display: flex; align-items: center; gap: 12px; margin-bottom: 10px;'>
            <img src='https://cdn-icons-png.flaticon.com/512/2966/2966327.png' width='30'>
            <h2 style='margin:0;'>Med-Cloud Pro</h2>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<h3>Sign in</h3>", unsafe_allow_html=True)
    st.markdown("<p style='margin-top:-15px; font-size:14px; color:#5F6368 !important;'>Access your secure health dashboard</p>", unsafe_allow_html=True)
    
    st.markdown("<p style='margin-bottom:-15px; font-weight:500; font-size:14px;'>Med-Cloud ID</p>", unsafe_allow_html=True)
    user_id_input = st.text_input("", placeholder="ex: (MED-1234)", key="input_main")
    
    # Forgot ID - Text only, tiny, 1.5cm gap
    if st.button("Forgot ID?", key="forgot_btn"):
        st.session_state.page = "forgot_id"
        st.rerun()

    st.write("")
    col_left, col_right = st.columns([1, 1])
    with col_left:
        # Create Account with Light Blue background
        if st.button("Create account", key="create_btn"):
            st.session_state.page = "create_account"
            st.rerun()
    with col_right:
        # Next with Light Blue background
        if st.button("Next", key="next_btn"):
            if user_id_input:
                st.session_state.user_id = user_id_input
                st.session_state.page = "dashboard"
                st.rerun()

    st.write("")
    # Back with Light Blue background
    if st.button("← Back", key="back_btn"):
        st.session_state.page = "welcome"
        st.rerun()

# --- OTHER PAGES ---
elif st.session_state.page == "dashboard":
    st.title("Main Dashboard")
    if st.button("Logout"): st.session_state.page = "auth"; st.rerun()
elif st.session_state.page == "forgot_id":
    st.title("Recovery")
    if st.button("Back"): st.session_state.page = "auth"; st.rerun()
elif st.session_state.page == "create_account":
    st.title("Registration")
    if st.button("Back"): st.session_state.page = "auth"; st.rerun()
