import streamlit
streamlit.title('My Healthy Diner')

streamlit.header('Todays Menu')

streamlit.text('🥣Dosa')
streamlit.text('🥗Pasta')   
streamlit.text('🐔Idli')
streamlit.text('🥑Omlette')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
