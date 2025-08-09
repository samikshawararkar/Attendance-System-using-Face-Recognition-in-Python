from tkinter import *  # Import tkinter for building the GUI
from tkinter import ttk
from PIL import Image, ImageTk  # Import Image and ImageTk for image handling
from tkinter import messagebox
import mysql.connector
import cv2

class Student:
    def __init__(self, root):  # Constructor to initialize the GUI window
        self.root = root  # Store the root window
        self.root.geometry("1350x750+0+0")  # Set the size and position of the window
        self.root.title("Face Recognition System")  # Set the window title


        #===============variables================
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()
        
       # First image
        img1 = Image.open(r"C:\Users\warar_3reymm5\Downloads\1628243597666college-images\college_images\smart-attendance.jpg")
        img1 = img1.resize((450, 100), Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        f_lbl1 = Label(self.root, image=self.photoimg1)
        f_lbl1.place(x=400, y=0, width=450, height=100)

        # Second image
        img2 = Image.open(r"C:\Users\warar_3reymm5\Downloads\1628243597666college-images\college_images\face-recognition.png")
        img2 = img2.resize((450, 100), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        f_lbl2 = Label(self.root, image=self.photoimg2)
        f_lbl2.place(x=850, y=0, width=450, height=100)
        
        # Third image
        img3 = Image.open(r"C:\Users\warar_3reymm5\Downloads\1628243597666college-images\college_images\AdobeStock_303989091.jpeg")
        img3 = img3.resize((450, 100), Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        f_lbl3 = Label(self.root, image=self.photoimg3)
        f_lbl3.place(x=0, y=0, width=450, height=100)

       # Background image
        img4 = Image.open(r"C:\Users\warar_3reymm5\OneDrive\Desktop\Face_Recognition\ghru-nag.png")
        img4 = img4.resize((1300, 550), Image.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)
        bg_img = Label(self.root, image=self.photoimg4)
        bg_img.place(x=0, y=100, width=1300, height=550)

        title_lbl = Label(bg_img, text="STUDENT MANAGEMENT SYSTEM", font=("times new roman", 20, "bold"), bg="yellow", fg="black")
        title_lbl.place(x=-0, y=0, width=1300, height=45)

        main_frame=Frame(bg_img,bd=2)
        main_frame.place(x=5,y=50,width=1510,height=490)
        
        
        #left side label frame

        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Left_frame.place(x=2,y=5,width=630,height=470)

        img_left= Image.open(r"C:\Users\warar_3reymm5\Downloads\1628243597666college-images\college_images\AdobeStock_303989091.jpeg")
        img_left = img_left.resize((770, 100), Image.LANCZOS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)
        f_lbl3 = Label(Left_frame, image=self.photoimg_left)
        f_lbl3.place(x=5, y=0, width=760, height=100)
        
        #current course
        current_course_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Current Course Information",font=("times new roman",9,"bold"))
        current_course_frame.place(x=5,y=100,width=770,height=100)

        dep_label=Label(current_course_frame,text="Department",font=("times new roman",10,"bold"),bg="White")
        dep_label.grid(row=0,column=0)

        dep_combo=ttk.Combobox(current_course_frame,text="Department",font=("times new roman",10,"bold"),state="readonly")
        dep_combo["values"]=("Select Department","Computer Science","IT","Civil","Data Science","Mechanical","AI","Electrical")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10)
        
        #Department
        dep_label=Label(current_course_frame,text="Department",font=("times new roman",10,"bold"),bg="White")
        dep_label.grid(row=0,column=0,padx=10)


        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("times new roman",10,"bold"),state="readonly")
        dep_combo["values"]=("Select Department","Computer Science","IT","Civil","Data Science","Mechanical","AI","Electrical")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10)
       #course

        course_label=Label(current_course_frame,text="Course",font=("times new roman",10,"bold"),bg="White")
        course_label.grid(row=0,column=2,padx=10,sticky=W)


        course_combo=ttk.Combobox(current_course_frame,text ="Course",textvariable=self.var_course,font=("times new roman",10,"bold"),state="readonly")
        course_combo["values"]=("Select Course","FE","SE","TE","BE")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)

         #Year
        year_label=Label(current_course_frame,text="Year",font=("times new roman",10,"bold"),bg="White")
        year_label.grid(row=1,column=0,padx=10,sticky=W)


        year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("times new roman",10,"bold"),state="readonly")
        year_combo["values"]=("Select Year","2020-21","2021-22","2022-23","2023-24","2024-25")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)
        

        #semester
        semester_label=Label(current_course_frame,text="Semester",font=("times new roman",10,"bold"),bg="White")
        semester_label.grid(row=1,column=2,padx=10,sticky=W)


        semester_combo=ttk.Combobox(current_course_frame,textvariable=self.var_semester,font=("times new roman",10,"bold"),state="readonly")
        semester_combo["values"]=("Select Semester","Semester-1","Semester-2","Semester-3","Semester-4","Semester-5","Semester-6","Semester-7","Semester-8")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)
          
        #class student information
        class_student_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Class student information",font=("times new roman",9,"bold"))
        class_student_frame.place(x=2,y=210,width=770,height=300)

        #student ID
        studentID_label=Label(class_student_frame,text="StudentID:",font=("times new roman",10,"bold"),bg="White")
        studentID_label.grid(row=0,column=0,padx=5,pady=5,sticky=W)

        studentID_entry=ttk.Entry(class_student_frame,width=20,textvariable=self.var_std_id,font=("times new roman",10,"bold"))
        studentID_entry.grid(row=0,column=1,padx=5,pady=5,sticky=W)

        #student name

        studentname_label=Label(class_student_frame,text="StudentName:",font=("times new roman",10,"bold"),bg="White")
        studentname_label.grid(row=0,column=2,padx=5,pady=5,sticky=W)

        studentname_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_name,width=20,font=("times new roman",10,"bold"))
        studentname_entry.grid(row=0,column=3,padx=5,pady=5,sticky=W)

        #class division
        class_div_label=Label(class_student_frame,text="Class Division:",font=("times new roman",10,"bold"),bg="White")
        class_div_label.grid(row=1,column=0,padx=5,pady=5,sticky=W)

       # class_div_entry=ttk.Entry(class_student_frame,text = "Class Division",width=20,font=("times new roman",11,"bold"))
        #class_div_entry.grid(row=1,column=1,padx=5,pady=5,sticky=W)
         
        div_combo=ttk.Combobox(class_student_frame,textvariable=self.var_div,font=("times new roman",10,"bold"),state="readonly",width=21)
        div_combo["values"]=("A","B","C","D","E","F","G","H","I")
        div_combo.current(0)
        div_combo.grid(row=1,column=1,padx=5,pady=5,sticky=W)

        #roll no
        roll_no_label=Label(class_student_frame,text="Roll no:",font=("times new roman",10,"bold"),bg="White")
        roll_no_label.grid(row=1,column=2,padx=5,pady=5,sticky=W)

        roll_no_entry=ttk.Entry(class_student_frame,textvariable=self.var_roll,width=20,font=("times new roman",10,"bold"))
        roll_no_entry.grid(row=1,column=3,padx=5,pady=5,sticky=W)

        #gender
        gender_label=Label(class_student_frame,text="Gender:",font=("times new roman",10,"bold"),bg="White")
        gender_label.grid(row=2,column=0,padx=5,pady=5,sticky=W)

        #gender_entry=ttk.Entry(class_student_frame,text="gender",width=20,font=("times new roman",11,"bold"))
        #gender_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)

        gender_combo=ttk.Combobox(class_student_frame,textvariable=self.var_gender,font=("times new roman",10,"bold"),state="readonly",width=21)
        gender_combo["values"]=("Male","Female")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=2,pady=5,sticky=W)
         #date of birth

        dob_label=Label(class_student_frame,text="DOB:",font=("times new roman",10,"bold"),bg="White")
        dob_label.grid(row=2,column=2,padx=5,pady=5,sticky=W)

        dob_entry=ttk.Entry(class_student_frame,textvariable=self.var_dob,width=20,font=("times new roman",10,"bold"))
        dob_entry.grid(row=2,column=3,padx=5,pady=5,sticky=W)

        #EMAIL
        email_label=Label(class_student_frame,text="Email:",font=("times new roman",10,"bold"),bg="White")
        email_label.grid(row=3,column=0,padx=5,pady=5,sticky=W)

        email_entry=ttk.Entry(class_student_frame,textvariable=self.var_email,width=20,font=("times new roman",10,"bold"))
        email_entry.grid(row=3,column=1,padx=5,pady=5,sticky=W)

        #phone no
        phone_label=Label(class_student_frame,text="Phone No:",font=("times new roman",10,"bold"),bg="White")
        phone_label.grid(row=3,column=2,padx=5,pady=5,sticky=W)

        phone_entry=ttk.Entry(class_student_frame,width=20,textvariable=self.var_phone,font=("times new roman",10,"bold"))
        phone_entry.grid(row=3,column=3,padx=5,pady=5,sticky=W)

        #address
        address_label=Label(class_student_frame,text="Address:",font=("times new roman",10,"bold"),bg="White")
        address_label.grid(row=4,column=0,padx=5,pady=5,sticky=W)

        address_entry=ttk.Entry(class_student_frame,width=20,textvariable=self.var_address,font=("times new roman",10,"bold"))
        address_entry.grid(row=4,column=1,padx=5,pady=5,sticky=W)

       #teacher name
        teacher_label=Label(class_student_frame,text="Teacher Name:",font=("times new roman",10,"bold"),bg="White")
        teacher_label.grid(row=4,column=2,padx=5,pady=5,sticky=W)

        teacher_entry=ttk.Entry(class_student_frame,width=20,textvariable=self.var_teacher,font=("times new roman",10,"bold"))
        teacher_entry.grid(row=4,column=3,padx=5,pady=5,sticky=W)

      #radio buttons
        self.var_radio1=StringVar()
        radionbtn1=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="Take photo sample",value="Yes")
        radionbtn1.grid(row=6,column=0)
        
        radionbtn2=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="No photo sample",value="No")
        radionbtn2.grid(row=6,column=1)

        #button frame
        btn_frame=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=173,width=1000,height=35)

        save_btn=Button(btn_frame,text="Save",width=18,command=self.add_data,font=("times new roman",10,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)

        
        update_btn=Button(btn_frame,text="Update",width=18,command=self.update_data,font=("times new roman",10,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)

        
        delete_btn=Button(btn_frame,text="Delete",width=18,command=self.delete_data,font=("times new roman",10,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)

        
        reset_btn=Button(btn_frame,text="Reset",width=18,command=self.reset_data,font=("times new roman",10,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)

        btn_frame1=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame1.place(x=0,y=201,width=1000,height=35)

        
        take_photo_btn=Button(btn_frame1,command= self.generate_dataset,text="Take Photo Sample",width=37,font=("times new roman",10,"bold"),bg="blue",fg="white")
        take_photo_btn.grid(row=0,column=0)

        update_photo_btn=Button(btn_frame1,text="Update Photo Sample",width=37,font=("times new roman",10,"bold"),bg="blue",fg="white")
        update_photo_btn.grid(row=0,column=1)
        
        
        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Detail",font=("times new roman",12,"bold"))
        Right_frame.place(x=630,y=2,width=650,height=470)

        img_Right= Image.open(r"C:\Users\warar_3reymm5\Downloads\1628243597666college-images\college_images\gettyimages-1022573162.jpg")
        img_Right= img_Right.resize((750, 100), Image.LANCZOS)
        self.photoimg_R = ImageTk.PhotoImage(img_Right) 
        f_lbl3 = Label(Right_frame, image=self.photoimg_R)
        f_lbl3.place(x=1, y=0, width=760, height=100)
        
         # ====SEARCH SYSTEM=======
        search_frame=LabelFrame(Right_frame,bd=2,bg="white",relief=RIDGE,text="Search  System",font=("times new roman",12,"bold"))
        search_frame.place(x=5,y=100,width=690,height=60)
        
        search_label=Label(search_frame,text="Search By:",font=("times new roman",13,"bold"),bg="Red",fg="White")
        search_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        search_combo=ttk.Combobox(search_frame,font=("times new roman",12,"bold"),state="readonly",width=15)
        search_combo["values"]=("Select","Roll no","Phone no")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        search_entry=ttk.Entry(search_frame,width=15,font=("times new roman",13,"bold"))
        search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        
        search_btn=Button(search_frame,text="Search",width=10,font=("times new roman",10,"bold"),bg="blue",fg="white")
        search_btn.grid(row=0,column=2,padx=2)

        showAll_btn=Button(search_frame,text="ShowAll",width=10,font=("times new roman",10,"bold"),bg="blue",fg="white")
        showAll_btn.grid(row=0,column=3,padx=2)
 
        table_frame=LabelFrame(Right_frame,bd=2,bg="white",relief=RIDGE,)
        table_frame.place(x=1,y=160,width=630,height=300)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,column=("dep","course","year","sem","id","name","div","roll","gender","dob","email","phone","address","teacher","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
        #========table frame=============
        table_frame=LabelFrame(Right_frame,bd=2,bg="white",relief=RIDGE,)
        table_frame.place(x=1,y=160,width=600,height=300)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,column=("dep","course","year","sem","id","name","div","roll","gender","dob","email","phone","address","teacher","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)



        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="Student id")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("div",text="Division")
        self.student_table.heading("roll",text="Roll number")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone",text="Phone")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("teacher",text="Teacher")
        self.student_table.heading("photo",text="PhotoSampleStatus")
        self.student_table["show"]="headings"


        
        self.student_table.column("dep",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("div",width=100)
        self.student_table.column("roll",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("phone",width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("teacher",width=100)
        self.student_table.column("photo",width=100)
        

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
     #=============funtion declaration============
    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
               conn=mysql.connector.connect(host="127.0.0.1",username="root",password="Abc@12345",database="face_recognizer",port="3306")
               my_cursor=conn.cursor()
               my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                             
                                                                                                            self.var_dep.get(),
                                                                                                            self.var_course.get(),
                                                                                                            self.var_year.get(),
                                                                                                            self.var_semester.get(),
                                                                                                            self.var_std_id.get(),
                                                                                                            self.var_std_name.get(),
                                                                                                            self.var_div.get(),
                                                                                                            self.var_roll.get(),
                                                                                                            self.var_gender.get(),
                                                                                                            self.var_dob.get(),
                                                                                                            self.var_email.get(),
                                                                                                            self.var_phone.get(),
                                                                                                            self.var_address.get(),
                                                                                                            self.var_teacher.get(),
                                                                                                            self.var_radio1.get()
                                                                                                           ))

                                                                                                            
               conn.commit()
               self.fetch_data()
               conn.close()
               messagebox.showinfo("Success","Student details has been added Successfully",parent=self.root)    
            except Exception as es:                                                                                                                                                                                                                                                                                                                                                               
               messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)
          
         # ====================fetch data=============
    def fetch_data(self):
        conn=mysql.connector.connect(host="127.0.0.1",username="root",password="Abc@12345",database="face_recognizer",port="3306")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()        
             

             #===================get cursor=====================
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]

        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_std_id.set(data[4]),
        self.var_std_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radio1.set(data[14])
        


    def update_data(self):
        if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.var_std_id.get() == "":
         messagebox.showerror("Error", "All Fields are required", parent=self.root)
        else:
         try:
            update = messagebox.askyesno("Update", "Do you want to update this student details?", parent=self.root)
            if update:
                conn = mysql.connector.connect(
                    host="127.0.0.1", username="root", password="Abc@12345",
                    database="face_recognizer", port="3306"
                )
                my_cursor = conn.cursor()
                my_cursor.execute(
                    """UPDATE student SET Dep=%s, course=%s, Year=%s, Semester=%s, Name=%s, Division=%s, 
                       Roll=%s, Gender=%s, Dob=%s, Email=%s, Phone=%s, Address=%s, Teacher=%s, PhotoSample=%s 
                       WHERE Student_id=%s""",
                    (
                        self.var_dep.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_semester.get(),
                        self.var_std_name.get(),
                        self.var_div.get(),
                        self.var_roll.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_email.get(),
                        self.var_phone.get(),
                        self.var_address.get(),
                        self.var_teacher.get(),
                        self.var_radio1.get(),
                        self.var_std_id.get(),
                    ),
                )
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Student details updated successfully", parent=self.root)
         except Exception as es:
            messagebox.showerror("Error", f"Due To: {str(es)}", parent=self.root)


    def delete_data(self):
        if self.var_std_id.get() == "":
         messagebox.showerror("Error", "Student ID must be required", parent=self.root)
        else:
         try:
            delete = messagebox.askyesno("Student Delete", "Do you want to delete this student?", parent=self.root)
            if delete:
                conn = mysql.connector.connect(
                    host="127.0.0.1", username="root", password="Abc@12345",
                    database="face_recognizer", port="3306"
                )
                my_cursor = conn.cursor()
                sql = "DELETE FROM student WHERE Student_id=%s"
                val = (self.var_std_id.get(),)
                my_cursor.execute(sql, val)
                conn.commit()
                conn.close()
                self.fetch_data()
                messagebox.showinfo("Delete", "Successfully deleted student details", parent=self.root)
         except Exception as es:
                messagebox.showerror("Error", f"Due To: {str(es)}", parent=self.root)


 #====================reset=====================
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.var_std_id.set("")
        self.var_std_name.set("")
        self.var_div.set("Select Division")
        self.var_roll.set("")
        self.var_gender.set("Male")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_teacher.set("")
        self.var_radio1.set("")


                 #==============generate data set or take photo sample==============
    def generate_dataset(self):
        
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
         try:
            conn=mysql.connector.connect(host="127.0.0.1",username="root",password="Abc@12345",database="face_recognizer",port="3306")
            my_cursor=conn.cursor()
            my_cursor.execute("select * from student")
            myresult=my_cursor.fetchall()
            id=0
            for x in myresult:
                id+=1
                my_cursor.execute("update student set  Dep=%s,course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s",(
                     
                                                                                                                                                                                                                 self.var_dep.get(),
                                                                                                                                                                                                                 self.var_course.get(),
                                                                                                                                                                                                                 self.var_year.get(),                
                                                                                                                                                                                                                 self.var_semester.get(),       
                                                                                                                                                                                                                       
                                                                                                                                                                                                                 self.var_std_name.get(),       
                                                                                                                                                                                                                 self.var_div.get(),       
                                                                                                                                                                                                                 self.var_roll.get(),       
                                                                                                                                                                                                                 self.var_gender.get(),       
                                                                                                                                                                                                                 self.var_dob.get(),       
                                                                                                                                                                                                                 self.var_email.get(),       
                                                                                                                                                                                                                 self.var_phone.get(),       
                                                                                                                                                                                                                 self.var_address.get(),       
                                                                                                                                                                                                                 self.var_teacher.get(),       
                                                                                                                                                                                                                 self.var_radio1.get(),
                                                                                                                                                                                                                 self.var_std_id.get()==id+1
                                                                                                                                                                                                              ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()
         

                #================load predefined data on face frontols from opencv================
                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)
                    #sacling factor=1.3
                    #minimum neighbour=5
                    
                    for(x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped
                    

                cap=cv2.VideoCapture(0)    
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(my_frame),(400,400))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Crooped Face",face)

                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result", "Generating data sets completed!!!!")
         except Exception as es:
                messagebox.showerror("Erorr",f"Due To:{str(es)}",parent=self.root)

               
             
if __name__ == "__main__":  #Entry point of the program
    root = Tk()  #Create the main application window
    obj = Student(root)  #Create an instance of the FaceRecognitionSystem class
    root.mainloop()  #Start the GUI event loop