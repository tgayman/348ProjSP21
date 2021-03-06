import tkinter as tk
import mysql.connector
from tkinter import *
from tkinter import messagebox
import main as main


def connect():
    cnx = mysql.connector.connect(user='root', password='rohanjerrytroy',
                                  host='35.224.65.220',
                                  database='schoolsystem')
    return cnx

def query_home(root):
    global temp_root
    temp_root = root
    for widget in root.winfo_children():
        widget.destroy()

    table_options = [
        "Student",
        "Faculty",
        "Dormitory",
        "Course",
        "CourseSection",
        "Department",
        "Classroom",
        "Club",
        "Building"
    ]

    clicked = tk.StringVar()
    clicked.set(table_options[0])
    drop = OptionMenu(root, clicked, *table_options).grid(row=2, column=5)
    myButton = tk.Button(root, text="Confirm Selection", command=lambda: change_page(clicked.get())).grid(row=2, column=6)
    back_btn = tk.Button(root, text="Back", command=lambda: change_page("main")).grid(row=2, column=7)

#----- v Student page and selection v --------
def student_page(root):
        id_var = tk.StringVar()

        id_label = tk.Label(root, text='Student ID', font=('calibre', 10, 'bold')).grid(row=0, column=0)
        id_entry = tk.Entry(root, textvariable=id_var, font=('calibre', 10, 'normal')).grid(row=0, column=1)


        sub_btn = tk.Button(root, text='QUERY', command=lambda: select_student(root, id_var)).grid(row=1, column=1)
        back_btn = tk.Button(root, text="Back", command=lambda: change_page("back")).grid(row=2, column=6)

def select_student(root, id_var):
    if(len(id_var.get()) == 0):
      messagebox.showinfo("showinfo", "Valid Arguments Required")
      change_page("back")
      return

    id = id_var.get()

    cnx = connect()
    cursor = cnx.cursor(prepared=True)
    student_data = (id,)
    selection = ("Select * from Student where student_id = %s")
    cursor.execute(selection, student_data)

    for (student_id, stu_name, grade_level, gpa, dormitory_name, classification, advisor) in cursor:
        message = "Student ID: " + str(student_id) +"\n"\
                  + "Student Name: " + str(stu_name) + "\n"\
                  + "Student Name: " + str(grade_level) + "\n"\
                  + "Student GPA: " + str(gpa) + "\n"\
                  + "Dormitory: " + str(dormitory_name) + "\n"\
                  + "Classification: " + str(classification) + "\n"\
                  + "Advisor: " + str(advisor) + "\n"

    messagebox.showinfo("showinfo", message)
    cnx.commit()
    cursor.close()
    cnx.close()
    
    change_page("main")

#----- v Faculty page and selection v --------
def faculty_page(root):
    id_var = tk.StringVar()

    id_label = tk.Label(root, text='Faculty ID', font=('calibre', 10, 'bold')).grid(row=0, column=0)
    id_entry = tk.Entry(root, textvariable=id_var, font=('calibre', 10, 'normal')).grid(row=0, column=1)

    sub_btn = tk.Button(root, text='QUERY', command=lambda: select_faculty(id_var)).grid(row=1, column=1)
    back_btn = tk.Button(root, text="Back", command=lambda: change_page("back")).grid(row=2, column=6)


def select_faculty(id_var):
    if (len(id_var.get()) == 0):
        messagebox.showinfo("showinfo", "Valid Arguments Required")
        change_page("back")
        return

    id = id_var.get()

    cnx = connect()
    cursor = cnx.cursor(prepared=True)
    faculty_data = (id,)
    selection = ("select *"
                "from Faculty "
                "where fac_id = %s) ")
    cursor.execute(selection, faculty_data)

    for (fac_id, faculty_name, department, salary, phone_number, office, building) in cursor:
        message = "Faculty ID: " + str(fac_id) + "\n" \
                  + "Name: " + str(faculty_name) + "\n" \
                  + "Department: " + str(department) + "\n" \
                  + "Salary: " + str(salary) + "\n" \
                  + "Phone: " + str(phone_number) + "\n" \
                  + "Office: " + str(office) + "\n" \
                  + "Building: " + str(building) + "\n"

    messagebox.showinfo("showinfo", message)

    cnx.commit()
    cursor.close()
    cnx.close()
    change_page("main")

