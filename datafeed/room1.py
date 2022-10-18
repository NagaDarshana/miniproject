import urllib.request
import time
import requests
import threading
import random
def thingspeak_post():
	threading.Timer(30,thingspeak_post).start()
	val1=random.randint(1,30)
	val2=random.randint(1,30)
	val3=random.randint(30,100)
	print( val1 )
	print( val2 )
	print( val3 )
	URL='https://api.thingspeak.com/update?api_key=DG2CVJRJRMYJV5J0'
	KEY="DG2CVJRJRMYJV5J0"
	conn=urllib.request.urlopen(URL+"&field7=%d" %(20))
	print("OK")


if __name__=='__main__':
	thingspeak_post()
