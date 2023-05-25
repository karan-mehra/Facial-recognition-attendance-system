from tkinter import*
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
import cv2
from main import Attendace_Monitoring

from PIL import Image, ImageTk


def main():
    win = Tk()
    obj = Login(win)
    win.mainloop()


class Login:
    def __init__(self, root):
        
        self.var_user = StringVar()
        self.var_logpass = StringVar()
        
        self.root = root
        self.root.title("Login window")
        self.root.geometry("1530x790+0+0")
        self.root.wm_iconbitmap("icon.ico")
        
        img1 = Image.open("images/login.jpg")
        img1 = img1.resize((1400, 900), Image.LANCZOS)
        self.bg = ImageTk.PhotoImage(img1)
        
        label_bg = Label(self.root, image = self.bg)
        label_bg.place(x = 0, y = 0, relwidth = 1, relheight = 1)
        
        frame = Frame(self.root, bg = "black")
        frame.place(x = 120, y = 100, width = 400, height = 500)
        
        img2 = Image.open("./images/login_logo.png")
        img2 = img2.resize((100, 100), Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img2)
        
        lbl_img1 = Label(frame, image = self.photoimg1, bg = "black", borderwidth = 0)
        lbl_img1.place(x = 150, y = 20, width = 100, height = 100)
        
        lbl1 = Label(frame, text = "Lets get started...!", font = ('Arial', 15, 'bold'), bg = "black", fg = "white")
        lbl1.place(x = 110, y = 125)
        
        #username
        username_lbl = Label(frame, text = "Email id", font = ('Arial', 12, 'bold'), bg = "black", fg = "white")
        username_lbl.place(x = 70, y = 180)
        
        self.text_username = ttk.Entry(frame, textvariable = self.var_user, font = ('Arial', 15, 'bold'))
        self.text_username.place(x = 50, y = 210, width = 300)
        
        img3 = Image.open("./images/login_icon.png")
        img3 = img3.resize((15, 15), Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        
        lbl_img2 = Label(frame, image = self.photoimg3, bg = "black", borderwidth = 0)
        lbl_img2.place(x = 50, y = 184, width = 15, height = 15)
        
        #Password
        img4 = Image.open("./images/pass_icon.png")
        img4 = img4.resize((15, 15), Image.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)
        
        lbl_img3 = Label(frame, image = self.photoimg4, bg = "black", borderwidth = 0)
        lbl_img3.place(x = 50, y = 265, width = 15, height = 15)
        
        password_lbl = Label(frame, text = "Password", font = ('Arial', 12, 'bold'), bg = "black", fg = "white")
        password_lbl.place(x = 70, y = 260)
        
        self.text_password = ttk.Entry(frame, show="*", textvariable = self.var_logpass, font = ('Arial', 15, 'bold'))
        self.text_password.place(x = 50, y = 290, width = 300)
        
        pass_forg = Button(frame, text = "Forgot password?", command = self.reset_pass, font = ('Arial', 10, 'bold'), borderwidth = 0, bg = "black", fg = "blue", cursor = "hand2", activeforeground = "red", activebackground = "black")
        pass_forg.place(x = 230, y = 320)
        
        login_btn = Button(frame, text = "Login", command = self.login, width = 17, font = ('Arial', 12, 'bold'), bd = 3, relief = RIDGE, bg = "blue", fg = "white", cursor = "hand2")
        login_btn.place(x = 150, y = 370, width = 100, height = 30)
        
        register_lbl1 = Label(frame, text = "Don't have an account?", font = ('Arial', 10, 'bold'), bg = "black", fg = "white")
        register_lbl1.place(x = 50, y = 430)
        
        register_lbl2 = Button(frame, text = "Register", command = self.register_win, font = ('Arial', 10, 'bold'), borderwidth = 0, bg = "black", fg = "blue", cursor = "hand2", activeforeground = "red", activebackground = "black")
        register_lbl2.place(x = 205, y = 430)
    
    def register_win(self):
        self.nwin = Toplevel(self.root)
        self.app = Register(self.nwin)
        
    def login(self):
        if self.var_user.get() == "" or self.var_logpass.get() == "":
            messagebox.showerror("Error", "Please enter email and password", parent = self.root)  
        else:
            try:
                db = mysql.connector.connect(host = "localhost", username = "root", password = "1234", database = "attendance_system")
                my_cursor = db.cursor()
                        
                my_cursor.execute("select * from registration where email = %s and password = %s", (
                        self.var_user.get(),
                        self.var_logpass.get()
                ))
                
                tuple = my_cursor.fetchone()
                if tuple == None:
                    messagebox.showerror("Error", "Invalid information...", parent = self.root)
                else:
                    opn = messagebox.askyesno("Agree", "Are you admin?", parent = self.root)
                    if opn > 0:
                        self.new_window = Toplevel(self.root)
                        self.app = Attendace_Monitoring(self.new_window)
                    else:
                        if not opn:
                            db.close()
                            return
                
                db.commit()
                db.close()
            except Exception as e:
                messagebox.showerror("Error", "Sorry error in login", parent = self.root)
    
    def reset(self):
        if self.var_secq1.get() == "Select":
            messagebox.showerror("Error", "Please select security question", parent = self.root2)
        elif self.var_seca1.get() == "":
            messagebox.showerror("Error", "Please give security answer", parent = self.root2)
        elif self.var_newpass.get() == "":
            messagebox.showerror("Error", "Please enter new password", parent = self.root2)
        else:
            db = mysql.connector.connect(host = "localhost", username = "root", password = "1234", database = "attendance_system")
            my_cursor = db.cursor()
                        
            my_cursor.execute("select * from registration where email = %s and secq = %s and seca = %s", (
                    self.var_user.get(),
                    self.var_secq1.get(),
                    self.var_seca1.get()
            ))
                
            tuple = my_cursor.fetchone()
            if tuple == None:
                messagebox.showerror("Error", "Enter correct information", parent = self.root2)
                db.close()
            else:
                my_cursor.execute("update registration set password = %s where email = %s", (
                        self.var_newpass.get(),
                        self.var_user.get(),
                ))
                db.commit()
                db.close()
                messagebox.showinfo("Success", "Your password has been updated successfully", parent = self.root2)
                self.root2.destroy()
            
    def reset_pass(self):
        if self.var_user.get() == "":
            messagebox.showerror("Error", "Please provide email address", parent = self.root)
        else:
            try:
                db = mysql.connector.connect(host = "localhost", username = "root", password = "1234", database = "attendance_system")
                my_cursor = db.cursor()
                        
                my_cursor.execute("select * from registration where email = %s", (
                        self.var_user.get(),
                ))
                
                tuple = my_cursor.fetchone()
                if tuple == None:
                    messagebox.showerror("Error", "Invalid Email address...", parent = self.root)
                else:
                    db.close()
                    self.root2 = Toplevel()
                    self.root2.title("Forgot Password")
                    self.root2.geometry("340x430+600+140")
                    
                    bg_lab1 = Label(self.root2, bg = "black")
                    bg_lab1.place(x = 0, y = 0, relwidth = 1, relheight = 1)
                    
                    lbl = Label(self.root2, text = "Forgot Password", font = ("arial", 16, "bold"), fg = "green", bg = "white")
                    lbl.place(x = 0, y = 0, relwidth = 1)
                    
                    qsecure_lbl = Label(self.root2, text = "Security Question:", font = ("arial", 10, "bold"), fg = "white", bg = "black")
                    qsecure_lbl.place(x = 50, y = 60)
                    
                    self.var_secq1 = StringVar()
                    qsecure = ttk.Combobox(self.root2, font = ("arial", 10, "bold"), state = "readonly", textvariable = self.var_secq1)
                    qsecure["values"] = ("Select", "Your Mother Name", "Your Favourite Color", "Your Pet Name")
                    qsecure.current(0)
                    qsecure.place(x = 50, y = 90, width = 240)
                    
                    self.var_seca1 = StringVar()
                    asecure_lbl = Label(self.root2, text = "Security Answer:", font = ("arial", 10, "bold"), bg = "black", fg = "white")
                    asecure_lbl.place(x = 50, y = 150)
                    
                    asecure = ttk.Entry(self.root2, font = ("arial", 10, "bold"), textvariable = self.var_seca1)
                    asecure.place(x = 50, y = 180, width = 240)
                    
                    self.var_newpass = StringVar()
                    new_pass_lbl = Label(self.root2, text = "New Password:", font = ("arial", 10, "bold"), bg = "black", fg = "white")
                    new_pass_lbl.place(x = 50, y = 240)
                    
                    new_pass = ttk.Entry(self.root2, font = ("arial", 10, "bold"), textvariable = self.var_newpass)
                    new_pass.place(x = 50, y = 270, width = 240)
                    
                    reset_btn = Button(self.root2, text = "Reset password", command = self.reset, width = 17, font = ('Arial', 11, 'bold'), bd = 3, relief = RIDGE, bg = "red", fg = "white", cursor = "hand2")
                    reset_btn.place(x = 100, y = 330, width = 150, height = 40)
                    
            except Exception as e:
                messagebox.showerror("Error", "Sorry error occured", parent = self.root)
            
        
        
class Register:
    def __init__(self, root):
        
        self.var_fname = StringVar()
        self.var_lname = StringVar()
        self.var_email = StringVar()
        self.var_phone = StringVar()
        self.var_pass = StringVar()
        self.var_cpass = StringVar()
        self.var_secq = StringVar()
        self.var_seca = StringVar()
        self.var_check = IntVar()
        
        self.root = root
        self.root.title("Register window")
        self.root.geometry("1530x790+0+0")
        
        img1 = Image.open("images/background.jpg")
        img1 = img1.resize((1400, 900), Image.LANCZOS)
        self.bg = ImageTk.PhotoImage(img1)
        
        bg_lab = Label(self.root, image = self.bg)
        bg_lab.place(x = 0, y = 0, relwidth = 1, relheight = 1)
        
        main_frame = Frame(bg_lab, bd = 2, bg = "white",)
        main_frame.place(x = 70, y = 85, width = 1210, height = 540)
        
        img2 = Image.open("images/register.jpg")
        img2 = img2.resize((400, 540), Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img2)
        
        left_lbl = Label(main_frame, image = self.photoimg1)
        left_lbl.place(x = -2, y = -2, width = 400, height = 540)
        
        register_lbl = Label(main_frame, text = "REGISTER", font = ("arial", 20, "bold"), fg = "green", bg = "white")
        register_lbl.place(x = 420, y = 10)
        
        # Input Area
        fname_lbl = Label(main_frame, text = "First Name:", font = ("arial", 15, "bold"), fg = "black", bg = "white")
        fname_lbl.place(x = 460, y = 70)
        
        fname = ttk.Entry(main_frame, font = ("arial", 15, "bold"), textvariable = self.var_fname)
        fname.place(x = 460, y = 105, width = 250)
        
        lname_lbl = Label(main_frame, text = "Last Name:", font = ("arial", 15, "bold"), fg = "black", bg = "white")
        lname_lbl.place(x = 840, y = 70)
        
        lname = ttk.Entry(main_frame, font = ("arial", 15, "bold"), textvariable = self.var_lname)
        lname.place(x = 840, y = 105, width = 250)
        
        email_lbl = Label(main_frame, text = "Email Id:", font = ("arial", 15, "bold"), fg = "black", bg = "white")
        email_lbl.place(x = 460, y = 150)
        
        email = ttk.Entry(main_frame, font = ("arial", 15, "bold"), textvariable = self.var_email)
        email.place(x = 460, y = 185, width = 250)
        
        phone_lbl = Label(main_frame, text = "Phone No:", font = ("arial", 15, "bold"), fg = "black", bg = "white")
        phone_lbl.place(x = 840, y = 150)
        
        phone = ttk.Entry(main_frame, font = ("arial", 15, "bold"), textvariable = self.var_phone)
        phone.place(x = 840, y = 185, width = 250)
        
        password_lbl = Label(main_frame, text = "Password:", font = ("arial", 15, "bold"), fg = "black", bg = "white")
        password_lbl.place(x = 460, y = 230)
        
        password = ttk.Entry(main_frame, show="*", font = ("arial", 15, "bold"), textvariable = self.var_pass)
        password.place(x = 460, y = 265, width = 250)
        
        con_password_lbl = Label(main_frame, text = "Confirm Password:", font = ("arial", 15, "bold"), fg = "black", bg = "white")
        con_password_lbl.place(x = 840, y = 230)
        
        con_password = ttk.Entry(main_frame, font = ("arial", 15, "bold"), textvariable = self.var_cpass)
        con_password.place(x = 840, y = 265, width = 250)
        
        qsecure_lbl = Label(main_frame, text = "Security Question:", font = ("arial", 15, "bold"), fg = "black", bg = "white")
        qsecure_lbl.place(x = 460, y = 310)
        
        qsecure = ttk.Combobox(main_frame, font = ("arial", 15, "bold"), state = "readonly", textvariable = self.var_secq)
        qsecure["values"] = ("Select", "Your Mother Name", "Your Favourite Color", "Your Pet Name")
        qsecure.current(0)
        qsecure.place(x = 460, y = 345, width = 250)
        
        asecure_lbl = Label(main_frame, text = "Security Answer:", font = ("arial", 15, "bold"), fg = "black", bg = "white")
        asecure_lbl.place(x = 840, y = 310)
        
        asecure = ttk.Entry(main_frame, font = ("arial", 15, "bold"), textvariable = self.var_seca)
        asecure.place(x = 840, y = 345, width = 250)
        
        check = Checkbutton(main_frame, text = "I agree with terms and conditions", variable = self.var_check, font = ("arial", 12, "bold"), bg = "white", onvalue = 1, offvalue = 0)
        check.place(x = 460, y = 390)
        
        img3 = Image.open("images/register_btn.png")
        img3 = img3.resize((200, 70), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img3)
        
        reg_btn = Button(main_frame, image = self.photoimg2, command = self.register_data, borderwidth = 0, cursor = "hand2")
        reg_btn.place(x = 480, y = 440)
        
        img4 = Image.open("images/login_btn1.png")
        img4 = img4.resize((100, 100), Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img4)
        
        login_btn = Button(main_frame, image = self.photoimg3, command = self.return_to_login, borderwidth = 0, cursor = "hand2", bg = "white", activebackground = "white")
        login_btn.place(x = 880, y = 410)
        
    def register_data(self):
        if self.var_fname.get() == "" or self.var_email.get() == "" or self.var_secq.get() == "Select" or self.var_seca.get() == "" or self.var_phone.get() == "":
            messagebox.showerror("Error", "All fields are required...", parent = self.root)
        elif self.var_pass.get() != self.var_cpass.get():
            messagebox.showerror("Error", "Confirm Password should be same as current password", parent = self.root)
        elif self.var_check.get() == 0:
            messagebox.showerror("Error", "Please agree to terms and conditions", parent = self.root)
        else:
            db = mysql.connector.connect(host = "localhost", username = "root", password = "1234", database = "attendance_system")
            my_cursor = db.cursor()
            query = ("select * from registration where email = %s")
            value = (self.var_email.get(),)
            
            my_cursor.execute(query, value)
            
            tuple = my_cursor.fetchone()
            if tuple != None:
                messagebox.showerror("Error", "User with this email address already present", parent = self.root)
                return
            else:            
                my_cursor.execute("insert into registration values(%s, %s, %s, %s, %s, %s, %s)", (
                    self.var_fname.get(),
                    self.var_lname.get(),
                    self.var_email.get(),
                    self.var_phone.get(),
                    self.var_secq.get(),
                    self.var_seca.get(),
                    self.var_pass.get(),
                ))
            db.commit()
            db.close()
            messagebox.showinfo("Success", "User registered successfully...", parent = self.root)
            
    def return_to_login(self):
        self.root.destroy()
        
        
if __name__ == "__main__":
    main()
    
    