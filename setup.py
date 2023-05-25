import cx_Freeze
import sys
import os 
base = None

if sys.platform == 'win32':
    base = "Win32GUI"

os.environ['TCL_LIBRARY'] = r"C:\Users\sarthak\AppData\Local\Programs\Python\Python38\tcl\tcl8.6"
os.environ['TK_LIBRARY'] = r"C:\Users\sarthak\AppData\Local\Programs\Python\Python38\tcl\tk8.6"

executables = [cx_Freeze.Executable("attendance_system.py", base=base, icon="icon.ico")]


cx_Freeze.setup(
    name = "Attendance Monitoring Software",
    options = {"build_exe": {"packages":["tkinter","os"], "include_files":["icon.ico",'tcl86t.dll','tk86t.dll', 'images','data_set','database','attendance']}},
    version = "1.0",
    description = "Attendance Monitoring Software | Developed By Karan ,Disha and Manvendra",
    executables = executables
)