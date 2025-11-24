#importing functions

from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox


# Read from the txt file

file_path = "finalasset/assesment3/studentMarks.txt" 
try:
    with open(file_path, "r") as file:
        file_content = file.read()
except FileNotFoundError:
    file_content = "File not found!"

# Creating def for all the functions

# Creating frame switch

def switch_to_frame(frame):
    frame.tkraise()

# To block user to edit in text box

def enable_edit():
    text_box.config(state=NORMAL)

# Read data from file 

def read_student_data():
    students = []
    with open(file_path, "r") as file:
        lines = file.readlines()
        for line in lines[1:]:  
            parts = line.strip().split(",")
            if len(parts) >= 6:
                code, name, m1, m2, m3, exam = parts[:6]
                m1, m2, m3, exam = map(int, (m1, m2, m3, exam))
                total = m1 + m2 + m3 + exam
                percent = total / 160 * 100
                if percent >= 70:
                    grade = "A"
                elif percent >= 60:
                    grade = "B"
                elif percent >= 50:
                    grade = "C"
                elif percent >= 40:
                    grade = "D"
                else:
                    grade = "F"
                students.append({
                    "code": code,
                    "name": name,
                    "marks": (m1, m2, m3),
                    "exam": exam,
                    "total": total,
                    "percent": percent,
                    "grade": grade
                })
    return students

# Show all students

def show_all_students():
    students = read_student_data()
    text_box.config(state=NORMAL)
    text_box.delete("1.0", END)
    for s in students:
        marks_str = ", ".join(f"{m}/20" for m in s['marks'])
        text_box.insert(END, f"Student Id: {s['code']} \nName: {s['name']} \nTest Result: {marks_str} \nFinal Exam: {s['exam']}/100 \nTotal Marks: {s['total']}/160 \nFinal Percentage: {s['percent']:.2f}% \nAcheived Grade: {s['grade']}\n\n")
    text_box.config(state=DISABLED)
    switch_to_frame(frame3)

# Show high grade

def show_highest_student():
    students = read_student_data()
    if not students:
        return
    max_score = max(s['total'] for s in students)
    top_students = [s for s in students if s['total'] == max_score]
    text_box.config(state=NORMAL)
    text_box.delete("1.0", END)
    for s in top_students:
        marks_str = ", ".join(f"{m}/20" for m in s['marks'])
        text_box.insert(END, f"Student Id: {s['code']} \nName: {s['name']} \nTest Result: {marks_str} \nFinal Exam: {s['exam']}/100 \nTotal Marks: {s['total']}/160 \nFinal Percentage: {s['percent']:.2f}% \nAcheived Grade: {s['grade']}\n\n")
    text_box.config(state=DISABLED)
    switch_to_frame(frame3)

# Show low grade 

def show_lowest_student():
    students = read_student_data()
    if not students:
        return
    min_score = min(s['total'] for s in students)
    low_students = [s for s in students if s['total'] == min_score]
    text_box.config(state=NORMAL)
    text_box.delete("1.0", END)
    for s in low_students:
        marks_str = ", ".join(f"{m}/20" for m in s['marks'])
        text_box.insert(END, f"Student Id: {s['code']} \nName: {s['name']} \nTest Result: {marks_str} \nFinal Exam: {s['exam']}/100 \nTotal Marks: {s['total']}/160 \nFinal Percentage: {s['percent']:.2f}% \nAcheived Grade: {s['grade']}\n\n")
    text_box.config(state=DISABLED)
    switch_to_frame(frame3)

# Search student by name
def search_student_by_name():
    students = read_student_data()
    name_to_search = search_entry.get().strip().lower()
    results = [s for s in students if s['name'].lower() == name_to_search]
    text_box.config(state=NORMAL)
    text_box.delete("1.0", END)
    if results:
        for s in results:
            marks_str = ", ".join(f"{m}/20" for m in s['marks'])
            text_box.insert(END, f"Student Id: {s['code']} \nName: {s['name']} \nTest Result: {marks_str} \nFinal Exam: {s['exam']}/100 \nTotal Marks: {s['total']}/160 \nFinal Percentage: {s['percent']:.2f}% \nAcheived Grade: {s['grade']}\n\n")
    else:
        text_box.insert(END, f"No student found with name: {name_to_search}")
    text_box.config(state=DISABLED)
    switch_to_frame(frame3)


