# Import required libraries
import re
import urllib.request
import sys
from bs4 import BeautifulSoup

# initialise variables
total = 0

#read filename as command line parameter, in case no paramater is provided use a default
try:
    url = sys.argv[1]
except:
    url = 'http://py4e-data.dr-chuck.net/comments_42.html'

# open the url and read the data
with urllib.request.urlopen(url) as response:
    html_doc = response.read()

# find all <span> in the HTML doc using BeautifulSoup
elements = BeautifulSoup(html_doc, features="html.parser").find_all('span')

# read the file content and do the processing
for element in elements:
    #find integer numbers in a single line
    numbers = re.findall('([0-9]+)', element.text)

    #in case no numbers in line - continue
    if len(numbers) == 0 :
        continue

    # maybe there are multiple numbers in one line. So we loop through the list
    for number in numbers:
        total = total + int(number)

print(total)