# importing funtions
from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox, ttk
import matplotlib
matplotlib.use("TkAgg")  
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# creating global variable

current_mode = None     
edit_mode_active = False 
edit_entry = None   
file_path = "finalasset/assesment3/studentMarks.txt"
sort_descending = True

# loading file
 
try:
    with open(file_path, "r") as file:
        file_content = file.read()
except FileNotFoundError:
    file_content = "File not found!"

# creating all functions 

# for frame switch

def switch_to_frame(frame):
    frame.tkraise()

# for reading the .txt file

def read_sd():
    students = []
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            lines = f.readlines()
    except FileNotFoundError:
        return students

    for line in lines[1:]:
        parts = line.strip().split(",")
        if len(parts) >= 6:
            code, name, m1, m2, m3, exam = parts[:6]
            try:
                m1, m2, m3, exam = map(int, (m1, m2, m3, exam))
            except:
                continue
            total = m1 + m2 + m3 + exam
            percent = total / 160 * 100
            grade = "A" if percent >= 70 else "B" if percent >= 60 else "C" if percent >= 50 else "D" if percent >= 40 else "F"
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

# creating table for displying data

def create_table(students):
    table.delete(*table.get_children())
    for s in students:
        m1, m2, m3 = s["marks"]
        tag = "failed" if s["grade"] == "F" else ""
        table.insert(
            "",
            END,
            values=(s["code"], s["name"], m1, m2, m3, s["exam"], s["total"], f"{s['percent']:.2f}", s["grade"]),
            tags=(tag,)
        )
    update_changes(students)

# updating editing in data

def update_changes(students):
    total_students = len(students)
    avg_percent = sum(s["percent"] for s in students)/total_students if total_students else 0
    label_stats.config(text=f"Total Students: {total_students}    |    Class Average: {avg_percent:.2f}%")

# display all students in txt file

def display_all_sd():
    students = read_sd()
    create_table(students)
    switch_to_frame(frame3)

# shows student detail and chart when clicked

def show_sd_profile(event):
    selected = table.selection()
    if not selected:
        return
    row = selected[0]
    vals = table.item(row, "values")
    try:
        student_id = vals[0]
        student_name = vals[1]
        marks = list(map(int, vals[2:5]))
        exam = int(vals[5])
        total = int(vals[6])
        percent = float(vals[7])
        grade = vals[8]
    except:
        messagebox.showerror("Error","Invalid student data!")
        return
    
    profile_win = Toplevel(root)
    profile_win.title(f"Profile of - {student_name}")
    profile_win.geometry("300x600")
    profile_win.config(bg="#ffd04d")
    
    
    Label(profile_win, text=f"ID: {student_id}", font=("Arial",12),bg="#ffd04d").pack(pady=5)
    Label(profile_win, text=f"Name: {student_name}", font=("Arial",12),bg="#ffd04d").pack(pady=5)
    Label(profile_win, text=f"Maths: {marks[0]}" , font=("Arial",12),bg="#ffd04d").pack(pady=5)
    Label(profile_win, text=f"Science: {marks[1]}",  font=("Arial",12),bg="#ffd04d").pack(pady=5)
    Label(profile_win, text=f"Computer: {marks[2]}", font=("Arial",12),bg="#ffd04d").pack(pady=5)
    Label(profile_win, text=f"Exam: {exam}", font=("Arial",12),bg="#ffd04d").pack(pady=5)
    Label(profile_win, text=f"Total: {total}",font=("Arial",12,"bold"),bg="#ffd04d").pack(pady=5)
    Label(profile_win, text=f"Percentage: {percent:.2f}%",font=("Arial",12,"bold"),bg="#ffd04d").pack(pady=5)
    Label(profile_win, text=f"Grade: {grade}", font=("Arial",12,"bold"),bg="#ffd04d").pack(pady=5)

    fig = plt.Figure(figsize=(4,2.5),facecolor="#f8b90d")
    ax = fig.add_subplot(111)
    subjects = ['Maths','Sci','Com','Exam']
    scores = marks + [exam]
    ax.bar(subjects, scores, color=['#4CAF50','#2196F3','#FF9800','#9C27B0'])
    ax.set_ylim(0, 100)
    ax.set_title("Marks Breakdown")

    canvas = FigureCanvasTkAgg(fig, master=profile_win)
    canvas.get_tk_widget().pack(pady=10)
    canvas.draw()



# display highest grades student

