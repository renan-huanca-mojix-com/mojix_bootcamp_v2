import streamlit as st 

st.write("HELLO FROM THE BOOTCAMP")

with st.echo(code_location='below'):
    total_points = st.slider("Number of points in spiral", 1, 5000, 2000)