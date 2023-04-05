import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.offline as pyo
import plotly.express as px
import plotly.graph_objects as go

df = pd.read_csv("heart_disease.csv")

def value_counts_to_dataframe(col):
    temp_df = df[col].value_counts().rename_axis(col).reset_index(name='counts')
    temp_df = temp_df.sort_values(by=[col])
    temp_df = temp_df.reset_index()
    temp_df.drop(columns=['index'],inplace=True)
    return temp_df


df1 = temp_df = value_counts_to_dataframe('age')
px.bar(data_frame = temp_df, x = 'age', y = 'counts', color = 'counts', 
       title = 'Total number of people with unique age values')
df1

st.title("Count of People of Education status")
df2 =fig = go.Figure(data=[go.Pie(labels=df['education'], hole=.4)])
fig.add_annotation(text='education',
                   x=0.5,y=0.5,showarrow=False,font_size=14,opacity=0.7,font_family='monospace')
fig.update_traces(hoverinfo='label+percent+value',
                  marker=dict(colors=['darkorange','blue'], line=dict(color='#000000', width=2)))
fig.update_layout(
    font_family='monospace',
    title=dict(text='',x=0.47,y=0.98,
               font=dict(color='black',size=20)),
    legend=dict(x=0.37,y=-0.05,orientation='h',traceorder='reversed'),
    hoverlabel=dict(bgcolor='white'))
fig.update_traces(textposition='outside', textinfo='percent+label')
fig.show()
df2




st.title("Total number of cigarette per day")


temp_df=value_counts_to_dataframe('cigsPerDay')
df3= px.bar(data_frame = temp_df, x = 'cigsPerDay', y = 'counts', color = 'counts', template = 'plotly_dark')
df3

st.title("Gender has heart stroke or not ")
df11 = px.histogram(df,
             x='Gender', 
             color='prevalentStroke', 
             color_discrete_map={'Yes':'#17becf', 'No':'#1f77b4'}
            )
df11

st.title("Gender has heart stroke or not ")
df4 = px.histogram(df,
             x='Gender', 
             color='Heart_ stroke', 
             color_discrete_map={'Yes':'#1becf', 'No':'#1f77b4'}
            )
df4

st.title("Relation between people age and has heart stroke or not")
df5 = px.histogram(df,
             x='age', 
             color='Heart_ stroke', 
             color_discrete_map={'Yes':'#17becf', 'No':'#1f77b4'}
            )
df5



df7 = fig = go.Figure(data=[go.Pie(labels=df['prevalentStroke'], hole=.4)])
fig.add_annotation(text='prevalentStroke',
                   x=0.5,y=0.5,showarrow=False,font_size=14,opacity=0.7,font_family='monospace')
fig.update_traces(hoverinfo='label+percent+value',
                  marker=dict(colors=['darkorange','blue'], line=dict(color='#000000', width=2)))
fig.update_layout(
    font_family='monospace',
    title=dict(text='',x=0.47,y=0.98,
               font=dict(color='black',size=20)),
    legend=dict(x=0.37,y=-0.05,orientation='h',traceorder='reversed'),
    hoverlabel=dict(bgcolor='white'))
fig.update_traces(textposition='outside', textinfo='percent+label')
fig.show()

df7





 

df10 = px.histogram(df,
             x='age', 
             color='Heart_ stroke', 
             color_discrete_map={'Yes':'#17becf', 'No':'#1f77b4'}, 
             title='Relation between people age and has heart stroke or not',
            )

df10



