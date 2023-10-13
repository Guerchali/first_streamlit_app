import pandas
import requests

import streamlit
import snowflake.connector

snowflake_params = {
    "user": "sguerchal",
    "password": "Tensh@wa3er12345",
    "account": "YPWUSKI-WT18555",
    "warehouse": "pc_rivery_wh",
    "database": "pc_rivery_db",
    "schema": "public",
    "role": "accountadmin"
}

# Establish the Snowflake connection
my_cnx = snowflake.connector.connect(**snowflake_params)
my_cur = my_cnx.cursor()
my_cur.execute("select * from fruit_load_list")
# Execute a SQL query
my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_data_row = my_cur.fetchone()

# Display the results using Streamlit
streamlit.text("Hello from Snowflake:")
streamlit.text(" the fruit list contains")
streamlit.text(my_data_row)

#my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
#my_cur = my_cnx.cursor()
#my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
#my_data_row = my_cur.fetchone()
#streamlit.text("Hello from Snowflake:")
#streamlit.text(my_data_row)


streamlit.title('My parent New HEALThy diner')
streamlit.header('hii everyone')
streamlit.header('🥑🍞Breakfast Menu')
streamlit.text('🐔Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗Kale, Spinach & Rocket Smoothie')
streamlit.text('🥣Hard-Boiled Free-Range Egg')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
# Let's put a pick list here so they can pick the fruit they want to include 
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))
fruits_selected = streamlit.multiselect("Select Multi fruit :",list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)

streamlit.header("Fruityvice Fruit Advice!")
fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
# normalize the data into a table 
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# output the screen as a table 
streamlit.dataframe(fruityvice_normalized)


