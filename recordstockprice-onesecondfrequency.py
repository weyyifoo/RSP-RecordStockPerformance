# -*- coding: utf-8 -*-
"""
Created on Sat Jan 20 19:44:22 2018

@author: Wey Yi
"""

# this script gets information from googlefinance at particular intervals and automatically updates a list data for real-time analyses

# import modules for use here in this script
import json
import requests
import schedule
import time

# initiate empty lists to populate into
k = []
Yr =[]
Mth = []
Dy = []
Hr = []
Mn = []
Sec = []

TickerSymbol="CGG"

rsp = requests.get('https://finance.google.com/finance?output=json&q='+TickerSymbol)    


# define function job to reload request from googlefinance in json.
def job():   
    rsp = requests.get('https://finance.google.com/finance?output=json&q='+TickerSymbol)   
if rsp.status_code in (200,):
    totdata = json.loads(rsp.content[6:-2].decode('unicode_escape'))
    
def app():

# capture Current Price from "totaldata"
    kadd=totdata['op']
# uses time module to produce the current date and time
    Year=time.strftime("%Y")
    Month=time.strftime("%m")
    Day=time.strftime("%d")
    Hour=time.strftime("%H")
    Minute=time.strftime("%M")
    Second=time.strftime("%S")
# appends returns to current list and populates it
    Yr.append(Year)
    Mth.append(Month)
    Dy.append(Day)
    Hr.append(Hour)
    Mn.append(Minute)
    Sec.append(Second)
    k.append(kadd)

# schedules for "job" to be done every 2 seconds    
schedule.every(1).seconds.do(job)
schedule.every(1).seconds.do(app)

while True:
    schedule.run_pending()
    time.sleep(1)