import pandas as pd

import streamlit as st
st.header("dataframimng")
df = pd.DataFrame({
    'name':['vlera','melika','andi'],
    'age':[24, 17, 22],
    'city':['nakarad','vushtrri',"prishtin"]

})

st.write(df)

st.title("bestselling books analysis")
st.write("this app analyzes the amazon top selling from 2009 to 2022.")

books_df = pd..read_csv('modele18/bestsellers_with_categories_2022_03_27.csv')

st.subheader("summary statistt")
total_books = books_df.shaape[0]
unique_tiles = books_





















\

