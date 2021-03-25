# -*- coding: utf-8 -*-
"""
Created on Tue May  5 19:43:54 2020

@author: soso
"""


import streamlit as st

st.title("This is My First Streamlit App")

##Heading
st.header("This is Header")
st.subheader("This is Subheader")

##Text
st.text("Hello This is Soheil from Zharfiran")
st.markdown("## MARKDOWN HERE")

## Colorful
st.success("SUCCESS")
st.info("INFO")
st.warning("Warning")
st.error("ERROR")
st.exception("EXCEPTION")

#get help from python
st.help("range")

#Write
st.write("-- Text with Write")
st.write(range(10,20))

#Image------------------------
#from PIL import Image
#soso=Image.open("SoSo.jpg")
#st.image(soso , caption="Soheil Tehranipour")

#st.video
#st.audio

#Checkbox------------------------
if st.checkbox("Show/Hide"):
    st.text("Showing or Hiding Checkbox")

#Radio------------------------
status = st.radio("What is your Status", ("Activate","Inactive"))

if status =="Activate":
    st.success("You are Active")
else:
    st.warning("You are Inactive")
    
    
#Selectbox------------------------
occupation = st.selectbox("Your job", ["CEO","Data Scientist","ML Engineer"])
st.write("Your job is",occupation)
    
#Multiselect------------------------
location = st.multiselect("Where do you live",("Tehran","Shiraz","Tabriz","Isfihan"))
st.write("You select:",len(location),"Location")  

#Slider------------------------
age = st.slider("How old are you?",18,35)
if age>30:
    st.write("You are OLD !!")
else:
    st.write("Newbie :D")
    
    
#Button------------------------
if st.button ("About"):
    st.text("This is my first app . Soheil Tehranipour")
    
    
#Input(TEXT)------------------
st.write("--------------------------------")
firstname = st.text_input("Firstname", "Enter your firstname here and press ENTER")
if st.button("Submit"):
    st.write("You Entered <<",firstname,">> as your firstname")
    st.success(firstname)


#Input(Message)------------------
message = st.text_area("Message", "Type here ...")
if st.button(label="Submit", key="sms_submit"):
    st.write("You Entered <<",message,">> as your message")



#Input(Time)------------------
import datetime
today = st.date_input("Today is:",datetime.datetime.now())
time = st.time_input("The Time is:", datetime.time())

#Displaying JSON------------------
st.text("Display JSON")
st.json({'Name':"Soheil",'Gender':"MALE"})

#Displaying RAW Code------------------
st.write("--------------------------------")
st.text("Displaying RAW Code")
st.code("import numpy as np")


with st.echo():
	#Show this line 
	import pandas as pd 
	df = pd.DataFrame([1,2,3],[4,5,6])


#Sidebars------------------
st.write("--------------------------------")
st.sidebar.header("About")
st.sidebar.text("This is my first app with Streamlit")
st.sidebar.text("Soheil tehranipour")


#Progress Bar------------------
import time

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(5):
  # Update the progress bar with each iteration.
  latest_iteration.text(f'Iteration {i+1}')
  bar.progress(i + 1)
  time.sleep(0.5)

'...and now we\'re done!'

#Spinner------------------
with st.spinner ("Waiting ..."):
	time.sleep(5)

st.success("Finished")

st.balloons()

'This is test ... You can just write everything you want this way'


#Dataframe
st.dataframe(df)


#Table
st.table(df)


