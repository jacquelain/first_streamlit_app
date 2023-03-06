import streamlit
#import pandas 
#import requests


streamlit.title('My Mom\'s New Healthy Diner')

streamlit.header('Breakfast Favorites')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

#y_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
#y_fruit_list = my_fruit_list.set_index('Fruit')
# Let's put a pick list here so they can pick the fruit they want to include 
# streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])

#ruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])

#ruits_to_show = my_fruit_list.loc[fruits_selected]

# Display the table on the page.
#treamlit.dataframe(my_fruit_list)

#treamlit.dataframe(fruits_to_show)


import pandas 
import requests
import snowflake.connector
from urllib.error import URLError

def get_fruityvice_data(this_fruit_choice):
    fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + this_fruit_choice)
    fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
    return fruityvice_normalized
  
streamlit.header("Fruityvice Fruit Advice!")  
try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?')
  if not fruit_choice:
      streamlit.error("Please select a fruit to get information.")
  else:
       #fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + this_fruit_choice)
       #fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
       #streamlit.dataframe(fruityvice_normalized)
    
       back_from_function = get_fruityvice_data(fruit_choice)
       streamlit.dataframe(back_from_function)
except URLError as e:
    streamlit.error()
  
####################################################################################
#streamlit.header("The fruit load list contains:")
streamlit.header("View Our Fruit List - Add Your Favorites!")
#Snowflake related functions
def get_fruit_load_list():
    with my_cnx.cursor() as my_cur:
        my_cur.execute("SELECT * FROM FRUIT_LOAD_LIST")
        return my_cur.fetchall()
#Add a button to load the fruit
if streamlit.button ('Get fruit list'):
    my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
    my_data_rows = get_fruit_load_list()
    streamlit.dataframe(my_data_rows)
 ####################################################################################   
 # Allow the end user to add a fruit to the list 
def insert_row_snowflake(new_fruit):
    with my_cnx.cursor() as my_cur:
        my_cur.execute("insert into PC_RIVERY_DB.PUBLIC.FRUIT_LOAD_LIST values ('"+ new_fruit +"')")
        return "Thanks for adding " + new_fruit
   
add_my_fruit = streamlit.text_input('What fruit would you like to add?')
if streamlit.button('Add a fruit to the list'):
    my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
    back_from_function = insert_row_snowflake(add_my_fruit)
    streamlit.text(back_from_function)   
####################################################################################    
# don't run anything past here while we troubleshoot
streamlit.stop()

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
# my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_cur.execute("SELECT * FROM FRUIT_LOAD_LIST")
# my_data_row = my_cur.fetchone()
my_data_rows = my_cur.fetchall()
# streamlit.text("Hello from Snowflake:")
streamlit.header("The fruit load list contains:")
# streamlit.dataframe(my_data_row)
streamlit.dataframe(my_data_rows)


streamlit.header("New Fruit Choice Menu!")

add_my_fruit = streamlit.text_input('What fruit would you like to add?','Jakfruit')
streamlit.write('Thanks for adding ', add_my_fruit)


my_cur.execute("insert into PC_RIVERY_DB.PUBLIC.FRUIT_LOAD_LIST values ('from streamlit')")
