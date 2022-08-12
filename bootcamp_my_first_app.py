import streamlit as st 

st.write("# 10 Cool Beginner Python Tricks That Will Make Your Life Easier")

st.write("""
    ## 1. Walrus operator
    The Walrus or := operator is one of the latest additions to python 3.8. It is an assignment operator that lets you assign value to a variable within an expression like conditional statements, loops, etc.
""")

with st.echo(code_location='below'):
    total_points = st.slider("Number of points in spiral", 1, 100, 20)