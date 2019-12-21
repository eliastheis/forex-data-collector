# author: Elias Theis
import requests
import time
import datetime
import json
from matplotlib import pyplot as plt

symbol = 'EUR/USD'

def getPrice():
	data = requests.get('https://fcsapi.com/api/forex/latest?symbol=' + symbol + '&access_key=O3hWhdPCCLlRsuO91Fibl6H8uCxSknKsNvTkKnscYiAo55').text
	data = json.loads(data)['response']
	return data[0]['price']

def getTime():
	return '[' + str(datetime.datetime.now()) + ']'

plt.ion()
prices = []
old = ''
while(True):
	
	p = getPrice()
	if old != p:
		old = p
		print(getTime(), symbol, p)
	prices.append(float(p))
	if len(prices) > 1:
		plt.clf()
		plt.plot(prices)
		plt.draw()
	
	plt.pause(6.1)

