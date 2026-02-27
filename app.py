import streamlit as st
import random
from datetime import time

# 1. Page Configuration
st.set_page_config(page_title="Med-Cloud Pro", layout="centered")

# 2. CSS - CLEAN UI (Fixes dark boxes and aligns icons)
st.markdown("""
    <style>
    .stApp { background-color: #FFFFFF; }
    
    /* GLOBAL LIGHT BLUE */
    h1, h2, h3, p, span, label {
        color: #1A73E8 !important;
        font-family: 'Segoe UI', sans-serif !important;
    }

    /* INPUT BOXES - White background, Grey border, Blue cursor */
    .stTextInput>div>div>input, .stNumberInput>div>div>input, .stTimeInput>div>div>input {
        background-color: #FFFFFF !important;
        color: #000000 !important;
        border: 1px solid #D1D5DB !important;
        border-radius: 4px !important;
        padding: 10px !important;
        caret-color: #1A73E8 !important; 
    }

    /* FIX FOR EXPANDER & TIME PICKER DARK BOXES */
    .streamlit-expanderHeader {
        background-color: #FFFFFF !important;
        color: #1A73E8 !important;
        border: 1px solid #E5E7EB !important;
        border-radius: 8px !important;
    }
    div[data-baseweb="select"] > div {
        background-color: #FFFFFF !important;
        color: #000000 !important;
    }

    /* FORGOT ID (Locked Page 2 design) */
    div[data-testid="stButton"] button:has(div p:contains("Forgot ID?")) {
        background: transparent !important;
        border: none !important;
        color: #1A73E8 !important;
        padding: 0 !important;
        font-size: 11px !important;
        margin-top: 55px !important;
        display: block !important;
    }

    /* PRIMARY BUTTONS - Solid Light Blue */
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
        font-weight: 500 !important;
    }

    /* HEADER STYLING */
    .dashboard-header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px; }
    .profile-icon { width: 40px; height: 40px; background-color: #E8F0FE; border-radius: 50%; display: flex; align-items: center; justify-content: center; overflow: hidden; }
    .line { width: 22px; height: 3px; background-color: #1A73E8; border-radius: 2px; margin: 3px 0; }

    /* DASHBOARD CARD */
    .dashboard-card {
        padding: 15px;
        border-radius: 12px;
        background-color: #F8FAFC;
        border-left: 5px solid #1A73E8;
        margin-bottom: 10px;
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

# --- PAGE 2: AUTH (SIGN IN) - LOCKED ---
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

# --- PAGE 3: MAIN DASHBOARD (RETIRED DARK BOXES) ---
elif st.session_state.page == "dashboard":
    st.markdown("""
        <div class="dashboard-header">
            <div class="profile-icon"><img src="https://cdn-icons-png.flaticon.com/512/3135/3135715.png" width="30"></div>
            <h2 style="margin:0;">Doctor Help</h2>
            <div class="menu-lines"><div class="line"></div><div class="line"></div><div class="line"></div></div>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown(f"<h3>Hello, {st.session_state.current_user}</h3>", unsafe_allow_html=True)

    # VITAL CARDS
    c1, c2 = st.columns(2)
    with c1: st.markdown("""<div class='dashboard-card'><p style='margin:0; font-size:12px;'>Heart Rate</p><h2 style='margin:0;'>72 BPM</h2></div>""", unsafe_allow_html=True)
    with c2: st.markdown("""<div class='dashboard-card'><p style='margin:0; font-size:12px;'>Blood Oxygen</p><h2 style='margin:0;'>98%</h2></div>""", unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("<h3>Pill Reminders</h3>", unsafe_allow_html=True)
    
    with st.expander("➕ Create Detailed Medication Schedule", expanded=True):
        med_name = st.text_input("Medicine Name", placeholder="e.g., Aspirin")
        
        col_d1, col_d2 = st.columns(2)
        with col_d1: start_date = st.date_input("Start Date")
        with col_d2: end_date = st.date_input("End Date")
        
        # DYNAMIC DOSAGE LOGIC
        dosage_per_day = st.number_input("Dosage Per Day (Number of Times)", min_value=1, max_value=10, value=1)
        
        st.write("Set Times for Each Dose:")
        time_slots = []
        t_cols = st.columns(2)
        for i in range(int(dosage_per_day)):
            with t_cols[i % 2]:
                t = st.time_input(f"Dose {i+1} Time", value=time(8 + (i*4)%24, 0), key=f"dose_t_{i}")
                time_slots.append(t.strftime("%I:%M %p"))

        st.markdown("#### Caretaker Information")
        ct_name = st.text_input("Caretaker Name", key="ct_name")
        col_ct1, col_ct2 = st.columns(2)
        with col_ct1: ct_phone1 = st.text_input("Primary Number", key="ct_p1")
        with col_ct2: ct_phone2 = st.text_input("Secondary Number", key="ct_p2")

        if st.button("Set Reminder", key="final_save_pill"):
            if med_name and ct_name:
                entry = {
                    "med": med_name,
                    "duration": f"{start_date} to {end_date}",
                    "times": ", ".join(time_slots),
                    "caretaker": f"{ct_name} ({ct_phone1})"
                }
                st.session_state.reminders.append(entry)
                st.success("Medication Schedule Saved!")

    # Show Active List
    for r in st.session_state.reminders:
        st.info(f"💊 **{r['med']}** ({r['duration']})\n\n⏰ Times: {r['times']}\n\n👤 Care: {r['caretaker']}")

    if st.button("Sign Out"): st.session_state.page = "auth"; st.rerun()

# --- CREATE ACCOUNT PAGE ---
elif st.session_state.page == "create_account":
    st.markdown("<h3>Create Account</h3>", unsafe_allow_html=True)
    phone = st.text_input("Phone Number")
    otp = st.text_input("OTP")
    if st.button("Verify & Register"):
        st.session_state.generated_id = f"MED-{random.randint(1000, 9999)}"; st.rerun()
    if st.session_state.generated_id:
        st.success(f"ID: {st.session_state.generated_id} (id)")
        if st.button("Go to Sign In"): st.session_state.page = "auth"; st.session_state.generated_id = None; st.rerun()

# --- FORGOT ID PAGE ---
elif st.session_state.page == "forgot_id":
    st.title("Recovery")
    if st.button("← Back"): st.session_state.page = "auth"; st.rerun()


