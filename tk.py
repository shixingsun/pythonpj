from  Tkinter import*
import threading
import time
##time show
root =Tk()
root.minsize(300,240)
root.maxsize(600,400)
root.title("test")
str=time.ctime(time.time())
label=Label(root,text=str)
label.pack()

#read system time
class myTh(threading.Thread):
    def __init__(self,threadID,name,counter):
        threading.Thread.__init__(self)
        self.threadID=threadID
        self.name=name
        self.counter=counter
    def run(self):
        while True:
            #print '1'
            showsystime()
def showsystime():
        str=time.ctime(time.time())
        #label.update()
        #l#abel.
        print str
        time.sleep(1)

thread=myTh(1,"",1)
#thread.start()
#root.update_idletasks()
root.mainloop()

