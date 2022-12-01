import streamlit as st
from streamlit.components.v1 import html
import pandas as pd
import matplotlib.pyplot as plt
from ipyvizzu import Chart, Data, Config, Style, DisplayTarget
import plotly_express as px

#-----set the page configuration-------
page_title = 'TELECOM ANALYSIS FOR AIRTEL AFRICA'
page_icon = "📶" #www.webfx.com/tools/emoji-cheat-sheet/
layout = 'wide'
st.set_page_config(page_title=(page_title),page_icon = page_icon, layout = layout)
st.title(page_title + '' + page_icon)

#-------READING IN THE DATA
df = pd.read_csv('data/telecom.csv')
df = df.fillna(0)

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

#--WRITE UP FOR INTRODUCTION---
st.write(""" This analysis was done on a telecom dataset, the aim of this project was to analysis the user engagment.""")
st.write("""The analysis was done by looking at the total number of customers and dividing them into groups based on age.
         From this division four sub classes was created.""")
st.write("""1. Less than 20 : This lo0ked at the ages of customers between 0 and 20. The total number of customers in this class is 1035.""")
st.write("""2. Between 20 and 40: This grouped the ages from 20 to 40 years old and the total number of customers within this age is 2529.""")
st.write("""3. Betweeen 40 and 60: This grouped the ages from 40 to 60 years old and the total number of customers in this age range is 261.""")
st.write("""4. More than 60: This class grouped the age from 60 and above and the total number of customers within this age is 175.""")

st.write("""The reason for using such age group to help us get a handful of dataset for the analysis, if we had made the age group small for instance 20 to 30.
         The number would be too small for a group analysis.""")



#--------MENU FOR SELECTING AGE GROUPS------
#This menu is to show the age groups and the filtered data 
less_than_20 = df.query('customerAge < 20')
btw_20_and_40 = df.query('(customerAge == 20 | customerAge > 20) & customerAge < 40')
btw_40_and_60 = df.query('(customerAge == 40 | customerAge > 40) & customerAge < 60')
more_than_60 = df.query('customerAge > 60')



#--------COUNT OF TOTAL CUSTOMERS IN THE VARIOUS AGE GROUP-------
number_of_customer_less_than_20 = less_than_20.count()
number_of_customer_btw_20_and_40 = btw_20_and_40.count()
number_of_customer_btw_40_and_60 = btw_40_and_60.count()
number_of_customer_more_than_60 = more_than_60.count()




#--------DISPLAY FOR STREAMING SERVICES--------
st.title('TOTAL NUMBER OF CUSTOMER USING SERVICES')
#----------Write up---------
st.write("""This subsection looks at the number of customers using the services offered at the telecom company.
         These services include streaming serivces such as Netflix and Hbo. It also offers services such as Whatsapp Free
         and Viber Free.""")


st.write("""By the classification below we can see the amount of people using the services, just click on the age group and click on the
         serivce you want to see.""")


user1, user2 = st.columns(2)
x = user1.selectbox('choose the age group', ['less_than_20', 'btw_20_and_40','btw_40_and_60','more_than_60'])
y = user2.selectbox('choose the service to view', ['netflixStream','pickboxStream','youtubeStream','hboGoStream','viberFree','whatsappFree'])
if x == 'less_than_20' and y == y:
    true_streaming = df.filter(['customerAge', y]).query(f'customerAge < 20 & {y} == True').count()
    true_streaming[y]
elif x == 'btw_20_and_40' and y == y:
    true_streaming = df.filter(['customerAge', y]).query(f'(customerAge == 20 | customerAge > 20) & customerAge < 40 & {y} == True').count()
    true_streaming[y]
elif x == 'btw_40_and_60' and y == y:
    true_streaming = df.filter(['customerAge', y]).query(f'(customerAge == 40 | customerAge > 40) & customerAge < 60 & {y} == True').count()
    true_streaming[y]
elif x == 'more_than_60' and y == y:
    true_streaming = df.filter(['customerAge', y]).query(f'customerAge > 60 & {y} == True').count()
    true_streaming[y]
    
st.write("""So by clicking less_than_20 and clicking netflix stream we can see that 24 people with an age less than 20 stream Netflix.""")
#--------DISPLAY FOR CALLS, SMS, AND DATA SERVICES ---------
st.title('SUM OF SERVICE USED PER AGE GROUP')
#------Write up------
st.write("""This section looks at the total sum of services used per age group. For example 
         it looks at the total amount of data used per age group. By doing this we know how to target our audience and create better incentives
         for the most lucrative group.""")






user3, user4 = st.columns(2)
w = user3.selectbox('choose the age groups', ['less_than_20', 'btw_20_and_40','btw_40_and_60','more_than_60'],key = 'age')
z = user4.selectbox('choose the service to view', ['customerPlansChanged','smsCountPerMonth','callMinutePerMonth','dataMBPerMonth'], key = 'service')
if w == 'less_than_20' and z == z:
    total_sum_of_service = df.filter(['customerAge', z]).query('customerAge < 20').sum()
    total_sum_of_service[z]
elif w == 'btw_20_and_40' and z == z:
    total_sum_of_service = df.filter(['customerAge', z]).query('(customerAge == 20 | customerAge > 20) & customerAge < 40').sum()
    total_sum_of_service[z]
elif w == 'btw_40_and_60' and z == z:
    total_sum_of_service = df.filter(['customerAge', z]).query('(customerAge == 40 | customerAge > 40) & customerAge < 60').sum()
    total_sum_of_service[z]
elif w == 'more_than_60' and z == z:
    total_sum_of_service = df.filter(['customerAge', z]).query('customerAge > 60').sum()
    total_sum_of_service[z] 


st.write("""By clicking data Mb per month we can see the age group that uses the most data and that group is between 20 and 40.""")

#---------MEAN VALUES OF CALLS, SMS AND DATA SERVICES
st.title('Total average of each service used per age group')
#---------Write up-------
st.write("""This section looks at the how much data of how many call does one person with an age group use. For example we look at the age group for less than 20 
         then we ask, what is the average amount of data consumed within this age group""")


user5, user6 = st.columns(2)
r = user5.selectbox('choose age groups', ['less_than_20', 'btw_20_and_40','btw_40_and_60','more_than_60'])
q = user6.selectbox('choose the service to view', ['customerPlansChanged','smsCountPerMonth','callMinutePerMonth','dataMBPerMonth'])
if r == 'less_than_20' and q == q:
    total_mean_of_service = df.filter(['customerAge', q]).query('customerAge < 20').mean()
    total_mean_of_service[q]
elif r == 'btw_20_and_40' and q == q:
    total_mean_of_service = df.filter(['customerAge', q]).query('(customerAge == 20 | customerAge > 20) & customerAge < 40').mean()
    total_mean_of_service[q]
elif r == 'btw_40_and_60' and q == q:
    total_mean_of_service = df.filter(['customerAge', q]).query('(customerAge == 40 | customerAge > 40) & customerAge < 60').mean()
    total_mean_of_service[q]
elif r == 'more_than_60' and q == q:
    total_mean_of_service = df.filter(['customerAge', q]).query('customerAge > 60').mean()
    total_mean_of_service[q]
    


hide_st_style = '''
<style>
#MainMenu {visibility:hidden:}
footer{visibility:hidden;}
header{visibility:hidden;}
</style>'''
st.markdown(hide_st_style, unsafe_allow_html=True)


