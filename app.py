import streamlit as st
import random
from datetime import time

# 1. Page Configuration
st.set_page_config(page_title="Med-Cloud Pro", layout="centered")

# 2. THE GLOBAL OVERLAP KILLER & IMAGE 2 STYLING
st.markdown("""
    <style>
    /* 1. FORCE THE LIGHT BACKGROUND */
    .stApp { background-color: #FFFFFF !important; }

    /* 2. THE GLOBAL OVERLAP KILLER */
    /* This removes the "arrow_drop_down" glitch from every single box (Date, Time, and Expander) */
    span:contains("arrow_"), 
    .streamlit-expanderHeader span, 
    .streamlit-expanderHeader svg,
    .streamlit-expanderHeader::after,
    .streamlit-expanderHeader p::after,
    div[data-baseweb="select"] svg,
    div[data-baseweb="icon"],
    [data-testid="stExpander"] svg {
        display: none !important;
        visibility: hidden !important;
        content: "" !important;
        width: 0px !important;
    }
    
    /* 3. STYLE THE HEADER BAR (Mirroring Image 2) */
    .streamlit-expanderHeader {
        background-color: #1E1E2E !important; 
        border-radius: 4px !important;
        padding: 8px 12px !important;
        border: none !important;
    }
    .streamlit-expanderHeader p {
        color: #1A73E8 !important; 
        font-weight: 500 !important;
        font-size: 16px !important;
    }

    /* 4. FIX BOX VISIBILITY (White background, Blue borders like Image 2) */
    input, [data-baseweb="input"], [data-baseweb="select"], .stNumberInput div {
        background-color: #FFFFFF !important;
        color: #000000 !important;
        border: 2px solid #1A73E8 !important;
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

# --- DASHBOARD (EXACT MIRROR OF IMAGE 2) ---

# Centered Title and Patient ID
st.markdown("<h1 style='text-align:center;'>Doctor Help</h1>", unsafe_allow_html=True)
st.markdown(f"### Patient Dashboard: wewfwef") 
st.markdown("---")

st.markdown("## Pill Reminders")

# THE EXPANDER (No overlap glitch here)
with st.expander("Add Medication Reminder", expanded=True):
    # Medicine Name Input (Placeholder matching your image)
    st.text_input("Medicine Name", placeholder="frgreg") 
    
    # DATE GRID (Side-by-side)
    col_d1, col_d2 = st.columns(2)
    with col_d1: 
        st.date_input("Start Date")
    with col_d2: 
        st.date_input("End Date")
    
    # DOSAGE (Matches Image 2 +/- buttons)
    dosage = st.number_input("Dosage Per Day", min_value=1, max_value=8, value=4)
    
    st.write("Set Times:")
    
    # DYNAMIC TIME SLOTS (2-Column Grid matching Dose 1, 2, 3, 4)
    t_cols = st.columns(2)
    for i in range(int(dosage)):
        with t_cols[i % 2]:
            # Standard times from your Image 2 screenshot
            default_times = [time(7, 30), time(12, 0), time(16, 0), time(20, 0)]
            val = default_times[i] if i < 4 else time(10, 0)
            st.time_input(f"Dose {i+1}", value=val, key=f"dose_input_grid_{i}")

    # CARETAKER SECTION (Matches Image 2 bottom)
    st.markdown("### Caretaker Details")
    st.text_input("Caretaker Name", key="ct_name")
    
    col_p1, col_p2 = st.columns(2)
    with col_p1: 
        st.text_input("Primary Phone", key="p_phone")
    with col_p2: 
        st.text_input("Secondary Phone", key="s_phone")

    st.button("Set Reminder")

# Sign Out Button at the bottom
if st.button("Sign Out"):
    st.rerun()
