import streamlit as st
from emails import send_email

st.header("Contact")

with st.form(key="contact"):
    user_email = st.text_input("Enter your email")
    message = st.text_input("Enter your message")
    message = f"Subject: Website Email\n{message}"
    submit = st.form_submit_button("Submit")
    if submit:
        st.write("Message sent, Thank you!")
        send_email(message)

