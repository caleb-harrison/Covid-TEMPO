#####################################################################################

# Averages out the last 3 days increase of positive cases

# API: https://api.covidtracking.com/v1/states/{state}/{date}.json


#####################################################################################

# Imports
import requests
from datetime import date
from datetime import timedelta
from pandas import json_normalize

# Gets increased cases from previous 3 days in a given state
def getAverageIncrease(stateAbbreviation):
	# Variable for increase across last 3 days
	increase = 0

	# Gets 3 previous dates and formats for API
	today = (date.today() - timedelta(days = 1)).strftime("%Y%m%d")
	yesterday = (date.today() - timedelta(days = 2)).strftime("%Y%m%d")
	dayBeforeYesterday = (date.today() - timedelta(days = 3)).strftime("%Y%m%d")
	print('Today: ' + today, 
		  '\nYesterday: ' + yesterday,
		  '\nDay Before Yesterday: ' + dayBeforeYesterday)

	# Setup API for today
	url = 'https://api.covidtracking.com/v1/states/'+stateAbbreviation+'/'+today+'.json'
	r = requests.get(url)
	increase += int(r.json()['positiveIncrease'])

	# Setup API for yesterday
	url = 'https://api.covidtracking.com/v1/states/'+stateAbbreviation+'/'+yesterday+'.json'
	r = requests.get(url)
	increase += int(r.json()['positiveIncrease'])

	# Setup API for day before yesterday
	url = 'https://api.covidtracking.com/v1/states/'+stateAbbreviation+'/'+dayBeforeYesterday+'.json'
	r = requests.get(url)
	increase += int(r.json()['positiveIncrease'])

	# Average positive case increase across last 3 days
	return (increase // 3)


print(getIncrease('CA'))