from tkinter import *  # Import tkinter for building the GUI
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog

class Attendance:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x750+0+0")
        self.root.title("Face Recognition System")
        
        #====================variables============
        self.var_atten_id=StringVar()
        self.var_atten_roll=StringVar()
        self.var_atten_name=StringVar()
        self.var_atten_dep=StringVar()
        self.var_atten_time=StringVar()
        self.var_atten_date=StringVar()
        self.var_atten_attendance=StringVar()
        
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
        img4 = Image.open(r"C:\Users\warar_3reymm5\OneDrive\Desktop\Face_Recognition\college_image\download (1).png")
        img4 = img4.resize((1300, 550), Image.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)
        bg_img = Label(self.root, image=self.photoimg4)
        bg_img.place(x=0, y=100, width=1300, height=550)


        title_lbl = Label(bg_img, text="ATTENDENCE MANAGEMENT SYSTEM", font=("times new roman", 20, "bold"), bg="pink", fg="black")
        title_lbl.place(x=-25, y=0, width=1300, height=35)

        main_frame=Frame(bg_img,bd=2)
        main_frame.place(x=1,y=40,width=1265,height=495)
      
      
                #left side label frame

        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Attendence Detail",font=("times new roman",10,"bold"))
        Left_frame.place(x=10,y=10,width=600,height=500)

        
        img_left= Image.open(r"C:\Users\warar_3reymm5\OneDrive\Desktop\Face_Recognition\college_image\ezgif.com-gif-maker-6 (1).png")
        img_left = img_left.resize((700, 100), Image.LANCZOS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)
        f_lbl3 = Label(Left_frame, image=self.photoimg_left)
        f_lbl3.place(x=3, y=0, width=600, height=130)

        left_inside_frame=Frame( Left_frame,bd=2,relief=RIDGE,bg="white")
        left_inside_frame.place(x=0,y=100,width=600,height=350)


  # ==== Labels & Entry Fields ====
        labels = ["Attendance ID:", "Roll:", "Name:", "Department:", "Time:", "Date:", "Attendance Status:"]
        variables = [self.var_atten_id, self.var_atten_roll, self.var_atten_name, self.var_atten_dep,
                     self.var_atten_time, self.var_atten_date]
        for i, (label_text, var) in enumerate(zip(labels, variables)):
            Label(left_inside_frame, text=label_text, font=("times new roman", 10, "bold"), bg="white").grid(row=i//2, column=(i % 2) * 2, padx=5, pady=5, sticky=W)
            Entry(left_inside_frame, width=25, textvariable=var, font=("times new roman", 10, "bold")).grid(row=i//2, column=(i % 2) * 2 + 1, padx=5, pady=5, sticky=W)

        # Attendance Status Dropdown
        self.atten_status = ttk.Combobox(left_inside_frame, width=20, textvariable=self.var_atten_attendance,
                                         font=("times new roman", 12, "bold"), state="readonly")
        self.atten_status["values"] = ("Status", "Present", "Absent")
        self.atten_status.grid(row=3, column=1, pady=8)
        self.atten_status.current(0)

        # ==== Button Frame ====
        btn_frame = Frame(left_inside_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=0, y=300, width=765, height=35)

        Button(btn_frame, text="Import CSV", command=self.importCsv, width=20, font=("times new roman", 13, "bold"),
               bg="blue", fg="white").grid(row=0, column=0)

        Button(btn_frame, text="Export CSV", command=self.exportCsv, width=20, font=("times new roman", 13, "bold"),
               bg="blue", fg="white").grid(row=0, column=1)
    
        
        Button(btn_frame, text="Reset", command=self.reset_data, width=20, font=("times new roman", 13, "bold"),
               bg="blue", fg="white").grid(row=0, column=2)

        # ==== Right Frame: Attendance Table ====
        right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Attendance Details",
                                 font=("times new roman", 10, "bold"))
        right_frame.place(x=610, y=10, width=700, height=500)

        table_frame = Frame(right_frame, bd=2, relief=RIDGE, bg="white")
        table_frame.place(x=1, y=1, width=680, height=456)

        # ==== Scrollbars ====
        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.AttendanceReportTable = ttk.Treeview(table_frame,
                                                  column=("id", "roll", "name", "department", "time", "date",
                                                          "attendance"),
                                                  xscrollcommand=scroll_x.set,
                                                  yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        # ==== Table Headers ====
        columns = ["id", "roll", "name", "department", "time", "date", "attendance"]
        headers = ["Attendance ID", "Roll", "Name", "Department", "Time", "Date", "Attendance"]
        for col, header in zip(columns, headers):
            self.AttendanceReportTable.heading(col, text=header)
            self.AttendanceReportTable.column(col, width=100)
        self.AttendanceReportTable["show"] = "headings"
        self.AttendanceReportTable.pack(fill=BOTH, expand=1)
        self.AttendanceReportTable.bind("<ButtonRelease>", self.get_cursor)

        # ==== Global Data Storage ====
        global mydata
        mydata = []

    # ==== Fetch Data into Table ====
    def fetchData(self, rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i, row in enumerate(rows):
            tag = "evenrow" if i % 2 == 0 else "oddrow"
            self.AttendanceReportTable.insert("", END, values=row, tags=(tag,))
        self.AttendanceReportTable.tag_configure('oddrow', background="lightgray")
        self.AttendanceReportTable.tag_configure('evenrow', background="white")

    # ==== Import CSV ====
    def importCsv(self):
        global mydata
        mydata.clear()
        try:
            fln = filedialog.askopenfilename(initialdir=os.getcwd(), title="Open CSV",
                                             filetypes=(("CSV File", "*.csv"), ("All Files", "*.*")),
                                             parent=self.root)
            with open(fln, newline="") as myfile:
                csvread = csv.reader(myfile)
                for row in csvread:
                    mydata.append(row)
                self.fetchData(mydata)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load file: {str(e)}", parent=self.root)

    # ==== Export CSV ====
    def exportCsv(self):
        try:
            if len(mydata) < 1:
                messagebox.showerror("No Data", "No data found to export", parent=self.root)
                return
            fln = filedialog.asksaveasfilename(initialdir=os.getcwd(), title="Save CSV",
                                               filetypes=(("CSV File", "*.csv"), ("All Files", "*.*")),
                                               defaultextension=".csv", parent=self.root)
            with open(fln, mode="w", newline="") as myfile:
                exp_write = csv.writer(myfile)
                for i in mydata:
                    exp_write.writerow(i)
            messagebox.showinfo("Success", f"Data exported successfully to {os.path.basename(fln)}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to export file: {str(e)}", parent=self.root)

    # ==== Get Cursor Data ====
    def get_cursor(self, event=""):
        cursor_row = self.AttendanceReportTable.focus()
        content = self.AttendanceReportTable.item(cursor_row)
        rows = content["values"]
        if rows:
            self.var_atten_id.set(rows[0])
            self.var_atten_roll.set(rows[1])
            self.var_atten_name.set(rows[2])
            self.var_atten_dep.set(rows[3])
            self.var_atten_time.set(rows[4])
            self.var_atten_date.set(rows[5])
            self.var_atten_attendance.set(rows[6])
  





    # ==== Reset Data ====
    def reset_data(self):
        for var in [self.var_atten_id, self.var_atten_roll, self.var_atten_name,
                    self.var_atten_dep, self.var_atten_time, self.var_atten_date, self.var_atten_attendance]:
            var.set("")
        
if __name__ == "__main__":
    root = Tk()
    obj = Attendance(root)
    root.mainloop()
