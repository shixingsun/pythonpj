import serial 
import time
ser=serial.Serial()
ser.port=0
ser.timeout=1
print ser
ser.open()
ser.write(chr(1))
time.sleep(5)
ser.write(chr(2))

def main():
	while True:
		count=ser.inWaiting()
		if count !=0:
			print count
			rev=ser.read(4)
			ser.write(chr(count))
			ser.flushInput()
		time.sleep(0.1)
if __name__=='__main__':
	try:
		main()
	except KeyboardInterrupt:
		if ser!=None:
			ser.close()
