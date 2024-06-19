import streamlit as st
from PIL import Image
from utils.streamlit_utils import hide_icons, hide_sidebar, remove_whitespaces
from streamlit_extras.switch_page_button import switch_page

# Hide icons, sidebar, and remove whitespaces
st.set_page_config(layout="wide", initial_sidebar_state="collapsed", page_title="Certif5", page_icon="🎓")
hide_icons()
hide_sidebar()
remove_whitespaces()

# Set background color to light blue
st.markdown(
    """
    <style>
    body {
        background-color: #cfe2f3 !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)


# Title and subheader
st.title("Certif5 - Generate and Validate your certificates here.")
st.markdown("---")  # Add a horizontal rule for better separation
st.subheader("Login as:")

# Display institute logo and button
col1, col2 = st.columns(2)
with col1:
    institite_logo = Image.open("../assets/institute_logo.png")
    st.image(institite_logo, output_format="jpg", width=230, caption="Institute")
    clicked_institute = st.button("Login as Institute")

# Display company logo and button
with col2:
    company_logo = Image.open("../assets/company_logo.jpg")
    st.image(company_logo, output_format="jpg", width=230, caption="Verifier")
    clicked_verifier = st.button("Login as Verifier")

# Handle button clicks and switch pages
if clicked_institute:
    st.session_state.profile = "Institute"
    switch_page('login')
elif clicked_verifier:
    st.session_state.profile = "Verifier"
    switch_page('login')