#importing functions

from tkinter import *
from PIL import ImageTk, Image
import random
from tkinter import messagebox


# creating def

def switch_to_frame(frame):
    frame.tkraise()

# creating window

root = Tk()
root.config(bg="#FFFFFF")
root.title("Math Quiz By Romila Faheem")
root.geometry('1900x1000')


# -----------------------------------------------frame 1--------------------------------------------------------

bg_image1 = Image.open("frame1.jpg")  
bg_image1 = bg_image1.resize((1280, 650))   
bg_photo1 = ImageTk.PhotoImage(bg_image1)

frame1 = Frame(root,width=1900, height=1000)
frame1.place(x=0, y=0)


bg_label1 = Label(frame1, image=bg_photo1)
bg_label1.place(x=0, y=0 ) 

# button 1

button_image1 = Image.open("button1.png")   
button_image1 = button_image1.resize((180, 160))   
button_photo1 = ImageTk.PhotoImage(button_image1)

circle_button1 = Button(frame1, image=button_photo1, borderwidth=0, highlightthickness=0,
                       bg=frame1["bg"], activebackground=frame1["bg"],
                       command=lambda:switch_to_frame(frame2) )
circle_button1.place(x=550, y=455)

# -----------------------------------------------frame 2--------------------------------------------------------

frame2 = Frame(root, width=1900, height=1000, bg="#234567")
frame2.place(x=0, y=0)

bg_image2 = Image.open("frame2.jpg")   
bg_image2 = bg_image2.resize((1280, 650))    
bg_photo2 = ImageTk.PhotoImage(bg_image2)


bg_label2 = Label(frame2, image=bg_photo2)
bg_label2.place(x=0, y=0 )


# button 2a

button_image2a = Image.open("button2a.png")   
button_image2a = button_image2a.resize((89, 80))  
button_photo2a = ImageTk.PhotoImage(button_image2a)

circle_button2a = Button(frame2, image=button_photo2a, borderwidth=0, highlightthickness=0,
                       bg=frame2["bg"], activebackground=frame2["bg"],
                       command=lambda: switch_to_frame(frame1))
circle_button2a.place(x=285, y=285)

# button 2b

button_image2b = Image.open("button2b.png")  
button_image2b = button_image2b.resize((89, 80))  
button_photo2b = ImageTk.PhotoImage(button_image2b)

circle_button2b = Button(frame2, image=button_photo2b, borderwidth=0, highlightthickness=0,
                       bg=frame2["bg"], activebackground=frame2["bg"],
                       command=lambda: switch_to_frame(frame3))
circle_button2b.place(x=910, y=285)

# -----------------------------------------------frame 3--------------------------------------------------------

frame3 = Frame(root, width=1900, height=1000, bg="#234567")
frame3.place(x=0, y=0)

bg_image3 = Image.open("frame3.jpg")   
bg_image3 = bg_image3.resize((1280, 650))    
bg_photo3 = ImageTk.PhotoImage(bg_image3)


bg_label3 = Label(frame3, image=bg_photo3)
bg_label3.place(x=0, y=0 )

# button 3a

img3a = Image.open("button3a.png")   
img3a = img3a.resize((220, 200))           
button_img3a = ImageTk.PhotoImage(img3a)

button3a = Button(frame3, image=button_img3a, borderwidth=0,highlightthickness=0,
                   command=lambda : switch_to_frame(frame4))
button3a.place(x=350, y=225)


# button 3b

img3b = Image.open("button3b.png")  
img3b = img3b.resize((220, 200))           
button_img3b = ImageTk.PhotoImage(img3b)

button3b = Button(frame3, image=button_img3b, borderwidth=0,highlightthickness=0,
                   command=lambda : switch_to_frame(frame5))
button3b.place(x=713, y=225)


# -----------------------------------------------frame 4--------------------------------------------------------

frame4 = Frame(root, width=1900, height=1000, bg="#234567")
frame4.place(x=0, y=0)

bg_image4 = Image.open("frame4.jpg")  
bg_image4 = bg_image4.resize((1280, 650))    
bg_photo4 = ImageTk.PhotoImage(bg_image4)


bg_label4 = Label(frame4, image=bg_photo4)
bg_label4.place(x=0, y=0 )

# button 4a

img4a = Image.open("button4a.png")  
img4a = img4a.resize((680, 100))           
button_img4a = ImageTk.PhotoImage(img4a)

button4a = Button(frame4, image=button_img4a, borderwidth=0,highlightthickness=0,
                   command=lambda : start_test("add", 1))
