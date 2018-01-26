# -*- coding: utf-8 -*-
"""
Created on Sat Jan 20 19:44:22 2018

@author: Wey Yi
"""

# this script gets information from googlefinance at particular intervals and automatically updates a list data for real-time analyses

# import modules for use here in this script
import json
import requests
import time
import numpy as np
import pandas as pd
# new code
import matplotlib.pyplot as plt

# initiate empty lists to populate into
k1, time_lapsed = [], []

# records the time the code initiates
start_time = time.time()

def clock():
    current_time = time.time()
    Lapsed = current_time - start_time
    time_lapsed.append(Lapsed)
    return Lapsed
    
TickerSymbol1="CVX"
rsp = requests.get('https://finance.google.com/finance?output=json&q='+TickerSymbol1)    
# define function job to reload request from googlefinance in json.
def job1():   
    rsp = requests.get('https://finance.google.com/finance?output=json&q='+TickerSymbol1)    
    if rsp.status_code in (200,):
        totdata = json.loads(rsp.content[6:-2].decode('unicode_escape'))
    kadd1=totdata['l']
    k1.append(float(kadd1))
    print(TickerSymbol1,"=",(time.time() - start_time),kadd1)
    
try:
    while True:
        data = clock() # get data from the function
        job1()
        plt.draw()
        time.sleep(2)
        if (time.time() - start_time) >= float(20):
            alldata = pd.DataFrame({'Timelapsed': time_lapsed, 'Chevron': k1})
            #to sort: alldata = alldata[['Day','Month', 'Year','Hour','Minute','Second','Chevron','ExxonMobil', 'ConocoPhilips']]
            alldata.to_csv('{}.csv'.format(start_time))
            break
except KeyboardInterrupt:
    print("Keyboard Interrupted after the script has lasped for",time.time() - start_time,"seconds")    