import streamlit
import pandas 
import requests
import snowflake.connector
from urllib.error import URLError 
streamlit.title('My Healthy Diner') 

streamlit.header('Todays Menu') 

streamlit.text('🥣Dosa')
streamlit.text('🥗Pasta')   
streamlit.text('🐔Idli')
streamlit.text('🥑Omlette')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇') 



my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')


def get_fruityvice_data(this_fruit_choice):
    fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" +this_fruit_choice)
    fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
    return fruityvice_normalized
streamlit.header("Fruityvice Fruit Advice!")
try:
    fruit_choice = streamlit.text_input('What fruit would you like information about?')
    if not fruit_choice:
        streamlit.error("Please select a fruit to get information.")
    else:
        back_from_function = get_fruityvice_data(fruit_choice)
        streamlit.dataframe(back_from_function)

