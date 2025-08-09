from tkinter import *  # Import tkinter for building the GUI
from tkinter import ttk
from PIL import Image, ImageTk  # Import Image and ImageTk for image handling
from studentdetail import Student
from train import Train
from attendance import Attendance
from face_decetor import Face_Recognition
import os
class FaceRecognitionSystem:
    def __init__(self, root):  # Constructor to initialize the GUI window
        self.root = root  # Store the root window
        self.root.geometry("1350x750+0+0")  # Set the size and position of the window
        self.root.title("Face Recognition System")  # Set the window title

        # Load the first image
        img = Image.open(r"C:\Users\warar_3reymm5\OneDrive\Desktop\Face_Recognition\college_image\download.png")
        img = img.resize((450, 100), Image.LANCZOS)  # Resize the image to 450x100 pixels using LANCZOS
        self.photoimg = ImageTk.PhotoImage(img)  # Convert the resized image into a format tkinter can use

        f_lbl = Label(self.root, image=self.photoimg)  # Create a label widget to display the image
        f_lbl.place(x=400, y=0, width=450, height=100)  # Position the label at the top-left corner

        # Load the second image
        img1 = Image.open(r"C:\Users\warar_3reymm5\OneDrive\Desktop\Face_Recognition\college_image\facial-recognition-technology-scan-detect-people-face-identification_31965-24741.jpg")
        img1 = img1.resize((450, 100), Image.LANCZOS)  
        self.photoimg1 = ImageTk.PhotoImage(img1)  

        s_lbl = Label(self.root, image=self.photoimg1)  # Use a different label for the second image
        s_lbl.place(x=850, y=0, width=450, height=100)  # Position it next to the first image

        # Load the third image
        img2 = Image.open(r"C:\Users\warar_3reymm5\OneDrive\Desktop\Face_Recognition\college_image\images (2).png")
        img2 = img2.resize((450, 100), Image.LANCZOS)  
        self.photoimg2 = ImageTk.PhotoImage(img2)  

        t_lbl = Label(self.root, image=self.photoimg2)  # Use a different label for the third image
        t_lbl.place(x=0, y=0, width=450, height=100)  # Position it to the far left

        # Load the background image
        img3 = Image.open(r"C:\Users\warar_3reymm5\OneDrive\Desktop\Face_Recognition\college_image\background.png")
        img3 = img3.resize((1300, 550), Image.LANCZOS)  # Resize the background image
        self.photoimg3 = ImageTk.PhotoImage(img3)

        # Define 'bg_lbl' as the background image label
        bg_lbl = Label(self.root, image=self.photoimg3)  # Now 'bg_lbl' is defined
        bg_lbl.place(x=0, y=100, width=1300, height=550)  # Correctly place the background image

        title_lbl = Label(bg_lbl,text= "FACE RECOGNITION SYSTEM SOFTWARE",font= ("times new roman", 30,"bold"),bg="White",fg="darkblue")
        title_lbl.place(x=0, y=0, width= 1300, height= 35)
     
     #student button
        img4=Image.open(r"C:\Users\warar_3reymm5\OneDrive\Desktop\Face_Recognition\college_image\collage-large-group-.png")
        img4= img4.resize((200,150),Image.LANCZOS)
        self.phtoimg4 = ImageTk.PhotoImage(img4)
        
        b1= Button (bg_lbl,image=self.phtoimg4,command=self.student_details,cursor="hand2")
        b1.place(x=100, y=100, width=150, height=150)
        
        b1_1= Button(bg_lbl,text="Student Details",command=self.student_details,cursor="hand2",font=("times of roman",13,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=100, y=250, width=150, height=20)
       
       
    # Detect face button 
    
        img5=Image.open(r"C:\Users\warar_3reymm5\OneDrive\Desktop\Face_Recognition\college_image\detect.png")
        img5= img5.resize((200,150),Image.LANCZOS)
        self.photoimg5 = ImageTk.PhotoImage(img5)
        
        b2= Button(bg_lbl,image=self.photoimg5,cursor="hand2",command=self.face_decetor_data)
        b2.place(x=400, y=100, width=150, height=150)
        
        b2_2= Button(bg_lbl,text="Face Detector",cursor="hand2",command=self.face_decetor_data,font=("times of roman",13,"bold"),bg="darkblue",fg="white")
        b2_2.place(x=400, y=250, width=150, height=20)
        
     # attendance
    
        img6=Image.open(r"C:\Users\warar_3reymm5\OneDrive\Desktop\Face_Recognition\college_image\download (1).png")
        img6= img6.resize((200,150),Image.LANCZOS)
        self.photoimg6 = ImageTk.PhotoImage(img6)
        
        b3= Button(bg_lbl,image=self.photoimg6,cursor="hand2",command=self.attendance_data)
        b3.place(x=700, y=100, width=150, height=150)
        
        b3_3= Button(bg_lbl,text="Attendance",command=self.attendance_data,cursor="hand2",font=("times of roman",13,"bold"),bg="darkblue",fg="white")
        b3_3.place(x=700, y=250, width=150, height=20)
        
 # chatbot
    
        img7=Image.open(r"C:\Users\warar_3reymm5\OneDrive\Desktop\Face_Recognition\college_image\images (4).jpg")
        img7= img7.resize((200,150),Image.LANCZOS)
        self.photoimg7 = ImageTk.PhotoImage(img7)
        
        b4= Button(bg_lbl,image=self.photoimg7,cursor="hand2")
        b4.place(x=1000, y=100, width=150, height=150)
        
        b4_4= Button(bg_lbl,text="Chatbot",cursor="hand2",font=("times of roman",13,"bold"),bg="darkblue",fg="white")
        b4_4.place(x=1000, y=250, width=150, height=20)
 
      
     #Train Data button
     
        img8=Image.open(r"C:\Users\warar_3reymm5\OneDrive\Desktop\Face_Recognition\college_image\images (5).jpg")
        img8= img8.resize((200,150),Image.LANCZOS)
        self.phtoimg8 = ImageTk.PhotoImage(img8)
        
        b5= Button(bg_lbl,image=self.phtoimg8,cursor="hand2",command=self.train_data)
        b5.place(x=100, y=300, width=150, height=150)
        
        b5_1= Button(bg_lbl,text="Train Data ",cursor="hand2",command=self.train_data,font=("times of roman",13,"bold"),bg="darkblue",fg="white")
        b5_1.place(x=100, y=450, width=150, height=20)
       
       
    # Photos button 
    
        img9=Image.open(r"C:\Users\warar_3reymm5\OneDrive\Desktop\Face_Recognition\college_image\apps.22511.13510798887465976.aa07486c-11e7-4970-9980-e89d870ab5af.jpg")
        img9= img9.resize((200,150),Image.LANCZOS)
        self.photoimg9 = ImageTk.PhotoImage(img9)
        
        b6= Button(bg_lbl,image=self.photoimg9,cursor="hand2",command=self.open_img)
        b6.place(x=400, y=300, width=150, height=150)
        
        b6_2= Button(bg_lbl,text="Photos",cursor="hand2",command=self.open_img,font=("times of roman",13,"bold"),bg="darkblue",fg="white")
        b6_2.place(x=400, y=450, width=150, height=20)
        
     # Developer Button
    
        img10=Image.open(r"C:\Users\warar_3reymm5\OneDrive\Desktop\Face_Recognition\college_image\download (1).jpg")
        img10= img10.resize((200,150),Image.LANCZOS)
        self.photoimg10 = ImageTk.PhotoImage(img10)
        
        b7= Button(bg_lbl,image=self.photoimg10,cursor="hand2")
        b7.place(x=700, y=300, width=150, height=150)
        
        b7_3= Button(bg_lbl,text="Developer",cursor="hand2",font=("times of roman",13,"bold"),bg="darkblue",fg="white")
        b7_3.place(x=700, y=450, width=150, height=20)
        
 # Exit
    
        img11=Image.open(r"C:\Users\warar_3reymm5\OneDrive\Desktop\Face_Recognition\college_image\images (1).jpg")
        img11= img11.resize((200,150),Image.LANCZOS)
        self.photoimg11 = ImageTk.PhotoImage(img11)
        
        b8= Button(bg_lbl,image=self.photoimg11,cursor="hand2")
        b8.place(x=1000, y=300, width=150, height=150)
        
        b8_4= Button(bg_lbl,text="Exit",cursor="hand2",font=("times of roman",13,"bold"),bg="darkblue",fg="white")
        b8_4.place(x=1000, y=450, width=150, height=20)
        
    def open_img(self):
        os.startfile("data")    
     # =================function button===================
    def student_details(self):
          self.new_window=Toplevel(self.root)
          self.app=Student(self.new_window)
          
    def train_data(self):
          self.new_window=Toplevel(self.root)
          self.app=Train(self.new_window)
              
              
    def attendance_data(self):
          self.new_window=Toplevel(self.root)
          self.app=Attendance(self.new_window)
       
    def face_decetor_data(self):
          self.new_window=Toplevel(self.root)
          self.app=Face_Recognition(self.new_window)
                
if __name__ == "__main__":  #Entry point of the program
    root = Tk()  #Create the main application window
    obj = FaceRecognitionSystem(root)  #Create an instance of the FaceRecognitionSystem class
    root.mainloop()  #Start the GUI event loop
