#TODO: add better gui
#TODO: make more user-friendly
#TODO: sort out files
#TODO: code organising
#TODO: make less todo'

#importing
import tkinter
import os  #in
import filemanager  #own

#setting up tkinter
master = tkinter.Tk()
master.withdraw()
top = tkinter.Toplevel(master)
top.protocol("WM_DELETE_WINDOW", master.destroy)

#defining tkinter functions
# noinspection PyUnresolvedReferences
def callback():
    #if not os.path.isfile(e.get()):
    #    textabc = tkinter.Text(top, height=1, font="font, 20", width=20)
    #    textabc.insert(tkinter.INSERT, "File does not exist!")
    #    textabc.config(state=tkinter.DISABLED, bg="#f0f0f0", bd=0)
    #    textabc.pack()
    #else:
    filemanager.wpitch(s.get() + 1)
    filemanager.wlength(l.get())
    filemanager.wpath("C:/Users/Daan Vink/PycharmProjects/hilbert/images/process.gif")
    top.withdraw()
    import curve  #next part in script, to keep it readable

#opening startscreen
b = tkinter.Text(top, height=1, font="font, 50", width=12)
b.insert(tkinter.INSERT, "Sight to Sound")
b.config(state=tkinter.DISABLED, bg="#f0f0f0", bd=0)
b.pack()
b = tkinter.Text(top, height=1, font="font, 15", width=21)
b.insert(tkinter.INSERT, "Select your average pitch")
b.pack()
b.config(state=tkinter.DISABLED, bg="#f0f0f0", bd=0)
s = tkinter.Scale(top, from_=1, to=100, orient=tkinter.HORIZONTAL, bd=4)
s.set(50)
s.pack()
b = tkinter.Text(top, height=1, font="font, 15", width=39)
b.insert(tkinter.INSERT, "Select how long you want each pixel to play (ms)")
b.config(state=tkinter.DISABLED, bg="#f0f0f0", bd=0)
b.pack()
l = tkinter.Scale(top, from_=1, to=1000, orient=tkinter.HORIZONTAL, length=300, bd=4)
l.set(100)
l.pack()
b = tkinter.Button(top, text="OK", command=callback)
b.pack()
b = tkinter.Text(top, height=1, font="font, 13", width=36)
b.insert(tkinter.INSERT, "Input the name and directory of your image")
b.config(state=tkinter.DISABLED, bg="#f0f0f0", bd=0)
b.pack()
e = tkinter.Entry(top, width=75, font="font, 15")
e.insert(tkinter.INSERT, "")
e.pack()
b = tkinter.Text(top, height=1, font="font, 13", width=36)
b.insert(tkinter.INSERT, "")
b.config(state=tkinter.DISABLED, bg="#f0f0f0", bd=0)
b.pack()
master.mainloop()
print("test")
