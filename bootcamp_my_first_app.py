import streamlit as st 

st.write("# 10 Cool Beginner Python Tricks That Will Make Your Life Easier")

st.write("""
## 1. Walrus operator
The Walrus or := operator is one of the latest additions to python 3.8. It is an assignment operator that lets you assign value to a variable within an expression like conditional statements, loops, etc.
### Example
If we want to check and print the length of a list:
```
Mylist = [1,2,3]
if(l := len(mylist) > 2)
    print(l)
```     
""")

st.write("### Try your self!!!")


Mylist = st.text_input("Mylist", "1,2,3").split(",")
    
if st.button('Test Here'):
    if(l := len(Mylist) > 2):
        st.write("Your array has more than 2 elements")
    else:
        st.write("Your array is small")