import streamlit as st
import random

# 1. Page Configuration
st.set_page_config(page_title="Med-Cloud Pro", layout="centered")

# 2. Refined CSS Styling (Better Blue, No Black, Better Button)
st.markdown("""
    <style>
    .stApp { background-color: #FFFFFF; }
    
    /* Global Text Visibility */
    p, span, label, li { color: #334155 !important; font-size: 16px; }

    /* Headline at the very top */
    .top-headline {
        text-align: center; 
        color: #1E3A8A; 
        font-weight: bold; 
        font-size: 26px;
        margin-bottom: 10px;
    }

    /* Professional Soft Medical Blue Button */
    .stButton>button {
        background-color: #3B82F6 !important;
        color: white !important;
        border-radius: 20px !important;
        border: none !important;
        padding: 8px 15px !important;
        font-weight: bold !important;
        width: 100% !important;
        transition: 0.3s;
    }
    .stButton>button:hover { background-color: #2563EB !important; transform: scale(1.02); }
    
    /* Center columns for thinner button */
    [data-testid="column"] { display: flex; justify-content: center; }
    </style>
    """, unsafe_allow_html=True)

# Initialize Session States
if 'page' not in st.session_state: st.session_state.page = "welcome"
if 'user_id' not in st.session_state: st.session_state.user_id = None

# --- PAGE 1: WELCOME (Final Design) ---
if st.session_state.page == "welcome":
    
    # 1. Headline at the top
    st.markdown("<div class='top-headline'>Smart Healthcare Monitoring & Caretaker Escalation</div>", unsafe_allow_html=True)

    # 2. Your Preferred Image
    st.image("https://img.freepik.com/free-vector/health-professional-team-concept-illustration_114360-1608.jpg", use_container_width=True)

    # 3. How it Works & Advantages (Bullet Points)
    col_a, col_b = st.columns(2)
    
    with col_a:
        st.markdown("""
        **What it does:**
        * Tracks daily pill schedules in real-time.
        * Alerts caretakers if a dose is missed.
        """)
        
    with col_b:
        st.markdown("""
        **Main Advantages:**
        * 100% Secure & Unique Patient IDs.
        * Built-in AI Doctor for instant help.
        """)

    # 4. Description Text
    st.markdown("""
    <p style='text-align: center; margin-top: 15px;'>
    Our cloud platform ensures you never miss a dose by bridging the gap between 
    patients and families through a 3-step smart escalation protocol.<br>
    <b>Thank you for choosing Med-Cloud to manage your health journey!</b>
    </p>
    """, unsafe_allow_html=True)

    # 5. Thinner Continue Button
    st.write("") 
    c1, c2, c3 = st.columns([1.5, 1, 1.5])
    with c2:
        if st.button("Continue ➔"):
            st.session_state.page = "auth"
            st.rerun()

# --- OTHER PAGES (Placeholder Logic) ---
elif st.session_state.page == "auth":
    st.markdown("<h2 style='text-align:center;'>System Access</h2>", unsafe_allow_html=True)
    if st.button("← Back"):
        st.session_state.page = "welcome"
        st.rerun()
