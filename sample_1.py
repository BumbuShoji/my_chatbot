import streamlit as st
import pandas as pd
from sample_2 import print_2

st.write('# Hello, world!\n\nThis is a simple example of a Streamlit app.')

print_2 = print_2()
text = print_2.add('# Hello, world!','This is a simple example of a Streamlit app.')
st.write(text)

"""
st.write('# Hello, world!\n\nThis is a simple example of a Streamlit app.')
st.caption('This is a caption')

st.image('https://static.streamlit.io/examples/cat.jpg', caption='A cat')

import pandas as pd
df = pd.DataFrame({
  'column 1': [1, 2, 3, 4],
  'column 2': [10, 20, 30, 40]
})
st.write(df)

st.line_chart(df)

#input text
name = st.text_input('Enter your name')

# input number
age = st.number_input('Enter your age',step=1)

st.write(f'Hello {name}, you are {age} years old.')

# button
if st.button('Say hello'):
    st.write('Why hello there')

# pull down

df = pd.DataFrame({
    'column 1': [1, 2, 3, 4],
})
option = st.selectbox(
    'Which number do you like best?',
    df['column 1'])
st.write('You selected:', option)

# pull down multi option
options = st.multiselect(
    'What are your favorite numbers?',
    df['column 1'])
st.write('You selected:', options)

#check box
agree = st.checkbox('I agree')
st.write('You agreed:', agree)

# radio button
genre = st.radio(
    "What's your favorite movie genre",
    ('Comedy', 'Drama', 'Documentary'))
if genre == 'Comedy':
    st.write('You selected comedy.')
elif genre == 'Drama':
    st.write('You selected drama.')
else:
    st.write("You selected documentary.")

#file upload
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
    st.write(data)
"""