def display_highest_sd():
    students = read_sd()
    if not students:
        create_table([])
        switch_to_frame(frame3)
        return
    max_score = max(s['total'] for s in students)
    top_students = [s for s in students if s['total']==max_score]
    create_table(top_students)
    switch_to_frame(frame3)

# display lowest grades students

def display_lowest_sd():
    students = read_sd()
    if not students:
        create_table([])
        switch_to_frame(frame3)
        return
    min_score = min(s['total'] for s in students)
    low_students = [s for s in students if s['total']==min_score]
    create_table(low_students)
    switch_to_frame(frame3)

# Search student by name

def search_for_sd_by_name():
    students = read_sd()
    name_to_search = search_entry.get().strip().lower()
    if not name_to_search:
        create_table([])
        switch_to_frame(frame3)
        return
    results = [s for s in students if name_to_search in s['name'].lower()]
    create_table(results)
    switch_to_frame(frame3)

def ready_search():
    search_entry.lift()
    search_entry.delete(0, END)
    create_table([])
    switch_to_frame(frame3)

def hide_search():
    search_entry.lower()

# sort student by percentage

def arrange_sd_by_percentage():
    global sort_descending
    students = read_sd()
    students.sort(key=lambda s: s['percent'], reverse=sort_descending)
    create_table(students)
    sort_descending = not sort_descending
    switch_to_frame(frame3)

# adding new student detail

def allow_add():
    global edit_mode_active, current_mode
    current_mode = "add"
    edit_mode_active = True
    table.insert("", END, values=("", "", "", "", "", "", "", "", ""))

    
    switch_to_frame(frame3)

# deleting an stduent detail from data

def delete_selected_row():
    global current_mode
    current_mode = "delete"
    selected = table.selection()
    if not selected:
        messagebox.showerror("Error","Select a row to delete.")
        return
    if not messagebox.askyesno("Confirm","Are you sure you want to delete the selected student(s)?"):
        return
    for row in selected:
        table.delete(row)


    save_button_sd()

# editing an existing student data

def allow_edit_mode():
    global current_mode, edit_mode_active
    current_mode = "edit"
    edit_mode_active = True

    load_for_editing()

# loading data for editing 

def load_for_editing():
    students = read_sd()
    create_table(students)

# making the table editable

def enable_table_editing():
    global edit_entry
    def on_click_cell(event):
        global edit_entry
        if not edit_mode_active:
            return
        region = table.identify("region", event.x, event.y)
        if region != "cell":
            return
        row_id = table.identify_row(event.y)
        column = table.identify_column(event.x)
        col_name = table.column(column, "id")

        if col_name not in ["id","name","m1","m2","m3","exam"]:
            return

        x,y,width,height = table.bbox(row_id,column)
        value = table.set(row_id,column)

        if edit_entry:
            try:
                old_row, old_col = edit_entry.row_id, edit_entry.col_name
                val = edit_entry.get().strip()
                if old_col in ["m1","m2","m3","exam"]:
                    val = int(val)
                table.set(old_row, old_col, val)
            except:
                pass
            edit_entry.destroy()
            edit_entry = None

        entry = Entry(table)
        entry.place(x=x, y=y, width=width, height=height)
        entry.insert(0, value)
        entry.focus()
        entry.row_id = row_id
        entry.col_name = col_name
        edit_entry = entry

        def save_edit(event=None):
            global edit_entry
            if not edit_entry:
                return
            new_val = edit_entry.get().strip()
            try:
                if col_name in ["m1","m2","m3","exam"]:
                    new_val_int = int(new_val)
                    if col_name != "exam" and (new_val_int < 0 or new_val_int > 20):
                        raise ValueError
                    if col_name=="exam" and (new_val_int <0 or new_val_int>100):
                        raise ValueError
                    table.set(row_id,column,new_val_int)
                else:
                    table.set(row_id,column,new_val)
            except ValueError:
                messagebox.showerror("Error","Invalid value.")
                return
            edit_entry.destroy()
            edit_entry = None

        entry.bind("<Return>", save_edit)
        entry.bind("<FocusOut>", save_edit)

    table.bind("<Button-1>", on_click_cell)

# blocking table from editing

def disable_editing():
    global edit_mode_active
    edit_mode_active = False

# save button for diffrent modes 