#----- v Dormitory page and selection v --------
def dormitory_page(root):
    name_var = tk.StringVar()

    name_label = tk.Label(root, text='Dormitory Name', font=('calibre', 10, 'bold')).grid(row=0, column=0)
    name_entry = tk.Entry(root, textvariable=name_var, font=('calibre', 10, 'normal')).grid(row=0, column=1)

    sub_btn = tk.Button(root, text='QUERY',
                        command=lambda: select_dormitory(name_var)).grid(row=1, column=1)
    back_btn = tk.Button(root, text="Back", command=lambda: change_page("back")).grid(row=2, column=6)


def select_dormitory(name_var):
    if (len(name_var.get()) == 0):
        messagebox.showinfo("showinfo", "Valid Arguments Required")
        change_page("back")
        return

    name = name_var.get()

    cnx = connect()
    cursor = cnx.cursor(prepared=True)
    dormitory_data = (name,)
    selection = ("select *"
                "from Dormitory "
                "where name = %s) ")
    cursor.execute(selection, dormitory_data)

    for (dorm_name, address, dining_hall) in cursor:
        message = "Dormitory Name: " + str(dorm_name) + "\n" \
                  + "Address: " + str(address) + "\n" \
                  + "Dining Hall: " + str(dining_hall) + "\n"

    messagebox.showinfo("showinfo", message)

    cnx.commit()
    cursor.close()
    cnx.close()
    
    change_page("main")

#----- v Course page and selection v --------
def course_page(root):
    id_var = tk.StringVar()

    id_label = tk.Label(root, text='Course ID', font=('calibre', 10, 'bold')).grid(row=0, column=0)
    id_entry = tk.Entry(root, textvariable=id_var, font=('calibre', 10, 'normal')).grid(row=0, column=1)

    sub_btn = tk.Button(root, text='QUERY',
                        command=lambda: select_course(id_var)).grid(row=1, column=1)
    back_btn = tk.Button(root, text="Back", command=lambda: change_page("back")).grid(row=2, column=6)


def select_course(id_var):
    if (len(id_var.get()) == 0):
        messagebox.showinfo("showinfo", "Valid Arguments Required")
        change_page("back")
        return

    id = id_var.get()

    cnx = connect()
    cursor = cnx.cursor(prepared=True)
    course_data = (id,)
    selection = ("select *"
                "from Course "
                "where id = %s) ")
    cursor.execute(selection, course_data)

    for (course_id, course_name, department) in cursor:
        message = "Course ID: " + str(course_id) + "\n" \
                  + "Name: " + str(course_name) + "\n" \
                  + "Department: " + str(department) + "\n"

    messagebox.showinfo("showinfo", message)

    cnx.commit()
    cursor.close()
    cnx.close()
    change_page("main")

#----- v CourseSection page and selection v --------

def course_section_page(root):
    sec_id_var = tk.StringVar()
    course_id_var = tk.StringVar()

    sec_id_label = tk.Label(root, text='Section ID', font=('calibre', 10, 'bold')).grid(row=0, column=0)
    sec_id_entry = tk.Entry(root, textvariable=sec_id_var, font=('calibre', 10, 'normal')).grid(row=0, column=1)

    course_id_label = tk.Label(root, text='Course ID', font=('calibre', 10, 'bold')).grid(row=1, column=0)
    course_id_entry = tk.Entry(root, textvariable=course_id_var, font=('calibre', 10, 'normal')).grid(row=1, column=1)

    sub_btn = tk.Button(root, text='QUERY',
                        command=lambda: select_course_section(sec_id_var, course_id_var).grid(row=7, column=1))
    back_btn = tk.Button(root, text="Back", command=lambda: change_page("back").grid(row=2, column=6))


