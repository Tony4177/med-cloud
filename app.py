import streamlit as st

# 1. Page Configuration
st.set_set_page_config(page_title="Med-Cloud Pro", layout="centered")

# 2. CSS - FORCE COLORS & DESIGN (LOCKED)
st.markdown("""
    <style>
    .stApp { background-color: #FFFFFF; }
    
    /* FORCE DARK BLUE ON TITLES */
    h1, h2, h3, .top-headline {
        color: #1E3A8A !important;
        font-family: 'Segoe UI', sans-serif !important;
    }
    
    /* FORCE BLUE ON LABELS */
    p, span, label, li { 
        color: #1E3A8A !important; 
        font-family: 'Segoe UI', sans-serif !important; 
    }

    .stepper { display: flex; justify-content: center; margin-bottom: 25px; }
    .step-dot { height: 6px; width: 35px; background-color: #1A73E8; border-radius: 4px; margin: 0 4px; }
    .step-dot-off { height: 6px; width: 35px; background-color: #E2E8F0; border-radius: 4px; margin: 0 4px; }

    /* Header Alignment: Icon and Text on same line */
    .header-container {
        display: flex;
        align-items: center;
        gap: 12px;
        margin-bottom: 10px;
    }

    /* Next Button: Increased Width & Decreased Height */
    div[data-testid="stButton"] button:has(div p:contains("Next")) {
        background-color: #1A73E8 !important;
        color: white !important;
        border-radius: 20px !important;
        border: none !important;
        padding: 0 !important;
        font-weight: 500 !important;
        width: 120px !important; 
        height: 32px !important; 
        display: flex;
        align-items: center;
        justify-content: center;
        margin: 0 auto; 
    }

    /* ID Box & Blinking Cursor */
    .stTextInput>div>div>input {
        background-color: #F8FAFC !important;
        color: #000000 !important;
        border: 1px solid #747775 !important;
        border-radius: 4px !important;
        padding: 12px !important;
        caret-color: #1A73E8 !important; /* The blinking cursor line */
    }
    
    /* FORGOT ID: Smaller words, No Button, 1.3cm (50px) Gap */
    div[data-testid="stButton"] button:has(div p:contains("Forgot ID?")) {
        background: transparent !important;
        border: none !important;
        color: #1A73E8 !important;
        padding: 0 !important;
        font-size: 11px !important; 
        box-shadow: none !important;
        width: auto !important;
        margin-top: 50px !important; /* Exact 1.3cm gap */
        text-align: left !important;
    }

    /* Create account as a text link */
    div[data-testid="stButton"] button:has(div p:contains("Create account")) {
        background: transparent !important;
        border: none !important;
        color: #1A73E8 !important;
        padding: 0 !important;
        font-size: 14px !important;
        box-shadow: none !important;
        width: auto !important;
    }

    header {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# Session State
if 'page' not in st.session_state: st.session_state.page = "welcome"

# --- PAGE 1: WELCOME ---
if st.session_state.page == "welcome":
    st.markdown("<h1 style='text-align:center;'>Smart Healthcare Monitoring</h1>", unsafe_allow_html=True)
    st.image("https://img.freepik.com/free-vector/health-professional-team-concept-illustration_114360-1608.jpg", use_container_width=True)
    if st.button("Continue ➔", key="welcome_go"):
        st.session_state.page = "auth"
        st.rerun()

# --- PAGE 2: AUTH (LOCKED) ---
elif st.session_state.page == "auth":
    st.markdown("""<div class='stepper'><div class='step-dot'></div><div class='step-dot-off'></div><div class='step-dot-off'></div></div>""", unsafe_allow_html=True)
    
    with st.container():
        # ICON AND NAME BESIDE EACH OTHER
        st.markdown("""
            <div class='header-container'>
                <img src='https://cdn-icons-png.flaticon.com/512/2966/2966327.png' width='30'>
                <h2 style='color:#1E3A8A;'>Med-Cloud Pro</h2>
            </div>
        """, unsafe_allow_html=True)
        
        st.markdown("<h3>Sign in</h3>", unsafe_allow_html=True)
        st.markdown("<p style='margin-top:-15px; font-size:14px; color:#5F6368 !important;'>Access your secure health dashboard</p>", unsafe_allow_html=True)
        
        st.markdown("<p style='margin-bottom:-15px; font-weight:500; font-size:14px;'>Med-Cloud ID</p>", unsafe_allow_html=True)
        user_id_input = st.text_input("", placeholder="ex: (MED-1234)", key="input_main")
        
        # FORGOT ID - Tiny, Blue words, 1.3cm gap
        if st.button("Forgot ID?", key="forgot_final"):
            st.session_state.page = "forgot_id"
            st.rerun()

        st.write("")
        c1, c2 = st.columns([1, 1])
        with c1:
            if st.button("Create account", key="create_final"):
                st.session_state.page = "create_account"
                st.rerun()
        with c2:
            if st.button("Next", key="next_final"):
                if user_id_input:
                    st.session_state.user_id = user_id_input
                    st.session_state.page = "dashboard"
                    st.rerun()
    
    st.write("")
    if st.button("← Back", key="back_final"):
        st.session_state.page = "welcome"
        st.rerun()

# --- PLACEHOLDER PAGES ---
elif st.session_state.page == "dashboard":
    st.title("Main Dashboard")
    if st.button("Logout"): st.session_state.page = "auth"; st.rerun()

elif st.session_state.page == "forgot_id":
    st.title("Recovery")
    if st.button("Back"): st.session_state.page = "auth"; st.rerun()

elif st.session_state.page == "create_account":
    st.title("Registration")
    if st.button("Back"): st.session_state.page = "auth"; st.rerun()
