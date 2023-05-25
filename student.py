from tkinter import*
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
import cv2

from PIL import Image, ImageTk

class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.wm_iconbitmap("icon.ico")
        self.root.title("Attendance Monitoring System")

        self.var_id = StringVar()
        self.var_name = StringVar()
        self.var_phone = StringVar()
        self.var_email = StringVar()
        self.var_gender = StringVar()
        self.var_roll = StringVar()
        self.var_dep = StringVar()
        self.var_course = StringVar()
        self.var_sem = StringVar()
        self.search_by = StringVar()
        self.var_search = StringVar()

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

        title = Label(bg_lab, text = "STUDENT DETAILS", font=("arial", 35, 'bold'), bg="white", fg='red')
        title.place(x = 0, y = 100, width = 1400, height = 50)

        main_frame = Frame(bg_lab, bd = 2, bg = "white",)
        main_frame.place(x = 20, y = 155, width = 1310, height = 550)

        # left Frame
        left_f = LabelFrame(main_frame, bg = "white", bd = 2, relief = RIDGE, text = "ENTER DETAILS", font = ('Arial', 12, 'bold'))
        left_f.place(x = 10, y = 10, width = 640, height = 530)

        img_left = Image.open("images/student_head.jpg")
        img_left = img_left.resize((1400, 100), Image.LANCZOS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        img_lab = Label(left_f, image = self.photoimg_left)
        img_lab.place(x = 10, y = 0, width = 620, height = 100)

        # course
        course_f = LabelFrame(left_f, bg = "white", bd = 2, relief = RIDGE, text = "Course Information: ",font = ('Arial', 12, 'bold'))
        course_f.place(x = 10, y = 110, width = 620, height = 100)

        # department
        dep_lab = Label(course_f, text = "Department: ", font = ('Arial', 12, 'bold'))
        dep_lab.grid(row = 0, column = 0,  padx = 10, sticky = W)

        dep_box = ttk.Combobox(course_f, textvariable = self.var_dep, font = ('Arial', 12, 'bold'), state = "readonly", width = 17)
        dep_box["values"] = ("Select", "Computer Science", "Mechanical", "Electrical", "Civil", "Management")
        dep_box.current(0)
        dep_box.grid(row = 0, column = 1, padx = 2, pady = 5, sticky = W)

        # course
        course_lab = Label(course_f, text = "Course: ", font = ('Arial', 12, 'bold'))
        course_lab.grid(row = 0, column = 2,  padx = 10, sticky = W)

        course_box = ttk.Combobox(course_f, textvariable = self.var_course, font = ('Arial', 12, 'bold'), state = "readonly", width = 17)
        course_box["values"] = ("Select", "B.Tech", "BCA", "MBA", "BBA", "B.Com", "MCA", "B.Sc")
        course_box.current(0)
        course_box.grid(row = 0, column = 3, padx = 2, pady = 5, sticky = W)

        # semester
        sem_lab = Label(course_f, text = "Semester: ", font = ('Arial', 12, 'bold'))
        sem_lab.grid(row = 1, column = 0,  padx = 10, sticky = W)

        sem_box = ttk.Combobox(course_f, textvariable = self.var_sem, font = ('Arial', 12, 'bold'), state = "readonly", width = 17)
        sem_box["values"] = ("Select", "1", "2", "3", "4", "5", "6", "7", "8")
        sem_box.current(0)
        sem_box.grid(row = 1, column = 1, padx = 2, pady = 5, sticky = W)

        # student info
        st_f = LabelFrame(left_f, bg = "white", bd = 2, relief = RIDGE, text = "Student Information: ", font = ('Arial', 12, 'bold'))
        st_f.place(x = 10, y = 220, width = 620, height = 280)

        # student id
        st_id = Label(st_f, text = "Student Id: ", font = ('Arial', 12, 'bold'))
        st_id.grid(row = 0, column = 0,  padx = 10, sticky = W)

        st_id_inp = ttk.Entry(st_f, textvariable = self.var_id, width = 19, font = ('Arial', 12, 'bold'))
        st_id_inp.grid(row = 0, column = 1, padx = 10, sticky=W)

        # student name
        st_name = Label(st_f, text = "Name: ", font = ('Arial', 12, 'bold'))
        st_name.grid(row = 0, column = 2,  padx = 10, pady = 5, sticky = W)

        st_name_inp = ttk.Entry(st_f, textvariable = self.var_name, width = 19, font = ('Arial', 12, 'bold'))
        st_name_inp.grid(row = 0, column = 3, padx = 10, pady = 5, sticky=W)

        # University Roll No
        st_rn = Label(st_f, text = "Roll No: ", font = ('Arial', 12, 'bold'))
        st_rn.grid(row = 1, column = 0,  padx = 10, pady = 5, sticky = W)

        st_rn_inp = ttk.Entry(st_f, textvariable = self.var_roll, width = 19, font = ('Arial', 12, 'bold'))
        st_rn_inp.grid(row = 1, column = 1, padx = 10, pady = 5, sticky=W)

        # Gender
        st_gn = Label(st_f, text = "Gender: ", font = ('Arial', 12, 'bold'))
        st_gn.grid(row = 1, column = 2, padx = 10, pady = 5, sticky = W)

        gen_box = ttk.Combobox(st_f, textvariable = self.var_gender, font = ('Arial', 12, 'bold'), state = "readonly", width = 17)
        gen_box["values"] = ("Select", "Male", "Female", "Others")
        gen_box.current(0)
        gen_box.grid(row = 1, column = 3, padx = 10, pady = 5, sticky = W)

        # Phone
        st_phone = Label(st_f, text = "Phone No: ", font = ('Arial', 12, 'bold'))
        st_phone.grid(row = 2, column = 0, padx = 10, pady = 5, sticky = W)

        st_phone_inp = ttk.Entry(st_f, textvariable = self.var_phone, width = 19, font = ('Arial', 12, 'bold'))
        st_phone_inp.grid(row = 2, column = 1, padx = 10, pady = 5, sticky=W)

        # email
        st_email = Label(st_f, text = "Email: ", font = ('Arial', 12, 'bold'))
        st_email.grid(row = 2, column = 2, padx = 10, pady = 5, sticky = W)

        st_email_inp = ttk.Entry(st_f, textvariable = self.var_email, width = 19, font = ('Arial', 12, 'bold'))
        st_email_inp.grid(row = 2, column = 3, padx = 10, pady = 5, sticky=W)

        # Radio btns
        st_photo = Label(st_f, text = "Take Photo: ", font = ('Arial', 12, 'bold'))
        st_photo.grid(row = 3, column = 0, padx = 10, pady = 5, sticky = W)

        self.var_radio1 = StringVar()
        radioBtn1 = ttk.Radiobutton(st_f, variable = self.var_radio1, text = "Yes", value = "Yes")
        radioBtn1.grid(row = 3, column = 1, padx = 10, pady = 5, sticky = W)

        radioBtn2 = ttk.Radiobutton(st_f, variable = self.var_radio1, text = "No", value = "No")
        radioBtn2.grid(row = 3, column = 2, padx = 10, pady = 5, sticky = W)

        # Buttons frame
        btn_f = LabelFrame(st_f, bg = "white", bd = 2, relief = RIDGE, font = ('Arial', 12, 'bold'))
        btn_f.place(x = 10, y = 150, width = 590, height = 90)

        save_btn = Button(btn_f, text = "Save", command = self.add_data, width = 17, font = ('Arial', 12, 'bold'), bg = "black", fg = "white", cursor = "hand2")
        save_btn.grid(row = 0, column = 0, padx = 7, pady = 5, sticky = W)

        update_btn = Button(btn_f, text = "Update", command = self.update_data, width = 17, font = ('Arial', 12, 'bold'), bg = "black", fg = "white", cursor = "hand2")
        update_btn.grid(row = 0, column = 1, padx = 7, pady = 5, sticky = W)

        del_btn = Button(btn_f, text = "Delete", command = self.del_data, width = 17, font = ('Arial', 12, 'bold'), bg = "black", fg = "white", cursor = "hand2")
        del_btn.grid(row = 0, column = 2, padx = 7, pady = 5, sticky = W)

        reset_btn = Button(btn_f, text = "Reset", command = self.reset_data, width = 17, font = ('Arial', 12, 'bold'), bg = "black", fg = "white", cursor = "hand2")
        reset_btn.grid(row = 1, column = 0, padx = 7, pady = 5, sticky = W)

        take_photo_btn = Button(btn_f, text = "Take Photo", command = self.generate_dataset, width = 17, font = ('Arial', 12, 'bold'), bg = "black", fg = "white", cursor = "hand2")
        take_photo_btn.grid(row = 1, column = 1, padx = 7, pady = 5, sticky = W)

        update_photo_btn = Button(btn_f, text = "Update Photo", width = 17, font = ('Arial', 12, 'bold'), bg = "black", fg = "white", cursor = "hand2")
        update_photo_btn.grid(row = 1, column = 2, padx = 7, pady = 5, sticky = W)


        # Right Frame
        right_f = LabelFrame(main_frame, bg = "white", bd = 2, relief = RIDGE, text = "DETAILS", font = ('Arial', 12, "bold"))
        right_f.place(x = 655, y = 10, width = 640, height = 530)

        img_right = Image.open("images/student_head.jpg")
        img_right = img_right.resize((1400, 100), Image.LANCZOS)
        self.photoimg_right = ImageTk.PhotoImage(img_right)

        img_lab = Label(right_f, image = self.photoimg_right)
        img_lab.place(x = 10, y = 0, width = 620, height = 100)


        # Search 
        search_f = LabelFrame(right_f, bg = "white", bd = 2, relief = RIDGE, text = "Search Information: ", font = ('Arial', 12, 'bold'))
        search_f.place(x = 10, y = 110, width = 620, height = 110)

        search_lab = Label(search_f, text = "Search By: ", font = ('Arial', 12, 'bold'))
        search_lab.grid(row = 0, column = 0,  padx = 10, sticky = W)

        search_box = ttk.Combobox(search_f, font = ('Arial', 12, 'bold'), textvariable = self.search_by, state = "readonly", width = 17)
        search_box["values"] = ("Select", "Student id", "Name", "Course")
        search_box.current(0)
        search_box.grid(row = 0, column = 1, padx = 2, pady = 5, sticky = W)

        search_inp = ttk.Entry(search_f, width = 20, textvariable = self.var_search, font = ('Arial', 12, 'bold'))
        search_inp.grid(row = 0, column = 2, padx = 10, pady = 5, sticky=W)

        search_btn = Button(search_f, text = "Search", command = self.fetch_filter_data, width = 17, font = ('Arial', 12, 'bold'), bg = "black", fg = "white", cursor = "hand2")
        search_btn.grid(row = 1, column = 1, padx = 7, pady = 5, sticky = W)

        showAll_btn = Button(search_f, text = "Show All", command = self.fetch_data, width = 17, font = ('Arial', 12, 'bold'), bg = "black", fg = "white", cursor = "hand2")
        showAll_btn.grid(row = 1, column = 2, padx = 7, pady = 5, sticky = W)

        # Table fram
        table_f = LabelFrame(right_f, bg = "white", bd = 2, relief = RIDGE, font = ('Arial', 12, 'bold'))
        table_f.place(x = 10, y = 225, width = 620, height = 280)

        scroll_x = ttk.Scrollbar(table_f, orient = HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_f, orient = VERTICAL)

        self.student_table = ttk.Treeview(table_f, column = ("id", "name", "phone", "email", "gender", "roll", "dep", "course", "sem"), xscrollcommand = scroll_x.set, yscrollcommand = scroll_y.set)
        scroll_x.pack(side = BOTTOM, fill = X)
        scroll_y.pack(side = RIGHT, fill = Y)
        scroll_x.config(command = self.student_table.xview)
        scroll_y.config(command = self.student_table.yview)

        self.student_table.heading(("id"), text = "Student id")
        self.student_table.heading(("name"), text = "Name")
        self.student_table.heading(("phone"), text = "Phone No.")
        self.student_table.heading(("email"), text = "Email id")
        self.student_table.heading(("gender"), text = "Gender")
        self.student_table.heading(("roll"), text = "Roll No.")
        self.student_table.heading(("dep"), text = "Department")
        self.student_table.heading(("course"), text = "Course")
        self.student_table.heading(("sem"), text = "Semester")
        self.student_table["show"] = "headings"

        self.student_table.column(("id"), width = 80)
        self.student_table.column(("name"), width = 120)
        self.student_table.column(("phone"), width = 100)
        self.student_table.column(("email"), width = 120)
        self.student_table.column(("gender"), width = 70)
        self.student_table.column(("roll"), width = 80)
        self.student_table.column(("dep"), width = 100)
        self.student_table.column(("course"), width = 80)
        self.student_table.column(("sem"), width = 80)

        self.student_table.pack(fill = BOTH, expand = 1)
        self.student_table.bind("<ButtonRelease>", self.get_cursor)
        self.fetch_data()


    # Declaration
    def add_data(self):
        if self.var_dep.get() == "Select" or self.var_course.get() == "Select" or self.var_name.get() == "" or self.var_id.get() == "":
            messagebox.showerror("Error", "All fields are required", parent = self.root)
        else:
            try:
                db = mysql.connector.connect(host = "localhost", username = "root", password = "1234", database = "attendance_system")
                my_cursor = db.cursor()
                my_cursor.execute("insert into student values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (
                    self.var_id.get(),
                    self.var_name.get(),
                    self.var_phone.get(),
                    self.var_email.get(),
                    self.var_gender.get(),
                    self.var_roll.get(),
                    self.var_dep.get(),
                    self.var_course.get(),
                    self.var_sem.get(),
                    self.var_radio1.get()
                ))
                db.commit()
                self.fetch_data()
                db.close()
                print(self.var_radio1.get())
                if self.var_radio1.get() == "Yes":
                    self.generate_dataset()
                messagebox.showinfo("Sucess", "Student Details has been added Successfully...", parent = self.root)
            except Exception as e:
                messagebox.showerror("Error", "Details not submitted...", parent = self.root)


    # Fetching
    def fetch_data(self):
        db = mysql.connector.connect(host = "localhost", username = "root", password = "1234", database = "attendance_system")
        my_cursor = db.cursor()
        my_cursor.execute("select * from student")
        data = my_cursor.fetchall()
        self.search_by.set("Select")
        self.var_search.set("")
        if len(data) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("", END, values = i)
            db.commit()
        db.close()

    # Fetching
    def fetch_filter_data(self):
        if self.search_by.get() == "Select" or self.var_search.get() == "":
            messagebox.showerror("Error", "All fields are required", parent = self.root)
        db = mysql.connector.connect(host = "localhost", username = "root", password = "1234", database = "attendance_system")
        my_cursor = db.cursor()
        if self.search_by.get() == "Student id":
            my_cursor.execute("select * from student where student_id = %s", (
                self.var_search.get(),
            ))
        elif self.search_by.get() == "Name":
            my_cursor.execute("select * from student where name = %s", (
                self.var_search.get(),
            ))
        else:
            my_cursor.execute("select * from student where course = %s", (
                self.var_search.get(),
            ))
        data = my_cursor.fetchall()

        if len(data) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("", END, values = i)
            db.commit()
        else:
            self.student_table.delete(*self.student_table.get_children())
            messagebox.showerror("Error", "No records found", parent = self.root)
        db.close()

    #get cursor
    def get_cursor(self, event = ""):
        cur_foc = self.student_table.focus()
        cont = self.student_table.item(cur_foc)
        data = cont["values"]
        # print(data)

        self.var_id.set(data[0])
        self.var_name.set(data[1])
        self.var_phone.set(data[2])
        self.var_email.set(data[3])
        self.var_gender.set(data[4])
        self.var_roll.set(data[5])
        self.var_dep.set(data[6])
        self.var_course.set(data[7])
        self.var_sem.set(data[8])
        self.var_radio1.set(data[9])
            
    # update
    def update_data(self):
        if self.var_dep.get() == "Select" or self.var_course.get() == "Select" or self.var_name.get() == "" or self.var_id.get() == "":
            messagebox.showerror("Error", "All fields are required", parent = self.root)
        else:
            try:
                flag = messagebox.askyesno("Update", "Are you sure you want to update..", parent = self.root)
                if flag > 0:
                    db = mysql.connector.connect(host = "localhost", username = "root", password = "1234", database = "attendance_system")
                    my_cursor = db.cursor()
                    my_cursor.execute("update student set name = %s, phone = %s, email = %s, gender = %s, roll = %s, dep = %s, course = %s, sem = %s, photo_sample = %s where student_id = %s", (
                        self.var_name.get(),
                        self.var_phone.get(),
                        self.var_email.get(),
                        self.var_gender.get(),
                        self.var_roll.get(),
                        self.var_dep.get(),
                        self.var_course.get(),
                        self.var_sem.get(),
                        self.var_radio1.get(),
                        self.var_id.get()
                    ))
                    db.commit()
                    self.fetch_data()
                    db.close()
                    messagebox.showinfo("Sucess", "Student Details has been updated successfully...", parent = self.root)
                else:
                    return
            except Exception as e:
                messagebox.showerror("Error", "Details not updated...", parent = self.root)

    # Delete
    def del_data(self):
        if self.var_id.get() == "":
            messagebox.showerror("Error", "Student Id is required to delete", parent = self.root)
        else:
            try:
                flag = messagebox.askyesno("Delete", "Are you sure you want to delete..", parent = self.root)
                if flag > 0:
                    db = mysql.connector.connect(host = "localhost", username = "root", password = "1234", database = "attendance_system")
                    my_cursor = db.cursor()
                    my_cursor.execute("delete from student where student_id = %s", (
                            self.var_id.get(),
                        ))
                    db.commit()
                    self.fetch_data()
                    db.close()
                    messagebox.showinfo("Sucess", "Student Details has been deleted Successfully...", parent = self.root)
                else:
                    return
            except Exception as e:
                messagebox.showerror("Error", "Details not deleted...", parent = self.root)

    # reset
    def reset_data(self):
        self.var_id.set(""),
        self.var_name.set(""),
        self.var_phone.set(""),
        self.var_email.set(""),
        self.var_gender.set("Select"),
        self.var_roll.set(""),
        self.var_dep.set("Select"),
        self.var_course.set("Select"),
        self.var_sem.set("Select"),
        self.var_radio1.set("")

    # generate dataset
    def generate_dataset(self):
        if self.var_dep.get() == "Select" or self.var_course.get() == "Select" or self.var_name.get() == "" or self.var_id.get() == "":
            messagebox.showerror("Error", "All fields are required", parent = self.root)
        else:
            try:
                db = mysql.connector.connect(host = "localhost", username = "root", password = "1234", database = "attendance_system")
                my_cursor = db.cursor()
                my_cursor.execute("select * from student")
                myresult = my_cursor.fetchall()
                
                id_t =0
                # print(myresult)
                #flag = False
                for x in myresult:
                    id_t =id_t+1
                my_cursor.execute("update student set name = %s, phone = %s, email = %s, gender = %s, roll = %s, dep = %s, course = %s, Sem = %s, photo_sample = %s where student_id = %s", (
                        self.var_name.get(),
                        self.var_phone.get(),
                        self.var_email.get(),
                        self.var_gender.get(),
                        self.var_roll.get(),
                        self.var_dep.get(),
                        self.var_course.get(),
                        self.var_sem.get(),
                        self.var_radio1.get(),
                        self.var_id.get()==id_t+1
                ))

                db.commit()
                self.fetch_data()
                self.reset_data()
                db.close()
                # print("debug")

                #if flag == True:
                face_cls = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_crop(img):
                    img_t = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces = face_cls.detectMultiScale(img_t, 1.3, 5)

                    for (x, y, w, h) in faces:
                        face_crop = img[y: y + h, x: x + w]
                        return face_crop
                cam = cv2.VideoCapture(0)
                img_id = 0
                while True:
                    ret, myframe = cam.read()
                    if face_crop(myframe) is not None:
                        img_id += 1
                        face = cv2.resize(face_crop(myframe), (450, 450))
                        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                        file_path = "data_set/user." + str(id_t) + "." + str(img_id) + ".jpg"
                        cv2.imwrite(file_path,face)
                        cv2.putText(face, str(img_id), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
                        cv2.imshow("Cropped Face",face)
        
                    if cv2.waitKey(1) == 13 or int(img_id) == 100:
                        break

                cam.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Sucess", "Data Set Generated Successfully...")

               # else:
                #    messagebox.showerror("Error", "Student not present...", parent = self.root)

            except Exception as e:
                messagebox.showerror("Error", f"Due To: {str(e)}", parent = self.root)

if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()


