import http.client
import urllib.parse
import time

def read_data_thingspeak():
    url = "https://api.thingspeak.com/channels/1161324/fields/1.json?apikey="
    key = "FHUUTQITZ4YX4QAO"
    header = "&results=2"
    new_url = url+key+header
    print(new_url)
    
    get_data=requests.get(new_url).json()
    print(get_data)
    channel_id = get_data['channel']['id']
    field_1 = get_data['feeds']
    
    for x in field_1:
        print(x['field1'])
        t.append(x['field1'])
        
if __name__== "__main__":
    while True:
        read_data_thingspeak()