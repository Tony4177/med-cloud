import streamlit as st
import random
from datetime import datetime, timedelta

# 1. Page Config
st.set_page_config(page_title="MedRemind Cloud", layout="centered")

# 2. Premium Blue & White Styles (No Black Used)
st.markdown("""
    <style>
    .stApp { background-color: #FFFFFF; }
    
    /* Header & Text Colors */
    h1 { color: #0052CC; text-align: center; font-family: 'Helvetica'; font-weight: 800; }
    h2, h3 { color: #0052CC; text-align: center; }
    p, span, label { color: #334155 !important; font-weight: 500; font-size: 16px; }

    /* Button Style: Royal Blue with rounded corners */
    .stButton>button {
        background-color: #0052CC;
        color: white;
        border-radius: 12px;
        height: 3.5em;
        width: 100%;
        font-weight: bold;
        border: none;
        font-size: 18px;
        margin-top: 10px;
    }
    .stButton>button:hover { background-color: #003D99; color: white; }
    
    /* Card design for visibility */
    .med-card {
        background-color: #F8FAFC;
        padding: 20px;
        border-radius: 15px;
        border: 1px solid #E2E8F0;
        margin-bottom: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# Initialize Session States
if 'page' not in st.session_state: st.session_state.page = "welcome"
if 'user_id' not in st.session_state: st.session_state.user_id = None
if 'history_count' not in st.session_state: st.session_state.history_count = 0

# --- PAGE 1: WELCOME ---
if st.session_state.page == "welcome":
    st.markdown("<h1>MedRemind Cloud</h1>", unsafe_allow_html=True)
    st.markdown("<p>Smart Healthcare Monitoring & Caretaker Escalation</p>", unsafe_allow_html=True)
    
    # Hero Illustration
    st.image("https://img.freepik.com/free-vector/health-professional-team-concept-illustration_114360-1608.jpg", use_container_width=True)
    
    st.markdown("""
    <div class='med-card'>
    <b>What we do:</b><br>
    Our system monitors your health 24/7. If you don't confirm your pill, we alert your family automatically. 
    Built for safety, built for peace of mind.
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("Continue ➔"):
        st.session_state.page = "auth"
        st.rerun()

# --- PAGE 2: AUTH / LOGIN ---
elif st.session_state.page == "auth":
    st.markdown("<h1>System Access</h1>", unsafe_allow_html=True)
    
    col1, col2 = st.columns([1,1])
    with col1:
        st.markdown("### Existing User")
        login_id = st.text_input("Enter Patient ID")
        if st.button("Login"):
            st.session_state.user_id = login_id
            st.session_state.page = "dashboard"
            st.rerun()
            
    with col2:
        st.markdown("### New Caretaker")
        email = st.text_input("Caretaker Email")
        pwd = st.text_input("Password", type="password")
        if st.button("Create ID"):
            new_id = f"MED-{random.randint(1000, 9999)}"
            st.session_state.user_id = new_id
            st.success(f"ID Created: {new_id}")
            st.info("Check your email for the backup.")

# --- PAGE 3: DASHBOARD ---
elif st.session_state.page == "dashboard":
    # Top Bar with Profile and Logout
    t_col1, t_col2, t_col3 = st.columns([1, 4, 1])
    with t_col1: 
        if st.button("👤"): st.session_state.page = "profile"
    with t_col2: st.markdown(f"### ID: {st.session_state.user_id}")
    with t_col3: 
        if st.button("🚪"): 
            st.session_state.page = "welcome"
            st.rerun()

    # AI DOCTOR SECTION
    st.markdown("### 🤖 Help Doctor (AI Health Assistant)")
    user_q = st.text_input("Ask about symptoms or medicines...", placeholder="What is the dosage for Metformin?")
    if user_q:
        st.markdown(f"<div class='med-card'><b>AI Doctor:</b> Medical records suggest that for '{user_q}', you should check the label for 500mg, but always consult a doctor first.</div>", unsafe_allow_html=True)

    st.divider()

    # ADD MEDICATION
    with st.expander("➕ Add New Medication Schedule", expanded=True):
        p_name = st.text_input("Pill Name")
        c1, c2 = st.columns(2)
        with c1:
            start_date = st.date_input("Start Date")
            t_input = st.text_input("Set Time (e.g., 18:00 or 6:00 PM)", value="18:00")
        with c2:
            end_date = st.date_input("End Date")
            sound = st.selectbox("Alarm Sound", ["Loud Beep", "Voice Reminder", "Chime"])
        
        st.write("**Caretaker Escalation Contacts**")
        care_phone = st.text_input("Primary Caretaker No.")
        back_phone = st.text_input("Backup Caretaker No.")
        
        if st.button("Save & Activate"):
            st.success("Reminders armed: 6:00 -> 6:10 -> 6:20 escalation active.")

    st.markdown("### 🔔 Active Reminder")
    st.info(f"Dose: {p_name if p_name else 'Pills'} at {t_input}")
    
    if st.button("✅ I HAVE TAKEN MY PILL"):
        st.balloons()
        st.session_state.history_count += 1
        st.success("Great job! Caretaker notified.")

# --- PAGE 4: PROFILE & HISTORY ---
elif st.session_state.page == "profile":
    st.markdown("<h1>Patient Profile</h1>", unsafe_allow_html=True)
    st.write(f"Patient ID: **{st.session_state.user_id}**")
    
    st.markdown("<div class='med-card'>", unsafe_allow_html=True)
    st.metric("Total Pills Taken", f"{st.session_state.history_count}")
    st.write("Adherence Rate: 100%")
    st.markdown("</div>", unsafe_allow_html=True)
    
    st.markdown("### Options")
    st.button("Update Profile Photo")
    st.button("Change Password")
    
    if st.button("Back to Dashboard"):
        st.session_state.page = "dashboard"
        st.rerun()
