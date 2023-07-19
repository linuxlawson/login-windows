#!/usr/bin/python3
# Login Window #4

import tkinter as tk

root = tk.Tk()
root.title("Login")
root.geometry("262x188")
root.option_add("*Font", "TkDefaultFont 9")
root.resizable(0,0)

class MainApp:
	def __init__(self, master):
		self.master = master
		
#Main Frame
mainframe = tk.Frame(root, highlightcolor="#1A1A1A",
                    highlightbackground="#7F7F7F", 
                    highlightthickness=1, 
                    relief='flat')
mainframe.grid(padx=4, pady=2, sticky='nsew')

username = tk.StringVar()
password = tk.StringVar()


def check_entry(event=None):
    if username.get() == 'smitty' and password.get() == 'pencil':
        status_label = tk.Label(mainframe, text="Permission Granted", anchor='w', 
                                fg="#008000", bd=0, relief='sunken')
        status_label.grid(column=1, row=4, padx=4, pady=4, columnspan=2, sticky='w')
        
    else:
        status_label = tk.Label(mainframe, text="Permission Denied\t", anchor='w', 
                                fg="#A52A2A", bd=0, relief='sunken')
        status_label.grid(column=1, row=4, padx=4, pady=4, columnspan=2, sticky='w')

#title
toplabel = tk.Label(mainframe, state='normal', text="\nAuthorized Users Only\n", 
                    relief='flat', bg="#000000", fg="#E5E5E5")
toplabel.grid(column=0, row=0, padx=0, pady=0, columnspan=2, sticky='new')
toplabel.config(font="Arial 10 bold")

#username
user_label = tk.Label(mainframe, text="Username:")
user_label.grid(column=0, row=1, padx=4, pady=6, sticky='e')
user_entry = tk.Entry(mainframe, textvariable=username)
user_entry.grid(column=1, row=1, padx=4, pady=6, sticky='e')
user_entry.focus_set()

#password
pass_label = tk.Label(mainframe, text="Password:")
pass_label.grid(column=0, row=2, padx=4, pady=6, sticky='e')
pass_entry = tk.Entry(mainframe, textvariable=password, show="*")
pass_entry.grid(column=1, row=2, padx=4, pady=6, sticky='e')
pass_entry.bind('<Return>', check_entry)

status_label = tk.Label(mainframe, text="", anchor='e', 
                        fg="#7F7F7F", bd=0, relief='sunken')
status_label.grid(column=0, row=4, padx=4, pady=4, sticky='e')


#buttons
cancel_button = tk.Button(mainframe, text="Cancel", command=root.destroy)
cancel_button.grid(column=1, row=3, padx=4, pady=4, sticky='w')
cancel_button.bind("<Return>", (lambda event: root.destroy()))

login_button = tk.Button(mainframe, text="Login ", command=check_entry)
login_button.grid(column=1, row=3, padx=4, pady=4, sticky='e')
login_button.bind("<Return>", (lambda event: check_entry()))


app = MainApp(root)
root.mainloop()
