
from base64 import b85decode
from getpass import getuser
from tkinter import END, Menu, Tk, Toplevel
from tkinter.filedialog import askdirectory
from tkinter.messagebox import WARNING, askokcancel
from tkinter.scrolledtext import ScrolledText
from tkinter.ttk import *
import string
import os
import copy

class Constants:
	CHARS = string.ascii_letters
	NUMS = string.digits
	SPECIAL = string.punctuation + string.whitespace
class Functions:
	consts = Constants()
	def deleteStrAtEnd(self, string):
		string = list(string)
		string.reverse()
		res = list(self.deleteStrAtStart(Functions, ''.join(string)))
		res.reverse()
		return ''.join(res)
	def deleteStrAtStart(self, string):
		string = list(string)
		string_ = copy.deepcopy(string)
		for i in string:
			if i in self.consts.CHARS:
				string_.pop(0)
			else:
				break
		string_ = ''.join(string_)
		return string_
	def deleteIntAtEnd(self, string):
		string = list(string)
		string.reverse()
		res = list(self.deleteIntAtStart(Functions, ''.join(string)))
		res.reverse()
		return ''.join(res)
	def deleteIntAtStart(self, string):
		string = list(string)
		string_ = copy.deepcopy(string)
		for i in string:
			if i in self.consts.NUMS:
				string_.pop(0)
			else:
				break
		string_ = ''.join(string_)
		return string_
	def deleteSpecAtEnd(self, string):
		string = list(string)
		string.reverse()
		res = list(self.deleteSpecAtStart(Functions, ''.join(string)))
		res.reverse()
		return ''.join(res)
	def deleteSpecAtStart(self, string):
		string = list(string)
		string_ = copy.deepcopy(string)
		for i in string:
			if i in self.consts.SPECIAL:
				string_.pop(0)
			else:
				break
		string_ = ''.join(string_)
		return string_
	def parse(self, input, command):
		res = []
		command += "_"
		for idx, i in enumerate(input):
			j = i
			where = ""
			mode = ""
			type_ = ""
			arg = ""
			arg_ = ""
			for k in command:
				if where == "":
					where = k
				elif mode == "":
					mode = k
				elif type_ == "":
					type_ = k
				elif mode == "a" and arg == "":
					if k == "|":
						arg = arg_
					else:
						arg_ += k
				else:
					try:
						match where:
							case "s": #start
								match mode:
									case "a": #add
										if type_ == "s": #string
											j = arg + j
										else: #int
											j = str(int(arg) + idx) + j
									case "d": #delete
										match type_:
											case "s": #string
												j = self.deleteStrAtStart(Functions, j)
											case "n": #int
												j = self.deleteIntAtStart(Functions, j)
											case "p": #special
												j = self.deleteSpecAtStart(Functions, j)
							case "e": #end
								match mode:
									case "a": #add
										if type_ == "s": #string
											j += arg
										else: #int
											j += str(int(arg) + idx)
									case "d": #delete
										match type_:
											case "s": #string
												j = self.deleteStrAtEnd(Functions, j)
											case "n": #int
												j = self.deleteIntAtEnd(Functions, j)
											case "p": #special
												j = self.deleteSpecAtEnd(Functions, j)
					except Exception as e:
						res_ = askokcancel(title="Bulk File Renamer: Error", message="Error: " + str(e) + "\nDo you want to proceed?", icon=WARNING)
						if not res_:
							return
					where = k
					mode = ""
					type_ = ""
					arg = ""
					arg_ = ""
			res.append(j)
		return res
	
icondata = b'LQN6`00000001@s001Ze000pH000vJ000317ytkO007(r00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000003;mkBpmG|9PI!A008p;0000?u_8>dB22L&0000?u_6Ef08FtWOtB(Nu_6Ef0000003;mk0000000000008p;000000000008FtW000000000008FtW00000000000000003;mk0000000000008p;0000?u_8>dB22L&000000000008FtW00000000000000003;mk0000000000008p;000000000008FtW000000000008FtW00000000000000003;mkBpmG|9PI!A008p;0000?u_8>dB22L&000000000008FtWOtB(Nu_6Ef00000000000000000000008p;00000000000000000000000000000000000000000000003;mkBpmG|9PI!A008p;0000?u_8>dB22L&0000?u_6Ef08FtWOtB(Nu_6Ef0000003;mk0000a9PI!A008p;0000?u_6Ef00000000000000008FtW0000?u_6Ef0000003;mkBpmG|9PI!A008p;0000?u_8>dB22L&000000000008FtWOtB(Nu_6Ef0000003;mk0000000000008p;000000000008FtW000000000008FtW00000000000000003;mk0000000000008p;0000?u_8>dB22L&000000000008FtW000000000000000000000000000000008p;00000000000000000000000000000000000000000000003;mk0000a9PI!A008p;0000?u_6Ef08FtW0000?u_6Ef08FtW00000000000000003;mk0000a9PI!A008p;0000?u_6Ef000000000?u_6Ef08FtW00000000000000003;mkBpmG|9PI!A008p;0000?u_6Ef000000000?u_8>dB22L&00000000000000003;mk0000a9PI!A008p;0000?u_6Ef000000000?u_6Ef08FtW00000000000000003;mkBpmG|9PI!A008p;0000?u_6Ef000000000?u_8>dB22L&000000000000000000000000000000000000000000000000000000000000000000000000000000'
os.makedirs(f"C:\\Users\\{getuser()}\\AppData\\Local\\Bulk_File_Renamer", exist_ok=True)
open(f"C:\\Users\\{getuser()}\\AppData\\Local\\Bulk_File_Renamer\\icon.ico", "wb").write(b85decode(icondata))
win = Tk()
win.title("Bulk File Renamer")
win.iconbitmap(f"C:\\Users\\{getuser()}\\AppData\\Local\\Bulk_File_Renamer\\icon.ico", f"C:\\Users\\{getuser()}\\AppData\\Local\\Bulk_File_Renamer\\icon.ico")
win.resizable(0, 0)
inp_files = ScrolledText(win, height=30, width=60)
inp_files.grid(column=0, row=0)
out_files = ScrolledText(win, height=30, width=60)
out_files.grid(column=1, row=0)
inp_files.config(state="disabled")
out_files.config(state="disabled")
Label(win, text="Regex (instructions in help): ").grid(column=0, row=2)
regex_inp = Entry(win, width=83)
regex_inp.grid(column=1, row=2)
def print_to_inp(text):
	inp_files.config(state="normal")
	inp_files.insert(END, text)
	inp_files.config(state="disabled")
