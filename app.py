import streamlit as st
from datetime import datetime
import time

# --- PROFESSIONAL THEME CONFIG ---
st.set_page_config(page_title="MedRemind Pro", page_icon="🏥", layout="centered")

# Custom CSS for Blue/White Professional Look
st.markdown("""
    <style>
    .main { background-color: #ffffff; }
    div.stButton > button {
        background-color: #007bff; color: white; border-radius: 5px;
        border: none; padding: 10px 20px; transition: 0.3s;
    }
    div.stButton > button:hover { background-color: #0056b3; border: none; }
    .welcome-text { text-align: center; color: #007bff; font-family: 'Helvetica'; }
    .card { padding: 20px; border: 1px solid #e0e0e0; border-radius: 10px; margin-bottom: 10px; }
    </style>
    """, unsafe_allow_html=True)

# --- STATE MANAGEMENT ---
if 'page' not in st.session_state:
    st.session_state.page = "welcome"
if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False
if 'meds' not in st.session_state:
    st.session_state.meds = []

# --- PAGE 1: WELCOME SCREEN ---
if st.session_state.page == "welcome":
    st.markdown("<br><br><br>", unsafe_allow_html=True)
    st.markdown("<h1 class='welcome-text'>Welcome to MedRemind Cloud</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;'>Your professional health companion.</p>", unsafe_allow_html=True)
    if st.button("Continue"):
        st.session_state.page = "login"
        st.rerun()

# --- PAGE 2: LOGIN / SIGNUP ---
elif st.session_state.page == "login":
    st.subheader("Account Login")
    tab1, tab2 = st.tabs(["Login", "Create Account"])
    
    with tab1:
        user = st.text_input("Username")
        pw = st.text_input("Password", type="password")
        if st.button("Login"):
            if user and pw: # Simple logic for hackathon
                st.session_state.username = user
                st.session_state.authenticated = True
                st.session_state.page = "dashboard"
                st.rerun()
    
    with tab2:
        st.text_input("Full Name")
        st.text_input("New Email")
        st.text_input("Set Password", type="password")
        if st.button("Create Account"):
            st.success("Account created! Please login.")

# --- PAGE 3: MAIN DASHBOARD ---
elif st.session_state.page == "dashboard" and st.session_state.authenticated:
    # Sidebar Settings
    with st.sidebar:
        st.title(f"Hi, {st.session_state.username}")
        st.markdown("---")
        if st.button("⚙️ Settings"):
            st.info("Change Password feature coming soon.")
        if st.button("🚪 Logout"):
            st.session_state.authenticated = False
            st.session_state.page = "welcome"
            st.rerun()

    st.header("Medical Dashboard")
    
    # Add Med Section
    with st.expander("Add New Schedule"):
        m_name = st.text_input("Medication Name")
        m_time = st.time_input("Set Time")
        if st.button("Add to Schedule"):
            st.session_state.meds.append({"name": m_name, "time": m_time.strftime("%H:%M")})
            st.rerun()

    # Display Meds
    st.subheader("Current Medications")
    for i, m in enumerate(st.session_state.meds):
        col1, col2 = st.columns([4, 1])
        col1.markdown(f"**{m['name']}** at {m['time']}")
        if col2.button("Delete", key=f"del_{i}"):
            st.session_state.meds.pop(i)
            st.rerun()

    # Notification Engine (Checks every 10 seconds)
    now = datetime.now().strftime("%H:%M")
    for m in st.session_state.meds:
        if m['time'] == now:
            st.toast(f"NOTIFICATION: Time for {m['name']}!", icon="🔔")
            st.warning(f"REMINDER: Please take your {m['name']} now.")
    
    time.sleep(10)
    st.rerun()
