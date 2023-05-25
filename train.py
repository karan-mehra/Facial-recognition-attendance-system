from tkinter import*
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
import cv2

from PIL import Image, ImageTk
import os
import numpy as np

class Train:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.wm_iconbitmap("icon.ico")
        self.root.title("Attendance Monitoring System")

        img1 = Image.open("images/train_bg.jpg")
        img1 = img1.resize((1400, 300), Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        top_lab = Label(self.root, image = self.photoimg1)
        top_lab.place(x = 0, y = 0, width = 1400, height = 300)

        title = Label(self.root, text = "TRAIN DATA SET", font=("arial", 35, 'bold'), bg="white", fg='red')
        title.place(x = 0, y = 300, width = 1400, height = 50)

        btn_1 = Button(self.root, text = "Click here to train...", command = self.train_data, width = 17, font = ('Arial', 20, 'bold'), bg = "red", fg = "white", cursor = "hand2")
        btn_1.place(x = 0, y = 350, width = 1400, height = 65)

        img2 = Image.open("images/train_bg.jpg")
        img2 = img2.resize((1400, 300), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        bottom_lab = Label(self.root, image = self.photoimg2)
        bottom_lab.place(x = 0, y = 415, width = 1400, height = 300)

    def train_data(self):
        data_dir = ("data_set")
        path = [os.path.join(data_dir, file) for file in os.listdir(data_dir)]

        faces = []
        ids = []

        for img in path:
            image = Image.open(img).convert('L')
            imageNp = np.array(image, 'uint8')
            id = int(os.path.split(img)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training", imageNp)
            cv2.waitKey(1) == 13
        ids = np.array(ids)


        classifier = cv2.face.LBPHFaceRecognizer_create()
        classifier.train(faces, ids)
        classifier.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Success", "Training data set done successfully...")



if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()


