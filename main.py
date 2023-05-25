from tkinter import*
from tkinter import ttk
import tkinter

from PIL import Image, ImageTk
from student import Student
from train import Train
from attendance import Attendance
from face_recognization import Face_recognition
import os

from time import strftime
from datetime import datetime

class Attendace_Monitoring:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.wm_iconbitmap("icon.ico")
        self.root.title("Attendance Monitoring System")

        img1 = Image.open("images/background.jpg")
        img1 = img1.resize((1400, 900), Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        bg_lab = Label(self.root, image = self.photoimg1)
        bg_lab.place(x = 0, y = 0, width = 1400, height = 900)

        img2 = Image.open("images/border.jpg")
        img2 = img2.resize((1400, 100), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        first_lab = Label(self.root, image = self.photoimg2)
        first_lab.place(x = 0, y = 0, width = 1400, height = 100)

        title = Label(bg_lab, text = "ATTENDANCE MONITORING SYSTEM", font=("arial", 35, 'bold'), bg="white", fg='red')
        title.place(x = 0, y = 100, width = 1365, height = 50)

        def show_time():
            st = strftime("%H:%M:%S")
            lab.config(text = st)
            lab.after(1000, show_time)

        lab = Label(title, font=("arial", 15, 'bold'), bg="white", fg='black')
        lab.place(x = 0, y = 0, width = 120, height = 50)
        show_time()

        # BUTTONS
        # student details
        img3 = Image.open("images/student.jpg")
        img3 = img3.resize((300, 180), Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        btn1 = Button(bg_lab, command = self.student_details, image = self.photoimg3, cursor = "hand2")
        btn1.place(x = 117, y = 180, width = 300, height = 180)

        btn1_lab = Button(bg_lab, command = self.student_details, text = "Student Details", font=("arial", 12, 'bold'), bg="white", fg='blue')
        btn1_lab.place(x = 117, y = 360, width = 300, height = 30)


        # Face details
        img4 = Image.open("images/faces.jpg")
        img4 = img4.resize((300, 180), Image.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        btn2 = Button(bg_lab, image = self.photoimg4, command = self.face_recognization, cursor = "hand2")
        btn2.place(x = 117, y = 420, width = 300, height = 180)

        btn2_lab = Button(bg_lab, text = "Detect Face", command = self.face_recognization, font=("arial", 12, 'bold'), bg="white", fg='blue')
        btn2_lab.place(x = 117, y = 600, width = 300, height = 30)

        # Attendance details
        img5 = Image.open("images/attendance.jpg")
        img5 = img5.resize((300, 180), Image.LANCZOS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        btn3 = Button(bg_lab, image = self.photoimg5, command = self.attendance, cursor = "hand2")
        btn3.place(x = 533, y = 180, width = 300, height = 180)

        btn3_lab = Button(bg_lab, text = "Attendance", font=("arial", 12, 'bold'), command = self.attendance, bg="white", fg='blue')
        btn3_lab.place(x = 533, y = 360, width = 300, height = 30)

        # Photos details
        img6 = Image.open("images/photos.jpg")
        img6 = img6.resize((300, 180), Image.LANCZOS)
        self.photoimg6 = ImageTk.PhotoImage(img6)

        btn4 = Button(bg_lab, image = self.photoimg6, command = self.open_img, cursor = "hand2")
        btn4.place(x = 533, y = 420, width = 300, height = 180)

        btn4_lab = Button(bg_lab, text = "Photos", command = self.open_img, font=("arial", 12, 'bold'), bg="white", fg='blue')
        btn4_lab.place(x = 533, y = 600, width = 300, height = 30)

        # Train data details
        img7 = Image.open("images/train.jpg")
        img7 = img7.resize((300, 300), Image.LANCZOS)
        self.photoimg7 = ImageTk.PhotoImage(img7)

        btn5 = Button(bg_lab, image = self.photoimg7, command = self.train_dataset, cursor = "hand2")
        btn5.place(x = 950, y = 180, width = 300, height = 180)

        btn5_lab = Button(bg_lab, text = "Training", command = self.train_dataset, font=("arial", 12, 'bold'), bg="white", fg='blue')
        btn5_lab.place(x = 950, y = 360, width = 300, height = 30)

        # Exit details
        img10 = Image.open("images/exit.jpg")
        img10 = img10.resize((300, 180), Image.LANCZOS)
        self.photoimg10 = ImageTk.PhotoImage(img10)

        btn8 = Button(bg_lab, image = self.photoimg10, command = self.exit_win, cursor = "hand2")
        btn8.place(x = 950, y = 420, width = 300, height = 180)

        btn8_lab = Button(bg_lab, text = "Exit", command = self.exit_win, font=("arial", 12, 'bold'), bg="white", fg='blue')
        btn8_lab.place(x = 950, y = 600, width = 300, height = 30)

    # Working of Buttons

    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)

    def train_dataset(self):
        self.new_window = Toplevel(self.root)
        self.app = Train(self.new_window)

    def face_recognization(self):
        self.new_window = Toplevel(self.root)
        self.app = Face_recognition(self.new_window)

    def attendance(self):
        self.new_window = Toplevel(self.root)
        self.app = Attendance(self.new_window)

    def exit_win(self):
        self.isExit = tkinter.messagebox.askyesno("Attendance Monitoring System", "Are you sure to exit", parent = self.root)
        if self.isExit > 0:
            self.root.destroy()
        else:
            return

        

    # fetching photos
    def open_img(self):
        os.startfile("data_set")


if __name__ == "__main__":
    root = Tk()
    obj = Attendace_Monitoring(root)
    root.mainloop()


