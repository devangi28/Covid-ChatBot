import streamlit as st
from selenium import webdriver
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import os
import pandas as pd

from PIL import Image

# def capture(txt):
#     options = webdriver.ChromeOptions()
#     options.add_argument('--headless')
#     options.add_argument('--start-maximized')
#     driver = webdriver.Chrome(ChromeDriverManager().install(),chrome_options=options)
#     driver.get(txt)
#     driver.get_screenshot_as_file("capture.png")
#     # st.image('capture.png', use_column_width=500)
#     driver.quit()


im = Image.open("A.jpg")

# Size of the image in pixels (size of original image)
# (This is not mandatory)
width, height = im.size
print(width, height)

# Setting the points for cropped image
left = 0
top = 0
right = 1200
bottom = 1200 - 300

# Cropped image of above dimension
# (It will not change orginal image)
im1 = im.crop((left, top, right, bottom))

# Shows the image in image viewer
st.image(im1, use_column_width=100)

chat = pd.read_csv('chat.csv')
input = st.selectbox('Ask me anything about Covid-19!', (list(chat['Questions'])))

#Basic Chat-bot
for i in range(len(chat['Questions'])):
    if input == chat['Questions'][i]:
        st.success(chat['Answers'][i])


st.sidebar.image('coVID-19.png', use_column_width=50)
st.sidebar.success("Wear a mask!")
st.sidebar.warning("Wash your hands!")
st.sidebar.error("Maintain Social Distancing!")
# def capture(txt):
#     options = webdriver.ChromeOptions()
#     options.add_argument('--headless')
#     options.add_argument('--start-maximized')
#     driver = webdriver.Chrome(ChromeDriverManager().install(),chrome_options=options)
#     driver.get(txt)
#     driver.get_screenshot_as_file("capture.png")
#     st.image('capture.png', use_column_width=500)
#     driver.quit()



# capture('https://www.google.com/search?rlz=1C5CHFA_enUS877US877&ei=0dSuX5vjM6-RggeS1464DA&q=covid+count&oq=covid+count&gs_lcp=CgZwc3ktYWIQAzILCAAQsQMQgwEQyQMyBQgAEJIDMgUIABCSAzIICAAQsQMQgwEyCAgAELEDEIMBMggIABCxAxCDATICCAAyAggAMggIABCxAxCDATIICAAQsQMQgwE6BAgAEEc6BAgAEEM6CggAELEDEIMBEEM6BwgAELEDEEM6CAgAELEDEMkDOg4IABCxAxCDARDJAxCRAjoFCAAQsQNQghVYrCVg6ydoAHADeACAAYICiAHVB5IBBTIuMi4ymAEAoAEBqgEHZ3dzLXdpesgBBsABAQ&sclient=psy-ab&ved=0ahUKEwjbj_y2l4DtAhWviOAKHZKrA8cQ4dUDCA0&uact=5')
# os.remove('capture.png')