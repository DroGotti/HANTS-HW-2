#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  6 20:10:54 2021

@author: drogotti
"""

import requests 
import pandas as pd

##Connect to API for Anime Facts

##Get Request

jsonResponse = requests.get('https://anime-facts-rest-api.herokuapp.com/api/v1')

##Check for status 
jsonResponse.status_code
jsonResponse.json()

print(jsonResponse)

##Get request

jsonResponse2 = requests.get('https://anime-facts-rest-api.herokuapp.com/api/v1/jujutsu_kaisen')
dataframe=pd.dataframe(jsonResponse2.json())