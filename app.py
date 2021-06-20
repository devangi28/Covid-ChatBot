import streamlit as st
from time import sleep
import os
import pandas as pd

from PIL import Image



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