def prepare_search():
    search_entry.lift() 
    search_entry.delete(0, END)
    text_box.config(state=NORMAL)
    text_box.delete("1.0", END)
    text_box.config(state=DISABLED)
    switch_to_frame(frame3)


def hide_search_entry():
    search_entry.lower()  


def sort_students_by_percentage():
    global sort_descending
    students = read_student_data()
    students.sort(key=lambda s: s['percent'], reverse=sort_descending)
    text_box.config(state=NORMAL)
    text_box.delete("1.0", END)
    for s in students:
        marks_str = ", ".join(f"{m}/20" for m in s['marks'])
        text_box.insert(END, f"Student Id: {s['code']} \nName: {s['name']} \nTest Result: {marks_str} \nFinal Exam: {s['exam']}/100 \nTotal Marks: {s['total']}/160 \nFinal Percentage: {s['percent']:.2f}% \nAcheived Grade: {s['grade']}\n\n")
    text_box.config(state=DISABLED)
    switch_to_frame(frame3)
    
    sort_descending = not sort_descending  


def enable_add_in_textbox():
    global current_mode
    current_mode = "add"

    text_box.config(state=NORMAL)
    text_box.delete("1.0", END)

    text_box.insert(END,
        "Student Id: \n"
        "Name: \n"
        "Test Result (comma separated, each /20): \n"
        "Final Exam (/100): \n"
        "Total Marks: (AUTO)\n"
        "Final Percentage: (AUTO)\n"
        "Achieved Grade: (AUTO)\n"
    )

    text_box.config(state=NORMAL)
    switch_to_frame(frame3)


def enable_delete_mode():
    global current_mode
    current_mode = "delete"

    students = read_student_data()
    text_box.config(state=NORMAL)
    text_box.delete("1.0", END)

    text_box.insert(END, "Enter Student ID to delete: \n\n")
    text_box.insert(END, "================ CURRENT STUDENTS ================\n\n")

    for s in students:
        text_box.insert(END,
            f"Student Id: {s['code']}\n"
            f"Name: {s['name']}\n"
            f"Test Marks: {s['marks']}\n"
            f"Final Exam: {s['exam']}/100\n"
            f"Total: {s['total']}/160\n"
            f"Percent: {s['percent']:.2f}%\n"
            f"Grade: {s['grade']}\n"
            f"----------------------------------------\n\n"
        )

    text_box.config(state=NORMAL)
    switch_to_frame(frame3)


def save_new_student():
    content = text_box.get("1.0", END).strip().split("\n")
    try:
        code = content[0].split(":")[1].strip()
        name = content[1].split(":")[1].strip()
        marks_list = [int(x.strip()) for x in content[2].split(":")[1].split(",")]
        exam = int(content[3].split(":")[1].strip())

        
        total = sum(marks_list) + exam
        percent = total / 160 * 100
        grade = ("A" if percent >= 70 else
                 "B" if percent >= 60 else
                 "C" if percent >= 50 else
                 "D" if percent >= 40 else "F")

       
        with open(file_path, "a") as file:
            file.write(f"{code},{name},{','.join(map(str, marks_list))},{exam}\n")

        messagebox.showinfo("Saved", "New student added successfully!")
        show_all_students()

    except Exception as e:
        messagebox.showerror("Error", f"Failed to save data.\n{e}")


def save_after_delete():
    lines = text_box.get("1.0", END).strip().split("\n")

    try:
        delete_id = lines[0].split(":")[1].strip()

        if delete_id == "":
            messagebox.showerror("Error", "Please enter a Student ID to delete.")
            return

        students = read_student_data()
        updated_students = [s for s in students if s['code'] != delete_id]

        if len(updated_students) == len(students):
            messagebox.showinfo("Not found", "No student found with that ID.")
            return

        
        with open(file_path, "w") as file:
            file.write(str(len(updated_students)) + "\n")
            for s in updated_students:
                m1, m2, m3 = s['marks']
                file.write(f"{s['code']},{s['name']},{m1},{m2},{m3},{s['exam']}\n")

        messagebox.showinfo("Deleted", "Student deleted successfully!")
        show_all_students()

    except Exception as e:
        messagebox.showerror("Error", f"Something went wrong.\n{e}")