def select_course_section(sec_id_var, course_id_var, instr_id_var, building_var):
    if (len(sec_id_var.get()) == 0 or len(course_id_var.get()) == 0):
        messagebox.showinfo("showinfo", "Valid Arguments Required")
        change_page("back")
        return

    sec_id = sec_id_var.get()
    co_id = course_id_var.get()

    cnx = connect()
    cursor = cnx.cursor(prepared=True)
    course_section_data = (sec_id, co_id)
    selection = ("select *"
                "from Student "
                "where section_id = %s AND course_id = %s) ")
    cursor.execute(selection, course_section_data)

    for (section_id, course_id, instructor_id, building_name) in cursor:
        message = "Section ID: " + str(section_id) + "\n" \
                  + "Course ID: " + str(course_id) + "\n" \
                  + "Instructor ID: " + str(instructor_id) + "\n" \
                  + "Building: " + str(building_name) + "\n"

    messagebox.showinfo("showinfo", message)

    cnx.commit()
    cursor.close()
    cnx.close()
    change_page("main")


#----- v Department page and selection v --------
def department_page(root):
    name_var = tk.StringVar()

    name_label = tk.Label(root, text='Department Name', font=('calibre', 10, 'bold')).grid(row=0, column=0)
    name_entry = tk.Entry(root, textvariable=name_var, font=('calibre', 10, 'normal')).grid(row=0, column=1)

    sub_btn = tk.Button(root, text='QUERY',
                        command=lambda: select_department(name_var)).grid(row=1, column=1)
    back_btn = tk.Button(root, text="Back", command=lambda: change_page("back")).grid(row=2, column=6)


def select_department(name_var):
    if (len(name_var.get()) == 0):
        messagebox.showinfo("showinfo", "Valid Arguments Required")
        change_page("back")
        return

    name = name_var.get()

    cnx = connect()
    cursor = cnx.cursor(prepared=True)
    department_data = (name,)
    selection = ("select *"
                "from Department "
                "where id = %s) ")
    cursor.execute(selection, department_data)

    for (dept_name, chair, building) in cursor:
        message = "Department Name: " + str(dept_name) + "\n" \
                  + "Chair: " + str(chair) + "\n" \
                  + "Building: " + str(building) + "\n"

    messagebox.showinfo("showinfo", message)


    cnx.commit()
    cursor.close()
    cnx.close()
    change_page("main")


#----- v Classroom page and selection v --------
def classroom_page(root):
    room_var = tk.StringVar()
    building_var = tk.StringVar()
    cap_var = tk.StringVar()

    name_label = tk.Label(root, text='Room Number', font=('calibre', 10, 'bold')).grid(row=0, column=0)
    name_entry = tk.Entry(root, textvariable=room_var, font=('calibre', 10, 'normal')).grid(row=0, column=1)

    building_label = tk.Label(root, text='Building', font=('calibre', 10, 'bold')).grid(row=1, column=0)
    building_entry = tk.Entry(root, textvariable=building_var, font=('calibre', 10, 'normal')).grid(row=1, column=1)

    sub_btn = tk.Button(root, text='QUERY',
                        command=lambda: select_classroom(room_var, building_var)).grid(row=2, column=1)
    back_btn = tk.Button(root, text="Back", command=lambda: change_page("back")).grid(row=2, column=6)


def select_classroom(room_var, building_var):
    if (len(room_var.get()) == 0 or len(building_var.get()) == 0):
        messagebox.showinfo("showinfo", "Valid Arguments Required")
        change_page("back")
        return

    room = room_var.get()
    building = building_var.get()

    cnx = connect()
    cursor = cnx.cursor(prepared=True)
    classrooom_data = (room, building)
    selection = ("select *"
                "from Classroom "
                "where room_number = %s AND building_name = %s) ")

    cursor.execute(selection, classrooom_data)

    for (room_number, building_name, capacity) in cursor:
        message = "Room Number: " + str(room_number) + "\n" \
                  + "Building: " + str(building_name) + "\n" \
                  + "Capacity: " + str(capacity) + "\n"

    messagebox.showinfo("showinfo", message)


    cnx.commit()
    cursor.close()
    cnx.close()
    change_page("main")


