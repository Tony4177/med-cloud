import streamlit as st
import random

# 1. Page Configuration
st.set_page_config(page_title="Med-Cloud Pro", layout="centered")

# 2. Premium CSS with your specific Blue (#0056D6)
st.markdown("""
    <style>
    /* Global Background and Text */
    .stApp { background-color: #FFFFFF; }
    p, span, label, li { color: #1E3A8A !important; font-family: 'Segoe UI', sans-serif; }

    /* Headline at the top */
    .top-headline {
        text-align: center; color: #1E3A8A; font-weight: bold; font-size: 26px; margin-bottom: 10px;
    }

    /* SPECIFIC BLUE BUTTONS (#0056D6) */
    .stButton>button {
        background-color: #0056D6 !important; 
        color: white !important;
        border-radius: 12px !important; 
        border: none !important;
        padding: 10px 25px !important;
        font-weight: bold !important;
        width: auto !important; 
        min-width: 140px;
        display: block;
        margin: 0 auto; 
        transition: 0.3s;
    }
    .stButton>button:hover { 
        background-color: #0044ab !important; 
        transform: translateY(-1px);
    }

    /* Custom styles for Links/Secondary buttons */
    .forgot-btn button, .create-btn button {
        background-color: transparent !important;
        color: #0056D6 !important;
        border: none !important;
        padding: 0 !important;
        font-weight: normal !important;
    }

    /* Input Box Styling */
    .stTextInput>div>div>input {
        background-color: #F0F4F9 !important;
        color: #1E3A8A !important;
        border: 1px solid #747775 !important;
        border-radius: 8px !important;
        padding: 12px !important;
    }
    
    header {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# Initialize Session States
if 'page' not in st.session_state: st.session_state.page = "welcome"
if 'user_id' not in st.session_state: st.session_state.user_id = None
if 'history_count' not in st.session_state: st.session_state.history_count = 0

# --- PAGE 1: WELCOME ---
if st.session_state.page == "welcome":
    st.markdown("<div class='top-headline'>Smart Healthcare Monitoring & Caretaker Escalation</div>", unsafe_allow_html=True)
    st.image("https://img.freepik.com/free-vector/health-professional-team-concept-illustration_114360-1608.jpg", use_container_width=True)

    col_a, col_b = st.columns(2)
    with col_a:
        st.markdown("**What it does:**\n* Tracks daily pill schedules.\n* Alerts caretakers if missed.")
    with col_b:
        st.markdown("**Main Advantages:**\n* Secure Unique IDs.\n* Built-in AI Doctor.")

    st.markdown("<p style='text-align: center;'>Thank you for choosing Med-Cloud!</p>", unsafe_allow_html=True)

    st.write("")
    if st.button("Continue ➔"):
        st.session_state.page = "auth"
        st.rerun()

# --- PAGE 2: AUTH (Sign-In) ---
elif st.session_state.page == "auth":
    st.write("")
    with st.container():
        logo_col, title_col = st.columns([0.15, 0.85])
        with logo_col:
            st.image("https://cdn-icons-png.flaticon.com/512/2966/2966327.png", width=35)
        with title_col:
            st.markdown("<h2 style='margin:0; padding-top:5px; color:#1E3A8A;'>Med-Cloud Pro</h2>", unsafe_allow_html=True)
        
        st.markdown("<h3 style='margin-top:10px;'>Sign in</h3>", unsafe_allow_html=True)
        
        st.markdown("<p style='margin-bottom:-10px; font-weight:bold;'>Med-Cloud ID</p>", unsafe_allow_html=True)
        user_id_input = st.text_input("", placeholder="ex: MED-1234", label_visibility="visible")
        
        col_forgot, col_empty = st.columns([1,1])
        with col_forgot:
            st.markdown("<div class='forgot-btn'>", unsafe_allow_html=True)
            if st.button("Forgot ID?"):
                st.toast("Contact support for ID recovery.")
            st.markdown("</div>", unsafe_allow_html=True)
        
        st.write("")
        col_act1, col_act2 = st.columns([1, 1])
        with col_act1:
            st.markdown("<div class='create-btn'>", unsafe_allow_html=True)
            if st.button("Create account"):
                st.info("New ID Generated: MED-9921")
            st.markdown("</div>", unsafe_allow_html=True)
            
        with col_act2:
            if st.button("Next"):
                if user_id_input:
                    st.session_state.user_id = user_id_input
                    st.session_state.page = "dashboard"
                    st.rerun()
                else:
                    st.error("Please enter ID")

    if st.button("← Back"):
        st.session_state.page = "welcome"
        st.rerun()

# --- PAGE 3: DASHBOARD ---
elif st.session_state.page == "dashboard":
    # Navigation Bar
    n1, n2, n3 = st.columns([1, 4, 1])
    with n1: 
        if st.button("👤"): st.session_state.page = "profile"
    with n2: st.markdown(f"<h3 style='text-align:center;'>Welcome, {st.session_state.user_id}</h3>", unsafe_allow_html=True)
    with n3:
        if st.button("☰"): st.toast("Menu opened")

    # AI Doctor
    st.markdown("### 🤖 AI Doctor Assistant")
    q = st.text_input("Ask a medical question:", placeholder="What does this tablet do?")
    if q:
        st.info("AI Doctor: Please ensure you follow the prescribed dosage. Checking database...")

    # Add Meds
    with st.expander("Add Medication", expanded=True):
        st.text_input("Medicine Name")
        st.text_input("Time (16:30)", value="08:00 AM")
        if st.button("Save Medication"):
            st.success("Medication Added!")
