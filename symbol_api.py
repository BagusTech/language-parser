'''
Created on Apr 24, 2017

@author: lissnerlistner
'''
import json, requests

res = requests.get('https://api.stocktwits.com/api/2/streams/symbol/AAPL.json')

response_json = json.loads(res.text)

messages = response_json.get('messages')
bodies = []

for message in messages:
    bodies.append(message.get('body'))
    
    if message.get('entities').get('sentiment') != None:
        print(message.get('body') + ' ' + message.get('entities').get('sentiment').get('basic'))
    #else:
        #print(message.get('body'))
#print(bodies)