import streamlit as st
import random
from datetime import time

# 1. Page Configuration
st.set_page_config(page_title="Med-Cloud Pro", layout="centered")

# 2. THE HIGH-VISIBILITY CSS OVERWRITE
st.markdown("""
    <style>
    /* FORCE THE ENTIRE APP TO STAY WHITE */
    .stApp, [data-testid="stAppViewContainer"], [data-testid="stHeader"] {
        background-color: #FFFFFF !important;
    }

    /* KILL THE "arrow_drop_down" OVERLAP GLITCH - STRENGTHENED */
    .streamlit-expanderHeader p::after, 
    .streamlit-expanderHeader span, 
    .streamlit-expanderHeader svg,
    [data-testid="stExpander"] svg,
    .st-emotion-cache-p88vun, 
    .st-emotion-cache-1pxmthq {
        display: none !important;
        visibility: hidden !important;
    }
    
    .streamlit-expanderHeader {
        background-color: #F0F7FF !important;
        border: 2px solid #1A73E8 !important;
        border-radius: 10px !important;
        padding: 10px !important;
    }

    /* FIX THE BOXES (INPUT FIELDS) */
    input, select, textarea, [data-baseweb="input"], [data-baseweb="select"], .stNumberInput div {
        background-color: #FFFFFF !important;
        color: #000000 !important;
        border: 2px solid #1A73E8 !important;
        opacity: 1 !important;
    }
    
    input::placeholder { color: #757575 !important; }

    /* TEXT COLOR FORCE (Deep Blue) */
    h1, h2, h3, h4, label, p, .stMarkdownContainer p {
        color: #1A73E8 !important;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif !important;
        font-weight: 600 !important;
    }

    /* BUTTONS (Solid Blue, White Text) */
    div[data-testid="stButton"] button {
        background-color: #1A73E8 !important;
        color: #FFFFFF !important;
        border-radius: 8px !important;
        border: none !important;
        padding: 10px 24px !important;
        width: 100% !important;
    }
    
    /* SIGN OUT STYLING */
    div[data-testid="stButton"] button:has(div p:contains("Sign Out")) {
        background-color: #333333 !important;
        width: auto !important;
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
    st.markdown("""<div style='display: flex; align-items: center; gap: 12px; margin-bottom: 10px;'><img src='https://cdn-icons-png.flaticon.com/512/2966/2966327.png' width='30'><h2>Med-Cloud Pro</h2></div>""", unsafe_allow_html=True)
    st.markdown("<h3>Sign in</h3>", unsafe_allow_html=True)
    st.markdown("<p>Med-Cloud ID</p>", unsafe_allow_html=True)
    user_id_input = st.text_input("", placeholder="ex: (MED-1234)", key="login_id", label_visibility="collapsed")
    
    if st.button("Forgot ID?"): 
        st.session_state.page = "forgot_id"
        st.rerun()
    
    col_l, col_r = st.columns([1, 1])
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

# --- PAGE 3: DASHBOARD ---
elif st.session_state.page == "dashboard":
    st.markdown(f"""
        <div style="display: flex; justify-content: space-between; align-items: center; padding-bottom: 10px; border-bottom: 1px solid #E0E0E0;">
            <div style="width: 45px; height: 45px; background-color: #E8F0FE; border-radius: 50%; display: flex; align-items: center; justify-content: center; border: 2px solid #1A73E8;"><img src="https://cdn-icons-png.flaticon.com/512/3135/3135715.png" width="35"></div>
            <h2 style="margin:0;">Doctor Help</h2>
            <div style="width:22px; color:#1A73E8;">☰</div>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown(f"<h3>Patient: {st.session_state.current_user}</h3>", unsafe_allow_html=True)
    st.markdown("---")
    st.markdown("### Pill Reminders")
    
    with st.expander("Add New Medication Reminder", expanded=True):
        med_name = st.text_input("Medicine Name", placeholder="Type medicine name here")
        c_d1, c_d2 = st.columns(2)
        with c_d1: s_date = st.date_input("Start Date")
        with c_d2: e_date = st.date_input("End Date")
        
        dosage = st.number_input("Dosage Per Day (Doses)", min_value=1, max_value=8, value=1)
        
        time_slots = []
        t_cols = st.columns(2)
        for i in range(int(dosage)):
            with t_cols[i % 2]:
                t = st.time_input(f"Dose {i+1}", value=time(8+(i*4)%24, 0), key=f"t_slot_{i}")
                time_slots.append(t.strftime("%I:%M %p"))

        st.markdown("#### Caretaker Details")
        ct_name = st.text_input("Caretaker Name")
        cp1, cp2 = st.columns(2)
        with cp1: p1 = st.text_input("Primary Phone")
        with cp2: p2 = st.text_input("Secondary Phone")

        if st.button("Set Reminder"):
            if med_name:
                st.session_state.reminders.append({"med": med_name, "times": ", ".join(time_slots)})
                st.success(f"Reminder for {med_name} locked!")

    if st.session_state.reminders:
        st.markdown("#### Active Schedule")
        for r in st.session_state.reminders:
            st.info(f"💊 {r['med']} | Times: {r['times']}")

    if st.button("Sign Out"): 
        st.session_state.page = "auth"
        st.session_state.current_user = None
        st.rerun()

# --- CREATE ACCOUNT PAGE ---
elif st.session_state.page == "create_account":
    st.markdown("<h3>Create Account</h3>", unsafe_allow_html=True)
    if st.button("Verify & Register"):
        st.session_state.generated_id = f"MED-{random.randint(1000, 9999)}"
    
    if 'generated_id' in st.session_state:
        st.success(f"Generated ID: {st.session_state.generated_id}")
        if st.button("Go to Sign In"): 
            st.session_state.page = "auth"
            st.rerun()

# --- FORGOT ID PAGE ---
elif st.session_state.page == "forgot_id":
    st.title("Recovery")
    if st.button("← Back"): 
        st.session_state.page = "auth"
        st.rerun()

