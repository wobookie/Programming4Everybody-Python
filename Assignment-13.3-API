# API Endpoint: http://py4e-data.dr-chuck.net/json?
# Actual Problem: "Tallinn University" 
# Sample Problem: "South Federal University"

# Import required libraries
import urllib.request, urllib.response, urllib.parse
import ssl
import sys
import json

# initialise variables
total = 0
proxy = 'http://user:password@proxyhost:proxyport'
api_key = '42'

#read address as command line parameter, in case no paramater is provided use a default
try:
    address = sys.argv[1]
except:
    address = 'South Federal University'

# ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# handle proxy
proxy_handler = urllib.request.ProxyHandler({'http': proxy})
proxy_auth_handler = urllib.request.ProxyBasicAuthHandler()
opener = urllib.request.build_opener(proxy_handler, proxy_auth_handler)

# api endpoint URL
endpoint = 'http://py4e-data.dr-chuck.net/json?'

params = urllib.parse.urlencode({'key':api_key, 'address':address})
url = endpoint + params

with opener.open(url) as response:
    json_doc = response.read().decode()

js = json.loads(json_doc)

print(json.dumps(js, indent=8))

for element in js['results']:
    print(element['place_id'])