def load_for_editing():
    text_box.config(state=NORMAL)  
    text_box.delete("1.0", END)

    students = read_student_data() 

    for s in students:
        
        marks_str = ", ".join(str(m) for m in s['marks'])

        
        text_box.insert(END,
            f"Student Id: {s['code']}\n"
            f"Name: {s['name']}\n"
            f"Test Result: {marks_str}\n"
            f"Final Exam: {s['exam']}/100\n"
            f"Total Marks: {s['total']}/160\n"
            f"Final Percentage: {s['percent']:.2f}%\n"
            f"Acheived Grade: {s['grade']}\n\n"
        )

    text_box.focus()  

def save_edited_list():
    content = text_box.get("1.0", END).strip().split("\n\n")  
    updated_students = []

    for block in content:
        lines = block.split("\n")
        if len(lines) < 4:
            continue

        try:
            student_id = lines[0].split(":")[1].strip()
            name = lines[1].split(":")[1].strip()
            marks_list = [int(x.strip()) for x in lines[2].split(":")[1].split(",")]
            exam = int(lines[3].split(":")[1].replace("/100","").strip())

            total = sum(marks_list) + exam
            percent = total / 160 * 100
            grade = ("A" if percent >= 70 else
                     "B" if percent >= 60 else
                     "C" if percent >= 50 else
                     "D" if percent >= 40 else "F")

            updated_students.append({
                "code": student_id,
                "name": name,
                "marks": marks_list,
                "exam": exam,
                "total": total,
                "percent": percent,
                "grade": grade
            })

        except Exception as e:
            messagebox.showerror("Error", f"Invalid format in block:\n{block}\n{e}")
            return

    
    with open(file_path, "w") as f:
        f.write(f"{len(updated_students)}\n")
        for s in updated_students:
            f.write(f"{s['code']},{s['name']},{','.join(map(str,s['marks']))},{s['exam']}\n")

    messagebox.showinfo("Success", "Student data updated!")
    show_all_students()  

def set_edit_mode():
    global current_mode
    current_mode = "edit"


def save_button_pressed():
    global current_mode

    if current_mode == "add":
        save_new_student()
    elif current_mode == "delete":
        save_after_delete()
    elif current_mode == "edit":
        save_edited_list()
    else:
        messagebox.showerror("Error", "No action selected (Add or Delete).")




# creating window

root = Tk()
root.iconphoto(False, PhotoImage(file="finalasset/assesment3/logo.png"))
root.config(bg="#FFFFFF")
root.title("Student Data By Romila Faheem")
root.geometry('1900x1000')

sort_descending = True 
current_mode = None


# -----------------------------------------------frame 1--------------------------------------------------------

bg_image1 = Image.open("finalasset/assesment3/frame1.jpg")  
bg_image1 = bg_image1.resize((1280, 650))   
bg_photo1 = ImageTk.PhotoImage(bg_image1)

frame1 = Frame(root,width=1900, height=1000)
frame1.place(x=0, y=0)


bg_label1 = Label(frame1, image=bg_photo1)
bg_label1.place(x=0, y=0 )

# button 1a

button_image1a = Image.open("finalasset/assesment3/button1a.jpg")   
button_image1a = button_image1a.resize((120, 100))   
button_photo1a = ImageTk.PhotoImage(button_image1a)

circle_button1a = Button(frame1, image=button_photo1a, borderwidth=0, highlightthickness=0,
                       bg=frame1["bg"], activebackground=frame1["bg"],
                       command=lambda:switch_to_frame(frame2) )
circle_button1a.place(x=780, y=126)

# button 1b

img1b = Image.open("finalasset/assesment3/button1b.jpg")   
img1b = img1b.resize((140, 200))           
button_img1b = ImageTk.PhotoImage(img1b)

button1b = Button(frame1, image=button_img1b, borderwidth=0,highlightthickness=0,
                   command=lambda : switch_to_frame(frame4))
