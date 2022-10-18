import urllib.request
import time
import requests
import threading
import random
def thingspeak_post():
	threading.Timer(30,thingspeak_post).start()
	val1=random.randint(1,30)
	val2=random.randint(1,30)
	val3=random.randint(1,10)
	print( val1 )
	print( val2 )
	print( val3 )
	URL='https://api.thingspeak.com/update?api_key=SXRMG95WO9RCN1WL&field1=0'
	KEY="SXRMG95WO9RCN1WL"
	conn=urllib.request.urlopen(URL+"&field1=%d" %(val1)+"&field2=%d" %(val2)+"&field3=%d" %(val3))

if __name__=='__main__':
	thingspeak_post()
