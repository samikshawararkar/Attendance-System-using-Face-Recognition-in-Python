from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import os
import numpy as np
import cv2

class Train:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x750+0+0")
        self.root.title("Face Recognition System")

        # Title Label
        title_lbl = Label(self.root, text="TRAIN DATASET", font=("times new roman", 20, "bold"), bg="yellow", fg="black")
        title_lbl.place(x=-320, y=0, width=1920, height=35)

        # Top Image
        img_top = Image.open(r"C:\Users\warar_3reymm5\OneDrive\Desktop\Face_Recognition\college_image\facial-recognition-technology-scan-detect-people-face-identification_31965-24741.jpg")
        img_top = img_top.resize((1300, 300), Image.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)
        f_lbl3 = Label(self.root, image=self.photoimg_top)
        f_lbl3.place(x=0, y=30, width=1300, height=300)

        # Train Button
        b1_1 = Button(self.root, text="TRAIN DATA", cursor="hand2", command=self.train_classifier,
                      font=("times new roman", 20, "bold"), bg="green", fg="white")
        b1_1.place(x=0, y=330, width=1300, height=35)

        # Bottom Image
        img_bottom = Image.open(r"C:\Users\warar_3reymm5\OneDrive\Desktop\Face_Recognition\college_image\collage-large-group-.png")
        img_bottom = img_bottom.resize((1300, 290), Image.LANCZOS)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)
        f_lbl3 = Label(self.root, image=self.photoimg_bottom)
        f_lbl3.place(x=0, y=360, width=1300, height=290)

    def train_classifier(self):
        data_dir = os.path.join(os.getcwd(), "data")  # Ensure the correct path
        if not os.path.exists(data_dir):
            messagebox.showerror("Error", "Data directory not found!")
            return

        faces = []
        ids = []
        image_paths = [os.path.join(data_dir, file) for file in os.listdir(data_dir) if file.endswith('.jpg') or file.endswith('.png')]

        if not image_paths:
            messagebox.showerror("Error", "No images found in dataset folder!")
            return

        for image in image_paths:
            try:
                img = Image.open(image).convert("L")  # Convert to grayscale
                imageNp = np.array(img, 'uint8')
                id = int(os.path.split(image)[1].split('.')[1])  # Extract ID

                faces.append(imageNp)
                ids.append(id)
                cv2.imshow("Training", imageNp)

                if cv2.waitKey(1) & 0xFF == ord('q'):  # Allow exiting loop with 'q'
                    break

                print(f"Processing image: {image}")

            except Exception as e:
                print(f"Error processing image {image}: {e}")

        ids = np.array(ids)

        # Train classifier and save model
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces, ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result", "Training datasets completed successfully!")

if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()
