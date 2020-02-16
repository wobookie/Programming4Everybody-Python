# Import required libraries
import re
import urllib.request
import sys
from bs4 import BeautifulSoup

# initialise variables
i = 0
depth = 7
link_pos = 18

# Actual Problem: http://py4e-data.dr-chuck.net/known_by_Muhsin.html
# Sample Problem: http://py4e-data.dr-chuck.net/known_by_Fikret.html

#read filename as command line parameter, in case no paramater is provided use a default
try:
    url = sys.argv[1]
except:
    url = 'http://py4e-data.dr-chuck.net/known_by_Fikret.html'

while i < depth:
    # open the initial url and read the data
    with urllib.request.urlopen(url) as response:
        html_doc = response.read()

        # find all <span> in the HTML doc using BeautifulSoup
        elements = BeautifulSoup(html_doc, features="html.parser").find_all('a', href=True)

        # Print name
        print('Found:', elements[link_pos-1].text)

        # extract element at position 3
        url = elements[link_pos-1]['href']

    i += 1