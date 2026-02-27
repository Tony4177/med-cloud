import streamlit as st
from datetime import time

# 1. Page Configuration
st.set_page_config(page_title="Med-Cloud Pro", layout="centered")

# 2. THE FORCE COMMANDS (CSS) - FIXES THE OVERLAP GLOBALLY
st.markdown("""
    <style>
    /* FORCE THE BACKGROUND WHITE */
    .stApp { background-color: #FFFFFF !important; }

    /* THE GLOBAL OVERLAP KILLER - HIDES "arrow_drop_down" ON ALL BARS & BOXES */
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
    
    /* STYLE THE HEADER BAR (EXACT MATCH FOR IMAGE 2) */
    .streamlit-expanderHeader {
        background-color: #1E1E2E !important; 
        border-radius: 4px !important;
        padding: 10px !important;
        border: none !important;
    }
    .streamlit-expanderHeader p {
        color: #1A73E8 !important; 
        font-weight: 600 !important;
        font-size: 16px !important;
    }

    /* FORCE BOX VISIBILITY (WHITE BOX + BLUE BORDER) */
    input, [data-baseweb="input"], [data-baseweb="select"], .stNumberInput div {
        background-color: #FFFFFF !important;
        color: #000000 !important;
        border: 2px solid #1A73E8 !important;
    }

    /* FORCE TEXT COLORS TO STAND OUT */
    h1, h2, h3, label, p, .stMarkdownContainer p { 
        color: #1A73E8 !important; 
        font-weight: 600 !important;
    }

    /* BUTTON STYLE */
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

# --- DASHBOARD LAYOUT (MIRRORING IMAGE 2) ---

# Centered Title
st.markdown("<h1 style='text-align:center;'>Doctor Help</h1>", unsafe_allow_html=True)
st.markdown("### Patient Dashboard: wewfwef") 
st.markdown("---")

st.markdown("## Pill Reminders")

# THE EXPANDER (All overlapping text is hidden by the CSS above)
with st.expander("Add Medication Reminder", expanded=True):
    # Medicine Name Input
    st.text_input("Medicine Name", placeholder="frgreg") 
    
    # DATE GRID (Side-by-side)
    col1, col2 = st.columns(2)
    with col1: 
        st.date_input("Start Date")
    with col2: 
        st.date_input("End Date")
    
    # DOSAGE (Matches Image 2 +/- buttons)
    dosage = st.number_input("Dosage Per Day", min_value=1, max_value=8, value=4)
    
    st.write("Set Times:")
    
    # DYNAMIC TIME SLOTS (2-Column Grid for Dose 1, 2, 3, 4)
    t_cols = st.columns(2)
    for i in range(int(dosage)):
        with t_cols[i % 2]:
            # Setting default times like your screenshot (07:30, 12:00, 16:00, 20:00)
            d_times = [time(7, 30), time(12, 0), time(16, 0), time(20, 0)]
            val = d_times[i] if i < 4 else time(10, 0)
            st.time_input(f"Dose {i+1}", value=val, key=f"dose_grid_{i}")

    # CARETAKER SECTION (Matches Image 2 bottom)
    st.markdown("### Caretaker Details")
    st.text_input("Name", key="caretaker_name_input")
    
    cp1, cp2 = st.columns(2)
    with cp1: 
        st.text_input("Primary Phone", key="phone_primary")
    with cp2: 
        st.text_input("Secondary Phone", key="phone_secondary")

    st.button("Set Reminder")

# Sign Out at the bottom
if st.button("Sign Out"):
    st.rerun()
