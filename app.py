import streamlit as st
import random

# 1. Page Configuration
st.set_page_config(page_title="Med-Cloud Pro", layout="centered")

# 2. CSS - Version 2.5 (LOCKED DESIGN)
st.markdown("""
    <style>
    .stApp { background-color: #FFFFFF; }
    p, span, label, li { color: #1E3A8A !important; font-family: 'Segoe UI', sans-serif; }

    .center-text { text-align: center !important; display: block; margin: 0 auto; }

    .stepper { display: flex; justify-content: center; margin-bottom: 25px; }
    .step-dot { height: 6px; width: 35px; background-color: #1A73E8; border-radius: 4px; margin: 0 4px; }
    .step-dot-off { height: 6px; width: 35px; background-color: #E2E8F0; border-radius: 4px; margin: 0 4px; }

    .top-headline { text-align: center; color: #1E3A8A; font-weight: bold; font-size: 26px; margin-bottom: 10px; }

    /* Main Action Buttons (Create/Next/Continue) */
    .stButton>button {
        background-color: #1A73E8 !important;
        color: white !important;
        border-radius: 8px !important;
        border: none !important;
        padding: 8px 16px !important;
        font-weight: 500 !important;
        font-size: 14px !important;
        width: auto !important;
        min-width: 120px;
        display: block;
        margin: 0 auto; 
    }

    /* Input Box Visibility & Cursor Focus */
    ::placeholder { color: #4A5568 !important; opacity: 1; }
    .stTextInput>div>div>input {
        background-color: #F8FAFC !important;
        color: #000000 !important;
        border: 1px solid #747775 !important;
        border-radius: 6px !important;
        padding: 10px !important;
        font-size: 16px !important;
        cursor: text !important; /* Ensures cursor shows for typing */
    }

    /* FORGET ID - BACK TO ORIGINAL TEXT LINK (No Button Shape/Color) */
    .forgot-link-btn {
        background: none !important;
        border: none !important;
        padding: 0 !important;
        color: #1A73E8 !important;
        text-decoration: none !important;
        font-size: 13px !important;
        font-weight: 500 !important;
        cursor: pointer !important;
        margin-top: -30px; /* Aligned exactly below the box */
        display: block;
    }
    
    header {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# Initialize Session States
if 'page' not in st.session_state: st.session_state.page = "welcome"
if 'user_id' not in st.session_state: st.session_state.user_id = None

# --- PAGE 1: WELCOME (LOCKED) ---
if st.session_state.page == "welcome":
    st.markdown("<div class='top-headline'>Smart Healthcare Monitoring & Caretaker Escalation</div>", unsafe_allow_html=True)
    st.image("https://img.freepik.com/free-vector/health-professional-team-concept-illustration_114360-1608.jpg", use_container_width=True)

    col_a, col_b = st.columns(2)
    with col_a:
        st.markdown("**What it does:**\n* Tracks daily pill schedules.\n* Alerts caretakers if missed.")
    with col_b:
        st.markdown("**Main Advantages:**\n* Secure Unique IDs.\n* Built-in AI Doctor.")

    st.markdown("<p class='center-text'>Thank you for choosing Med-Cloud to manage your health journey!</p>", unsafe_allow_html=True)
    st.write("")
    if st.button("Continue ➔", key="btn_welcome"):
        st.session_state.page = "auth"
        st.rerun()

# --- PAGE 2: AUTH (LOCKED DESIGN) ---
elif st.session_state.page == "auth":
    st.markdown("""<div class='stepper'><div class='step-dot'></div><div class='step-dot-off'></div><div class='step-dot-off'></div></div>""", unsafe_allow_html=True)
    with st.container():
        l_col, t_col = st.columns([0.1, 0.9])
        with l_col: st.image("https://cdn-icons-png.flaticon.com/512/2966/2966327.png", width=30)
        with t_col: st.markdown("<h2 style='margin:0; color:#1E3A8A; font-size:22px;'>Med-Cloud Pro</h2>", unsafe_allow_html=True)
        st.markdown("<h3 style='margin-top:10px; font-size:24px;'>Sign in</h3>", unsafe_allow_html=True)
        st.markdown("<p style='margin-top:-15px; font-size:14px; color:#5F6368 !important;'>Access your secure health dashboard</p>", unsafe_allow_html=True)
        
        st.markdown("<p style='margin-bottom:-15px; font-weight:500; font-size:14px;'>Med-Cloud ID</p>", unsafe_allow_html=True)
        
        # User ID Input - Typing Enabled
        user_id_input = st.text_input("", placeholder="ex: (MED-1234)", key="input_med_id")
        
        # Forgot ID - Text Link Only (No button styling)
        if st.button("Forgot ID?", key="forgot_text_link", help="Recover your ID"):
            st.session_state.page = "forgot_id"
            st.rerun()
            
        # CSS hack to make the above button look like a text link
        st.markdown("""
            <style>
            div[data-testid="stButton"] button[kind="secondary"]:has(div:contains("Forgot ID?")) {
                background: none !important;
                border: none !important;
                color: #1A73E8 !important;
                padding: 0 !important;
                margin-top: -30px !important;
                font-size: 13px !important;
                text-align: left !important;
                display: block !important;
            }
            </style>
        """, unsafe_allow_html=True)

        st.write("")
        c_act1, c_act2 = st.columns([1, 1])
        with c_act1:
            if st.button("Create account", key="btn_create"):
                st.session_state.page = "create_account"
                st.rerun()
        with c_act2:
            if st.button("Next", key="btn_next"):
                if user_id_input:
                    st.session_state.user_id = user_id_input
                    st.session_state.page = "dashboard"
                    st.rerun()
                else: st.error("Please enter ID")

    st.write("")
    if st.button("← Back", key="btn_back"):
        st.session_state.page = "welcome"
        st.rerun()

# --- NEW PAGES (PLACEHOLDERS) ---
elif st.session_state.page == "dashboard":
    st.title(f"Dashboard: {st.session_state.user_id}")
    if st.button("Logout"):
        st.session_state.page = "auth"
        st.rerun()

elif st.session_state.page == "forgot_id":
    st.title("ID Recovery Page")
    if st.button("Back"):
        st.session_state.page = "auth"
        st.rerun()

elif st.session_state.page == "create_account":
    st.title("Registration Page")
    if st.button("Back"):
        st.session_state.page = "auth"
        st.rerun()
