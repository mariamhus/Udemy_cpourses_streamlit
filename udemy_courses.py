import streamlit as st

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import numpy as np

st.title('Udemy Courses EDA')
#  loading data
df = pd.read_csv('./udemy_courses.csv')
st.dataframe(df.head())

col1,col2=st.columns(2)

st.subheader('how many courses in each subject?')
fig = px.bar(data_frame=df,x=df['subject'])
st.plotly_chart(fig)



st.subheader('what is the average price for each subject?')
fig2=px.bar(df,
      x=dict(df.groupby('subject').mean()['price']).keys(),
      y=dict(df.groupby('subject').mean()['price']).values())
fig2.update_xaxes(title='subjects')
fig2.update_yaxes(title='Average Price')
st.plotly_chart(fig2)


st.subheader('how many subscribers per each subject?')
fig3=px.pie(data_frame=df,
      names=df.groupby('subject').sum()['num_subscribers'].index,
     values=df.groupby('subject').sum()['num_subscribers'].values,
      hole=0.5)
st.plotly_chart(fig3)


st.subheader('how many paied/unpaied courses per each subject?')
fig4=px.bar(data_frame=df,x=df['subject'],color=df['is_paid'])
st.plotly_chart(fig4)
