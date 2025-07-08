import streamlit as st


st.set_page_config(layout="wide")


col1, col2 = st.columns(2)



with col1:
    st.image("images/photo.png", width=600)

with col2:
    st.title("TheGameBoi")
    content = ("""Hello! My name is GameBoi, and I am a software programmer, gamer, and music junky. This is my personal 
    showcase website I built from scratch!""")

    st.info(content)

st.title("")
add = """Below are some of my apps I have created. Feel free to contact me!"""

st.write(add)