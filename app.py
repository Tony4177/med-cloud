import streamlit as st
import random

# 1. Page Configuration
st.set_page_config(page_title="Med-Cloud Pro", layout="centered")

# 2. CSS - FINAL LOCKED DESIGN & NEW DASHBOARD HEADER
st.markdown("""
    <style>
    .stApp { background-color: #FFFFFF; }
    
    /* GLOBAL LIGHT BLUE */
    h1, h2, h3, p, span, label {
        color: #1A73E8 !important;
        font-family: 'Segoe UI', sans-serif !important;
    }

    /* INPUT BOXES (Locked Style) */
    .stTextInput>div>div>input {
        background-color: #FFFFFF !important;
        color: #000000 !important;
        border: 1px solid #747775 !important;
        border-radius: 4px !important;
        padding: 12px !important;
        caret-color: #1A73E8 !important; 
    }

    /* FORGOT ID (Locked Style) */
    div[data-testid="stButton"] button:has(div p:contains("Forgot ID?")) {
        background: transparent !important;
        border: none !important;
        color: #1A73E8 !important;
        padding: 0 !important;
        font-size: 11px !important;
        box-shadow: none !important;
        width: auto !important;
        margin-top: 55px !important;
        display: block !important;
        text-align: left !important;
    }

    /* PRIMARY BUTTONS (Locked Style) */
    div[data-testid="stButton"] button:has(div p:contains("Next")),
    div[data-testid="stButton"] button:has(div p:contains("Create account")),
    div[data-testid="stButton"] button:has(div p:contains("Verify & Register")),
    div[data-testid="stButton"] button:has(div p:contains("Go to Sign In")),
    div[data-testid="stButton"] button:has(div p:contains("Sign Out")) {
        background-color: #1A73E8 !important;
        color: white !important;
        border-radius: 20px !important;
        border: none !important;
        padding: 4px 15px !important;
        font-weight: 500 !important;
        font-size: 14px !important;
    }

    /* DASHBOARD TOP BAR */
    .dashboard-header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 10px 0px;
        margin-bottom: 20px;
    }
    .profile-icon {
        width: 40px;
        height: 40px;
        background-color: #E8F0FE;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        cursor: pointer;
    }
    .menu-lines {
        cursor: pointer;
        display: flex;
        flex-direction: column;
        gap: 4px;
    }
    .line {
        width: 24px;
        height: 3px;
        background-color: #1A73E8;
        border-radius: 2px;
    }

    /* DASHBOARD CARD */
    .dashboard-card {
        padding: 20px;
        border-radius: 15px;
        background-color: #F0F7FF;
        border-left: 5px solid #1A73E8;
        margin-bottom: 20px;
    }

    header {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# Initialize Session State
if 'page' not in st.session_state: st.session_state.page = "welcome"
if 'current_user' not in st.session_state: st.session_state.current_user = None

# --- PAGE 1: WELCOME ---
if st.session_state.page == "welcome":
    st.markdown("<h1 style='text-align:center;'>Smart Healthcare Monitoring</h1>", unsafe_allow_html=True)
    st.image("https://img.freepik.com/free-vector/health-professional-team-concept-illustration_114360-1608.jpg", use_container_width=True)
    if st.button("Continue ➔", key="welcome_go"):
        st.session_state.page = "auth"; st.rerun()

# --- PAGE 2: AUTH (LOCKED) ---
elif st.session_state.page == "auth":
    st.markdown("""<div style='display: flex; align-items: center; gap: 12px; margin-bottom: 10px;'><img src='https://cdn-icons-png.flaticon.com/512/2966/2966327.png' width='30'><h2>Med-Cloud Pro</h2></div>""", unsafe_allow_html=True)
    st.markdown("<h3>Sign in</h3>", unsafe_allow_html=True)
    st.markdown("<p style='font-weight:500; font-size:14px;'>Med-Cloud ID</p>", unsafe_allow_html=True)
    user_id_input = st.text_input("", placeholder="ex: (MED-1234)", key="login_id")
    
    if st.button("Forgot ID?", key="forgot_btn"):
        st.session_state.page = "forgot_id"; st.rerun()

    col_l, col_r = st.columns([1, 1])
    with col_l:
        if st.button("Create account", key="create_trigger"):
            st.session_state.page = "create_account"; st.rerun()
    with col_r:
        if st.button("Next", key="next_btn"):
            if user_id_input: 
                st.session_state.current_user = user_id_input
                st.session_state.page = "dashboard"; st.rerun()

# --- PAGE 3: MAIN DASHBOARD (NEW HEADER) ---
elif st.session_state.page == "dashboard":
    # Custom Top Bar with Profile (Left) and Menu (Right)
    st.markdown("""
        <div class="dashboard-header">
            <div class="profile-icon">
                <img src="https://cdn-icons-png.flaticon.com/512/3135/3135715.png" width="30">
            </div>
            <h2 style="margin:0;">Dashboard</h2>
            <div class="menu-lines">
                <div class="line"></div>
                <div class="line"></div>
                <div class="line"></div>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown(f"<h3>Hello, {st.session_state.current_user}</h3>", unsafe_allow_html=True)
    
    # Dashboard Content
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""<div class='dashboard-card'><p>Heart Rate</p><h2>72 BPM</h2></div>""", unsafe_allow_html=True)
    with col2:
        st.markdown("""<div class='dashboard-card'><p>Blood Oxygen</p><h2>98%</h2></div>""", unsafe_allow_html=True)

    if st.button("Sign Out", key="logout"):
        st.session_state.page = "auth"
        st.session_state.current_user = None
        st.rerun()

# --- REGISTRATION FLOW ---
elif st.session_state.page == "create_account":
    st.markdown("<h3>Create Account</h3>", unsafe_allow_html=True)
    phone = st.text_input("Phone Number", placeholder="+1 (555) 000-0000")
    otp = st.text_input("Enter 6-digit OTP", placeholder="· · · · · ·")
    if st.button("Verify & Register"):
        st.session_state.generated_id = f"MED-{random.randint(1000, 9999)}"; st.rerun()
    if 'generated_id' in st.session_state and st.session_state.generated_id:
        st.markdown(f"<div class='dashboard-card'><h2>{st.session_state.generated_id} (id)</h2></div>", unsafe_allow_html=True)
        if st.button("Go to Sign In"):
            st.session_state.page = "auth"; st.session_state.generated_id = None; st.rerun()

