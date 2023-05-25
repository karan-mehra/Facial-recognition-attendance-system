from csv import writer
from tkinter import*
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
import cv2
from time import strftime
from datetime import datetime

from PIL import Image, ImageTk
import csv
import numpy as np

class Face_recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.wm_iconbitmap("icon.ico")
        self.root.title("Attendance Monitoring System")

        img1 = Image.open("images/face_recognize.jpg")
        img1 = img1.resize((1400, 670), Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        bg_lab = Label(self.root, image = self.photoimg1)
        bg_lab.place(x = 0, y = 50, width = 1380, height = 670)

        title = Label(self.root, text = "FACE RECOGNIZATION", font=("arial", 35, 'bold'), bg="yellow", fg='red')
        title.place(x = 0, y = 0, width = 1400, height = 50)

        btn_1 = Button(bg_lab, text = "Click here to Recognize...", command = self.recognize_face, width = 17, font = ('Arial', 15, 'bold'), bg = "red", fg = "white", cursor = "hand2")
        btn_1.place(x = 220, y = 420, width = 303, height = 43)

    def take_attendance(self, var1, var2, var3, var4,var5):
        with open("attendance.csv", "r+", newline = '\n') as f:
            dataList = f.readlines()
            curr_file = writer(f)
            name_list = []
            for i in dataList:
                en = i.split((","))
                name_list.append(en[0])

            if((var1 not in name_list) and (var2 not in name_list) and (var3 not in name_list) and(var4 not in name_list)):
                curr = datetime.now()
                d1 = strftime("%d/%m/%Y")
                d2 = curr.strftime("%H:%M:%S")
                curr_file.writerow([var1, var2, var3, var4,var5, d1, d2, "Present"])

    def recognize_face(self):
        def draw_rect(img, classifier, scl_fac, minNeighbour, col, txt, clf):
            gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            feature = classifier.detectMultiScale(gray_img, scl_fac, minNeighbour)

            coord = []
            for (x, y, w, h) in feature:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
                id, predict = clf.predict(gray_img[y: y + h, x: x + w])
                conf = int((100 * (1 - predict / 300)))

                db = mysql.connector.connect(host = "localhost", username = "root", password = "1234", database = "attendance_system")
                my_cursor = db.cursor()
                
                my_cursor.execute("select student_id from student where student_id = "+str(id))
                var1 = my_cursor.fetchone()
                #print(var2)
                var1 = "+".join(var1)

                my_cursor.execute("select name from student where student_id = "+str(id))
                var2 = my_cursor.fetchone()
                #print(var4)
                var2 = "+".join(var2)

                my_cursor.execute("select sem from student where student_id = "+str(id))
                var3 = my_cursor.fetchone()
                #print(var5)
                var3 = "+".join(var3)

                my_cursor.execute("select dep from student where student_id = "+str(id))
                var4 = my_cursor.fetchone()
                var4 = "+".join(var4)

                my_cursor.execute("select course from student where student_id = "+str(id))
                var5 = my_cursor.fetchone()
                var5 = "+".join(var5)
                

                # db.close()

                if conf > 77:
                    
                    cv2.putText(img, f"ID: {var1}", (x, y - 80), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 2)
                    cv2.putText(img, f"Name: {var2}", (x, y - 60), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 2)
                    cv2.putText(img, f"Course: {var5}", (x, y - 40), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 2)
                    self.take_attendance(var1, var2, var3,var4,var5)
                else:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 3)
                    cv2.putText(img, "Unknown", (x, y - 10), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 0, 0), 2)

                coord = [x, y, w, h]
            return coord

        def recognize(img, clf, faceCascade):
            coord = draw_rect(img, faceCascade, 1.1, 10, (255, 25, 255), "Face", clf)
            return img

        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("Classifier.xml")

        cam = cv2.VideoCapture(0)
        while True:
            ret, img = cam.read()
            img = recognize(img, clf, faceCascade)
            cv2.imshow("Face Recognition", img)

            if cv2.waitKey(1) == 13:
                break
        cam.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    root = Tk()
    obj = Face_recognition(root)
    root.mainloop()
