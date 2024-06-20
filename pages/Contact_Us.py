import streamlit as st
from send_email import send_email

st.header("Contact Us")

with st.form(key="email_form"):
    user_email = st.text_input("Enter your email")
    raw_message = st.text_area("Your message")
    message = f"""\
    Subject: New Message\n
    {raw_message}
    
    From: {user_email}
    
"""
    button = st.form_submit_button("Submit")
    if button:
        send_email(message)
        st.info("Your message was sent successfully!")