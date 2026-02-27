import streamlit as st
import random
from datetime import datetime, timedelta

# 1. Page Config
st.set_page_config(page_title="Med-Cloud Elite", layout="centered")

# 2. Modern Medical Styling
st.markdown("""
    <style>
    /* Main Background */
    .stApp { background-color: #f8faff; }
    
    /* Clean Cards for Visibility */
    .med-card {
        background-color: white;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.05);
        border: 1px solid #e1e8f0;
        margin-bottom: 20px;
        color: #1e3a8a;
    }
    
    /* Premium Blue Buttons */
    .stButton>button {
        background-color: #007bff;
        color: white;
        border-radius: 10px;
        border: none;
        padding: 12px;
        font-weight: 600;
        width: 100%;
    }
    .stButton>button:hover { background-color: #0056b3; color: white; }
    
    /* Sidebar Styling */
    [data-testid="stSidebar"] { background-color: #ffffff; border-right: 1px solid #e1e8f0; }
    
    /* Text Colors */
    h1, h2, h3 { color: #1e3a8a; font-family: 'Segoe UI', sans-serif; }
    p, label { color: #4a5568 !important; font-weight: 500; }
    </style>
    """, unsafe_allow_html=True)

# Initialize Session States
if 'page' not in st.session_state: st.session_state.page = "Welcome"
if 'history' not in st.session_state: st.session_state.history = 12 # Mock data: 12 days streak
if 'user_id' not in st.session_state: st.session_state.user_id = "MED-7741"

# --- SIDEBAR NAVIGATION ---
with st.sidebar:
    st.markdown("### 👤 User Menu")
    st.write(f"Logged in as: **{st.session_state.user_id}**")
    st.divider()
    choice = st.radio("Go to:", ["Dashboard", "AI Doctor", "My Profile", "Settings"])
    st.divider()
    if st.button("🚪 Logout"):
        st.session_state.page = "Welcome"
        st.rerun()

# --- PAGE 1: WELCOME ---
if st.session_state.page == "Welcome":
    st.markdown("<h1 style='text-align:center;'>Med-Cloud</h1>", unsafe_allow_html=True)
    st.image("https://img.freepik.com/free-vector/medical-care-concept-illustration_114360-1534.jpg", use_container_width=True)
    
    st.markdown("""
    <div class='med-card'>
    <h3 style='text-align:center;'>Smart Health Tracking</h3>
    <p style='text-align:center;'>Real-time monitoring with automated caretaker escalation (6:00 → 6:10 → 6:20 PM).</p>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("Start My Health Journey"):
        st.session_state.page = "Dashboard"
        st.rerun()

# --- PAGE 2: DASHBOARD ---
elif choice == "Dashboard":
    st.markdown("<h1>Medical Dashboard</h1>", unsafe_allow_html=True)
    
    # Active Schedule Section
    st.markdown("""<div class='med-card'>
    <h4>➕ Add New Schedule</h4>
    </div>""", unsafe_allow_html=True)
    
    with st.container():
        pill = st.text_input("Pill Name", placeholder="e.g. Vitamin D3")
        c1, c2 = st.columns(2)
        with c1:
            # Manual keyboard entry for time
            pill_time = st.text_input("Set Time (24h format)", value="18:00", help="Type like 16:30")
        with c2:
            freq = st.selectbox("Frequency", ["Every Day", "Twice a Day", "Weekly"])
        
        care_no = st.text_input("Caretaker Phone Number")
        
        if st.button("Activate Schedule"):
            st.success(f"Logic Armed: Reminders set for {pill_time}")

    st.divider()
    
    # Current Reminder
    st.markdown(f"""<div class='med-card' style='border-left: 5px solid #007bff;'>
    <h3>🔔 Current Reminder</h3>
    <p>Take <b>{pill if pill else 'Medication'}</b> at <b>{pill_time}</b></p>
    <p style='font-size:12px;'><i>Escalation: 10m & 20m delay active.</i></p>
    </div>""", unsafe_allow_html=True)
    
    if st.button("✅ MARK AS TAKEN"):
        st.balloons()
        st.session_state.history += 1
        st.success("Caretaker Notified: Dose Complete!")

# --- PAGE 3: AI DOCTOR ---
elif choice == "AI Doctor":
    st.markdown("<h1>🤖 AI Medical Assistant</h1>", unsafe_allow_html=True)
    st.markdown("<p>Ask about medicine side effects, dosages, or general health doubts.</p>", unsafe_allow_html=True)
    
    user_q = st.text_input("How can I help you today?")
    if user_q:
        with st.spinner("Analyzing medical database..."):
            # Simulation of AI Response
            st.markdown(f"""<div class='med-card' style='background-color:#eef2ff;'>
            <b>AI Doctor says:</b><br>
            Regarding '{user_q}': Always consult your local physician first. 
            Generally, this is associated with standard protocols for patient care. 
            Ensure you follow the dosage instructions on the packet.
            </div>""", unsafe_allow_html=True)

# --- PAGE 4: PROFILE & HISTORY ---
elif choice == "My Profile":
    st.markdown("<h1>Your Health Profile</h1>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Pill Streak", f"{st.session_state.history} Days")
    with col2:
        st.metric("Success Rate", "98%")
    
    st.markdown("### 📊 Adherence History")
    # Generating a mock history chart
    chart_data = {"Day": ["Mon", "Tue", "Wed", "Thu", "Fri"], "Taken": [1, 1, 0, 1, 1]}
    st.bar_chart(chart_data, x="Day", y="Taken")
    
    if st.button("Edit Profile Information"):
        st.info("Profile editing enabled in next update.")

# --- PAGE 5: SETTINGS ---
elif choice == "Settings":
    st.markdown("<h1>Account Settings</h1>", unsafe_allow_html=True)
    new_id = st.text_input("Change Patient ID", value=st.session_state.user_id)
    if st.button("Update ID"):
        st.session_state.user_id = new_id
        st.success("ID Updated successfully!")
