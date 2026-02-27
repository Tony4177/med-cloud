import streamlit as st
from datetime import datetime
import time

st.set_page_config(page_title="Med-Cloud 24/7", page_icon="💊", layout="centered")

# --- CUSTOM CSS FOR STYLING ---
st.markdown("""
    <style>
    .main { background-color: #f5f7f9; }
    .stButton>button { width: 100%; border-radius: 20px; height: 3em; background-color: #FF4B4B; color: white; }
    .med-card { padding: 15px; border-radius: 10px; border-left: 5px solid #FF4B4B; background: white; margin-bottom: 10px; box-shadow: 2px 2px 5px rgba(0,0,0,0.1); }
    </style>
    """, unsafe_allow_html=True)

st.title("💊 Smart Med Reminder")
st.write("Logged in as: **Tony4177** (Cloud Mode)")

# Initialize storage
if 'meds' not in st.session_state:
    st.session_state.meds = []

# --- INPUT SECTION ---
with st.expander("➕ Add New Medication", expanded=True):
    col1, col2 = st.columns(2)
    with col1:
        name = st.text_input("Medicine Name", placeholder="e.g. Vitamin C")
    with col2:
        time_input = st.time_input("Reminder Time")
    
    if st.button("Save to Cloud"):
        if name:
            st.session_state.meds.append({"name": name, "time": time_input.strftime("%H:%M")})
            st.success(f"Added {name}!")
            st.rerun()

# --- LIVE ALERT SYSTEM ---
current_time = datetime.now().strftime("%H:%M")
for med in st.session_state.meds:
    if med['time'] == current_time:
        st.error(f"🚨 **IT IS TIME!** Take your {med['name']} now!")
        st.balloons()

# --- DISPLAY SECTION ---
st.subheader("📋 Your Schedule")
if not st.session_state.meds:
    st.info("No medications scheduled. Stay healthy!")
else:
    for i, med in enumerate(st.session_state.meds):
        # Create a "Card" for each medicine
        cols = st.columns([4, 1])
        with cols[0]:
            st.markdown(f"""<div class="med-card"><strong>{med['name']}</strong><br>⏰ {med['time']}</div>""", unsafe_allow_html=True)
        with cols[1]:
            if st.button("🗑️", key=f"del_{i}"):
                st.session_state.meds.pop(i)
                st.rerun()

# Auto-refresh every 30 seconds to check the time
time.sleep(30)
st.rerun()