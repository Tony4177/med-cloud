import streamlit as st
import random

# 1. Page Configuration
st.set_page_config(page_title="Med-Cloud Pro", layout="centered")

# 2. Premium CSS (Medical Google-Style Interface)
st.markdown("""
    <style>
    .stApp { background-color: #FFFFFF; }
    
    /* Navigation/Global Text */
    p, span, label, li { color: #3C4043 !important; font-family: 'Roboto', arial, sans-serif; }

    /* Sign-In Card Container */
    .signin-card {
        background-color: #000000;
        padding: 40px;
        border-radius: 28px;
        color: white !important;
        margin: auto;
        max-width: 450px;
    }

    /* Headlines */
    .top-headline {
        text-align: center; color: #1E3A8A; font-weight: bold; font-size: 26px; margin-bottom: 10px;
    }
    .auth-headline {
        font-size: 24px; color: white !important; margin-bottom: 8px;
    }

    /* Google-style Next Button */
    .stButton>button {
        background-color: #A8C7FA !important; /* Soft medical blue from your image */
        color: #062E6F !important;
        border-radius: 20px !important;
        border: none !important;
        padding: 10px 24px !important;
        font-weight: bold !important;
        float: right;
    }
    
    /* Transparent Button for 'Create Account' */
    div[data-testid="stHorizontalBlock"] div:nth-child(1) button {
        background-color: transparent !important;
        color: #A8C7FA !important;
        border: none !important;
        text-align: left !important;
        float: none;
    }

    /* Input Box Styling */
    .stTextInput>div>div>input {
        background-color: transparent !important;
        color: white !important;
        border: 1px solid #9AA0A6 !important;
        border-radius: 4px !important;
    }
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

    c1, c2, c3 = st.columns([1.5, 1, 1.5])
    with c2:
        if st.button("Continue ➔"):
            st.session_state.page = "auth"
            st.rerun()

# --- PAGE 2: AUTH (Medical "Sign-In" Interface) ---
elif st.session_state.page == "auth":
    # Spacer to center the card vertically
    st.write("")
    st.write("")
    
    # Start of the Dark Sign-In Card
    with st.container():
        st.markdown("""<div style='background-color: #1F1F1F; padding: 40px; border-radius: 28px;'>""", unsafe_allow_html=True)
        
        # 1. Medical Logo (Cross Icon)
        st.image("https://cdn-icons-png.flaticon.com/512/2966/2966327.png", width=40)
        
        # 2. Sign In to Project Name
        st.markdown("<h2 style='color: white; margin-bottom:0;'>Sign in</h2>", unsafe_allow_html=True)
        st.markdown("<p style='color: white !important; margin-bottom: 20px;'>Use your Med-Cloud Account</p>", unsafe_allow_html=True)
        
        # 3. ID Input Box
        user_id_input = st.text_input("ID", placeholder="Enter your Unique ID")
        
        # 4. Forgot ID
        st.markdown("<p style='color: #A8C7FA; font-size: 14px; cursor: pointer;'>Forgot ID?</p>", unsafe_allow_html=True)
        
        # Spacer
        st.write("")
        st.write("")
        
        # 5. Bottom Buttons (Create Account and Next)
        col_btn1, col_btn2 = st.columns([1, 1])
        with col_btn1:
            if st.button("Create account"):
                st.info("Registration: MED-" + str(random.randint(1000,9999)))
        with col_btn2:
            if st.button("Next"):
                if user_id_input:
                    st.session_state.user_id = user_id_input
                    st.session_state.page = "dashboard"
                    st.rerun()
                else:
                    st.error("Please enter ID")
        
        st.markdown("""</div>""", unsafe_allow_html=True)

    # Small Footer
    st.markdown("<p style='font-size: 12px; color: grey; text-align:center; margin-top:20px;'>English (United States)</p>", unsafe_allow_html=True)
