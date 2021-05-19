
import pyscreenshot
import tkinter
from tkinter import messagebox, filedialog
import sys
from datetime import datetime
import time

def uniqeImageName():
    now = datetime.now()
    imageName = now.strftime("%d-%m-%Y_%H-%M-%S")
    return imageName


class screenshot:
    where = ""
    filename = "C:/Users/Public"

    def takeScreenShot(self):
        try:
            top.withdraw()
            time.sleep(0.1)
            im = pyscreenshot.grab()
            im.save(self.filename + '/' + uniqeImageName() + ".png")
            top.deiconify()
            messagebox.showinfo("Taken", "Screen Captured")
        except:
            e = sys.exc_info()[0]+sys.exc_info()[1]
            messagebox.showinfo("Error", e)

    def whrereToSave(self):
        self.filename = filedialog.askdirectory()

        try:
            self.where = self.filename + "/" + uniqeImageName() + ".png"
            loc.delete(0, 'end')
            loc.insert(-1, ss.where)
        except:
            pass


top = tkinter.Tk()
top.title("bhyeanhasan")
top.iconbitmap("b.ico")
top.resizable(False, False)
top.configure(background="white")

ss = screenshot()
tkinter.Label(background='white').pack()
tkinter.Label(background='white').pack()

scrTake = tkinter.Button(text="Take Screenshot", command=ss.takeScreenShot, width=25, height=2, relief='groove')
scrTake.configure(background="orange")

dirView = tkinter.Button(text="Change Location", command=ss.whrereToSave, width=15, relief='groove')

loc = tkinter.Entry(width=50)
loc.configure(relief='groove')
loc.insert(-1, ss.filename)

scrTake.pack()
tkinter.Label(background='white').pack()
dirView.pack()
tkinter.Label(background='white').pack()
loc.pack()

top.mainloop()