def save_button_sd():
    global current_mode, edit_mode_active, edit_entry

    if edit_entry:
        try:
            val = edit_entry.get().strip()
            if edit_entry.col_name in ["m1","m2","m3","exam"]:
                val = int(val)
            table.set(edit_entry.row_id, edit_entry.col_name, val)
        except:
            pass
        edit_entry.destroy()
        edit_entry = None

    rows = table.get_children()
    students = []

    for r in rows:
        vals = table.item(r, "values")
        
        if not all(vals[i] for i in range(6)):
            continue
        try:
            code = str(vals[0]).strip()
            name = str(vals[1]).strip()
            m1, m2, m3, exam = map(int, vals[2:6])
        except:
            continue

        total = m1 + m2 + m3 + exam
        percent = total / 160 * 100
        grade = "A" if percent >= 70 else "B" if percent >= 60 else "C" if percent >= 50 else "D" if percent >= 40 else "F"

        students.append({
            "code": code,
            "name": name,
            "marks": (m1, m2, m3),
            "exam": exam,
            "total": total,
            "percent": percent,
            "grade": grade
        })

    if not students:
        messagebox.showerror("Error", "No valid student data to save!")
        return

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(str(len(students)) + "\n")
        for s in students:
            m1_, m2_, m3_ = s["marks"]
            f.write(f"{s['code']},{s['name']},{m1_},{m2_},{m3_},{s['exam']}\n")

    create_table(students)   
    edit_mode_active = False    
    current_mode = None        

    messagebox.showinfo("Success", "Student data saved successfully!")

# updating the edited student detail 

def update_edited_sd():
    rows = table.get_children()
    updated_students = []
    for r in rows:
        vals = table.item(r,"values")
        try:
            code = str(vals[0])
            name = str(vals[1])
            m1 = int(vals[2])
            m2 = int(vals[3])
            m3 = int(vals[4])
            exam = int(vals[5])
        except:
            continue
        total = m1+m2+m3+exam
        percent = total/160*100
        grade = "A" if percent>=70 else "B" if percent>=60 else "C" if percent>=50 else "D" if percent>=40 else "F"
        updated_students.append({"code":code,"name":name,"marks":(m1,m2,m3),"exam":exam,"total":total,"percent":percent,"grade":grade})

    with open(file_path,"w",encoding="utf-8") as f:
        f.write(str(len(updated_students))+"\n")
        for s in updated_students:
            m1_,m2_,m3_ = s["marks"]
            f.write(f"{s['code']},{s['name']},{m1_},{m2_},{m3_},{s['exam']}\n")

    messagebox.showinfo("Success","Student data updated!")
    display_all_sd()

# creating window

root = Tk()
root.iconphoto(False, PhotoImage(file="finalasset/assesment3/logo.png"))
root.config(bg="#FFFFFF")
root.title("Student Data By Romila Faheem")
root.geometry('1900x1000')


# -----------------------------------------------frame 1--------------------------------------------------------

bg_image1 = Image.open("finalasset/assesment3/frame1.jpg")
bg_image1 = bg_image1.resize((1280, 650))
bg_photo1 = ImageTk.PhotoImage(bg_image1)

frame1 = Frame(root, width=1900, height=1000)
frame1.place(x=0, y=0)

bg_label1 = Label(frame1, image=bg_photo1)
bg_label1.place(x=0, y=0)

# button 1a

button_image1a = Image.open("finalasset/assesment3/button1a.jpg")
button_image1a = button_image1a.resize((120, 100))
button_photo1a = ImageTk.PhotoImage(button_image1a)

circle_button1a = Button(frame1, image=button_photo1a, borderwidth=0, highlightthickness=0,
                       bg=frame1["bg"], activebackground=frame1["bg"],
                       command=lambda: switch_to_frame(frame2))
circle_button1a.place(x=780, y=126)

# button 1b

img1b = Image.open("finalasset/assesment3/button1b.jpg")
img1b = img1b.resize((140, 200))
button_img1b = ImageTk.PhotoImage(img1b)

button1b = Button(frame1, image=button_img1b, borderwidth=0, highlightthickness=0,
                   command=lambda: switch_to_frame(frame4))
button1b.place(x=1029, y=380)

# -----------------------------------------------frame 2--------------------------------------------------------

frame2 = Frame(root, width=1900, height=1000, bg="#234567")
frame2.place(x=0, y=0)

bg_image2 = Image.open("finalasset/assesment3/frame2.jpg")
bg_image2 = bg_image2.resize((1280, 650))
bg_photo2 = ImageTk.PhotoImage(bg_image2)

bg_label2 = Label(frame2, image=bg_photo2)
bg_label2.place(x=0, y=0)

# button 2a