button4a.place(x=300, y=232)

# button 4b

img4b = Image.open("button4b.png")   
img4b = img4b.resize((680, 100))           
button_img4b = ImageTk.PhotoImage(img4b)

button4b = Button(frame4, image=button_img4b, borderwidth=0,highlightthickness=0,
                   command=lambda : start_test("add", 2))
button4b.place(x=300, y=365)


# button 4c

img4c = Image.open("button4c.png")  
img4c = img4c.resize((680, 100))           
button_img4c = ImageTk.PhotoImage(img4c)

button4c = Button(frame4, image=button_img4c, borderwidth=0,highlightthickness=0,
                   command=lambda : start_test("add", 4))
button4c.place(x=300, y=495)

# -----------------------------------------------frame 5--------------------------------------------------------

frame5 = Frame(root, width=1900, height=1000, bg="#234567")
frame5.place(x=0, y=0)

bg_image5 = Image.open("frame5.jpg")   
bg_image5 = bg_image5.resize((1280, 650))   
bg_photo5 = ImageTk.PhotoImage(bg_image5)


bg_label5 = Label(frame5, image=bg_photo5)
bg_label5.place(x=0, y=0 )

# button 5a

img5a = Image.open("button5a.png")   
img5a = img5a.resize((680, 100))           
button_img5a = ImageTk.PhotoImage(img5a)

button5a = Button(frame5, image=button_img5a, borderwidth=0,highlightthickness=0,
                   command=lambda : start_test("subtract", 1))
button5a.place(x=300, y=232)

# button 5b

img5b = Image.open("button5b.png")   
img5b = img5b.resize((680, 100))         
button_img5b = ImageTk.PhotoImage(img5b)

button5b = Button(frame5, image=button_img5b, borderwidth=0,highlightthickness=0,
                   command=lambda : start_test("subtract", 2))
button5b.place(x=300, y=365)


# button 5c

img5c = Image.open("button5c.png")   
img5c = img5c.resize((680, 100))           
button_img5c = ImageTk.PhotoImage(img5c)

button5c = Button(frame5, image=button_img5c, borderwidth=0,highlightthickness=0,
                   command=lambda : start_test("subtract", 4))
button5c.place(x=300, y=495)


# -----------------------------------------------frame 6--------------------------------------------------------

frame6 = Frame(root, width=1900, height=1000, bg="#234567")
frame6.place(x=0, y=0)

bg_image6 = Image.open("frame6.jpg")   
bg_image6 = bg_image6.resize((1280, 650))   
bg_photo6 = ImageTk.PhotoImage(bg_image6)


bg_label6 = Label(frame6, image=bg_photo6)
bg_label6.place(x=0, y=0 )


test_mode = None
digit_count = None
level = 1
q_num = 0
marks = 0
attempt = 1
max_q = 10
q_ans = 0


def start_test(mode, digits):
    global test_mode, digit_count, level, q_num, marks, max_q
    test_mode = mode
    digit_count = digits
    level = 1
    q_num = 0
    marks = 0
    max_q = 10
    switch_to_frame(frame6)
    make_q()


def make_q():
    global q_ans, q_num, attempt

    attempt = 1
    q_num += 1
    counter_label.config(text=f"Question {q_num} / {max_q}")
    level_label.config(text=f"Level # {level}")

    n1 = random.randint(10**(digit_count-1), 10**digit_count - 1)
    n2 = random.randint(10**(digit_count-1), 10**digit_count - 1)

    if test_mode == "add":
        q_ans = n1 + n2
        symbol = "+"
    else:
        q_ans = n1 - n2
        symbol = "-"

    question_label.config(text=f"{n1} {symbol} {n2} = ?")
    feedback_label.config(text="")
    entry_ans.delete(0, END)

def check_ans():
    global marks, attempt, q_num, level, max_q

    try:
        ans = int(entry_ans.get())
    except ValueError:
        feedback_label.config(text="Enter a valid number!", fg="red")
        return

    if ans == q_ans:
        gained = 10 if attempt == 1 else 5
        marks += gained
        feedback_label.config(text=f"Correct! +{gained} points", fg="green")
        frame6.after(1000, next_q)
    else:
        if attempt == 1:
            attempt = 2
            feedback_label.config(text="Try again!", fg="red")
        else:
            feedback_label.config(text=f"Wrong! Answer: {q_ans}", fg="red")
            frame6.after(1500, next_q)

