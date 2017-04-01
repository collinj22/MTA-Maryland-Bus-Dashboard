#!/usr/bin/python
# MTA Baltimore Bus Tracker
import sys, getopt
import pandas as pd
import urllib.request
import re
from bs4 import BeautifulSoup
import pyprind