import streamlit as st
import random

# 1. Page Configuration
st.set_page_config(page_title="Med-Cloud Pro", layout="centered")

# 2. CSS - Precise Adjustments Based on Your Feedback
st.markdown("""
    <style>
    /* Global Background */
    .stApp { background-color: #FFFFFF; }
    
    /* Global Text Visibility - Navy for contrast */
    p, span, label, li { color: #1E3A8A !important; font-family: 'Segoe UI', sans-serif; }

    /* Centered Headline */
    .top-headline {
        text-align: center; color: #1E3A8A; font-weight: bold; font-size: 26px; margin-bottom: 10px;
    }

    /* SPECIFIC LIGHTER BLUE BUTTON (#1A73E8) - Reduced Width */
    .stButton>button {
        background-color: #1A73E8 !important; /* Slightly lighter than #0056D6 */
        color: white !important;
        border-radius: 8px !important; 
        border: none !important;
        padding: 8px 16px !important;
        font-weight: 500 !important;
        font-size: 14px !important;
        width: auto !important; 
        min-width: 100px; /* Thinner width */
        display: block;
        margin: 0 auto; 
    }

    /* Forget ID - Not a button, just a small clickable link style */
    .forgot-link {
        color: #1A73E8 !important;
        font-size: 13px !important;
        font-weight: 500 !important;
        text-decoration: none;
        cursor: pointer;
        margin-top: -15px;
        margin-bottom: 20px;
        display: inline-block;
    }

    /* Input Box Visibility Fix - Dark Text for Naked Eye */
    .stTextInput>div>div>input {
        background-color: #F8FAFC !important;
        color: #000000 !important; /* Pure black text for high visibility */
        border: 1px solid #747775 !important;
        border-radius: 6px !important;
        padding: 10px !important;
        font-size: 16px !important; /* Larger font */
    }
    
    /* Row Alignment for Create and Next */
    .auth-row {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-top: 20px;
    }

    header {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# Initialize Session States
if 'page' not in st.session_state: st.session_state.page = "welcome"
if 'user_id' not in st.session_state: st.session_state.user_id = None

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

    # Continue Button - Centered, Thinner, Lighter Blue
    st.write("")
    if st.button("Continue ➔"):
        st.session_state.page = "auth"
        st.rerun()

# --- PAGE 2: AUTH (Sign-In) ---
elif st.session_state.page == "auth":
    st.write("")
    with st.container():
        # Header Row
        logo_col, title_col = st.columns([0.1, 0.9])
        with logo_col:
            st.image("https://cdn-icons-png.flaticon.com/512/2966/2966327.png", width=30)
        with title_col:
            st.markdown("<h2 style='margin:0; padding-top:2px; color:#1E3A8A; font-size:22px;'>Med-Cloud Pro</h2>", unsafe_allow_html=True)
        
        st.markdown("<h3 style='margin-top:15px; text-align:left; font-size:24px;'>Sign in</h3>", unsafe_allow_html=True)
        
        # ID Box Label
        st.markdown("<p style='margin-bottom:-15px; font-weight:500; font-size:14px;'>Med-Cloud ID</p>", unsafe_allow_html=True)
        user_id_input = st.text_input("", placeholder="ex: MED-1234", label_visibility="visible")
        
        # Forget ID - Small link below big box
        st.markdown("<span class='forgot-link'>Forgot ID?</span>", unsafe_allow_html=True)
        
        st.write("")
        
        # Create and Next in the SAME LINE
        col_act1, col_act2 = st.columns([1, 1])
        with col_act1:
            # Create account styled as a text-link but functional
            if st.button("Create account", key="create_acc"):
                st.info("New ID: MED-8829")
        with col_act2:
            # Next Button aligned to the right
            if st.button("Next", key="next_step"):
                if user_id_input:
                    st.session_state.user_id = user_id_input
                    st.session_state.page = "dashboard"
                    st.rerun()
                else:
                    st.error("Please enter ID")

    # Simple Back link
    st.write("")
    if st.button("← Back"):
        st.session_state.page = "welcome"
        st.rerun()
