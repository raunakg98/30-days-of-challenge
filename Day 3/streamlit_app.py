import numpy as np
import pandas as pd
import streamlit as st
import altair as alt

st.title('My first app')
st.header('st.write')

#example 1
st.write('Hello, *World!* :sunglasses:')

#example 2

st.write(1234)

#example 3

df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
})

st.write(df)

#example 4

st.write('This is a dataframe:', df, 'This is a series:', df['first column'])

#example 5

st.write('This is a chart')
df2 = pd.DataFrame(
     np.random.randn(200, 3),
     columns=['a', 'b', 'c'])
c = alt.Chart(df2).mark_circle().encode(
     x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])
st.write(c)