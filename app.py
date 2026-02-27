import streamlit as st
import random
from datetime import time

# 1. Page Configuration
st.set_page_config(page_title="Med-Cloud Pro", layout="centered")

# 2. CSS - TARGETED FIX FOR "arrow_drop_down" OVERLAP
st.markdown("""
    <style>
    /* 1. FORCE THE ENTIRE APP TO STAY WHITE (Light Mode) */
    .stApp, [data-testid="stAppViewContainer"] {
        background-color: #FFFFFF !important;
    }

    /* 2. THE OVERLAP KILLER: This removes the glitchy "arrow_drop_down" text */
    /* We target the span and the pseudo-elements that Streamlit uses for icons */
    .streamlit-expanderHeader span, 
    .streamlit-expanderHeader svg,
    .streamlit-expanderHeader::after,
    .streamlit-expanderHeader p::after {
        display: none !important;
        visibility: hidden !important;
        content: "" !important;
        width: 0 !important;
        height: 0 !important;
    }
    
    /* 3. CLEAN BLUE BAR FOR THE TITLE */
    .streamlit-expanderHeader {
        background-color: #F0F7FF !important;
        border: 2px solid #1A73E8 !important;
        border-radius: 10px !important;
        color: #1A73E8 !important;
        font-weight: bold !important;
        display: flex !important;
        justify-content: center !important;
    }

    /* 4. FIX BOX VISIBILITY (White background, Black text) */
    input, select, textarea, [data-baseweb="input"], .stNumberInput div {
        background-color: #FFFFFF !important;
        color: #000000 !important;
        border: 2px solid #1A73E8 !important;
    }
    
    /* 5. TITLES AND LABELS */
    h1, h2, h3, h4, label, p {
        color: #1A73E8 !important;
        font-weight: 600 !important;
    }

    /* 6. BUTTONS (Solid Blue) */
    div[data-testid="stButton"] button {
        background-color: #1A73E8 !important;
        color: #FFFFFF !important;
        border-radius: 8px !important;
        width: 100% !important;
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
    user_id_input = st.text_input("Med-Cloud ID", placeholder="MED-1234")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Create account"): st.session_state.page = "create_account"; st.rerun()
    with col2:
        if st.button("Next"):
            if user_id_input: 
                st.session_state.current_user = user_id_input
                st.session_state.page = "dashboard"
                st.rerun()

# --- PAGE 3: DASHBOARD (NO OVERLAP / NO HEALTH STATS) ---
elif st.session_state.page == "dashboard":
    # Simple Header
    st.markdown(f"""
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px;">
            <div style="width: 45px; height: 45px; background: #E8F0FE; border-radius: 50%; display: flex; align-items: center; justify-content: center; border: 2px solid #1A73E8;">
                <img src="https://cdn-icons-png.flaticon.com/512/3135/3135715.png" width="30">
            </div>
            <h2 style="margin:0;">Doctor Help</h2>
            <div style="width:22px;"></div>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown(f"<h3>Patient: {st.session_state.current_user}</h3>", unsafe_allow_html=True)
    st.markdown("---")
    
    # PILL REMINDERS (The "arrow_drop_down" is hidden by the CSS above)
    st.markdown("<h3>Pill Reminders</h3>", unsafe_allow_html=True)
    
    with st.expander("Add Medication Reminder", expanded=True):
        med_name = st.text_input("Medicine Name", placeholder="e.g. Paracetamol")
        
        c1, c2 = st.columns(2)
        with c1: start_d = st.date_input("Start Date")
        with c2: end_d = st.date_input("End Date")
        
        dosage = st.number_input("Dosage Per Day", min_value=1, max_value=8, value=1)
        
        st.write("Set Times:")
        time_slots = []
        t_cols = st.columns(2)
        for i in range(int(dosage)):
            with t_cols[i % 2]:
                t = st.time_input(f"Dose {i+1}", value=time(8+(i*4)%24, 0), key=f"t_{i}")
                time_slots.append(t.strftime("%I:%M %p"))

        st.markdown("#### Caretaker Details")
        ct_name = st.text_input("Caretaker Name")
        cp1, cp2 = st.columns(2)
        with cp1: p1 = st.text_input("Primary Number")
        with cp2: p2 = st.text_input("Secondary Number")

        if st.button("Set Reminder"):
            if med_name:
                st.session_state.reminders.append({"med": med_name, "times": ", ".join(time_slots)})
                st.success("Schedule Saved!")

    # Display Active List
    for r in st.session_state.reminders:
        st.info(f"💊 {r['med']} | Times: {r['times']}")

    if st.button("Sign Out"): 
        st.session_state.page = "auth"
        st.rerun()

# --- OTHER PAGES ---
elif st.session_state.page == "create_account":
    st.markdown("<h3>Create Account</h3>", unsafe_allow_html=True)
    if st.button("Get ID"):
        st.session_state.generated_id = f"MED-{random.randint(1000, 9999)}"
        st.rerun()
    if 'generated_id' in st.session_state:
        st.success(f"Your ID: {st.session_state.generated_id}")
        if st.button("Back to Login"): st.session_state.page = "auth"; st.rerun()