button1b.place(x=1029, y=380)


# -----------------------------------------------frame 2--------------------------------------------------------

frame2 = Frame(root, width=1900, height=1000, bg="#234567")
frame2.place(x=0, y=0)

bg_image2 = Image.open("finalasset/assesment3/frame2.jpg")   
bg_image2 = bg_image2.resize((1280, 650))    
bg_photo2 = ImageTk.PhotoImage(bg_image2)


bg_label2 = Label(frame2, image=bg_photo2)
bg_label2.place(x=0, y=0 )

# button 2a

button_image2a = Image.open("finalasset/assesment3/button2a.jpg")   
button_image2a = button_image2a.resize((120, 100))   
button_photo2a = ImageTk.PhotoImage(button_image2a)

circle_button2a = Button(frame2, image=button_photo2a, borderwidth=0, highlightthickness=0,
                       bg=frame2["bg"], activebackground=frame2["bg"],
                       command=lambda:switch_to_frame(frame1) )
circle_button2a.place(x=780, y=126)

# button 2b

img2b = Image.open("finalasset/assesment3/button2b.jpg")   
img2b = img2b.resize((1005, 60))           
button_img2b = ImageTk.PhotoImage(img2b)

button2b = Button(frame2, image=button_img2b, borderwidth=0,highlightthickness=0,
                   command=lambda: [hide_search_entry(), show_all_students()])
button2b.place(x=140, y=260)

# button 2c

img2c = Image.open("finalasset/assesment3/button2c.jpg")   
img2c = img2c.resize((1005, 60))           
button_img2c = ImageTk.PhotoImage(img2c)

button2c = Button(frame2, image=button_img2c, borderwidth=0,highlightthickness=0,
                   command= prepare_search)
button2c.place(x=140, y=330)

# button 2d

img2d = Image.open("finalasset/assesment3/button2d.jpg")   
img2d = img2d.resize((1005, 60))           
button_img2d = ImageTk.PhotoImage(img2d)

button2d = Button(frame2, image=button_img2d, borderwidth=0,highlightthickness=0,
                   command=lambda: [hide_search_entry(), show_highest_student()])
button2d.place(x=140, y=400)

# button 2e

img2e = Image.open("finalasset/assesment3/button2e.jpg")   
img2e = img2e.resize((1005, 60))           
button_img2e = ImageTk.PhotoImage(img2e)

button2e = Button(frame2, image=button_img2e, borderwidth=0,highlightthickness=0,
                   command=lambda: [hide_search_entry(), show_lowest_student()])
button2e.place(x=140, y=470)

# -----------------------------------------------frame 3--------------------------------------------------------

frame3 = Frame(root, width=1900, height=1000, bg="#234567")
frame3.place(x=0, y=0)

bg_image3 = Image.open("finalasset/assesment3/frame3.jpg")   
bg_image3 = bg_image3.resize((1280, 650))    
bg_photo3 = ImageTk.PhotoImage(bg_image3)


bg_label3 = Label(frame3, image=bg_photo3)
bg_label3.place(x=0, y=0 )

# Scrollbar for the text box

scrollbar = Scrollbar(frame3, bg= "#ffd04d")
scrollbar.place(x=290 + 680, y=160, height=200)   

# Text box to replace the label

text_box = Text(frame3,font=("Arial", 15),bg="#ffd04d",fg="black",wrap="word",width=40,height=8,borderwidth=0,highlightthickness=0,yscrollcommand=scrollbar.set) 
text_box.place(x=290, y=160, width=680, height=200)

# Initially disable editing

text_box.config(state=DISABLED)

# Connect scrollbar to text box

scrollbar.config(command=text_box.yview)


# Insert initial text

text_box.insert(END, file_content)

search_entry = Entry(frame3, font=("Arial", 16))
search_entry.place(x=290, y=120, width=300, height=30)
search_entry.bind("<Return>", lambda event: search_student_by_name())
search_entry.lower()  

# button 3a

button_image3a = Image.open("finalasset/assesment3/button3a.jpg")   
button_image3a = button_image3a.resize((46, 46))   
button_photo3a = ImageTk.PhotoImage(button_image3a)

