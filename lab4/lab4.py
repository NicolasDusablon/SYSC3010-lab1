import http.client
import urllib.parse
import time

key = "54CDA6FJF4RCJ92C"
email = "nicolasdusablon@cmail.carleton.ca"
group = "L2-M-11"
member = "B"

params = urllib.parse.urlencode({'field1':email, 'field2':group, 'field3':member, 'key':key})
headers = {"Content-typZZe": "application/x-www-form-urlencoded","Accept": "text/plain"}
conn = http.client.HTTPConnection("api.thingspeak.com:80")
try:
    conn.request("POST", "/update", params, headers)
    response = conn.getresponse()
    print(response.status, response.reason)
    data = response.read()
    conn.close()
except:
    print("connection failed")
