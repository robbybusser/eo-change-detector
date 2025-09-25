import streamlit as st
from PIL import Image

st.title("EO Change Demo")

before = Image.open("before.png")
after  = Image.open("after.png")

st.subheader("Before vs After")
col1, col2 = st.columns(2)
with col1:
    st.image(before, caption="Before", use_container_width=True)
with col2:
    st.image(after, caption="After", use_container_width=True)

st.subheader("Blinking GIF")
st.image("demo.gif", caption="Demo GIF", use_container_width=True)

