from tkinter import *
from tkinter.ttk import *
import tkinter as Tkinter
import cv2
from time import strftime
from datetime import datetime

counter = 66600
running = False
def module():
    start.invoke()
def counter_label(label):
 def count():
  if running:
   global counter

   # To manage the initial delay.
   if counter==66600:   
    display="Starting..."
   else:
    tt = datetime.fromtimestamp(counter)
    string = tt.strftime("%H:%M:%S")
    display=string

   label['text']=display # Or label.config(text=display)

   label.after(1000, count)
   counter += 1

 # Triggering the start of the counter.
 count() 

# start function of the stopwatch
def Start(label):
 global running
 running=True
 counter_label(label)
 start['state']='disabled'
 stop['state']='normal'
 reset['state']='normal'

# Stop function of the stopwatch
def Stop():
 global running
 start['state']='normal'
 stop['state']='disabled'
 reset['state']='normal'
 running = False

# Reset function of the stopwatch
def Reset(label):
 global counter
 counter=66600

 # If rest is pressed after pressing stop.
 if running==False: 
  reset['state']='disabled'
  label['text']='Welcome!'

 # If reset is pressed while the stopwatch is running.
 else:   
  label['text']='Starting...'


list=['t','t','t','t','t']
face_cascade = cv2.CascadeClassifier('haarcascade_profileface.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
face2_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)

def face_value():
   _,img = cap.read()
   gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
   faces = face_cascade.detectMultiScale(gray, 1.3, 5)
   face2 = face2_cascade.detectMultiScale(gray, 1.3, 5)
   eyes = eye_cascade.detectMultiScale(gray,1.3,5)
   # print(faces,eyes,face2)
   # cv2.imshow('img',img)
   if faces==() and face2==() and eyes==():
      list.append('f')
   else : 
      # start.invoke()
      list.append('t')
def time1():
 string = strftime('%H:%M:%S')
 lbl.config(text = string)
 lbl.after(1000, time1)

def face():
 check()
 lb2.config(text = face_value())
 lb2.after(1000, face)
 list=[]



def check():
   list_check=['f','f']

   if len(list)>4:
      # print(list[-3:-1])
      if list[-3:-1] == list_check:
         print('not studing')
         stop.invoke()
         # list=[]
      else: 
         print('studing')
         start.invoke()


root = Tk()


lbl = Label(root, font = ('calibri', 40, 'bold'),foreground = 'black')
lbl.pack(anchor = 'center')
time1()

label = Tkinter.Label(root, text="Welcome!", fg="black", font="Verdana 30 bold")
label.pack()
f = Tkinter.Frame(root)
start = Tkinter.Button(f, text='Start', width=6, command=lambda:Start(label))
stop = Tkinter.Button(f, text='Stop',width=6,state='disabled', command=Stop)
reset = Tkinter.Button(f, text='Reset',width=6, state='disabled', command=lambda:Reset(label))
f.pack(anchor = 'center',pady=5)
# start.pack(side="left")
# stop.pack(side ="left")
reset.pack(side="left")


lb2 = Label(root, font = ('calibri', 1, 'bold'),foreground = 'black')
lb2.pack(anchor = 'center')
face()

root.attributes('-topmost',True)
root.mainloop()
print(list)
