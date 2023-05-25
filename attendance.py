from tkinter import*
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
import cv2

import shutil
from tempfile import NamedTemporaryFile, TemporaryFile
import os
import csv
from tkinter import filedialog

from PIL import Image, ImageTk

my_list = []

class Attendance:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.wm_iconbitmap("icon.ico")
        self.root.title("Attendance:")

        self.var_id = StringVar()
        self.var_name = StringVar()
        self.var_sem = StringVar()
        self.var_dep = StringVar()
        self.var_course = StringVar()
        self.var_date = StringVar()
        self.var_time = StringVar()
        self.var_status = StringVar()

        bg_lab = LabelFrame(self.root, bg = "black", bd = 2, relief = RIDGE)
        bg_lab.place(x = 0, y = 0, width = 1400, height = 900)

        img2 = Image.open("images/border.jpg")
        img2 = img2.resize((1400, 100), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        first_lab = Label(self.root, image = self.photoimg2)
        first_lab.place(x = 0, y = 0, width = 1400, height = 100)

        title = Label(bg_lab, text = "ATTENDANCE RECORD", font=("arial", 35, 'bold'), bg="white", fg='red')
        title.place(x = 0, y = 100, width = 1400, height = 50)

        main_frame = Frame(bg_lab, bd = 2, bg = "white",)
        main_frame.place(x = 20, y = 155, width = 1310, height = 550)

        # left Frame
        left_f = LabelFrame(main_frame, bg = "white", bd = 2, relief = RIDGE, text = "STUDENTS DETAILS", font = ('Arial', 12, 'bold'))
        left_f.place(x = 10, y = 10, width = 640, height = 530)

        img_left = Image.open("images/attendance.jpg")
        img_left = img_left.resize((1400, 100), Image.LANCZOS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        img_lab = Label(left_f, image = self.photoimg_left)
        img_lab.place(x = 10, y = 0, width = 620, height = 100)

        # input
        input_f = LabelFrame(left_f, bg = "white", bd = 2, relief = RIDGE, font = ('Arial', 12, 'bold'))
        input_f.place(x = 10, y = 110, width = 620, height = 300)

        # student id
        st_id = Label(input_f, text = "Student Id: ", font = ('Arial', 12, 'bold'))
        st_id.grid(row = 0, column = 0,  padx = 10, pady = 10, sticky = W)

        st_id_inp = ttk.Entry(input_f, width = 19, textvariable = self.var_id, font = ('Arial', 12, 'bold'))
        st_id_inp.grid(row = 0, column = 1, padx = 10, pady = 10, sticky=W)

        # student name
        st_name = Label(input_f, text = "Name: ", font = ('Arial', 12, 'bold'))
        st_name.grid(row = 0, column = 2,  padx = 10, pady = 10, sticky = W)

        st_name_inp = ttk.Entry(input_f, textvariable = self.var_name, width = 19, font = ('Arial', 12, 'bold'))
        st_name_inp.grid(row = 0, column = 3, padx = 10, pady = 10, sticky=W)

        # Sem no
        sem = Label(input_f, text = "Semester: ", font = ('Arial', 12, 'bold'))
        sem.grid(row = 1, column = 0,  padx = 10, pady = 10, sticky = W)

        sem_inp = ttk.Combobox(input_f, textvariable = self.var_sem, font = ('Arial', 12, 'bold'), state = "readonly", width = 17)
        sem_inp["values"] = ("Select", "Semester-1", "Semester-2", "Semester-3", "Semester-4", "Semester-5", "Semester-6", "Semester-7", "Semester-8",)
        sem_inp.current(0)
        sem_inp.grid(row = 1, column = 1, padx = 10, pady = 10, sticky=W)

        # date
        dt = Label(input_f, text = "Date: ", font = ('Arial', 12, 'bold'))
        dt.grid(row = 1, column = 2,  padx = 10, pady = 10, sticky = W)

        dt_inp = ttk.Entry(input_f, textvariable = self.var_date, width = 19, font = ('Arial', 12, 'bold'))
        dt_inp.grid(row = 1, column = 3, padx = 10, pady = 10, sticky=W)

        # Department
        dep = Label(input_f, text = "Department: ", font = ('Arial', 12, 'bold'))
        dep.grid(row = 2, column = 0,  padx = 10, pady = 10, sticky = W)

        dep_inp = ttk.Entry(input_f, textvariable = self.var_dep, width = 19, font = ('Arial', 12, 'bold'))
        dep_inp.grid(row = 2, column = 1, padx = 10, pady = 10, sticky=W)

        # time
        time = Label(input_f, text = "Time: ", font = ('Arial', 12, 'bold'))
        time.grid(row = 2, column = 2,  padx = 10, pady = 10, sticky = W)

        time_inp = ttk.Entry(input_f, textvariable = self.var_time, width = 19, font = ('Arial', 12, 'bold'))
        time_inp.grid(row = 2, column = 3, padx = 10, pady = 10, sticky=W)

        # Course
        course = Label(input_f, text = "Course: ", font = ('Arial', 12, 'bold'))
        course.grid(row = 3, column = 0,  padx = 10, pady = 10, sticky = W)

        course_inp = ttk.Entry(input_f, textvariable = self.var_course, width = 19, font = ('Arial', 12, 'bold'))
        course_inp.grid(row = 3, column = 1, padx = 10, pady = 10, sticky=W)

        # Attendance
        att_lab = Label(input_f, text = "Status: ", font = ('Arial', 12, 'bold'))
        att_lab.grid(row = 3, column = 2,  padx = 10, pady = 10, sticky = W)

        att_box = ttk.Combobox(input_f, textvariable = self.var_status, font = ('Arial', 12, 'bold'), state = "readonly", width = 17)
        att_box["values"] = ("Select", "Present", "Absent")
        att_box.current(0)
        att_box.grid(row = 3, column = 3, padx = 10, pady = 10, sticky = W)


        # Buttons frame
        btn_f = LabelFrame(input_f, bg = "white", bd = 2, relief = RIDGE, font = ('Arial', 12, 'bold'))
        btn_f.place(x = 10, y = 200, width = 590, height = 80)

        import_btn = Button(btn_f, text = "Import csv", command = self.import_csv, width = 12, font = ('Arial', 12, 'bold'), bg = "black", fg = "white", cursor = "hand2")
        import_btn.grid(row = 0, column = 0, padx = 7, pady = 20, sticky = W)

        export_btn = Button(btn_f, text = "Export csv", command = self.export_csv, width = 12, font = ('Arial', 12, 'bold'), bg = "black", fg = "white", cursor = "hand2")
        export_btn.grid(row = 0, column = 1, padx = 7, pady = 20, sticky = W)

        update_btn = Button(btn_f, text = "Update", width = 12, font = ('Arial', 12, 'bold'), command = self.update_attendance, bg = "black", fg = "white", cursor = "hand2")
        update_btn.grid(row = 0, column = 2, padx = 7, pady = 20, sticky = W)

        reset_btn = Button(btn_f, text = "Reset", command = self.reset_data, width = 12, font = ('Arial', 12, 'bold'), bg = "black", fg = "white", cursor = "hand2")
        reset_btn.grid(row = 0, column = 3, padx = 7, pady = 20, sticky = W)


        # Right Frame
        right_f = LabelFrame(main_frame, bg = "white", bd = 2, relief = RIDGE, text = "ATTENDANCE DETAILS", font = ('Arial', 12, "bold"))
        right_f.place(x = 655, y = 10, width = 640, height = 530)

        # Table frame
        table_f = LabelFrame(right_f, bg = "white", bd = 2, relief = RIDGE, font = ('Arial', 12, 'bold'))
        table_f.place(x = 10, y = 7, width = 620, height = 490)

        scroll_x = ttk.Scrollbar(table_f, orient = HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_f, orient = VERTICAL)

        self.atteendance_table = ttk.Treeview(table_f, column = ("st_id", "name", "sem", "dep", "course", "date", "time", "status"), xscrollcommand = scroll_x.set, yscrollcommand = scroll_y.set)

        scroll_x.pack(side = BOTTOM, fill = X)
        scroll_y.pack(side = RIGHT, fill = Y)

        scroll_x.config(command = self.atteendance_table.xview)
        scroll_y.config(command = self.atteendance_table.yview)

        self.atteendance_table.heading("st_id", text = "Student Id")
        self.atteendance_table.heading("name", text = "Name")
        self.atteendance_table.heading("sem", text = "Semester")
        self.atteendance_table.heading("dep", text = "Department")
        self.atteendance_table.heading("course", text = "Course")
        self.atteendance_table.heading("date", text = "Date")
        self.atteendance_table.heading("time", text = "Time")
        self.atteendance_table.heading("status", text = "Status")

        self.atteendance_table["show"] = "headings"

        self.atteendance_table.column(("st_id"), width = 80)
        self.atteendance_table.column(("name"), width = 130)
        self.atteendance_table.column(("sem"), width = 80)
        self.atteendance_table.column(("dep"), width = 130)
        self.atteendance_table.column(("course"), width = 80)
        self.atteendance_table.column(("date"), width = 80)
        self.atteendance_table.column(("time"), width = 70)
        self.atteendance_table.column(("status"), width = 120)

        self.atteendance_table.pack(fill = BOTH, expand = 1)

        self.atteendance_table.bind("<ButtonRelease>", self.get_cursor)

    def update_attendance(self):
        try:
            fileName = "attendance.csv"
            tmp = NamedTemporaryFile(mode="w", delete = False)
            global my_list
            my_list.clear()
            with open(fileName, "r", newline = '') as f, tmp:
                reader = csv.reader(f)
                tmp.truncate(0)
                writer = csv.writer(tmp, lineterminator='\n')
                for i in reader:
                    if len(i) != 0:
                        if i[0] == self.var_id.get():
                            i[1], i[2], i[3], i[4], i[5], i[6], i[7] = self.var_name.get(), self.var_sem.get(), self.var_dep.get(), self.var_course.get(), self.var_date.get(), self.var_time.get(), self.var_status.get()
                        i = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7]]
                        writer.writerow(i)
                        my_list.append(i)
                self.import_data(my_list)
            shutil.move(tmp.name, fileName)
            messagebox.showinfo("Sucess", "Data updated successfully...", parent = self.root)
        except Exception as e:
            messagebox.showerror("Error", "Data not updated...", parent = self.root)
        

    def import_data(self, rows):
        self.atteendance_table.delete(*self.atteendance_table.get_children())
        for i in rows:
            self.atteendance_table.insert("", END, values = i)

    def import_csv(self):
        global my_list
        my_list.clear()
        file_name = filedialog.askopenfilename(initialdir = os.getcwd(), title = "Opening Csv...", filetypes = (("CSV File", "*csv"), ("ALL File", "*.*")), parent = self.root)
        with open(file_name) as f:
            csvread = csv.reader(f, delimiter = ",")
            for i in csvread:
                my_list.append(i)
            self.import_data(my_list)

    def export_csv(self):
        try:
            if len(my_list) < 1:
                messagebox.showerror("Error", "No data found...", parent = self.root)
                return False
            file_name = filedialog.asksaveasfilename(initialdir = os.getcwd(), title = "Opening Csv...", filetypes = (("CSV File", "*csv"), ("ALL File", "*.*")), parent = self.root)
            with open(file_name, mode = "w", newline = '\n') as f:
                ex_file = csv.writer(f, delimiter = ",")
                for i in my_list:
                    ex_file.writerow(i)
                messagebox.showinfo("Success", "Data is exported successfully...")
        except Exception as e:
            messagebox.showerror("Error", "Data not exported...", parent = self.root)

    def get_cursor(self, event = ""):
        cur_foc = self.atteendance_table.focus()
        cont = self.atteendance_table.item(cur_foc)
        data = cont["values"]

        self.var_id.set(data[0])
        self.var_name.set(data[1])
        self.var_sem.set(data[2])
        self.var_dep.set(data[3])
        self.var_course.set(data[4])
        self.var_date.set(data[5])
        self.var_time.set(data[6])
        self.var_status.set(data[7])

    # reset
    def reset_data(self):
        self.var_id.set(""),
        self.var_name.set(""),
        self.var_sem.set("Select"),
        self.var_dep.set(""),
        self.var_course.set(""),
        self.var_date.set(""),
        self.var_time.set(""),
        self.var_status.set("Select")

    def update_data(self):
        pass


if __name__ == "__main__":
    root = Tk()
    obj = Attendance(root)
    root.mainloop()
