import streamlit as st
import random
from datetime import time

# 1. Page Configuration
st.set_page_config(page_title="Med-Cloud Pro", layout="centered")

# 2. CSS - Locked Design + Dynamic Form Styling
st.markdown("""
    <style>
    .stApp { background-color: #FFFFFF; }
    h1, h2, h3, p, span, label { color: #1A73E8 !important; font-family: 'Segoe UI', sans-serif !important; }
    
    .stTextInput>div>div>input {
        background-color: #FFFFFF !important;
        color: #000000 !important;
        border: 1px solid #747775 !important;
        border-radius: 4px !important;
        padding: 12px !important;
        caret-color: #1A73E8 !important; 
    }

    div[data-testid="stButton"] button:has(div p:contains("Set Reminder")),
    div[data-testid="stButton"] button:has(div p:contains("Next")),
    div[data-testid="stButton"] button:has(div p:contains("Create account")),
    div[data-testid="stButton"] button:has(div p:contains("Sign Out")) {
        background-color: #1A73E8 !important;
        color: white !important;
        border-radius: 20px !important;
        padding: 4px 15px !important;
    }

    .dashboard-header { display: flex; justify-content: space-between; align-items: center; padding: 10px 0px; }
    .profile-icon { width: 42px; height: 42px; background-color: #E8F0FE; border-radius: 50%; display: flex; align-items: center; justify-content: center; overflow: hidden; }
    .line { width: 24px; height: 3px; background-color: #1A73E8; border-radius: 2px; margin: 4px 0; }
    
    header {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# --- SESSION STATE ---
if 'page' not in st.session_state: st.session_state.page = "welcome"
if 'current_user' not in st.session_state: st.session_state.current_user = None
if 'reminders' not in st.session_state: st.session_state.reminders = []

# --- PAGE 1 & 2 (Logic remains same for Welcome/Auth) ---
if st.session_state.page == "welcome":
    st.markdown("<h1 style='text-align:center;'>Smart Healthcare Monitoring</h1>", unsafe_allow_html=True)
    st.image("https://img.freepik.com/free-vector/health-professional-team-concept-illustration_114360-1608.jpg")
    if st.button("Continue ➔"): st.session_state.page = "auth"; st.rerun()

elif st.session_state.page == "auth":
    st.markdown("<h3>Sign in</h3>", unsafe_allow_html=True)
    user_id = st.text_input("Med-Cloud ID", placeholder="ex: (MED-1234)")
    if st.button("Next"):
        if user_id: st.session_state.current_user = user_id; st.session_state.page = "dashboard"; st.rerun()

# --- PAGE 3: MAIN PAGE (ADVANCED REMINDERS) ---
elif st.session_state.page == "dashboard":
    st.markdown("""<div class="dashboard-header"><div class="profile-icon"><img src="https://cdn-icons-png.flaticon.com/512/3135/3135715.png" width="35"></div><h2 style="margin:0;">Doctor Help</h2><div class="menu-lines"><div class="line"></div><div class="line"></div><div class="line"></div></div></div>""", unsafe_allow_html=True)
    
    st.markdown(f"<h3>Patient Dashboard: {st.session_state.current_user}</h3>", unsafe_allow_html=True)

    with st.expander("➕ Create Advanced Medication Schedule", expanded=True):
        # 1. Basic Info
        med_name = st.text_input("Medicine Name", placeholder="e.g., Amoxicillin")
        
        col_d1, col_d2 = st.columns(2)
        with col_d1: start_date = st.date_input("Start Date")
        with col_d2: end_date = st.date_input("End Date")
        
        # 2. Dynamic Dosage Logic
        dosage_per_day = st.number_input("Dosage Per Day (How many times?)", min_value=1, max_value=12, value=1)
        
        st.write("Set Times for Each Dose:")
        time_slots = []
        # Creates as many clock pickers as the user asked for
        cols = st.columns(3) 
        for i in range(int(dosage_per_day)):
            with cols[i % 3]:
                t = st.time_input(f"Dose {i+1}", value=time(9 + i, 0), key=f"time_{i}")
                time_slots.append(t.strftime("%I:%M %p"))

        st.markdown("---")
        # 3. Caretaker Details
        st.markdown("<h4>Caretaker Information</h4>", unsafe_allow_html=True)
        ct_name = st.text_input("Caretaker Name")
        col_p1, col_p2 = st.columns(2)
        with col_p1: ct_num1 = st.text_input("Primary Phone")
        with col_p2: ct_num2 = st.text_input("Secondary Phone")

        if st.button("Set Reminder"):
            if med_name and ct_name:
                reminder_data = {
                    "med": med_name,
                    "times": time_slots,
                    "caretaker": ct_name,
                    "dates": f"{start_date} to {end_date}"
                }
                st.session_state.reminders.append(reminder_data)
                st.success(f"Schedule for {med_name} locked!")
            else:
                st.error("Please fill in Medicine Name and Caretaker Name.")

    # Display Active Schedules
    if st.session_state.reminders:
        st.markdown("### Active Schedules")
        for r in st.session_state.reminders:
            with st.container():
                st.info(f"💊 **{r['med']}** ({r['dates']})\n\n**Times:** {', '.join(r['times'])}\n\n**Contact:** {r['caretaker']}")

    if st.button("Sign Out"): st.session_state.page = "auth"; st.rerun()
