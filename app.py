import streamlit as st
import random
from datetime import time

# 1. Page Configuration
st.set_page_config(page_title="Med-Cloud Pro", layout="centered")

# 2. CSS - FIXING ICON OVERLAP AND DARK BOXES
st.markdown("""
    <style>
    /* Force white background and blue text */
    .stApp { background-color: #FFFFFF; }
    h1, h2, h3, p, span, label { color: #1A73E8 !important; font-family: 'Segoe UI', sans-serif !important; }

    /* Fix the "arrow_drop_down" text glitch in Expanders */
    .streamlit-expanderHeader {
        background-color: #FFFFFF !important;
        border: 1px solid #E5E7EB !important;
        border-radius: 8px !important;
        padding: 10px !important;
    }
    .streamlit-expanderHeader p {
        color: #1A73E8 !important;
        font-weight: 600 !important;
    }
    /* Hide the broken icon text if it appears as raw text */
    .streamlit-expanderHeader svg { fill: #1A73E8 !important; }

    /* Fix for Time/Date Input Dark Boxes */
    div[data-baseweb="input"], div[data-baseweb="select"] {
        background-color: #FFFFFF !important;
    }
    input { color: #000000 !important; }

    /* SIGN-IN PAGE: FORGOT ID (Locked V2.8 Design) */
    div[data-testid="stButton"] button:has(div p:contains("Forgot ID?")) {
        background: transparent !important;
        border: none !important;
        color: #1A73E8 !important;
        padding: 0 !important;
        font-size: 11px !important;
        margin-top: 55px !important;
        display: block !important;
    }

    /* ALL PRIMARY BUTTONS */
    div[data-testid="stButton"] button:has(div p:contains("Next")),
    div[data-testid="stButton"] button:has(div p:contains("Create account")),
    div[data-testid="stButton"] button:has(div p:contains("Verify & Register")),
    div[data-testid="stButton"] button:has(div p:contains("Go to Sign In")),
    div[data-testid="stButton"] button:has(div p:contains("Sign Out")),
    div[data-testid="stButton"] button:has(div p:contains("Set Reminder")),
    div[data-testid="stButton"] button:has(div p:contains("← Back")) {
        background-color: #1A73E8 !important;
        color: white !important;
        border-radius: 20px !important;
        border: none !important;
        padding: 6px 20px !important;
    }

    /* DASHBOARD TOP BAR */
    .dashboard-header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 30px; }
    .profile-icon { width: 40px; height: 40px; background-color: #E8F0FE; border-radius: 50%; display: flex; align-items: center; justify-content: center; overflow: hidden; }
    .line { width: 22px; height: 3px; background-color: #1A73E8; border-radius: 2px; margin: 3px 0; }

    .dashboard-card {
        padding: 15px;
        border-radius: 12px;
        background-color: #F8FAFC;
        border-left: 5px solid #1A73E8;
        margin-bottom: 15px;
    }

    header {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# --- SESSION STATE ---
if 'page' not in st.session_state: st.session_state.page = "welcome"
if 'current_user' not in st.session_state: st.session_state.current_user = None
if 'reminders' not in st.session_state: st.session_state.reminders = []

# --- PAGE 1: WELCOME ---
if st.session_state.page == "welcome":
    st.markdown("<h1 style='text-align:center;'>Smart Healthcare Monitoring</h1>", unsafe_allow_html=True)
    st.image("https://img.freepik.com/free-vector/health-professional-team-concept-illustration_114360-1608.jpg")
    if st.button("Continue ➔"): st.session_state.page = "auth"; st.rerun()

# --- PAGE 2: AUTH (SIGN IN) - LOCKED DESIGN ---
elif st.session_state.page == "auth":
    st.markdown("""<div style='display: flex; align-items: center; gap: 12px; margin-bottom: 10px;'><img src='https://cdn-icons-png.flaticon.com/512/2966/2966327.png' width='30'><h2>Med-Cloud Pro</h2></div>""", unsafe_allow_html=True)
    st.markdown("<h3>Sign in</h3>", unsafe_allow_html=True)
    st.markdown("<p style='font-weight:500; font-size:14px;'>Med-Cloud ID</p>", unsafe_allow_html=True)
    user_id_input = st.text_input("", placeholder="ex: (MED-1234)", key="login_id")
    if st.button("Forgot ID?"): st.session_state.page = "forgot_id"; st.rerun()
    col_l, col_r = st.columns([1, 1])
    with col_l:
        if st.button("Create account"): st.session_state.page = "create_account"; st.rerun()
    with col_r:
        if st.button("Next"):
            if user_id_input: st.session_state.current_user = user_id_input; st.session_state.page = "dashboard"; st.rerun()

# --- PAGE 3: MAIN DASHBOARD ---
elif st.session_state.page == "dashboard":
    st.markdown("""
        <div class="dashboard-header">
            <div class="profile-icon"><img src="https://cdn-icons-png.flaticon.com/512/3135/3135715.png" width="30"></div>
            <h2 style="margin:0;">Doctor Help</h2>
            <div class="menu-lines"><div class="line"></div><div class="line"></div><div class="line"></div></div>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown(f"<h3>Hello, {st.session_state.current_user}</h3>", unsafe_allow_html=True)

    # Vitals
    c1, c2 = st.columns(2)
    with c1: st.markdown("<div class='dashboard-card'><p>Heart Rate</p><h2>72 BPM</h2></div>", unsafe_allow_html=True)
    with c2: st.markdown("<div class='dashboard-card'><p>Blood Oxygen</p><h2>98%</h2></div>", unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("<h3>Pill Reminders</h3>", unsafe_allow_html=True)
    
    # REMINDER FORM (Fixed Arrow/Glitch)
    with st.expander("Add Medication Reminder", expanded=True):
        med_name = st.text_input("Medicine Name", placeholder="e.g. Paracetamol")
        
        c_date1, c_date2 = st.columns(2)
        with c_date1: s_date = st.date_input("Start Date")
        with c_date2: e_date = st.date_input("End Date")
        
        # Dosage Logic
        dosage = st.number_input("Dosage Per Day", min_value=1, max_value=8, value=1)
        
        st.write("Set Times:")
        time_slots = []
        t_cols = st.columns(2)
        for i in range(int(dosage)):
            with t_cols[i % 2]:
                t = st.time_input(f"Dose {i+1}", value=time(8+(i*4)%24, 0), key=f"t_slot_{i}")
                time_slots.append(t.strftime("%I:%M %p"))

        st.markdown("#### Caretaker Details")
        ct_name = st.text_input("Name")
        cp1, cp2 = st.columns(2)
        with cp1: p1 = st.text_input("Phone 1")
        with cp2: p2 = st.text_input("Phone 2")

        if st.button("Set Reminder"):
            if med_name and ct_name:
                st.session_state.reminders.append({"med": med_name, "times": ", ".join(time_slots)})
                st.success("Reminder Locked!")

    # Saved Reminders
    for r in st.session_state.reminders:
        st.info(f"💊 {r['med']} at {r['times']}")

    if st.button("Sign Out"): st.session_state.page = "auth"; st.rerun()

# --- CREATE ACCOUNT PAGE ---
elif st.session_state.page == "create_account":
    st.markdown("<h3>Create Account</h3>", unsafe_allow_html=True)
    # Simple logic to generate ID
    if st.button("Verify & Register"):
        st.session_state.generated_id = f"MED-{random.randint(1000, 9999)}"; st.rerun()
    if 'generated_id' in st.session_state and st.session_state.generated_id:
        st.success(f"New ID: {st.session_state.generated_id}")
        if st.button("Go to Sign In"): st.session_state.page = "auth"; st.rerun()



