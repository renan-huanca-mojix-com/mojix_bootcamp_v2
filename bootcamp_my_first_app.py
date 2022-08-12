import streamlit as st 

st.write("# 10 Cool Beginner Python Tricks That Will Make Your Life Easier")

with st.echo(code_location='below'):
    total_points = st.slider("Number of points in spiral", 1, 100, 20)