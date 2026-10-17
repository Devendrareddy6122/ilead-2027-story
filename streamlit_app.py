from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components


st.set_page_config(
    page_title="Devendra Kumar Reddy — iLEAD 2027",
    page_icon="🌱",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown(
    """
    <style>
      [data-testid="stHeader"], [data-testid="stToolbar"], footer {display:none;}
      [data-testid="stMainBlockContainer"] {padding:0 !important; max-width:none !important;}
      .stApp {background:#eef3f9;}
      iframe {border:0;}
    </style>
    """,
    unsafe_allow_html=True,
)

site_file = Path(__file__).parent / "index.html"
if not site_file.exists():
    st.error("The portfolio page (index.html) is missing from this repository.")
else:
    components.html(site_file.read_text(encoding="utf-8"), height=5200, scrolling=True)
