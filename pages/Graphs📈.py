# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 08:52:24 2022

@author: HP USERPC
"""

import streamlit as st
import pandas as pd
import plotly_express as px

df = pd.read_csv(r'C:\Users\HP USERPC\Desktop\Telecom_analysis\data\telecom.csv')
df = df.fillna(0)
#-------Defining customerage group
def age(df):
        if df['customerAge'] < 20:
            return('less_than_20')
        elif df['customerAge'] >= 20 and df['customerAge'] < 40:
            return('btw_20_and_40')
        elif df['customerAge'] >= 40 and df['customerAge'] < 60:
            return('btw_40_and_60')
        elif df['customerAge'] >= 60:
            return('more_than_60')
        
df['customerClass'] = df.apply(age,axis=1)
#--------WRITE UP-------
st.title('Graphs 📊')

st.write("""This section shows the shows the charts of our analysis.
         The charts are also grouped based on age.""")
st.write("""On the chart below we can see the amount of people using the streaming services and the amount of people not using it.
         The sum of all these number equals 4000, which is the total number of customers we have.""")

#------PLOTTING THE CHARTS--------

y = st.selectbox('choose a service',['netflixStream','pickboxStream','youtubeStream','hboGoStream','viberFree','whatsappFree'], key = None)
if y == 'netflixStream':     
    total = df.groupby('customerClass')['netflixStream'].value_counts()
    
    w = [24,1011,369,2160,261,175]
    x = ['True', 'False', 'True', 'False', 'False', 'False']
    q = ['Less_than_20','less_than_20','btw_20_and_40','btw_20_and_40', 'btw_40_and_60','more_than_60']
    r = {'customerClass':q, 'streaming/not_streaming':x, 'number':w}
    d = pd.DataFrame(r)
    st.table(d)
    fig = px.bar(d, x ='customerClass', y = 'number', color = 'streaming/not_streaming', title = 'NETFLIX STREAMS')
    st.plotly_chart(fig, use_container_width=True)
    
elif y == 'pickboxStream':
    total = df.groupby('customerClass')['pickboxStream'].value_counts()
    
    
    
    w = [26,1009,330,2199,261,175]
    x = ['True', 'False', 'True', 'False', 'False', 'False']
    q = ['Less_than_20','less_than_20','btw_20_and_40','btw_20_and_40', 'btw_40_and_60','more_than_60']
    r = {'customerClass':q, 'streaming/not_streaming':x, 'number':w}
    d = pd.DataFrame(r)
    st.table(d)
    fig = px.bar(d, x ='customerClass', y = 'number', color = 'streaming/not_streaming', title = 'PICKBOX STREAMS')
    st.plotly_chart(fig, use_container_width=True)
    

elif y == 'youtubeStream':
    total = df.groupby('customerClass')['youtubeStream'].value_counts()
    
    
    
    w = [63,972,899,1630,261,175]
    x = ['True', 'False', 'True', 'False', 'False', 'False']
    q = ['Less_than_20','less_than_20','btw_20_and_40','btw_20_and_40', 'btw_40_and_60','more_than_60']
    r = {'customerClass':q, 'streaming/not_streaming':x, 'number':w}
    d = pd.DataFrame(r)
    st.table(d)
    fig = px.bar(d, x ='customerClass', y = 'number', color = 'streaming/not_streaming', title = 'YOUTUBE STREAMS')
    st.plotly_chart(fig, use_container_width=True)
    

elif y == 'hboGoStream':
    total = df.groupby('customerClass')['hboGoStream'].value_counts()
    
    
    
    w = [16,1019,319,2210,261,175]
    x = ['True', 'False', 'True', 'False', 'False', 'False']
    q = ['Less_than_20','less_than_20','btw_20_and_40','btw_20_and_40', 'btw_40_and_60','more_than_60']
    r = {'customerClass':q, 'streaming/not_streaming':x, 'number':w}
    d = pd.DataFrame(r)
    st.table(d)
    fig = px.bar(d, x ='customerClass', y = 'number', color = 'streaming/not_streaming', title = 'HBO STREAMS')
    st.plotly_chart(fig, use_container_width=True)
    

elif y == 'viberFree':
    total = df.groupby('customerClass')['viberFree'].value_counts()
    
    
    
    w = [427,608,760,1769,261,175]
    x = ['True', 'False', 'True', 'False', 'False', 'False']
    q = ['Less_than_20','less_than_20','btw_20_and_40','btw_20_and_40', 'btw_40_and_60','more_than_60']
    r = {'customerClass':q, 'streaming/not_streaming':x, 'number':w}
    d = pd.DataFrame(r)
    st.table(d)
    fig = px.bar(d, x ='customerClass', y = 'number', color = 'streaming/not_streaming', title = 'VIBER FREE')
    st.plotly_chart(fig, use_container_width=True)
    
    
elif y == 'whatsappFree':
    dataframe= df.groupby('customerClass')['whatsappFree'].value_counts()
    total = pd.DataFrame(dataframe)
    #st.write(total.columns)
    
    w = [407,628,690,1839,261,175]
    x = ['True', 'False', 'True', 'False', 'False', 'False']
    q = ['Less_than_20','less_than_20','btw_20_and_40','btw_20_and_40', 'btw_40_and_60','more_than_60']
    r = {'customerClass':q, 'streaming/not_streaming':x, 'number':w}
    d = pd.DataFrame(r)
    st.table(d)
    fig = px.bar(d, x ='customerClass', y = 'number', color = 'streaming/not_streaming', title = 'WHATSAPP FREE')
    st.plotly_chart(fig, use_container_width=True)
    
#--------DISPLAY FOR CALLS, SMS, AND DATA SERVICES ---------
st.header("""TOTAL SUM OF USERS FOR OTHER SERVICES""")
st.write("""This section looks at the total number of users we have for others services such as Data mb usage per month. It answers one of these questions,
         what is the total amount of data used by each age group.""")
user = st.selectbox('choose the service to view', ['customerPlansChanged','smsCountPerMonth','callMinutePerMonth','dataMBPerMonth'], key = 'sum')
if user == user:
    x = df.groupby('customerClass')[user].sum()
    st.write(x)
    st.area_chart(x)
    
#---------MEAN VALUES OF CALLS, SMS AND DATA SERVICES----
st.header("""AVERAGE SERVICE PER USER""")
st.write("""This section looks at the avergae usage of service per user. It answers one of these question how much data does one person in the various age group use.""")
user = st.selectbox('choose the service to view', ['customerPlansChanged','smsCountPerMonth','callMinutePerMonth','dataMBPerMonth'], key = 'mean')
if user == user:
    x = df.groupby('customerClass')[user].mean()
    st.write(x)
    st.area_chart(x)
    

hide_st_style = '''
<style>
#MainMenu {visibility:hidden:}
footer{visibility:hidden;}
header{visibility:hidden;}
</style>'''
st.markdown(hide_st_style, unsafe_allow_html=True)