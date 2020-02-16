# Import required libraries
import urllib.request
import sys
import xml.etree.ElementTree as ET

# initialise variables
total = 0

# Actual Problem: http://py4e-data.dr-chuck.net/comments_370205.xml
# Sample Problem: http://py4e-data.dr-chuck.net/comments_42.xml

#read filename as command line parameter, in case no paramater is provided use a default
try:
    url = sys.argv[1]
except:
    url = 'http://py4e-data.dr-chuck.net/comments_42.xml'

with urllib.request.urlopen(url) as response:
    xml_doc = response.read()

root = ET.fromstring(xml_doc)

for count in root.findall('.//count'):
    total = total + int((count.text))

print(total)