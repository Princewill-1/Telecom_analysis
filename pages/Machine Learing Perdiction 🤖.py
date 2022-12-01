# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 11:04:53 2022

@author: HP USERPC
"""
import streamlit as st
import pandas as pd
import numpy as np 
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
from sklearn.tree import DecisionTreeRegressor

#---------READING THE FILE-----
df = pd.read_csv(r'data/telecom.csv')
df = df.fillna(0)
#-----WRTIE UP-----
st.header('AI PREDICTION 🤖')
st.write("""This section is created to help us learn from the data set and make precise business decisions with the help of artifical intelligence.
         I created the model to help us know if a certain customer would use one of the streaming services. From the data we analysed the AI model obeserved certain patterns, that lets it know
         if a user is more likely and less likely to use the streaming services.
         """)
st.write("""For example if you choose netflix stream, then put the customer Age at 30, customer plans changed at 5, the sms count per month at 5000, the call minute per month at 10000 and the data mb per month at 100000, the result will show 
streaming which means that we can target customer above the age of thirty with more data offers and this will push them to use our streaming services.""")

#------CREATING USER INPUT-------
user = st.selectbox('choose a service', ['netflixStream','pickboxStream','youtubeStream','hboGoStream','viberFree','whatsappFree'])
if user == user:
    y = df[user]
    features_x = ['customerAge','customerPlansChanged','smsCountPerMonth','callMinutePerMonth','dataMBPerMonth']
    x = df[features_x]

#-------DEFINING MY MODEL---------
my_model = DecisionTreeClassifier()
my_model.fit(x,y)

#------CREATING A USER FORM---------
with st.form('Analysis Form'):
    age = st.number_input('write the customer age')
    plans = st.number_input('write the customer plans changed')
    sms = st.number_input('write the sms count per month')
    call = st.number_input('write the call minute per month')
    data = st.number_input('write the data mb per month')
 #-------SUBMIT BUTTON--------   
    submitted = st.form_submit_button('Enter Data')
    if submitted:
        o = my_model.predict([[age, plans, sms, call, data]])
        for i in o:
            if i == 0:
                st.write('Not Streaming')
            else:
                st.write('Streaming')
            
            
hide_st_style = '''
<style>
#MainMenu {visibility:hidden:}
footer{visibility:hidden;}
header{visibility:hidden;}
</style>'''
st.markdown(hide_st_style, unsafe_allow_html=True)