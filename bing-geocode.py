#!/usr/bin/python3
## Author:  Christopher Mortimer
## Date:    2020-10-26
## Desc:    Geocode a suburb using Bing Maps

## Import Libraries
from dotenv import load_dotenv
import os
import geocoder 
## Get bing API key from .env file
load_dotenv()
bingkey = os.environ.get("bingkey")

# Call service and print response
g = geocoder.bing('Rivett, ACT, 2611', key=bingkey)
print(g.json)