button_image2a = Image.open("finalasset/assesment3/button2a.jpg")
button_image2a = button_image2a.resize((120, 100))
button_photo2a = ImageTk.PhotoImage(button_image2a)

circle_button2a = Button(frame2, image=button_photo2a, borderwidth=0, highlightthickness=0,
                       bg=frame2["bg"], activebackground=frame2["bg"],
                       command=lambda: switch_to_frame(frame1))
circle_button2a.place(x=780, y=126)

# button 2b

img2b = Image.open("finalasset/assesment3/button2b.jpg")
img2b = img2b.resize((1005, 60))
button_img2b = ImageTk.PhotoImage(img2b)

button2b = Button(frame2, image=button_img2b, borderwidth=0, highlightthickness=0,
                   command=lambda: [hide_search(), display_all_sd()])
button2b.place(x=140, y=260)

# button 2c

img2c = Image.open("finalasset/assesment3/button2c.jpg")
img2c = img2c.resize((1005, 60))
button_img2c = ImageTk.PhotoImage(img2c)

button2c = Button(frame2, image=button_img2c, borderwidth=0, highlightthickness=0,
                   command=ready_search)
button2c.place(x=140, y=330)

# button 2d

img2d = Image.open("finalasset/assesment3/button2d.jpg")
img2d = img2d.resize((1005, 60))
button_img2d = ImageTk.PhotoImage(img2d)

button2d = Button(frame2, image=button_img2d, borderwidth=0, highlightthickness=0,
                   command=lambda: [hide_search(), display_highest_sd()])
button2d.place(x=140, y=400)

# button 2e

img2e = Image.open("finalasset/assesment3/button2e.jpg")
img2e = img2e.resize((1005, 60))
button_img2e = ImageTk.PhotoImage(img2e)

button2e = Button(frame2, image=button_img2e, borderwidth=0, highlightthickness=0,
                   command=lambda: [hide_search(), display_lowest_sd()])
button2e.place(x=140, y=470)

# -----------------------------------------------frame 3--------------------------------------------------------

frame3 = Frame(root, width=1900, height=1000, bg="#234567")
frame3.place(x=0, y=0)

bg_image3 = Image.open("finalasset/assesment3/frame3.jpg")
bg_image3 = bg_image3.resize((1280, 650))
bg_photo3 = ImageTk.PhotoImage(bg_image3)

bg_label3 = Label(frame3, image=bg_photo3)
bg_label3.place(x=0, y=0)

# styling table

style = ttk.Style()
style.theme_use("clam") 
style.configure("Treeview",
                background="#ffd04d",      
                foreground="black",        
                fieldbackground="#ffd04d") 


style.configure("Treeview.Heading",
                background="#f6be24",
                foreground="white",
                font=("Arial", 12, "bold"))
style.map("Treeview.Heading",
          background=[('active',"#f5da91")]) 

# creating table 

table = ttk.Treeview(frame3, columns=("id", "name", "m1", "m2", "m3", "exam", "total", "percent", "grade"), show="headings", height=8)

# creating header and coloums

table.heading("id", text="ID",anchor="w")
table.column("id", width=70,anchor="w")

table.heading("name", text="Name",anchor="w")
table.column("name", width=140,anchor="w")

table.heading("m1", text="Maths", anchor="center")
table.column("m1", width=50,anchor="center")

table.heading("m2", text="Science", anchor="center")
table.column("m2", width=50, anchor="center")

table.heading("m3", text="Computer", anchor="center")
table.column("m3", width=50, anchor="center")

table.heading("exam", text="Exam", anchor="center")
table.column("exam", width=60, anchor="center")

table.heading("total", text="Total", anchor="center")
table.column("total", width=60, anchor="center")

table.heading("percent", text="Percentage", anchor="center")
table.column("percent", width=60, anchor="center")

table.heading("grade", text="Grade", anchor="center")
table.column("grade", width=60, anchor="center")


table.place(x=290, y=160, width=680, height=200)

table_scroll = Scrollbar(frame3, orient="vertical", command=table.yview)
table.configure(yscrollcommand=table_scroll.set)
table_scroll.place(x=970, y=160, height=200)


table.tag_configure("failed", background="#FFCCCC") 
enable_table_editing()

table.bind("<Double-1>", show_sd_profile) 

# label for average student and  total numbers of students 

label_stats = Label(frame3, text="", font=("Arial", 13, "bold"), bg="#ffd04d", fg="white")
label_stats.place(x=290, y=360)

# search box 

