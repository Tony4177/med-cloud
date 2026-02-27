import streamlit as st
import random
from datetime import time

# 1. Page Configuration
st.set_page_config(page_title="Med-Cloud Pro", layout="centered")

# 2. CSS - FULL APP STYLING (Locked Sign-in + Dynamic Main Page)
st.markdown("""
    <style>
    .stApp { background-color: #FFFFFF; }
    
    /* GLOBAL LIGHT BLUE */
    h1, h2, h3, p, span, label {
        color: #1A73E8 !important;
        font-family: 'Segoe UI', sans-serif !important;
    }

    /* INPUT BOXES (Locked Style) */
    .stTextInput>div>div>input, .stNumberInput>div>div>input {
        background-color: #FFFFFF !important;
        color: #000000 !important;
        border: 1px solid #747775 !important;
        border-radius: 4px !important;
        padding: 12px !important;
        caret-color: #1A73E8 !important; 
    }

    /* FORGOT ID: No box, Small text, 1.5cm Gap (Locked Page 2) */
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
    div[data-testid="stButton"] button:has(div p:contains("Sign Out")),
    div[data-testid="stButton"] button:has(div p:contains("Set Reminder")),
    div[data-testid="stButton"] button:has(div p:contains("← Back")) {
        background-color: #1A73E8 !important;
        color: white !important;
        border-radius: 20px !important;
        border: none !important;
        padding: 4px 15px !important;
        font-weight: 500 !important;
        font-size: 14px !important;
    }

    /* DOCTOR HELP HEADER */
    .dashboard-header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 10px 0px;
        margin-bottom: 30px;
    }
    .profile-icon {
        width: 42px;
        height: 42px;
        background-color: #E8F0FE;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        overflow: hidden;
    }
    .line {
        width: 24px;
        height: 3px;
        background-color: #1A73E8;
        border-radius: 2px;
        margin: 4px 0;
    }

    /* DASHBOARD CARDS */
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

# --- SESSION STATE ---
if 'page' not in st.session_state: st.session_state.page = "welcome"
if 'current_user' not in st.session_state: st.session_state.current_user = None
if 'generated_id' not in st.session_state: st.session_state.generated_id = None
if 'reminders' not in st.session_state: st.session_state.reminders = []

# --- PAGE 1: WELCOME ---
if st.session_state.page == "welcome":
    st.markdown("<h1 style='text-align:center;'>Smart Healthcare Monitoring</h1>", unsafe_allow_html=True)
    st.image("https://img.freepik.com/free-vector/health-professional-team-concept-illustration_114360-1608.jpg", use_container_width=True)
    if st.button("Continue ➔", key="welcome_go"):
        st.session_state.page = "auth"; st.rerun()

# --- PAGE 2: AUTH (SIGN IN) - LOCKED DESIGN ---
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

    if st.button("← Back", key="back_welcome"):
        st.session_state.page = "welcome"; st.rerun()

# --- PAGE 3: MAIN DASHBOARD (DOCTOR HELP) ---
elif st.session_state.page == "dashboard":
    st.markdown("""
        <div class="dashboard-header">
            <div class="profile-icon"><img src="https://cdn-icons-png.flaticon.com/512/3135/3135715.png" width="35"></div>
            <h2 style="margin:0; font-weight: 600;">Doctor Help</h2>
            <div class="menu-lines"><div class="line"></div><div class="line"></div><div class="line"></div></div>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown(f"<h3>Hello, {st.session_state.current_user}</h3>", unsafe_allow_html=True)

    # VITAL CARDS
    c1, c2 = st.columns(2)
    with c1: st.markdown("""<div class='dashboard-card'><p>Heart Rate</p><h2>72 BPM</h2></div>""", unsafe_allow_html=True)
    with c2: st.markdown("""<div class='dashboard-card'><p>Blood Oxygen</p><h2>98%</h2></div>""", unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("<h3>Pill Reminders</h3>", unsafe_allow_html=True)
    
    with st.expander("➕ Add New Medication Schedule", expanded=True):
        med_name = st.text_input("Medicine Name", placeholder="e.g., Metformin")
        
        col_date1, col_date2 = st.columns(2)
        with col_date1: start_date = st.date_input("Start Date")
        with col_date2: end_date = st.date_input("End Date")
        
        dosage_count = st.number_input("Dosage Per Day (Number of times)", min_value=1, max_value=10, value=1)
        
        st.write("Set Specific Times:")
        time_slots = []
        # Dynamic Time Slots Generation
        t_cols = st.columns(3)
        for i in range(int(dosage_count)):
            with t_cols[i % 3]:
                t = st.time_input(f"Dose {i+1}", value=time(8 + (i*4) % 24, 0), key=f"t_{i}")
                time_slots.append(t.strftime("%I:%M %p"))

        st.markdown("#### Caretaker Details")
        ct_name = st.text_input("Caretaker Name")
        cp1, cp2 = st.columns(2)
        with cp1: ct_phone1 = st.text_input("Primary Number")
        with cp2: ct_phone2 = st.text_input("Secondary Number")

        if st.button("Set Reminder"):
            if med_name and ct_name:
                entry = {
                    "med": med_name,
                    "dates": f"{start_date} to {end_date}",
                    "times": ", ".join(time_slots),
                    "care": f"{ct_name} ({ct_phone1})"
                }
                st.session_state.reminders.append(entry)
                st.success("Medication Schedule Saved!")

    # Show Active List
    for r in st.session_state.reminders:
        st.info(f"💊 **{r['med']}** | 📅 {r['dates']}\n\n⏰ Times: {r['times']}\n\n👤 Caretaker: {r['care']}")

    if st.button("Sign Out"): st.session_state.page = "auth"; st.rerun()

# --- CREATE ACCOUNT PAGE ---
elif st.session_state.page == "create_account":
    st.markdown("<h3>Create Account</h3>", unsafe_allow_html=True)
    phone = st.text_input("Phone Number", placeholder="+1 (555) 000-0000")
    otp = st.text_input("Enter 6-digit OTP", placeholder="· · · · · ·")
    if st.button("Verify & Register"):
        if phone and otp: st.session_state.generated_id = f"MED-{random.randint(1000, 9999)}"; st.rerun()
    if st.session_state.generated_id:
        st.markdown(f"<div class='dashboard-card'><h2>{st.session_state.generated_id} (id)</h2></div>", unsafe_allow_html=True)
        if st.button("Go to Sign In"):
            st.session_state.page = "auth"; st.session_state.generated_id = None; st.rerun()

# --- FORGOT ID PAGE ---
elif st.session_state.page == "forgot_id":
    st.title("Recovery")
    if st.button("← Back"): st.session_state.page = "auth"; st.rerun()
