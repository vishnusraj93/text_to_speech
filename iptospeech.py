from gtts import gTTS
import os
from tkinter import *
from tkinter import messagebox
root = Tk()
root.title("Text to Speech Converter")
root.geometry("370x320")
root.resizable(0,0)
canvas=Canvas(root,width = 370, height = 320)
canvas.pack()
icon = PhotoImage(file='C:\Images\index.png')
root.iconphoto(False, icon)
def texttospeech():
    text = entry.get()
    try:
        res = gTTS(text=text,lang='en')
        res.save('res.mp3')
        os.system('start res.mp3')
    except:
        messagebox.showerror('Error',"Please enter a text!!!")

entry = Entry(root,font=('open sans', 10, 'bold'),
                     bd=5, background ='#000000',width = 45, bg='#c9d1cf', fg='#000000')
img = PhotoImage(file='C:\Images\gimage.png')
canvas.create_image(270,370,image=img,anchor='center')
canvas.create_window(185,160,window=entry)
label = Label(root,font=('open sans', 15, 'bold'),text="Enter the text below",bg='#000000',
              fg='#ffffff').place(x=90,y=100)
button = Button(text="Convert", width='6', font=('open sans', 12, 'bold'),bg='#000000',
                fg='#ffffff',command=texttospeech)
canvas.create_window(185,195,window=button)
root.mainloop()



