import streamlit as st
from datetime import datetime

st.set_page_config(page_title="24/7 Med Reminder", page_icon="💊")
st.title("💊 24/7 Cloud Med Reminder")

# This keeps data in the app while it's running in the cloud
if 'meds' not in st.session_state:
    st.session_state.meds = []

# Input section
with st.container(border=True):
    name = st.text_input("Medicine Name")
    time_val = st.time_input("Reminder Time")
    if st.button("Add to Cloud Schedule", use_container_width=True):
        if name:
            st.session_state.meds.append({"name": name, "time": str(time_val)})
            st.success("Saved to Cloud!")
            st.rerun()

# Display section
st.subheader("Active Reminders")
if not st.session_state.meds:
    st.write("No reminders yet.")
else:
    for m in st.session_state.meds:
        st.info(f"⏰ {m['time'][:5]} — **{m['name']}**")