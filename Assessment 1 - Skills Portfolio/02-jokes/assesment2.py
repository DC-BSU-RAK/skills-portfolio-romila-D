#importing functions

from tkinter import *
from PIL import ImageTk, Image
import random
import pygame

#

with open("Assessment 1 - Skills Portfolio/02-jokes/randomjokes.txt", "r", encoding="utf-8") as f:
    jokes = [line.strip() for line in f.readlines() if "?" in line]

current_setup = ""     
current_punchline = "" 


# creating functions

def switch_to_frame(frame):
    frame.tkraise()

def pick_joke():
    global current_setup, current_punchline
    joke = random.choice(jokes)
    parts = joke.split("?")
    current_setup = parts[0].strip()
    current_punchline = parts[1].strip()

def show_setup():
    pick_joke()
    joke_label.config(text=current_setup + "?")  # add question mark
    punchline_label.config(text="") 

def show_punchline():
    if current_punchline:
        punchline_label.config(text=current_punchline)
    else:
        punchline_label.config(text="Please click the  button first.")


def next_joke():
    show_setup()


def end_game():
    a5.play()
    root.after(500, root.destroy)



# creating window

root = Tk()
root.config(bg="#FFFFFF")
root.title("Random Jokes By Romila Faheem")
root.geometry('1900x1000')

# ------------------------------------------------ AUDIO SETUP ------------------------------------------------

pygame.mixer.init()

# background music
pygame.mixer.music.load("Assessment 1 - Skills Portfolio/02-jokes/zbackground.mp3") 
pygame.mixer.music.play(-1)  

# buttons sounds

a1 = pygame.mixer.Sound("Assessment 1 - Skills Portfolio/02-jokes/zpounch.mp3") 
a2 = pygame.mixer.Sound("Assessment 1 - Skills Portfolio/02-jokes/zexit.mp3")    
a3 = pygame.mixer.Sound("Assessment 1 - Skills Portfolio/02-jokes/zclick.mp3")   
a4 = pygame.mixer.Sound("Assessment 1 - Skills Portfolio/02-jokes/zpunch.mp3")  
a5 = pygame.mixer.Sound("Assessment 1 - Skills Portfolio/02-jokes/zbye.mp3")  




# -----------------------------------------------frame 1--------------------------------------------------------

bg_image1 = Image.open("Assessment 1 - Skills Portfolio/02-jokes/frame1.jpg")  
bg_image1 = bg_image1.resize((1280, 650))   
bg_photo1 = ImageTk.PhotoImage(bg_image1)

frame1 = Frame(root,width=1900, height=1000)
frame1.place(x=0, y=0)


bg_label1 = Label(frame1, image=bg_photo1)
bg_label1.place(x=0, y=0 )

# button 1

img1 = Image.open("Assessment 1 - Skills Portfolio/02-jokes/button1.jpg")   
img1 = img1.resize((66, 90))           
button_img1 = ImageTk.PhotoImage(img1)

button1 = Button(frame1, image=button_img1, borderwidth=0,highlightthickness=0,
                   command=lambda : (a1.play(), switch_to_frame(frame2)))
button1.place(x=152, y=216)

# -----------------------------------------------frame 2--------------------------------------------------------

bg_image2 = Image.open("Assessment 1 - Skills Portfolio/02-jokes/frame2.jpg")  
bg_image2 = bg_image2.resize((1280, 650))   
bg_photo2 = ImageTk.PhotoImage(bg_image2)

frame2 = Frame(root,width=1900, height=1000)
frame2.place(x=0, y=0)


bg_label2 = Label(frame2, image=bg_photo2)
bg_label2.place(x=0, y=0 )

# LABEL to show joke text
joke_label = Label(frame2, text="", bg="#e4e0d5", fg="black",
                   font=("Arial", 20), wraplength=360, justify="left")
joke_label.place(x=460, y=100)   # <<< You can move this position as needed

punchline_label = Label(frame2, text="", bg="#e4e0d5", fg="black",
                        font=("Arial", 18), wraplength=360, justify="left")
punchline_label.place(x=460, y=200)


# button 2a

img2a = Image.open("Assessment 1 - Skills Portfolio/02-jokes/button2a.jpg")   
img2a = img2a.resize((66, 90))           
button_img2a = ImageTk.PhotoImage(img2a)

button2a = Button(frame2, image=button_img2a, borderwidth=0,highlightthickness=0,
                   command=lambda : (a2.play(),switch_to_frame(frame3)) )
button2a.place(x=152, y=216)

# button 2b

img2b = Image.open("Assessment 1 - Skills Portfolio/02-jokes/button2b.jpg")   
img2b = img2b.resize((100, 139))           
button_img2b = ImageTk.PhotoImage(img2b)

button2b = Button(frame2, image=button_img2b, borderwidth=0,highlightthickness=0,
                   command=lambda: (a3.play(), show_setup()))
button2b.place(x=408, y=482)

# button 2c

img2c = Image.open("Assessment 1 - Skills Portfolio/02-jokes/button2c.jpg")   
img2c = img2c.resize((102, 139))           
button_img2c = ImageTk.PhotoImage(img2c)

button2c = Button(frame2, image=button_img2c, borderwidth=0,highlightthickness=0,
                   command=lambda: (a4.play(), show_punchline()))
button2c.place(x=591, y=482)

# button 2d

img2d = Image.open("Assessment 1 - Skills Portfolio/02-jokes/button2d.jpg")   
img2d = img2d.resize((102, 138))           
button_img2d = ImageTk.PhotoImage(img2d)

button2d = Button(frame2, image=button_img2d, borderwidth=0,highlightthickness=0,
                   command=lambda: (a3.play(), next_joke()))
button2d.place(x=775, y=482)

# -----------------------------------------------frame 3--------------------------------------------------------

bg_image3 = Image.open("Assessment 1 - Skills Portfolio/02-jokes/frame3.jpg")  
bg_image3 = bg_image3.resize((1280, 650))   
bg_photo3 = ImageTk.PhotoImage(bg_image3)

frame3 = Frame(root,width=1900, height=1000)
frame3.place(x=0, y=0)


bg_label3 = Label(frame3, image=bg_photo3)
bg_label3.place(x=0, y=0 )

# button 3a

img3a = Image.open("Assessment 1 - Skills Portfolio/02-jokes/button3a.jpg")   
img3a = img3a.resize((180, 143))           
button_img3a = ImageTk.PhotoImage(img3a)

button3a = Button(frame3, image=button_img3a, borderwidth=0,highlightthickness=0,
                   command= end_game)
button3a.place(x=403, y=360)

# button 3b

img3b = Image.open("Assessment 1 - Skills Portfolio/02-jokes/button3b.jpg")   
img3b = img3b.resize((180, 143))           
button_img3b = ImageTk.PhotoImage(img3b)

button3b = Button(frame3, image=button_img3b, borderwidth=0,highlightthickness=0,
                   command=lambda : (a1.play(),switch_to_frame(frame1)))
button3b.place(x=710, y=360)


switch_to_frame(frame1)


root.mainloop()


