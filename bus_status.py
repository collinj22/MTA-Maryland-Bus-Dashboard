#!/usr/bin/python
# MTA Baltimore Bus Tracker

import pandas as pd
import urllib.request
from bs4 import BeautifulSoup
import gtfs_realtime_pb2
import urllib

feed = gtfs_realtime_pb2.FeedMessage()
response = urllib.request.urlopen('http://gtfsrt.mta.maryland.gov:8888/TMGTFSRealTimeWebService/TripUpdate/TripUpdates.pb')
feed.ParseFromString(response.read())
for entity in feed.entity:
  if entity.HasField('trip_update'):
    print(entity.trip_update)


def bus_time(stop):
    html = urllib.request.urlopen(job_url).read()
    soup = BeautifulSoup(html, 'html.parser')
    texts = soup.findAll(text=True)
    pass
