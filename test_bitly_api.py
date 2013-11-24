# import the modules
 
import bitly_api
import sys

API_USER = "cfd992841301aabcd843e8ed4622b9c88e320e8e"
API_KEY = "c5955c440b750b215924bd08d1b79518ca4a82c4"
 
b = bitlyapi.BitLy(API_USER, API_KEY)
 
# Define how to use the program
 
usage = """Usage: python shortener.py [url]
e.g python shortener.py http://www.google.com"""
 
if len(sys.argv) != 2:
    print usage
    sys.exit(0)
 
longurl = sys.argv[1]
 
response = b.shorten(longUrl=longurl)
 
print response['url']
