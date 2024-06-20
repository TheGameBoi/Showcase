import pandas
import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("GameBoi")
    content ="""My name is GameBoi and I am an avid gamer, I enjoy gaming when I get the chance to, and computers have been my passion for the past 12 years.
    I am currently studying the Python language in order to design apps for my favorite games, and possibly your favorite games!
    This is an online log of my coding journey thus far and into the future!
    """
    st.write(content)

content2 = """Below you can find some of the apps I have created using Python."""

st.write(content2)

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])
df = pandas.read_csv("data.csv", sep=";")

with col3:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.header(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")

with col4:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.header(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")