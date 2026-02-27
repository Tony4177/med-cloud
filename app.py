import streamlit as st
import random
from datetime import datetime, timedelta

# 1. Page Configuration
st.set_page_config(page_title="Med-Cloud Pro", layout="centered")

# 2. Custom CSS for Professional Medical Look (No Black, No Box on Front Page)
st.markdown("""
    <style>
    /* Global Background and Text */
    .stApp { background-color: #FFFFFF; }
    
    /* Global Text Visibility Fix */
    p, span, label, .stMarkdown { color: #1E293B !important; }

    /* Headline Styling */
    .main-headline {
        text-align: center; 
        color: #1E3A8A; 
        font-weight: bold; 
        font-size: 24px;
        margin-top: 20px;
        margin-bottom: 20px;
    }

    /* Professional Action Blue Button - Reduced Width */
    .stButton>button {
        background-color: #2563EB !important;
        color: white !important;
        border-radius: 8px !important;
        border: none !important;
        padding: 10px 20px !important;
        font-weight: bold !important;
        font-size: 16px !important;
        width: 100% !important;
    }
    .stButton>button:hover { background-color: #1E40AF !important; }
    
    /* Medical Card Styling for Dashboard */
    .med-card {
        background-color: #F8FAFC;
        padding: 20px;
        border-radius: 12px;
        border: 1px solid #E2E8F0;
        margin-bottom: 15px;
    }
    
    /* Hide Streamlit Header/Footer for cleaner Look */
    header {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# Initialize Session States
if 'page' not in st.session_state: st.session_state.page = "welcome"
if 'user_id' not in st.session_state: st.session_state.user_id = None
if 'history_count' not in st.session_state: st.session_state.history_count = 0

# --- PAGE 1: WELCOME (Updated Design) ---
if st.session_state.page == "welcome":
    # Image at the very top (No title above it)
    st.image("https://img.freepik.com/free-vector/health-professional-team-concept-illustration_114360-1608.jpg", use_container_width=True)

    # Centered, Bold Title
    st.markdown("<div class='main-headline'>Smart Healthcare Monitoring & Caretaker Escalation</div>", unsafe_allow_html=True)

    # 10 Lines of Professional Description (No Box)
    st.markdown("""
    <p style='text-align: center; line-height: 1.8;'>
    Our cloud-integrated platform redefines patient medication adherence.<br>
    Using advanced real-time tracking, we eliminate the risk of missed doses.<br>
    The system features a 3-step smart escalation protocol for patient safety.<br>
    If a dose is not confirmed, automated alerts are sent to the primary caretaker.<br>
    A secondary backup notification ensures no emergency goes unnoticed.<br>
    Built with a secure architecture to protect sensitive patient medical data.<br>
    Designed for easy accessibility across all mobile and desktop devices.<br>
    Bridging the communication gap between patients, families, and doctors.<br>
    Empowering elderly users to manage chronic conditions independently.<br>
    Your digital health companion for a safer, more connected tomorrow.
    </p>
    """, unsafe_allow_html=True)

    # Centered Button with reduced width
    st.write("") 
    col1, col2, col3 = st.columns([1.3, 1, 1.3])
    with col2:
        if st.button("Continue ➔"):
            st.session_state.page = "auth"
            st.rerun()

# --- PAGE 2: AUTH / LOGIN ---
elif st.session_state.page == "auth":
    st.markdown("<h2 style='text-align: center; color: #1E3A8A;'>System Access</h2>", unsafe_allow_html=True)
    
    tab1, tab2 = st.tabs(["Existing User", "New Caretaker"])
    
    with tab1:
        login_id = st.text_input("Enter Patient ID", placeholder="e.g. MED-1234")
        if st.button("Access Dashboard"):
            if login_id:
                st.session_state.user_id = login_id
                st.session_state.page = "dashboard"
                st.rerun()
            
    with tab2:
        st.write("Register to receive a Unique ID.")
        email = st.text_input("Caretaker Email")
        pwd = st.text_input("Password", type="password")
        if st.button("Generate My ID"):
            if email and pwd:
                new_id = f"MED-{random.randint(1000, 9999)}"
                st.session_state.user_id = new_id
                st.success(f"ID Created: {new_id}")
                st.info("Log in using this ID in the first tab.")

# --- PAGE 3: DASHBOARD ---
elif st.session_state.page == "dashboard":
    # Top Navigation
    nav_l, nav_m, nav_r = st.columns([1, 4, 1])
    with nav_l:
        if st.button("👤"): st.session_state.page = "profile"
    with nav_m:
        st.markdown(f"<h3 style='text-align: center; margin:0;'>ID: {st.session_state.user_id}</h3>", unsafe_allow_html=True)
    with nav_r:
        if st.button("🚪"): 
            st.session_state.page = "welcome"
            st.rerun()

    # AI Doctor Section
    st.markdown("<div class='med-card'>", unsafe_allow_html=True)
    st.markdown("### 🤖 Help Doctor (AI Assistant)")
    user_q = st.text_input("Ask about symptoms or tablets:", placeholder="Side effects of Paracetamol?")
    if user_q:
        st.info(f"**AI Doctor:** Based on medical guidelines for '{user_q}', standard dosages vary by age. Always verify with your physician.")
    st.markdown("</div>", unsafe_allow_html=True)

    # Add Medication
    with st.expander("➕ Add New Medication Schedule", expanded=True):
        p_name = st.text_input("Pill Name")
        c1, c2 = st.columns(2)
        with c1:
            start_d = st.date_input("Start Date")
            t_input = st.text_input("Set Time (e.g. 18:30)", value="06:00 PM")
        with c2:
            end_d = st.date_input("End Date")
            sound = st.selectbox("Alarm", ["Loud Beep", "Voice", "Chime"])
        
        c_no = st.text_input("Primary Caretaker No.")
        b_no = st.text_input("Backup Caretaker No.")
        
        if st.button("Save Schedule"):
            st.success(f"Escalation Logic Armed for {p_name} at {t_input}")

    # Active Reminder
    st.divider()
    st.markdown(f"### 🔔 Current Reminder: {p_name if p_name else 'Medication'}")
    st.write(f"Scheduled for: **{t_input}** | Escalation Active: Yes")
    
    if st.button("✅ I HAVE TAKEN MY PILL"):
        st.balloons()
        st.session_state.history_count += 1
        st.success("Caretaker Alert Cancelled. Dose logged.")

# --- PAGE 4: PROFILE ---
elif st.session_state.page == "profile":
    st.markdown("<h2 style='text-align: center; color: #1E3A8A;'>Patient Profile</h2>", unsafe_allow_html=True)
    
    st.markdown("<div class='med-card'>", unsafe_allow_html=True)
    st.metric("Total Doses Confirmed", f"{st.session_state.history_count}")
    st.write("Adherence Streak: **Strong**")
    st.markdown("</div>", unsafe_allow_html=True)
    
    st.text_input("Update Name", value="Tony")
    st.text_input("Update User ID", value=st.session_state.user_id)
    
    if st.button("Save & Back"):
        st.session_state.page = "dashboard"
        st.rerun()