def print_to_out(text):
	out_files.config(state="normal")
	out_files.insert(END, text)
	out_files.config(state="disabled")
def clear():
	inp_files.config(state="normal")
	out_files.config(state="normal")
	inp_files.delete("1.0", END)
	out_files.delete("1.0", END)
	inp_files.config(state="disabled")
	out_files.config(state="disabled")
files = []
def refresh(_=None):
	global files
	clear()
	if files != []:
		files = os.listdir(directory)
	res = Functions.parse(Functions, files, regex_inp.get())
	for i in files:
		print_to_inp(i + "\n")
	for i in res:
		print_to_out(i + "\n")
directory = ""
def open_():
	global files, directory
	a = askdirectory(mustexist=True, title="Bulk File Renamer: Open")
	if a != "":
		win.title("Bulk File Renamer: " + a)
		files = os.listdir(a)
		if a.endswith("\\"):
			directory = a[:-1]
		else:
			directory = a
		
	refresh()
def rename(_=None):
	global directory
	res = Functions.parse(Functions, files, regex_inp.get())
	for i, j in zip(files, res):
		try:
			os.renames(directory + "\\" + i, directory + "\\" + j)
		except Exception as e:
			res_ = askokcancel(title="Bulk File Renamer: Error", message="Error: " + str(e) + "\nDo you want to proceed?", icon=WARNING)
			if not res_:
				return
	refresh()
def rename_(_=None, dir=None):
	global directory
	res = Functions.parse(Functions, files, regex_inp.get())
	if dir:
		res = Functions.parse(Functions, os.listdir(dir), regex_inp.get())
		for i, j in zip(os.listdir(dir), res):
			try:
				os.renames(os.path.abspath(dir + "\\" + i), os.path.abspath(dir + "\\" + j))
				if os.path.isdir(os.path.abspath(directory + "\\" + j)):
					rename_(os.path.abspath(dir + "\\" + j))
			except Exception as e:
				res_ = askokcancel(title="Bulk File Renamer: Error", message="Error: " + str(e) + "\nDo you want to proceed?", icon=WARNING)
				if not res_:
					return
	else:
		for i, j in zip(files, res):
			try:
				os.renames(directory + "\\" + i, directory + "\\" + j)
				if os.path.isdir(directory + "\\" + j):
					rename_(None, directory + "\\" + j)
			except Exception as e:
				res_ = askokcancel(title="Bulk File Renamer: Error", message="Error: " + str(e) + "\nDo you want to proceed?", icon=WARNING)
				if not res_:
					return
		refresh()
def help(_=None):
	w = Toplevel()
	w.title("Bulk File Renamer: Help")
	w.resizable(0, 0)
	Label(w, text="""Help:
"Open..." opens a folder
"Convert" converts the folder
"Convert recursively" converts the folder and subfolders

Keybinds:
Enter: refresh
Control+r: rename
Control+t: rename recursively
Control+h: help

Regex rules:
<where><mode><type><arg (optional)>
where is s (start) or e (end)
mode is a (add) or d (delete)
type is s (string) or n (number) (apply to add)
type is s (string) or n (number) or p (special) (apply to delete)
arg is A NUMBER (mode is a, type is n), then add "|"
arg is A STRING (mode is a, type is s), then add "|"
Examples:
sas. |san1|
(start add string ". " END; start add number 1 END)
sdnsdp
(start delete number; start delete special)""").grid(column=0, row=0)
	w.mainloop()
menu = Menu(win, tearoff=0)
file = Menu(menu, tearoff=0)
file.add_command(label="Open...", command=open_)
file.add_command(label="Convert", command=rename)
file.add_command(label="Convert recursively", command=rename_)
file.add_command(label="Help", command=help)
menu.add_cascade(label="File", menu=file)
win.config(menu=menu)
win.bind("<Return>", refresh)
win.bind("<Control-r>", rename)
win.bind("<Control-t>", rename_)
win.bind("<Control-h>", help)

win.mainloop()