def next_q():
    global q_num, level, max_q, marks

    if q_num < max_q:
        make_q()
    else:
        if level == 1:
            switch_to_frame(frame7)
            summary_marks_label7.config(text=f"Level 1 Complete!\nScore so far: {marks}")
        elif level == 2:
            switch_to_frame(frame8)
            summary_marks_label8.config(text=f"Level 2 Complete!\nScore so far: {marks}")
        elif level == 3:
            show_final_summary()

def next_level():
    global level, q_num, max_q
    level += 1
    q_num = 0
    if level == 2:
        max_q = 15
    elif level == 3:
        max_q = 20
    switch_to_frame(frame6)
    make_q()


def show_final_summary():
    global marks
    switch_to_frame(frame9)
    final_score_label.config(text=f"Your Final Score: {marks}")

    if marks >= 90:
        grade = "A+"
    elif marks >= 80:
        grade = "A"
    elif marks >= 70:
        grade = "B"
    elif marks >= 60:
        grade = "C"
    else:
        grade = "F"

    grade_label.config(text=f"Your Grade: {grade}")


def show_summary():
    global marks, level

    switch_to_frame(frame7)
    summary_marks_label.config(text=f"Your Final Score: {marks}")
    level = 1

def retry_quiz():
    switch_to_frame(frame2)


question_label = Label(frame6, text="", font=("Arial", 28, "bold"), bg="#a8ba80")
question_label.place(x=640, y=289, width=155)

entry_ans = Entry(frame6, font=("Arial", 24), justify="center", bg="#a8ba80")
entry_ans.place(x=640, y=398, width=155)

feedback_label = Label(frame6, text="", font=("Arial", 15), bg="#8ea158")
feedback_label.place(x=641, y=350)

counter_label = Label(frame6, text="", font=("Arial", 40, "bold"), bg="#83d0fe")
counter_label.place(x=510, y=60)

level_label = Label(frame6, text="", font=("Arial", 20, "bold"), bg="#83d0fe")
level_label.place(x=650, y=130)


# button 6a

img6a = Image.open("button6a.png")  
img6a = img6a.resize((110, 100))          
button_img6a = ImageTk.PhotoImage(img6a)

button6a = Button(frame6, image=button_img6a, borderwidth=0,highlightthickness=0,
                   command=lambda : switch_to_frame(frame1))
button6a.place(x=360, y=461)


# button 6b

img6b = Image.open("button6b.png") 
img6b = img6b.resize((110, 100))           
button_img6b = ImageTk.PhotoImage(img6b)

button6b = Button(frame6, image=button_img6b, borderwidth=0,highlightthickness=0,
                    command=lambda: check_ans())
button6b.place(x=587, y=461)


# button 6c

img6c = Image.open("button6c.png")  
img6c = img6c.resize((110, 100))           
button_img6c = ImageTk.PhotoImage(img6c)

button6c = Button(frame6, image=button_img6c, borderwidth=0,highlightthickness=0,
                   command=lambda : switch_to_frame(frame10))
button6c.place(x=813, y=461)

# -----------------------------------------------frame 7--------------------------------------------------------

frame7 = Frame(root, width=1900, height=1000, bg="#234567")
frame7.place(x=0, y=0)

bg_image7 = Image.open("frame7.jpg")   
bg_image7 = bg_image7.resize((1280, 650))    
bg_photo7 = ImageTk.PhotoImage(bg_image7)


bg_label7 = Label(frame7, image=bg_photo7)
bg_label7.place(x=0, y=0 )

summary_marks_label7 = Label(frame7, text="", font=("Arial", 28), bg="#a41d2e", fg="#050505")
summary_marks_label7.place(x=510, y=250)

# button 7a

img7a = Image.open("button7a.png")   
img7a = img7a.resize((115, 119))          
button_img7a = ImageTk.PhotoImage(img7a)

button7a = Button(frame7, image=button_img7a, borderwidth=0,highlightthickness=0,
                   command=lambda : switch_to_frame(frame1))
button7a.place(x=369, y=370)


# button 7b

img7b = Image.open("button7b.png")  
img7b = img7b.resize((115, 119))           
button_img7b = ImageTk.PhotoImage(img7b)

button7b = Button(frame7, image=button_img7b, borderwidth=0,highlightthickness=0,
                    command=lambda: next_level())
button7b.place(x=584, y=370)


# button 7c

img7c = Image.open("button7c.png")   
img7c = img7c.resize((115, 119))           
button_img7c = ImageTk.PhotoImage(img7c)

button7c = Button(frame7, image=button_img7c, borderwidth=0,highlightthickness=0,
                   command=lambda : switch_to_frame(frame10))
