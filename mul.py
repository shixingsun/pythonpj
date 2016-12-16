#!/usr/bin/python
import thread
import time

def print_time(namethread,delay):
	count=0
	
	while count<5:
		time.sleep(delay)
		count+=1
		print "%s: %s" %(namethread,time.ctime(time.time()))
		if count==5:
			thread.exit()	
try:
	thread.start_new_thread(print_time,("T1",2))
except:
	print 'error: unable to start thread'
while 1:
	pass
