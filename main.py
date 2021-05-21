# Used Library and packages
import tkinter
import cv2
import numpy as np
from tkinter import messagebox, filedialog
import sys
from datetime import datetime
import time
from win32api import GetSystemMetrics
from threading import Thread

try:
    import pyautogui
except:
    import pip

    pip.main(['install', 'pyautogui'])
    pip.main(['install', 'pillow'])


# For getting unique name using time
def uniqeImageName():
    now = datetime.now()
    imageName = now.strftime("%d-%m-%Y_%H-%M-%S")
    return imageName


# Main backend Class
class screenClass:
    filename = "C:/Users/Public"
    key = True
    pressed = True
    w = GetSystemMetrics(0)
    h = GetSystemMetrics(1)
    dimension = (w, h)
    videoOutput = filename + '/' + uniqeImageName() + ".avi"
    fourcc = cv2.VideoWriter_fourcc(*"XVID")
    output = cv2.VideoWriter(videoOutput, fourcc, 20.0, dimension)

    # For changing directory
    def whrereToSave(self):
        self.filename = filedialog.askdirectory()

        try:
            loc.delete(0, 'end')
            loc.insert(-1, self.filename)
        except:
            pass

    # To start record
    def startRecord(self):
        self.key = True
        self.pressed = False
        self.videoOutput = self.filename + '/' + uniqeImageName() + ".avi"
        self.output = cv2.VideoWriter(self.videoOutput, self.fourcc, 20.0, self.dimension)
        scrEnd.pack()
        thread = Thread(target=self.recording)
        thread.start()


    # Thread ei function tare chlabe noile infinity loop freeze kore dibe
    def recording(self):
        t = time.time()
        scrRecord.configure(text="Recording ...")
        Time.pack()

        while self.key:
            img = pyautogui.screenshot()
            frame = np.array(img)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            self.output.write(frame)
            Time.delete(0, 'end')
            Time.insert(-1,"Recording: "+ str(round(time.time()-t)))
        self.output.release()

    # key false hoile loop stop hoye jabe
    def endRecord(self):
        scrRecord.configure(text="Record Again")
        scrEnd.pack_forget()
        self.key = False
        self.pressed = True
        Time.pack_forget()

    # For taking screenshot
    def takeScreenShot(self):
        try:
            top.withdraw()
            time.sleep(0.2)
            im = pyautogui.screenshot()
            im.save(self.filename + '/' + uniqeImageName() + ".png")
            top.deiconify()
            messagebox.showinfo("Taken", "Screen Captured")
        except:
            e = sys.exc_info()[0] + sys.exc_info()[1]
            messagebox.showinfo("Error", e)


# Front-End part
top = tkinter.Tk()
top.title("bhyeanhasan")
top.iconbitmap("b.ico")
top.resizable(False, False)
top.configure(background="#2b2b33")

ss = screenClass()

scrTake = tkinter.Button(text="Take Screenshot", command=ss.takeScreenShot, width=20, height=2, relief='groove',
                         background="#131354", foreground="yellow", font=("Courier", 12))
dirView = tkinter.Button(text="Change Location", command=ss.whrereToSave, width=15, relief='groove',
                         background="#131354", foreground="white")
loc = tkinter.Entry(width=60)
scrRecord = tkinter.Button(text="Start Recording", command=ss.startRecord, width=20, height=3, relief='groove',
                           background="#131354", foreground="#EDA63A"
                           , font=("Courier", 15)
                           )
scrEnd = tkinter.Button(text="End Recording", command=ss.endRecord, width=20, height=2, relief='groove',
                        background="#131354", foreground="red", font=("Courier", 12))

loc.configure(relief='groove', background="#131354", foreground="white")
loc.insert(-1, ss.filename)


tkinter.Label(background='#2b2b33').pack()
tkinter.Label(background='#2b2b33').pack()

scrRecord.pack()
tkinter.Label(background='#2b2b33').pack()

# scrEnd.pack()

tkinter.Label(background='#2b2b33').pack()

scrTake.pack()

tkinter.Label(background='#2b2b33').pack()
tkinter.Label(background='#2b2b33').pack()

dirView.pack()

tkinter.Label(background='#2b2b33').pack()

loc.pack()
tkinter.Label(background='#2b2b33').pack()


Time = tkinter.Entry(width=15,background='#2b2b33',relief='flat',foreground="orange",font=("Courier", 12))

top.mainloop()
