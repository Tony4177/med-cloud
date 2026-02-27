import streamlit as st
from datetime import time

# 1. Page Configuration
st.set_page_config(page_title="Med-Cloud Pro", layout="centered")

# 2. THE GLOBAL OVERLAP KILLER & STYLE (FORCED IMAGE 2 LOOK)
st.markdown("""
    <style>
    /* 1. FORCE THE LIGHT BACKGROUND */
    .stApp { background-color: #FFFFFF !important; }
    
    /* 2. THE GLOBAL OVERLAP KILLER - HIDES "arrow_drop_down" EVERYWHERE */
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
    
    /* 3. STYLE THE HEADER BAR (Mirroring Image 2) */
    .streamlit-expanderHeader { 
        background-color: #1E1E2E !important; 
        border-radius: 4px !important; 
        padding: 10px !important; 
    }
    .streamlit-expanderHeader p { 
        color: #1A73E8 !important; 
        font-weight: 600 !important; 
    }

    /* 4. FIX BOX VISIBILITY (White background, Blue borders) */
    input, [data-baseweb="input"], [data-baseweb="select"], .stNumberInput div {
        background-color: #FFFFFF !important; 
        color: #000000 !important; 
        border: 2px solid #1A73E8 !important;
    }

    /* 5. TITLES AND LABELS (High Visibility Blue) */
    h1, h2, h3, label, p, .stMarkdownContainer p { 
        color: #1A73E8 !important; 
        font-weight: 600 !important; 
    }

    /* 6. BUTTON STYLE */
    div[data-testid="stButton"] button {
        background-color: #1A73E8 !important;
        color: white !important;
        border-radius: 8px !important;
        border: none !important;
        font-weight: bold !important;
    }

    header {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# --- SESSION STATE (THE LOCKING SYSTEM) ---
if 'page' not in st.session_state: 
    st.session_state.page = "welcome"
if 'current_user' not in st.session_state: 
    st.session_state.current_user = None

# --- PAGE 1: WELCOME SCREEN (IMAGE & CONTINUE) ---
if st.session_state.page == "welcome":
    st.markdown("<h1 style='text-align:center;'>Smart Healthcare Monitoring</h1>", unsafe_allow_html=True)
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
            st.info("Directing to Account Creation...")
    with col_btn2:
        if st.button("Next"):
            if user_id:
                st.session_state.current_user = user_id
                st.session_state.page = "dashboard"
                st.rerun()

# --- PAGE 3: DASHBOARD (MIRRORING IMAGE 2 - NO OVERLAP) ---
elif st.session_state.page == "dashboard":
    st.markdown("<h1 style='text-align:center;'>Doctor Help</h1>", unsafe_allow_html=True)
    st.markdown(f"### Patient Dashboard: {st.session_state.current_user}")
    st.markdown("---")
    
    with st.expander("Add Medication Reminder", expanded=True):
        st.text_input("Medicine Name", placeholder="frgreg")
        
        # Grid layout for dates
        c1, c2 = st.columns(2)
        with c1: st.date_input("Start Date")
        with c2: st.date_input("End Date")
        
        dosage = st.number_input("Dosage Per Day", min_value=1, max_value=8, value=4)
        
        st.write("Set Times:")
        # 2-Column Grid for Doses (Dose 1, Dose 2, etc.)
        t_cols = st.columns(2)
        for i in range(int(dosage)):
            with t_cols[i % 2]:
                d_times = [time(7, 30), time(12, 0), time(16, 0), time(20, 0)]
                st.time_input(f"Dose {i+1}", value=d_times[i] if i < 4 else time(10,0), key=f"d_input_{i}")

        st.markdown("### Caretaker Details")
        st.text_input("Caretaker Name")
        cp1, cp2 = st.columns(2)
        with cp1: st.text_input("Primary Phone")
        with cp2: st.text_input("Secondary Phone")
        st.button("Set Reminder")

    if st.button("Log Out"):
        st.session_state.page = "welcome"
        st.session_state.current_user = None
        st.rerun()