circle_button3a = Button(frame3, image=button_photo3a, borderwidth=0, highlightthickness=0,
                       bg=frame3["bg"], activebackground=frame3["bg"],
                       command= sort_students_by_percentage)
circle_button3a.place(x=750, y=110)

# button 3b

button_image3b = Image.open("finalasset/assesment3/button3b.jpg")   
button_image3b = button_image3b.resize((46, 46))   
button_photo3b = ImageTk.PhotoImage(button_image3b)

circle_button3b = Button(frame3, image=button_photo3b, borderwidth=0, highlightthickness=0,
                       bg=frame3["bg"], activebackground=frame3["bg"],
                       command= enable_add_in_textbox)
circle_button3b.place(x=811, y=110)

# button 3c

button_image3c = Image.open("finalasset/assesment3/button3c.jpg")   
button_image3c = button_image3c.resize((46, 46))   
button_photo3c = ImageTk.PhotoImage(button_image3c)

circle_button3c = Button(frame3, image=button_photo3c, borderwidth=0, highlightthickness=0,
                       bg=frame3["bg"], activebackground=frame3["bg"],
                       command= enable_delete_mode )
circle_button3c.place(x=873, y=110)

# button 3d

button_image3d = Image.open("finalasset/assesment3/button3d.jpg")   
button_image3d = button_image3d.resize((46, 46))   
button_photo3d = ImageTk.PhotoImage(button_image3d)

circle_button3d = Button(frame3, image=button_photo3d, borderwidth=0, highlightthickness=0,
                       bg=frame3["bg"], activebackground=frame3["bg"],
                       command=lambda: [set_edit_mode(), load_for_editing()])
circle_button3d.place(x=935, y=110)

# button 3e

img3e = Image.open("finalasset/assesment3/button3e.jpg")   
img3e = img3e.resize((230, 60))           
button_img3e = ImageTk.PhotoImage(img3e)

button3e = Button(frame3, image=button_img3e, borderwidth=0,highlightthickness=0,
                   command=lambda : switch_to_frame(frame2))
button3e.place(x=328, y=460)

# button 3f

img3f = Image.open("finalasset/assesment3/button3f.jpg")   
img3f = img3f.resize((230, 60))           
button_img3f = ImageTk.PhotoImage(img3f)

button3f = Button(frame3, image=button_img3f, borderwidth=0,highlightthickness=0,
                   command= save_button_pressed)
button3f.place(x=712, y=460)

# button 3g

img3g = Image.open("finalasset/assesment3/button3g.jpg")   
img3g = img3g.resize((140, 200))           
button_img3g = ImageTk.PhotoImage(img3g)

button3g = Button(frame3, image=button_img3g, borderwidth=0,highlightthickness=0,
                   command=lambda: switch_to_frame(frame4))
button3g.place(x=1029, y=380)

# -----------------------------------------------frame 4--------------------------------------------------------

frame4 = Frame(root, width=1900, height=1000, bg="#234567")
frame4.place(x=0, y=0)

bg_image4 = Image.open("finalasset/assesment3/frame4.jpg")   
bg_image4 = bg_image4.resize((1280, 650))    
bg_photo4 = ImageTk.PhotoImage(bg_image4)


bg_label4 = Label(frame4, image=bg_photo4)
bg_label4.place(x=0, y=0 )

# button 4a

img4a = Image.open("finalasset/assesment3/button4a.jpg")   
img4a = img4a.resize((220, 100))           
button_img4a = ImageTk.PhotoImage(img4a)

button4a = Button(frame4, image=button_img4a, borderwidth=0,highlightthickness=0,
                   command= root.destroy)
button4a.place(x=330, y=384)

# button 4b

img4b = Image.open("finalasset/assesment3/button4b.jpg")   
img4b = img4b.resize((220, 100))           
button_img4b = ImageTk.PhotoImage(img4b)

button4b = Button(frame4, image=button_img4b, borderwidth=0,highlightthickness=0,
                   command=lambda : switch_to_frame(frame1))
button4b.place(x=693, y=384)




switch_to_frame(frame1)


root.mainloop()