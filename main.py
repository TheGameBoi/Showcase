import streamlit as st
import pandas


st.set_page_config(layout="wide")


col1, col2 = st.columns(2)



with col1:
    st.image("images/photo.png", width=400)

with col2:
    st.title("TheGameBoi")
    content = ("""Hello! My name is GameBoi, and I am a software programmer, gamer, and music junky. This is my personal 
    showcase website I built from scratch!""")

    st.info(content)

st.title("")
add = """Below are some of my apps I have created. Feel free to contact me!"""

st.write(add)


df = pandas.read_csv("data.csv", sep=";")
col3, col4 = st.columns(2)

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"], width=400)
        st.write(f"[Source Code]({row['url']})")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"], width=400)
        st.write(f"[Source Code]({row['url']})")