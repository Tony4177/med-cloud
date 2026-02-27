import streamlit as st
import random
from datetime import datetime, timedelta

# 1. Advanced Page Config
st.set_page_config(page_title="MedRemind Pro", layout="centered", initial_sidebar_state="collapsed")

# 2. Premium UI Styling (White & Clean)
st.markdown("""
    <style>
    .stApp { background-color: #FFFFFF; }
    
    /* Header Bar */
    .nav-bar {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 10px 20px;
        background: #F8FAFC;
        border-bottom: 1px solid #E2E8F0;
        margin-bottom: 20px;
        border-radius: 10px;
    }
    
    /* Premium Buttons */
    .stButton>button {
        background: linear-gradient(135deg, #0052cc 0%, #0074e4 100%);
        color: white;
        border-radius: 12px;
        border: none;
        padding: 15px;
        font-weight: 600;
        transition: all 0.3s;
    }
    .stButton>button:hover { transform: translateY(-2px); box-shadow: 0 5px 15px rgba(0,82,204,0.3); }
    
    /* AI Chat Box */
    .ai-box {
        background: #F0F7FF;
        border-left: 5px solid #0052cc;
        padding: 15px;
        border-radius: 8px;
        margin: 10px 0;
    }
    </style>
    """, unsafe_allow_html=True)

# Initialize Session States
if 'page' not in st.session_state: st.session_state.page = "welcome"
if 'user_id' not in st.session_state: st.session_state.user_id = None

# --- TOP NAVIGATION BAR ---
def draw_nav():
    cols = st.columns([1, 8, 1])
    with cols[0]: st.button("👤") # Profile
    with cols[1]: st.markdown("<h3 style='text-align:center;margin:0;'>MedRemind</h3>", unsafe_allow_html=True)
    with cols[2]: 
        if st.button("☰"): st.toast("Settings & Help coming soon!")

# --- PAGE 1: WELCOME (The "Hook") ---
if st.session_state.page == "welcome":
    st.markdown("<h1>Med-Cloud Pro</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center;'>Advanced Patient Adherence & Caretaker Escalation System</p>", unsafe_allow_html=True)
    
    # Hero Section
    st.image("https://img.freepik.com/free-vector/doctors-concept-illustration_114360-1515.jpg", use_container_width=True)
    
    st.markdown("""
    <div style='background:#F1F5F9; padding:20px; border-radius:15px;'>
    <b>Why MedRemind?</b><br>
    ✅ 3-Step Escalation Logic (6:00 → 6:10 → 6:20 Alert)<br>
    ✅ Unique Caretaker IDs for Privacy<br>
    ✅ 24/7 AI Health Assistant
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("Get Started ➔"):
        st.session_state.page = "auth"
        st.rerun()

# --- PAGE 2: AUTH ---
elif st.session_state.page == "auth":
    draw_nav()
    st.markdown("<h2>Access Portal</h2>", unsafe_allow_html=True)
    tab1, tab2 = st.tabs(["Login with ID", "Create ID"])
    
    with tab1:
        u_id = st.text_input("Enter Unique ID")
        if st.button("Enter Dashboard"):
            st.session_state.user_id = u_id
            st.session_state.page = "dashboard"
            st.rerun()
            
    with tab2:
        st.write("New Caretaker? Register below.")
        st.text_input("Email")
        st.text_input("Password", type="password")
        if st.button("Generate ID"):
            new_id = f"MED-{random.randint(1000,9999)}"
            st.success(f"Your ID: {new_id}")

# --- PAGE 3: DASHBOARD & AI ---
elif st.session_state.page == "dashboard":
    draw_nav()
    
    # 1. AI DOCTOR SECTION
    with st.expander("🤖 Ask AI Doctor (Symptoms/Tablets)", expanded=False):
        st.markdown("<div class='ai-box'>I am your AI health assistant. Ask me about medicine side effects or dosages.</div>", unsafe_allow_html=True)
        query = st.text_input("Type your question here...")
        if query:
            st.write(f"**AI Response:** Based on medical guidelines, {query} should be discussed with a doctor, but generally, users report...")
            st.warning("Note: AI is for info only. Consult a real doctor.")

    # 2. ADD MEDICATION (THE FULL STUFF)
    st.markdown("### ➕ Add Medication")
    with st.container():
        p_name = st.text_input("Pill Name")
        col1, col2 = st.columns(2)
        with col1:
            start = st.date_input("Start Date")
            end = st.date_input("End Date")
        with col2:
            # FLEXIBLE TIME INPUT (AM/PM)
            t_str = st.text_input("Time (e.g. 16:30 or 06:00 PM)", value="18:00")
            sound = st.selectbox("Alarm", ["Loud Beep", "Voice Alert", "Melody"])
        
        reason = st.text_area("Why are you taking this pill? (Optional)")
        
        st.markdown("#### Caretaker Escalation")
        c1, c2 = st.columns(2)
        with c1: c_phone = st.text_input("Primary Phone")
        with c2: b_phone = st.text_input("Backup Phone")
        
        if st.button("Set Schedule & Activate Escalation"):
            st.success("System Armed! 6:00 -> 6:10 -> 6:20 sequence set.")

    # 3. ACTIVE DOSES
    st.divider()
    st.markdown("### 🔔 Active Reminders")
    c1, c2 = st.columns([3, 1])
    with c1:
        st.info(f"**{p_name if p_name else 'Medicine'}** at {t_str}")
        st.write("Status: *Escalation Active*")
    with c2:
        if st.button("DONE ✅"):
            st.balloons()

    if st.button("Logout"):
        st.session_state.page = "welcome"
        st.rerun()
