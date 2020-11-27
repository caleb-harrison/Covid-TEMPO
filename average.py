#####################################################################################

# Averages out the last 3 days increase of positive cases

# API: https://api.covidtracking.com/v1/states/{state}/{date}.json

#####################################################################################

# Imports
import requests
from datetime import date
from datetime import timedelta
from pandas import json_normalize

# Gets 3 previous dates and formats for API
def getDates():
	# returns 3 dates: today, yesterday, day before yesterday
	return ((date.today() - timedelta(days = 1)).strftime("%Y%m%d"),
	(date.today() - timedelta(days = 2)).strftime("%Y%m%d"),
	(date.today() - timedelta(days = 3)).strftime("%Y%m%d"))

# Search API and find positive test increase for given day and state
def getIncrease(stateAbbreviation, date):
	url = 'https://api.covidtracking.com/v1/states/'+stateAbbreviation+'/'+date+'.json'
	r = requests.get(url)
	return int(r.json()['positiveIncrease'])

# Gets increased cases from previous 3 days in a given state
def getAverageIncrease(stateAbbreviation):
	# Get 3 previous dates
	today, yesterday, dayBeforeYesterday = getDates()

	# Gets total increase from last 3 days
	increase = getIncrease(stateAbbreviation, today) + getIncrease(stateAbbreviation, yesterday) + getIncrease(stateAbbreviation, dayBeforeYesterday)

	# Average increase from last 3 days
	return (increase // 3)
