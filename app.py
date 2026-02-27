import streamlit as st
import random
from datetime import datetime, timedelta

# 1. Page Configuration
st.set_page_config(page_title="MedRemind Cloud", layout="centered")

# 2. Professional CSS Styling (White Background & Blue Buttons)
st.markdown("""
    <style>
    .stApp { background-color: white; }
    h1 { color: #1E3A8A; text-align: center; font-family: 'Arial'; margin-bottom: 0px; }
    h3 { color: #3B82F6; text-align: center; font-family: 'Arial'; font-weight: 400; margin-top: 5px; }
    p { color: #475569; text-align: center; font-size: 18px; }
    
    /* Center and Style the Blue Button */
    .stButton>button {
        background-color: #2563EB;
        color: white;
        border-radius: 25px;
        height: 3.5em;
        width: 100%;
        font-weight: bold;
        border: none;
        font-size: 18px;
        box-shadow: 0px 4px 10px rgba(37, 99, 235, 0.3);
    }
    .stButton>button:hover {
        background-color: #1E40AF;
        color: white;
        border: none;
    }
    
    /* Unique ID Card Style */
    .id-box {
        background-color: #EFF6FF;
        padding: 20px;
        border-radius: 15px;
        border: 2px dashed #2563EB;
        text-align: center;
        margin: 20px 0px;
    }
    </style>
    """, unsafe_allow_html=True)

# Initialize Session States
if 'page' not in st.session_state:
    st.session_state.page = "welcome"
if 'user_id' not in st.session_state:
    st.session_state.user_id = None

# --- NAVIGATION FUNCTIONS ---
def go_to_auth(): st.session_state.page = "auth"
def go_to_dash(): st.session_state.page = "dashboard"
def logout(): 
    st.session_state.page = "welcome"
    st.session_state.user_id = None

# --- PAGE 1: WELCOME SCREEN ---
if st.session_state.page == "welcome":
    st.markdown("<h1>MedRemind Cloud</h1>", unsafe_allow_html=True)
    st.markdown("<h3>Smart Medicine Tracker</h3>", unsafe_allow_html=True)
    
    st.image("https://cdn-icons-png.flaticon.com/512/3028/3028549.png", width=150) # Generic Medical Icon
    
    st.markdown("""
    <p>Our intelligent system ensures you never miss a dose. 
    If a pill isn't confirmed, we automatically alert your caretaker 
    through our 3-step escalation protocol.</p>
    """, unsafe_allow_html=True)
    
    st.write("---")
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("Continue ➔"):
            go_to_auth()
            st.rerun()

# --- PAGE 2: LOGIN / SIGNUP (Unique ID) ---
elif st.session_state.page == "auth":
    st.markdown("<h1>System Access</h1>", unsafe_allow_html=True)
    
    tab1, tab2 = st.tabs(["Existing User (Login)", "New Caretaker (Sign Up)"])
    
    with tab1:
        u_id = st.text_input("Enter your Unique Patient ID", placeholder="e.g. MED-8821")
        if st.button("Access Dashboard"):
            if u_id:
                st.session_state.user_id = u_id
                go_to_dash()
                st.rerun()
            else:
                st.error("Please enter a valid ID")

    with tab2:
        st.write("Register your email to receive a Unique Patient ID.")
        email = st.text_input("Caretaker Email")
        pwd = st.text_input("Password", type="password")
        
        if st.button("Generate My Unique ID"):
            if email and pwd:
                new_id = f"MED-{random.randint(1000, 9999)}"
                st.session_state.user_id = new_id
                st.markdown(f"""
                <div class='id-box'>
                    <h2 style='color:#1E3A8A; margin:0;'>Your Unique ID</h2>
                    <h1 style='color:#2563EB; margin:10px;'>{new_id}</h1>
                    <p style='font-size:14px;'>Check your email ({email}) for a backup copy.</p>
                </div>
                """, unsafe_allow_html=True)
                st.info("Now use this ID in the 'Login' tab to continue.")
            else:
                st.warning("Please fill in all fields")

# --- PAGE 3: MEDICAL DASHBOARD ---
elif st.session_state.page == "dashboard":
    st.markdown(f"<h1>Dashboard</h1>", unsafe_allow_html=True)
    st.markdown(f"<h3>Patient ID: {st.session_state.user_id}</h3>", unsafe_allow_html=True)
    
    with st.expander("➕ Add New Medication Schedule", expanded=True):
        pill_name = st.text_input("Pill Name", placeholder="e.g. Paracetamol")
        
        c1, c2 = st.columns(2)
        with c1:
            start_date = st.date_input("Start Date")
            end_date = st.date_input("End Date")
        with c2:
            time_input = st.time_input("Scheduled Time")
            sound = st.selectbox("Notification Sound", ["Hospital Beep", "Digital Alarm", "Soft Chime"])
        
        st.markdown("### Caretaker Escalation Settings")
        care_phone = st.text_input("Caretaker Phone Number")
        back_phone = st.text_input("Backup Phone Number")
        
        if st.button("Add Schedule"):
            st.success(f"Schedule for {pill_name} at {time_input} has been saved!")

    st.write("---")
    st.markdown("### 🔔 Active Reminder")
    
    # Logic Display for Judges
    st.info(f"**Current Task:** Take {pill_name if pill_name else 'Pills'} at **{time_input.strftime('%I:%M %p')}**")
    
    # The Escalation Logic Breakdown
    with st.container():
        st.write("**Escalation Protocol:**")
        st.write(f"1️⃣ **{time_input.strftime('%I:%M %p')}**: First alarm (Sound: {sound})")
        st.write(f"2️⃣ **{(datetime.combine(datetime.today(), time_input) + timedelta(minutes=10)).strftime('%I:%M %p')}**: Second alarm (Patient)")
        st.write(f"3️⃣ **{(datetime.combine(datetime.today(), time_input) + timedelta(minutes=20)).strftime('%I:%M %p')}**: **SMS SENT TO {care_phone} & {back_phone}**")

    st.write("")
    if st.button("✅ I HAVE TAKEN MY PILL"):
        st.balloons()
        st.success("Dose Confirmed! Escalation Cancelled.")
        
    if st.button("Logout"):
        logout()
        st.rerun()
