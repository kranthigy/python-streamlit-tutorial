import streamlit as st
from PIL import Image

import requests
######################
# Page Title
######################

image = Image.open("findash.png")

st.image(image, use_column_width=True)


st.sidebar.title("Options")

option = st.sidebar.selectbox("Which Dashboard?", ('twitter', 'wallstreetbets', 'stocktwits', 'chart', 'pattern'))


st.write(
    f"""
# Whats going on in - {option} ?
***
"""
)

if option == 'stocktwits':
    symbol = st.sidebar.text_input("Symbol", value='AAPL', max_chars=5)

    r = requests.get(f"https://api.stocktwits.com/api/2/streams/symbol/{symbol}.json")

    data = r.json()

    for message in data['messages']:
        st.image(message['user']['avatar_url'])
        st.write(message['user']['username'])
        st.write(message['created_at'])
        st.write(message['body'])
