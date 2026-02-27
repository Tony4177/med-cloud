import streamlit as st
import random
from datetime import time

# 1. Page Configuration
st.set_page_config(page_title="Med-Cloud Pro", layout="centered")

# 2. CSS - FIXING OVERLAPS AND REMOVING GLITCHES
st.markdown("""
    <style>
    /* FORCE WHITE BACKGROUND */
    .stApp, [data-testid="stAppViewContainer"] {
        background-color: #FFFFFF !important;
    }

    /* REMOVE THE "arrow_drop_down" OVERLAP GLITCH COMPLETELY */
    .streamlit-expanderHeader p::after, 
    .streamlit-expanderHeader span, 
    .streamlit-expanderHeader svg,
    .streamlit-expanderHeader div::after {
        display: none !important;
        content: "" !important;
    }
    
    /* CLEAN EXPANDER HEADER */
    .streamlit-expanderHeader {
        background-color: #F0F7FF !important;
        border: 2px solid #1A73E8 !important;
        border-radius: 10px !important;
        padding: 12px !important;
        color: #1A73E8 !important;
    }

    /* FIX BLACK-ON-BLACK TEXT BOXES */
    input, select, textarea, [data-baseweb="input"], .stNumberInput div {
        background-color: #FFFFFF !important;
        color: #000000 !important;
        border: 2px solid #1A73E8 !important;
    }
    
    /* TEXT COLORS */
    h1, h2, h3, h4, label, p {
        color: #1A73E8 !important;
        font-weight: 600 !important;
    }

    /* BUTTONS */
    div[data-testid="stButton"] button {
        background-color: #1A73E8 !important;
        color: #FFFFFF !important;
        border-radius: 8px !important;
        border: none !important;
        width: 100% !important;
    }

    /* HEADER */
    .dashboard-header { 
        display: flex; 
        justify-content: space-between; 
        align-items: center; 
        margin-bottom: 25px; 
        padding-bottom: 10px;
    }
    .profile-icon { 
        width: 45px; height: 45px; 
        background-color: #E8F0FE; 
        border-radius: 50%; 
        display: flex; 
        align-items: center; 
        justify-content: center; 
        border: 2px solid #1A73E8; 
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
    if st.button("Continue ➔"): 
        st.session_state.page = "auth"
        st.rerun()

# --- PAGE 2: AUTH (SIGN IN) ---
elif st.session_state.page == "auth":
    st.markdown("<h3>Sign in</h3>", unsafe_allow_html=True)
    user_id_input = st.text_input("Med-Cloud ID", placeholder="ex: (MED-1234)", key="login_id")
    
    if st.button("Forgot ID?"): 
        st.session_state.page = "forgot_id"
        st.rerun()
    
    col_l, col_r = st.columns(2)
    with col_l:
        if st.button("Create account"): 
            st.session_state.page = "create_account"
            st.rerun()
    with col_r:
        if st.button("Next"):
            if user_id_input: 
                st.session_state.current_user = user_id_input
                st.session_state.page = "dashboard"
                st.rerun()

# --- PAGE 3: DASHBOARD (REMOVED HEALTH CARDS) ---
elif st.session_state.page == "dashboard":
    st.markdown(f"""
        <div class="dashboard-header">
            <div class="profile-icon"><img src="https://cdn-icons-png.flaticon.com/512/3135/3135715.png" width="35"></div>
            <h2 style="margin:0;">Doctor Help</h2>
            <div>
                <div style="width:22px; height:3px; background:#1A73E8; margin:4px;"></div>
                <div style="width:22px; height:3px; background:#1A73E8; margin:4px;"></div>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown(f"<h3>Patient: {st.session_state.current_user}</h3>", unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("<h3>Pill Reminders</h3>", unsafe_allow_html=True)
    
    # REMINDER FORM (Arrow overlapping text is now hidden by CSS)
    with st.expander("Add Medication Reminder", expanded=True):
        med_name = st.text_input("Medicine Name", placeholder="Enter name")
        
        c_d1, c_d2 = st.columns(2)
        with c_d1: s_date = st.date_input("Start Date")
        with c_d2: e_date = st.date_input("End Date")
        
        dosage = st.number_input("Dosage Per Day", min_value=1, max_value=8, value=1)
        
        st.write("Set Dose Times:")
        time_slots = []
        t_cols = st.columns(2)
        for i in range(int(dosage)):
            with t_cols[i % 2]:
                t = st.time_input(f"Dose {i+1}", value=time(8+(i*4)%24, 0), key=f"t_slot_{i}")
                time_slots.append(t.strftime("%I:%M %p"))

        st.markdown("#### Caretaker Information")
        ct_name = st.text_input("Caretaker Name")
        cp1, cp2 = st.columns(2)
        with cp1: p1 = st.text_input("Primary Phone")
        with cp2: p2 = st.text_input("Secondary Phone")

        if st.button("Set Reminder"):
            if med_name:
                st.session_state.reminders.append({"med": med_name, "times": ", ".join(time_slots)})
                st.success(f"Reminder for {med_name} Saved!")

    # Display List
    if st.session_state.reminders:
        for r in st.session_state.reminders:
            st.info(f"💊 {r['med']} | {r['times']}")

    if st.button("Sign Out"): 
        st.session_state.page = "auth"
        st.rerun()

# --- OTHER PAGES ---
elif st.session_state.page == "create_account":
    st.markdown("<h3>Create Account</h3>", unsafe_allow_html=True)
    if st.button("Verify"):
        st.session_state.generated_id = f"MED-{random.randint(1000, 9999)}"
        st.rerun()
    if 'generated_id' in st.session_state:
        st.success(f"ID: {st.session_state.generated_id}")
        if st.button("Go to Sign In"): 
            st.session_state.page = "auth"
            st.rerun()

elif st.session_state.page == "forgot_id":
    if st.button("← Back"): 
        st.session_state.page = "auth"
        st.rerun()

