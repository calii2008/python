import streamlit as st

col1,col2,col3,col4,col5=st.columns(5,gap="small",vertical_alignment="center")

with col1:
    st.header("comlum 1")
    st.write("content for column 1")

with col2:
    st.header("comlum 2")
    st.write("content for column 1")

with col3:
    st.header("comlum 3")
    st.write("content for column 3")

with col4:
    st.header("comlum 4")
    st.write("content for column 4")

with col5:
    st.header("comlum 5")
    st.write("content for column 5")



with st.container():
    st.header("this is container")
    st.write("this is inside the coniener")

st.write("this is outside the continaier")

st.sidebar.radio()



