#----- v Club page and selection v --------
def club_page(root):
    name_var = tk.StringVar()

    name_label = tk.Label(root, text='Club Name', font=('calibre', 10, 'bold')).grid(row=0, column=0)
    name_entry = tk.Entry(root, textvariable=name_var, font=('calibre', 10, 'normal')).grid(row=0, column=1)

    sub_btn = tk.Button(root, text='QUERY',
                        command=lambda: select_club(name_var)).grid(row=1, column=1)
    back_btn = tk.Button(root, text="Back", command=lambda: change_page("back")).grid(row=2, column=6)


def select_club(name_var):
    if (len(name_var.get()) == 0):
        messagebox.showinfo("showinfo", "Valid Arguments Required")
        change_page("back")
        return

    name = name_var.get()

    cnx = connect()
    cursor = cnx.cursor(prepared=True)
    club_data = (name,)
    selection = ("select *"
                "from Club "
                "where club_name = %s) ")
    cursor.execute(selection, club_data)

    for (club_name, supervisor_id, funding, building_name) in cursor:
        message = "Club Name: " + str(club_name) + "\n" \
                  + "Supervisor ID: " + str(supervisor_id) + "\n" \
                  + "Funding($): " + str(funding) + "\n" \
                  + "Building: " + str(building_name) + "\n"

    messagebox.showinfo("showinfo", message)

    cnx.commit()
    cursor.close()
    cnx.close()
    change_page("main")

#----- v Building page and selection v --------
def building_page(root):
    name_var = tk.StringVar()

    name_label = tk.Label(root, text='Building Name', font=('calibre', 10, 'bold')).grid(row=0, column=0)
    name_entry = tk.Entry(root, textvariable=name_var, font=('calibre', 10, 'normal')).grid(row=0, column=1)

    sub_btn = tk.Button(root, text='QUERY',
                        command=lambda: select_building(name_var)).grid(row=1, column=1)
    back_btn = tk.Button(root, text="Back", command=lambda: change_page("back")).grid(row=2, column=6)


def select_building(name_var):
    if (len(name_var.get()) == 0):
        messagebox.showinfo("showinfo", "Valid Arguments Required")
        change_page("back")
        return

    name = name_var.get()

    cnx = connect()
    cursor = cnx.cursor(prepared=True)
    building_data = (name,)
    selection = ("select *"
                "from Building "
                "where building_name = %s) ")

    cursor.execute(selection, building_data)

    for (building_name, address, HasHandicapAccess) in cursor:
        message = "Club Name: " + str(building_name) + "\n" \
                  + "Supervisor ID: " + str(address) + "\n" \
                  + "Funding($): " + str(HasHandicapAccess) + "\n" \

    messagebox.showinfo("showinfo", message)

    cnx.commit()
    cursor.close()
    cnx.close()
    change_page("main")



def change_page(table):
    for widget in temp_root.winfo_children():
        widget.destroy()
    if table == "back":
        query_home(temp_root)
    elif table == "main":
        main.home(temp_root)
    elif table == "Student":
        student_page(temp_root)
    elif table == "Faculty":
        faculty_page(temp_root)
    elif table == "Dormitory":
        dormitory_page(temp_root)
    elif table == "Course":
        course_page(temp_root)
    elif table == "CourseSection":
        course_section_page(temp_root)
    elif table == "Department":
        department_page(temp_root)
    elif table == "Classroom":
       classroom_page(temp_root)
    elif table == "Club":
        club_page(temp_root)
    elif table == "Building":
        building_page(temp_root)
