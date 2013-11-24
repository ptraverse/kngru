# import the modules
 
import bitly_api
import sys

API_USER = "cfd992841301aabcd843e8ed4622b9c88e320e8e"
API_KEY = "c5955c440b750b215924bd08d1b79518ca4a82c4"
ACCESS_TOKEN = "1214d30c74adf88608b83bdc8eac7b053a57b6f4" 

b = bitly_api.Connection(access_token=ACCESS_TOKEN)
 
# Define how to use the program
 
usage = """Usage: python shortener.py [url]
e.g python shortener.py http://www.google.com"""
 
if len(sys.argv) != 2:
    print usage
    sys.exit(0)
 
longurl = sys.argv[1]
 
response = b.shorten(uri=longurl)
 
print response['url']
