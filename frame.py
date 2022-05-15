from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import pygame

pygame.mixer.init()

root=Tk()

# properties of the window
root.title("Happy Birthday")
root.geometry('700x500')
root.resizable(False,False)
root.iconbitmap('title2.ico')
# end of properties 

#begin of dynamic
def stop():
    pygame.mixer.music.stop()


def play():
    pygame.mixer.music.play(-1)

def hello():
    if len(name_field.get())!=0:
        w1=Toplevel(root)
        img1=ImageTk.PhotoImage(Image.open('hey2.png'))
        img2=ImageTk.PhotoImage(Image.open('up.png'))
        w1.title("Happy Birthday")
        w1.iconbitmap('title2.ico')
        w1.geometry('700x500')
        pygame.mixer.music.load("birth.mp3")
        pygame.mixer.music.play(-1)
        main_frame=Frame(
            w1
        )
        main_frame.pack(anchor=CENTER,expand=True,fill=BOTH)
        play_frame = Frame(
            w1
        )
        play_frame.pack(side='bottom',anchor=CENTER, expand=True, fill=BOTH)
        label1=Label(
            main_frame,
            image=img1,
        )
        label1.pack(side='top',expand=True,fill=BOTH,anchor=CENTER)

        label2=Label(
            main_frame,
            text=f'Happy Birthday {name_field.get()}',
            image=img2,
            compound='right',
            # pady=20,
            fg='black',
            font=("Segoe Print", 20,'bold'),
            padx=10
        )
        label2.pack(side='top',expand=True,anchor=CENTER,fill=BOTH)
        name_field.delete(0,END)
        # pygame.mixer.music.stop()
        p1 = Button(
            play_frame,
            text='Stop',
            compound='right',
            font=("Consolas", 20, 'bold'),
            bg='black',
            fg='white',
            pady=10,
            padx=20,
            relief=FLAT,
            command=stop
        )
        p1.pack(side='left',expand=True, anchor=CENTER)
        
        p2 = Button(
            play_frame,
            text='Play',
            compound='right',
            font=("Consolas", 20, 'bold'),
            bg='black',
            fg='white',
            pady=10,
            padx=20,
            relief=FLAT,
            command=play
        )
        p2.pack(side='right',expand=True, anchor=CENTER)
        w1.mainloop()
        
        
    else:
        messagebox.showwarning(title='Input Error',message="Please Enter Your Name")
        name_field.delete(0,END)
    
    
    




#end of dynamic

# begin of drawing

img_frame=Frame(
    root
)
img_frame.pack(side='top',expand=True,anchor=CENTER)


cover_img=ImageTk.PhotoImage(Image.open('birthday.png'))
icon_img=ImageTk.PhotoImage(Image.open('gifts.png'))
b_img=ImageTk.PhotoImage(Image.open('g2.png'))

cover_label=Label(
    img_frame,
    image=cover_img,
)
cover_label.pack(anchor=CENTER,expand=True,side='top')

'''cap_label=Label(
    img_frame,
    image=cap_img,
    compound='right',
    text='Hello Ramadan',
    font=("Segoe Print",25),
    padx=5
)
cap_label.pack(side='bottom',expand=True,anchor=CENTER)'''

#End of Cover frame


# Begin Of Field Frame

input_frame=Frame(
    root
)
input_frame.pack(expand=True,anchor=CENTER)

name_field=Entry(
    input_frame,
    bd=2,
    width=30,
    font=("Consolas",25,'bold'),
)
name_field.pack(side='right',expand=True,anchor=CENTER,padx=20)

icon_label=Label(
    input_frame,
    image=icon_img,
    # compound='left',
)
icon_label.pack(side='left',anchor=CENTER,expand=True)

#End of input Frame 


# Begin Of Button Frame

button_frame=Frame(
    root
)
button_frame.pack(side='bottom',anchor=CENTER,expand=True,fill=BOTH)

b1=Button(
    button_frame,
    text='Open Your Gift',
    image=b_img,
    compound='right',
    font=("Segoe Print",20,'bold'),
    bg='#e31ea8',
    fg='white',
    pady=10,
    padx=20,
    relief=FLAT,
    command=hello
)
b1.pack(side='bottom',expand=True,fill=BOTH)

root.mainloop()