search_entry = Entry(frame3, font=("Arial", 16))
search_entry.place(x=290, y=120, width=300, height=30)
search_entry.bind("<Return>", lambda event: search_for_sd_by_name())
search_entry.lower()

# button 3a

button_image3a = Image.open("finalasset/assesment3/button3a.jpg")
button_image3a = button_image3a.resize((46, 46))
button_photo3a = ImageTk.PhotoImage(button_image3a)

circle_button3a = Button(frame3, image=button_photo3a, borderwidth=0, highlightthickness=0,
                       bg=frame3["bg"], activebackground=frame3["bg"],
                       command=arrange_sd_by_percentage)
circle_button3a.place(x=750, y=110)

# button 3b

button_image3b = Image.open("finalasset/assesment3/button3b.jpg")
button_image3b = button_image3b.resize((46, 46))
button_photo3b = ImageTk.PhotoImage(button_image3b)

circle_button3b = Button(frame3, image=button_photo3b, borderwidth=0, highlightthickness=0,
                       bg=frame3["bg"], activebackground=frame3["bg"],
                       command=allow_add)
circle_button3b.place(x=811, y=110)

# button 3c

button_image3c = Image.open("finalasset/assesment3/button3c.jpg")
button_image3c = button_image3c.resize((46, 46))
button_photo3c = ImageTk.PhotoImage(button_image3c)

circle_button3c = Button(frame3, image=button_photo3c, borderwidth=0, highlightthickness=0,
                       bg=frame3["bg"], activebackground=frame3["bg"],
                       command=delete_selected_row)
circle_button3c.place(x=873, y=110)

# button 3d

button_image3d = Image.open("finalasset/assesment3/button3d.jpg")
button_image3d = button_image3d.resize((46, 46))
button_photo3d = ImageTk.PhotoImage(button_image3d)

circle_button3d = Button(frame3, image=button_photo3d, borderwidth=0, highlightthickness=0,
                       bg=frame3["bg"], activebackground=frame3["bg"],
                       command=lambda: [allow_edit_mode(), load_for_editing()])
circle_button3d.place(x=935, y=110)

# button 3e

img3e = Image.open("finalasset/assesment3/button3e.jpg")
img3e = img3e.resize((230, 60))
button_img3e = ImageTk.PhotoImage(img3e)

button3e = Button(frame3, image=button_img3e, borderwidth=0, highlightthickness=0,
                   command=lambda: [disable_editing(), switch_to_frame(frame2)])
button3e.place(x=328, y=460)

# button 3f

img3f = Image.open("finalasset/assesment3/button3f.jpg")
img3f = img3f.resize((230, 60))
button_img3f = ImageTk.PhotoImage(img3f)

button3f = Button(frame3, image=button_img3f, borderwidth=0, highlightthickness=0,
                   command=save_button_sd)
button3f.place(x=712, y=460)

# button 3g

img3g = Image.open("finalasset/assesment3/button3g.jpg")
img3g = img3g.resize((140, 200))
button_img3g = ImageTk.PhotoImage(img3g)

button3g = Button(frame3, image=button_img3g, borderwidth=0, highlightthickness=0,
                   command=lambda: switch_to_frame(frame4))
button3g.place(x=1029, y=380)

# -----------------------------------------------frame 4--------------------------------------------------------

frame4 = Frame(root, width=1900, height=1000, bg="#234567")
frame4.place(x=0, y=0)

bg_image4 = Image.open("finalasset/assesment3/frame4.jpg")
bg_image4 = bg_image4.resize((1280, 650))
bg_photo4 = ImageTk.PhotoImage(bg_image4)

bg_label4 = Label(frame4, image=bg_photo4)
bg_label4.place(x=0, y=0)

# button 4a

img4a = Image.open("finalasset/assesment3/button4a.jpg")
img4a = img4a.resize((220, 100))
button_img4a = ImageTk.PhotoImage(img4a)

button4a = Button(frame4, image=button_img4a, borderwidth=0, highlightthickness=0,
                   command=root.destroy)
button4a.place(x=330, y=384)

# button 4b

img4b = Image.open("finalasset/assesment3/button4b.jpg")
img4b = img4b.resize((220, 100))
button_img4b = ImageTk.PhotoImage(img4b)

button4b = Button(frame4, image=button_img4b, borderwidth=0, highlightthickness=0,
                   command=lambda: switch_to_frame(frame1))
button4b.place(x=693, y=384)

switch_to_frame(frame1)

root.mainloop()