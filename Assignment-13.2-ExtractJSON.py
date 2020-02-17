# Import required libraries
import urllib.request, urllib.response, urllib.parse
import ssl
import sys
import json

# initialise variables
total = 0
proxy = 'http://user:password@proxyhost:port'

# ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# handle proxy
proxy_handler = urllib.request.ProxyHandler({'http': proxy})
proxy_auth_handler = urllib.request.ProxyBasicAuthHandler()

opener = urllib.request.build_opener(proxy_handler, proxy_auth_handler)

# Actual Problem: http://py4e-data.dr-chuck.net/comments_370206.json
# Sample Problem: http://py4e-data.dr-chuck.net/comments_42.json

#read filename as command line parameter, in case no paramater is provided use a default
try:
    url = sys.argv[1]
except:
    url = 'http://py4e-data.dr-chuck.net/comments_42.json'

with opener.open(url) as response:
    json_doc = response.read().decode()

js = json.loads(json_doc)
for element in js['comments']:
    total = total + int(element['count'])

print(total)
