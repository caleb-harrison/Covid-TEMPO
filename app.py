#####################################################################################






#####################################################################################

# Imports
import streamlit as st
import pandas as pd
import numpy as np
import us
import requests
from plotly.offline import iplot
import plotly.graph_objs as go
import plotly.express as px
from pandas import json_normalize

# Setup Streamlit
st.set_page_config(page_title='COVID-19 Music',
				   page_icon ='assets/favicon.png',
				   layout ='centered',
				   initial_sidebar_state ='auto')

# Header
st.write("""
# Covid19 Tracking App 🚑
[Coronavirus COVID19 API](https://covidtracking.com/data/api) is used to get the data in this app.
""")

st.write('Coronavirus is officially a pandemic. Since the first case in december the disease has spread fast reaching almost every corner of the world.'+
		 'They said it\'s not a severe disease but the number of people that needs hospital care is growing as fast as the new cases.'+
		 'Some governments are taking measures to prevent a sanitary collapse to be able to take care of all these people.'+
		 'I\'m tackling this challenge here. Let\'s see how some countries/regions are doing!')

# Setup API
url = 'https://api.covidtracking.com/v1/states/current.json'
r = requests.get(url)
df0 = json_normalize(r.json())

# Setup state selection
top_row = pd.DataFrame({'States':['Select a state']})
df0 = pd.concat([top_row[1:], df0]).reset_index(drop = True)

# Select case type
st.sidebar.header('Select a case type 🧪')
caseSelection = st.sidebar.selectbox('Cases type',('Total positive cases',
												   'Total deaths',
												   'Total recovered cases'))

# Select state
st.sidebar.subheader('Select a state 📍')
state = st.sidebar.selectbox('State',df0.state)

# Find selected state's results in API
if state != 'LOLOL':

	# Find API URL
	fullStateName = str(us.states.lookup(state))
	url = 'https://api.covidtracking.com/v1/states/'+ state +'/current.json'
	r = requests.get(url)
	print('API URL: ' + url)
	print(state + ': ' + fullStateName + '\n')

	# Scrape API for data and make selection API-friendly
	if caseSelection == 'Total positive cases':
		data = r.json()['positive']
		caseSelection = 'positive cases'
	elif caseSelection == 'Total deaths':
		data = r.json()['death']
		caseSelection = 'deaths'
	else:
		data = r.json()['recovered']
		caseSelection = 'recovered cases'

	# Show results
	st.write("""# Total """+ caseSelection +""" in """+ fullStateName +""" are: """ + str(data))

# Default selection
else:
	# Find API URL
	url = 'https://api.covidtracking.com/v1/us/current.json'
	r = requests.get(url)

	# Scrape API for data
	total = r.json()["positive"]
	deaths = r.json()["death"]
	recovered = r.json()["recovered"]

	# Show results
	st.write("""# United States Data:""")
	st.write("Total cases: "+str(total)+", Total deaths: "+str(deaths)+", Total recovered: "+str(recovered))

# Subheader
st.sidebar.subheader("""Created with 💖 by [Caleb Harrison](https://www.linkedin.com/in/calebharrison0)""")
