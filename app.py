import streamlit as st
import random

# 1. Page Configuration
st.set_page_config(page_title="Med-Cloud Pro", layout="centered")

# 2. CSS - FINAL LOCKED DESIGN (V2.5)
st.markdown("""
    <style>
    .stApp { background-color: #FFFFFF; }
    p, span, label, li { color: #1E3A8A !important; font-family: 'Segoe UI', sans-serif; }

    .center-text { text-align: center !important; display: block; margin: 0 auto; }

    .stepper { display: flex; justify-content: center; margin-bottom: 25px; }
    .step-dot { height: 6px; width: 35px; background-color: #1A73E8; border-radius: 4px; margin: 0 4px; }
    .step-dot-off { height: 6px; width: 35px; background-color: #E2E8F0; border-radius: 4px; margin: 0 4px; }

    /* Header Alignment: Icon and Text on same line */
    .header-container {
        display: flex;
        align-items: center;
        gap: 10px;
        margin-bottom: 10px;
    }

    /* Main Action Button (Next) - INCREASED WIDTH & DECREASED HEIGHT */
    div[data-testid="stButton"] button:has(div p:contains("Next")) {
        background-color: #1A73E8 !important;
        color: white !important;
        border-radius: 20px !important;
        border: none !important;
        padding: 4px 0px !important; /* Decreased height by reducing vertical padding */
        font-weight: 500 !important;
        font-size: 14px !important;
        width: 110px !important; /* Increased width */
        height: 32px !important; /* Fixed shorter height */
        display: block;
        margin: 0 auto; 
    }

    /* Big Box & Blinking Cursor */
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
    
    /* FORGOT ID: Pure text, smaller size, 1.3cm (approx 50px) gap */
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
        margin-top: 25px !important; /* 1.3cm gap from box */
        margin-bottom: 20px !important;
    }

    /* Create account text link */
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

# Initialize Session States
if 'page' not in st.session_state: st.session_state.page = "welcome"
if 'user_id' not in st.session_state: st.session_state.user_id = None

# --- PAGE 1: WELCOME ---
if st.session_state.page == "welcome":
    st.markdown("<div class='top-headline'>Smart Healthcare Monitoring</div>", unsafe_allow_html=True)
    st.image("https://img.freepik.com/free-vector/health-professional-team-concept-illustration_114360-1608.jpg", use_container_width=True)
    if st.button("Continue ➔", key="welcome_go"):
        st.session_state.page = "auth"
        st.rerun()

# --- PAGE 2: AUTH (LOCKED DESIGN) ---
elif st.session_state.page == "auth":
    st.markdown("""<div class='stepper'><div class='step-dot'></div><div class='step-dot-off'></div><div class='step-dot-off'></div></div>""", unsafe_allow_html=True)
    
    with st.container():
        st.markdown("""
            <div class='header-container'>
                <img src='https://cdn-icons-png.flaticon.com/512/2966/2966327.png' width='30'>
                <h2 style='margin:0; color:#1E3A8A; font-size:22px;'>Med-Cloud Pro</h2>
            </div>
        """, unsafe_allow_html=True)
        
        st.markdown("<h3 style='margin-top:10px; font-size:24px;'>Sign in</h3>", unsafe_allow_html=True)
        st.markdown("<p style='margin-top:-15px; font-size:14px; color:#5F6368 !important;'>Access your secure health dashboard</p>", unsafe_allow_html=True)
        
        st.markdown("<p style='margin-bottom:-15px; font-weight:500; font-size:14px;'>Med-Cloud ID</p>", unsafe_allow_html=True)
        user_id_input = st.text_input("", placeholder="ex: (MED-1234)", key="input_main")
        
        if st.button("Forgot ID?", key="forgot_final"):
            st.session_state.page = "forgot_id"
            st.rerun()

        c_act1, c_act2 = st.columns([1, 1])
        with c_act1:
            if st.button("Create account", key="create_final"):
                st.session_state.page = "create_account"
                st.rerun()
        with c_act2:
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
    st.title("Main Dashboard")
    if st.button("Logout"): st.session_state.page = "auth"; st.rerun()

elif st.session_state.page == "forgot_id":
    st.title("Recovery Page")
    if st.button("Back"): st.session_state.page = "auth"; st.rerun()

elif st.session_state.page == "create_account":
    st.title("Registration Page")
    if st.button("Back"): st.session_state.page = "auth"; st.rerun()
