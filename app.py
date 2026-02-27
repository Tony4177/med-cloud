import streamlit as st
from datetime import time

# 1. Page Configuration
st.set_page_config(page_title="Med-Cloud Pro", layout="centered")

# 2. THE OVERLAP KILLER (Removes the glitch without changing your colors)
st.markdown("""
    <style>
    /* Keeps the background white as seen in your screenshot */
    .stApp { background-color: #FFFFFF !important; }
    
    /* GLOBAL FIX: This deletes the overlapping "arrow_drop_down" text glitch */
    span:contains("arrow_"), 
    .streamlit-expanderHeader span, 
    .streamlit-expanderHeader svg,
    [data-testid="stExpander"] svg, 
    div[data-baseweb="icon"], 
    div[data-baseweb="select"] svg {
        display: none !important; 
        visibility: hidden !important; 
        width: 0px !important; 
        height: 0px !important;
        content: "" !important;
    }
    
    /* YOUR COLORS: Dark Navy Header (#1E1E2E) and Blue Text (#1A73E8) */
    .streamlit-expanderHeader { 
        background-color: #1E1E2E !important; 
        border-radius: 4px !important; 
        padding: 10px !important;
    }
    .streamlit-expanderHeader p { 
        color: #1A73E8 !important; 
        font-weight: 600 !important; 
    }

    /* INPUT BOXES: White with Blue borders to match your screenshot */
    input, [data-baseweb="input"], .stNumberInput div {
        background-color: #FFFFFF !important; 
        color: #000000 !important; 
        border: 2px solid #1A73E8 !important;
    }

    /* TITLES AND LABELS: High visibility Blue (#1A73E8) */
    h1, h2, h3, label, p, .stMarkdownContainer p { 
        color: #1A73E8 !important; 
        font-weight: 600 !important; 
    }

    /* BUTTON STYLE */
    div[data-testid="stButton"] button {
        background-color: #1A73E8 !important;
        color: white !important;
        border-radius: 8px !important;
        font-weight: bold !important;
    }

    header {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# --- SESSION STATE (THE LOCKING SYSTEM) ---
# Ensures the app starts at the Welcome Page every time it is refreshed
if 'page' not in st.session_state: 
    st.session_state.page = "welcome"
if 'current_user' not in st.session_state: 
    st.session_state.current_user = None

# --- PAGE 1: WELCOME SCREEN ---
if st.session_state.page == "welcome":
    st.markdown("<h1 style='text-align:center;'>Smart Healthcare Monitoring</h1>", unsafe_allow_html=True)
    # The healthcare image we previously selected
    st.image("https://img.freepik.com/free-vector/health-professional-team-concept-illustration_114360-1608.jpg")
    
    if st.button("Continue ➔"): 
        st.session_state.page = "auth"
        st.rerun()

# --- PAGE 2: SIGN IN / SIGN UP ---
elif st.session_state.page == "auth":
    st.markdown("### Sign in")
    user_id = st.text_input("Med-Cloud ID", placeholder="ex: MED-1234")
    
    col_btn1, col_btn2 = st.columns([1, 1])
    with col_btn1:
        if st.button("Create account"):
            st.info("Creating Account...")
    with col_btn2:
        if st.button("Next"):
            if user_id:
                st.session_state.current_user = user_id
                st.session_state.page = "dashboard"
                st.rerun()

# --- PAGE 3: DASHBOARD (Exact layout from your screenshot) ---
elif st.session_state.page == "dashboard":
    st.markdown("## Pill Reminders")
    
    # The glitch is now removed from this header bar
    with st.expander("Add New Medication Schedule", expanded=True):
        st.text_input("Medicine Name", placeholder="e.g., Metformin")
        
        # Grid layout for dates
        c1, c2 = st.columns(2)
        with c1: st.date_input("Start Date")
        with c2: st.date_input("End Date")
        
        st.number_input("Dosage Per Day (Number of times)", min_value=1, value=1)
        
        st.write("Set Specific Times:")
        st.time_input("Dose 1", value=time(8, 0))

        st.markdown("### Caretaker Details")
        st.text_input("Caretaker Name")
        
        col_phone1, col_phone2 = st.columns(2)
        with col_phone1: st.text_input("Primary Number")
        with col_phone2: st.text_input("Secondary Number")
        
        st.button("Set Reminder")

    if st.button("Log Out"):
        st.session_state.page = "welcome"
        st.session_state.current_user = None
        st.rerun()