button7c.place(x=800, y=370)

# -----------------------------------------------frame 8--------------------------------------------------------

frame8 = Frame(root, width=1900, height=1000, bg="#234567")
frame8.place(x=0, y=0)

bg_image8 = Image.open("frame8.jpg")  
bg_image8 = bg_image8.resize((1280, 650))    
bg_photo8 = ImageTk.PhotoImage(bg_image8)


bg_label8 = Label(frame8, image=bg_photo8)
bg_label8.place(x=0, y=0 )

summary_marks_label8 = Label(frame8, text="", font=("Arial", 28), bg="#a41d2e", fg="#060606")
summary_marks_label8.place(x=510, y=250)

# button 8a

img8a = Image.open("button8a.png")   
img8a = img8a.resize((115, 119))           
button_img8a = ImageTk.PhotoImage(img8a)

button8a = Button(frame8, image=button_img8a, borderwidth=0,highlightthickness=0,
                   command=lambda : switch_to_frame(frame1))
button8a.place(x=369, y=370)


# button 8b

img8b = Image.open("button8b.png")  
img8b = img8b.resize((115, 119))           
button_img8b = ImageTk.PhotoImage(img8b)

button8b = Button(frame8, image=button_img8b, borderwidth=0,highlightthickness=0,
                    command=lambda: next_level())
button8b.place(x=584, y=370)


# button 8c

img8c = Image.open("button8c.png") 
img8c = img8c.resize((115, 119))          
button_img8c = ImageTk.PhotoImage(img8c)

button8c = Button(frame8, image=button_img8c, borderwidth=0,highlightthickness=0,
                   command=lambda : switch_to_frame(frame10))
button8c.place(x=800, y=370)


# -----------------------------------------------frame 9--------------------------------------------------------


frame9 = Frame(root, width=1900, height=1000, bg="#234567")
frame9.place(x=0, y=0)

bg_image9 = Image.open("frame9.jpg")   
bg_image9 = bg_image9.resize((1280, 650))    
bg_photo9 = ImageTk.PhotoImage(bg_image9)


bg_label9 = Label(frame9, image=bg_photo9)
bg_label9.place(x=0, y=0 )

summary_marks_label = Label(frame9, text="", font=("Arial", 20), bg="#a41d2e", fg="#070707")
summary_marks_label.place(x=510, y=220)

final_score_label = Label(frame9, text="", font=("Arial", 22, "bold"), bg="#a41d2e", fg="#080808")
final_score_label.place(x=510, y=270)

grade_label = Label(frame9, text="", font=("Arial", 20, "bold"), bg="#a41d2e", fg="#030303")
grade_label.place(x=510, y=320)

# button 9a

img9a = Image.open("button9a.jpg") 
img9a = img9a.resize((115, 119))           
button_img9a = ImageTk.PhotoImage(img9a)

button9a = Button(frame9, image=button_img9a, borderwidth=0,highlightthickness=0,
                   command=lambda : switch_to_frame(frame1))
button9a.place(x=448, y=370)


# button 9b

img9b = Image.open("button9b.jpg")   
img9b = img9b.resize((115, 119))           
button_img9b = ImageTk.PhotoImage(img9b)

button9b = Button(frame9, image=button_img9b, borderwidth=0,highlightthickness=0,
                    command=lambda: switch_to_frame(frame10))
button9b.place(x=724, y=370)

# -----------------------------------------------frame 10--------------------------------------------------------


frame10 = Frame(root, width=1900, height=1000, bg="#234567")
frame10.place(x=0, y=0)

bg_image10 = Image.open("frame10.jpg")   
bg_image10 = bg_image10.resize((1280, 650))    
bg_photo10 = ImageTk.PhotoImage(bg_image10)


bg_label10 = Label(frame10, image=bg_photo10)
bg_label10.place(x=0, y=0 )

# button 10a

img10a = Image.open("button10a.jpg")   
img10a = img10a.resize((185, 119))           
button_img10a = ImageTk.PhotoImage(img10a)

button10a = Button(frame10, image=button_img10a, borderwidth=0,highlightthickness=0,
                   command=lambda : switch_to_frame(frame1))
button10a.place(x=377, y=384)


# button 10b

img10b = Image.open("button10b.jpg") 
img10b = img10b.resize((179, 116))           
button_img10b = ImageTk.PhotoImage(img10b)

button10b = Button(frame10, image=button_img10b, borderwidth=0,highlightthickness=0,
                    command= root.destroy)
button10b.place(x=764, y=383)



switch_to_frame(frame1)


root.mainloop()
