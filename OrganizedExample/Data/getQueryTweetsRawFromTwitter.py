'''
Nathaniel Gottschalt, Reena Sharma, Garikapati Geethika
Data Mining 431 Project
'''

import tweepy   
import json   
  
OAuth = tweepy.OAuthHandler('MR8ZLoqeJroECduiUqpiWcC6e', 'hNT3lC8FF4l9dHXgLCwlnakW9sLtv2ZyeU6seAGEWxEn1PO0Th')
OAuth.set_access_token('4907808432-aqyXbzfh8Q2YtGcxgVrVQ3SEtqFcCjOiUByIRyX', '2oxYraMYUYUF3adcVaqhR42lIg646B9u5DavN8NOc3uYz')
  
class StreamListener(tweepy.StreamListener):
     def on_data(self, raw_data):
  
        jdata = json.loads(str(raw_data))
        print jdata['text']
  
        try:
            f = open("queryTweetsRaw.txt", 'a+')
            f.write(json.dumps(jdata['text']) + '\n')
            f.close()
        except:
            print 'Data writting exception.'
  
def main():
    while(True): 
        sl = StreamListener()
        stream = tweepy.Stream(OAuth, sl)
        try: 
            stream.filter(track = ['sneezing', 'vomit', 'Fever', 'heahache', 'fever', 'diarrhea', 'dehydrated', 'flu'])
        except:
            print 'Exception occur!'
  
if __name__ == '__main__':
    main()
     