import streamlit as st
import random

# 1. Page Configuration
st.set_page_config(page_title="Med-Cloud Pro", layout="centered")

# 2. CSS - FINAL LOCKED DESIGN (V2.5)
st.markdown("""
    <style>
    /* Force background and global text color */
    .stApp { background-color: #FFFFFF; }
    
    /* Global Blue Text for labels and paragraphs */
    p, span, label, li { color: #1E3A8A !important; font-family: 'Segoe UI', sans-serif; }

    .center-text { text-align: center !important; display: block; margin: 0 auto; }

    .stepper { display: flex; justify-content: center; margin-bottom: 25px; }
    .step-dot { height: 6px; width: 35px; background-color: #1A73E8; border-radius: 4px; margin: 0 4px; }
    .step-dot-off { height: 6px; width: 35px; background-color: #E2E8F0; border-radius: 4px; margin: 0 4px; }

    /* Header: Icon and Text on same line with Fixed Blue Color */
    .header-container {
        display: flex;
        align-items: center;
        gap: 10px;
        margin-bottom: 10px;
    }
    .header-container h2 {
        color: #1E3A8A !important; 
        margin: 0 !important;
        font-size: 22px !important;
        font-family: 'Segoe UI', sans-serif;
    }

    /* Next Button: Wide & Short */
    div[data-testid="stButton"] button:has(div p:contains("Next")) {
        background-color: #1A73E8 !important;
        color: white !important;
        border-radius: 20px !important;
        border: none !important;
        padding: 0px !important; 
        font-weight: 500 !important;
        font-size: 14px !important;
        width: 120px !important; 
        height: 30px !important; 
        display: block;
        margin: 0 auto; 
    }

    /* ID Box & Blinking Cursor */
    ::placeholder { color: #4A5568 !important; opacity: 1; }
    .stTextInput>div>div>input {
        background-color: #F8FAFC !important;
        color: #000000 !important;
        border: 1px solid #747775 !important;
        border-radius: 4px !important;
        padding: 12px !important;
        font-size: 16px !important;
        caret-color: #1A73E8 !important;
    }
    
    /* Forgot ID: Small, Blue, No Button styling, 1.3cm Gap */
    div[data-testid="stButton"] button:has(div p:contains("Forgot ID?")) {
        background: transparent !important;
        border: none !important;
        color: #1A73E8 !important;
        padding: 0 !important;
        font-weight: 500 !important;
        font-size: 11px !important; 
        box-shadow: none !important;
        width: auto !important;
        display: block !important;
        text-align: left !important;
        margin-top: 25px !important; /* The 1.3cm gap */
    }

    /* Create account as a text link */
    div[data-testid="stButton"] button:has(div p:contains("Create account")) {
        background: transparent !important;
        border: none !important;
        color: #1A73E8 !important;
        padding: 0 !important;
        font-weight: 500 !important;
        font-size: 14px !important;
        box-shadow: none !important;
        width: auto !important;
    }

    header {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# Session State
if 'page' not in st.session_state: st.session_state.page = "welcome"

# --- PAGE 1: WELCOME ---
if st.session_state.page == "welcome":
    st.markdown("<h1 class='top-headline' style='color:#1E3A8A; text-align:center;'>Smart Healthcare Monitoring</h1>", unsafe_allow_html=True)
    st.image("https://img.freepik.com/free-vector/health-professional-team-concept-illustration_114360-1608.jpg", use_container_width=True)
    if st.button("Continue ➔", key="welcome_go"):
        st.session_state.page = "auth"
        st.rerun()

# --- PAGE 2: AUTH (LOCKED) ---
elif st.session_state.page == "auth":
    st.markdown("""<div class='stepper'><div class='step-dot'></div><div class='step-dot-off'></div><div class='step-dot-off'></div></div>""", unsafe_allow_html=True)
    
    with st.container():
        # Re-applying the Blue Header
        st.markdown("""
            <div class='header-container'>
                <img src='https://cdn-icons-png.flaticon.com/512/2966/2966327.png' width='30'>
                <h2>Med-Cloud Pro</h2>
            </div>
        """, unsafe_allow_html=True)
        
        st.markdown("<h3 style='margin-top:10px; font-size:24px; color:#1E3A8A;'>Sign in</h3>", unsafe_allow_html=True)
        st.markdown("<p style='margin-top:-15px; font-size:14px; color:#5F6368 !important;'>Access your secure health dashboard</p>", unsafe_allow_html=True)
        
        st.markdown("<p style='margin-bottom:-15px; font-weight:500; font-size:14px; color:#1E3A8A;'>Med-Cloud ID</p>", unsafe_allow_html=True)
        user_id_input = st.text_input("", placeholder="ex: (MED-1234)", key="input_main")
        
        if st.button("Forgot ID?", key="forgot_final"):
            st.session_state.page = "forgot_id"
            st.rerun()

        st.write("")
        c1, c2 = st.columns([1, 1])
        with c1:
            if st.button("Create account", key="create_final"):
                st.session_state.page = "create_account"
                st.rerun()
        with c2:
            if st.button("Next", key="next_final"):
                if user_id_input:
                    st.session_state.user_id = user_id_input
                    st.session_state.page = "dashboard"
                    st.rerun()
    
    st.write("")
    if st.button("← Back", key="back_final"):
        st.session_state.page = "welcome"
        st.rerun()

# --- OTHER PAGES ---
elif st.session_state.page == "dashboard":
    st.title("Dashboard")
    if st.button("Logout"): st.session_state.page = "auth"; st.rerun()

elif st.session_state.page == "forgot_id":
    st.title("Recovery")
    if st.button("Back"): st.session_state.page = "auth"; st.rerun()

elif st.session_state.page == "create_account":
    st.title("Registration")
    if st.button("Back"): st.session_state.page = "auth"; st.rerun()
