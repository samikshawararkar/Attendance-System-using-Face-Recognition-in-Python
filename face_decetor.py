from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
from time import strftime
from datetime import datetime
import cv2
import os
import numpy as np
import traceback

class Face_Recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1920x1080+0+0")  # Adjusted for full-screen width
        self.root.title("Face Recognition System")
        
        # Get screen width and height
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        # Title label
        title_lbl = Label(self.root, text="FACE RECOGNITION", font=("times new roman", 25, "bold"), bg="orange", fg="black")
        title_lbl.place(x=0, y=0, width=screen_width, height=45)

        # Resize images based on screen size
        img_top = Image.open(r"C:\Users\warar_3reymm5\Downloads\1628243597666college-images\college_images\face_detector1.jpg")
        img_top = img_top.resize((int(screen_width * 0.45), int(screen_height * 0.65)), Image.LANCZOS)  # Resize dynamically
        self.photoimg_top = ImageTk.PhotoImage(img_top)
        Label(self.root, image=self.photoimg_top).place(x=0, y=55, width=int(screen_width * 0.45), height=int(screen_height * 0.65))

        img_bottom = Image.open(r"C:\Users\warar_3reymm5\Downloads\1628243597666college-images\college_images\facial_0.jpeg")
        img_bottom = img_bottom.resize((int(screen_width * 0.55), int(screen_height * 0.65)), Image.LANCZOS)  # Resize dynamically
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)
        Label(self.root, image=self.photoimg_bottom).place(x=int(screen_width * 0.45), y=55, width=int(screen_width * 0.55), height=int(screen_height * 0.65))

        # Button for face recognition - Positioned towards the bottom center
        button_width = 250
        button_height = 40
        button_y_position = screen_height - 150  # Ensures there’s space between button and bottom of window
        b1_1 = Button(self.root, text="FACE RECOGNITION", cursor="hand2", font=("times new roman", 18, "bold"), bg="darkgreen", fg="white", command=self.face_recog)
        b1_1.place(x=(screen_width - button_width) // 2, y=button_y_position, width=button_width, height=button_height)

    def mark_attendence(self, i, r, n, d):
        with open("ATTENDENCE.csv", "r+", newline="\n") as f:
            myDataList = f.readlines()
            name_list = [line.split(",")[0] for line in myDataList]

            if i not in name_list:
                now = datetime.now()
                dtString = now.strftime("%H:%M:%S")
                d1 = now.strftime("%d/%m/%Y")
                f.write(f"\n{i},{r},{n},{d},{dtString},{d1},Present")

    def face_recog(self):
        try:
            if not os.path.exists("haarcascade_frontalface_default.xml") or not os.path.exists("classifier.xml"):
                messagebox.showerror("Error", "Missing required files!")
                return

            faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
            clf = cv2.face.LBPHFaceRecognizer_create()
            clf.read("classifier.xml")

            video_cap = cv2.VideoCapture(0)
            try:
                while True:
                    ret, img = video_cap.read()
                    if not ret:
                        break

                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces = faceCascade.detectMultiScale(gray, 1.1, 10)

                    for (x, y, w, h) in faces:
                        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
                        id, predict = clf.predict(gray[y:y + h, x:x + w])
                        confidence = int(100 * (1 - predict / 300))

                        if confidence > 77:
                            cv2.putText(img, f"ID: {id}", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                        else:
                            cv2.putText(img, "Unknown", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 0, 255), 3)

                    cv2.imshow("Face Recognition", img)
                    if cv2.waitKey(1) == 13:
                        break
            finally:
                video_cap.release()
                cv2.destroyAllWindows()

        except Exception as e:
            messagebox.showerror("Error", traceback.format_exc())

if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()


