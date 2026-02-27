import streamlit as st
import random
from datetime import time

# 1. Page Configuration
st.set_page_config(page_title="Med-Cloud Pro", layout="centered")

# 2. CSS - GLOBAL OVERLAP REMOVAL (Targeting all icons/arrows)
st.markdown("""
    <style>
    /* 1. FORCE LIGHT MODE */
    .stApp { background-color: #FFFFFF !important; }

    /* 2. THE GLOBAL OVERLAP KILLER */
    /* This removes "arrow_drop_down" from Expanders, Date Pickers, and Time Pickers */
    span:contains("arrow_"), 
    .streamlit-expanderHeader span, 
    .streamlit-expanderHeader svg,
    div[data-baseweb="select"] svg,
    div[data-baseweb="icon"] {
        display: none !important;
        visibility: hidden !important;
        content: "" !important;
        width: 0px !important;
    }
    
    /* 3. STYLE THE HEADER BOX (Matches Image 2) */
    .streamlit-expanderHeader {
        background-color: #1E1E2E !important; /* Dark background from screenshot */
        border-radius: 4px !important;
        padding: 8px 12px !important;
        border: none !important;
    }
    .streamlit-expanderHeader p {
        color: #1A73E8 !important; /* Blue text from screenshot */
        font-weight: 500 !important;
        font-size: 16px !important;
    }

    /* 4. INPUT BOXES (White background, Blue borders to match Image 2) */
    input, [data-baseweb="input"], [data-baseweb="select"], .stNumberInput div {
        background-color: #FFFFFF !important;
        color: #000000 !important;
        border: 2px solid #1A73E8 !important; /* Blue border visibility */
    }

    /* 5. TITLES AND LABELS (High Visibility Blue) */
    h1, h2, h3, h4, label, p, .stMarkdownContainer p {
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

# --- SESSION STATE ---
if 'page' not in st.session_state: st.session_state.page = "dashboard"
if 'current_user' not in st.session_state: st.session_state.current_user = "wewfwef" # Matches your image
if 'reminders' not in st.session_state: st.session_state.reminders = []

# --- MAIN DASHBOARD (EXACT MIRROR OF IMAGE 2) ---
if st.session_state.page == "dashboard":
    # Centered Title
    st.markdown("<h1 style='text-align:center;'>Doctor Help</h1>", unsafe_allow_html=True)
    st.markdown(f"### Patient Dashboard: {st.session_state.current_user}")
    
    st.markdown("---")
    st.markdown("## Pill Reminders")
    
    # THE EXPANDER (Overlapping "arrow_drop_down" is now hidden globally)
    with st.expander("Add Medication Reminder", expanded=True):
        med_name = st.text_input("Medicine Name", placeholder="frgreg") 
        
        # START/END DATE GRID
        col_date1, col_date2 = st.columns(2)
        with col_date1:
            st.date_input("Start Date", key="s_date")
        with col_date2:
            st.date_input("End Date", key="e_date")
        
        # DOSAGE (Matches Image 2 +/- buttons)
        dosage = st.number_input("Dosage Per Day", min_value=1, max_value=8, value=4)
        
        st.write("Set Times:")
        
        # DOSE SLOTS (2-Column Grid)
        time_slots = []
        cols = st.columns(2)
        for i in range(int(dosage)):
            with cols[i % 2]:
                # Default times as seen in your screenshot
                times_list = [time(7, 30), time(12, 0), time(16, 0), time(20, 0)]
                default_val = times_list[i] if i < len(times_list) else time(10, 0)
                st.time_input(f"Dose {i+1}", value=default_val, key=f"dose_input_{i}")

        # CARETAKERS SECTION
        st.markdown("### Caretaker Details")
        st.text_input("Name", key="ct_name_field")
        
        col_p1, col_p2 = st.columns(2)
        with col_p1:
            st.text_input("Primary Phone", key="phone_1")
        with col_p2:
            st.text_input("Secondary Phone", key="phone_2")

        # SET REMINDER BUTTON
        st.button("Set Reminder")

    if st.button("Sign Out"):
        st.session_state.page = "auth"
        st.rerun()
