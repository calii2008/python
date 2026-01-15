import streamlit as st

def main():
    st.title("hello, world!")

if st.button("click me"):
    st.write("button clicked!")
st.checkbox("check me")
if st.checkbox("sdFGHJ"):
    st.write("you ar seeing this text because you cheked the chekbox")

user_input = st.text_input("enter text", "sample text")
st.write("you have enterd: ", user_imput)
age = st.number_input("enter your are", min_value)
st.write(f"your age is: {age}")
0

if __name__ == "__main__":
    main()