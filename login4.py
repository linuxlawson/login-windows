#!/usr/bin/env python3
# Login Window #4


try:
    import Tkinter as tk
except:
    import tkinter as tk


root = tk.Tk()
root.title("User Login")
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
mainframe.grid(sticky='nsew', padx=4, pady=2)


username = tk.StringVar()
password = tk.StringVar()


def check_entry():
    if username.get() == 'smitty' and password.get() == 'pencil':
        status_label = tk.Label(mainframe, text="Permission Granted", anchor='w', 
                                fg="#008000", bd=0, relief='sunken')
        status_label.grid(row=4, column=1, columnspan=2, sticky='w', padx=4, pady=4)
        
    else:
        status_label = tk.Label(mainframe, text="Permission Denied\t", anchor='w', 
                                fg="#A52A2A", bd=0, relief='sunken')
        status_label.grid(row=4, column=1, columnspan=2, sticky='w', padx=4, pady=4)


toplabel = tk.Label(mainframe, state='normal', text="\nAuthorized Users Only\n", 
                    relief='flat', bg="#000000", fg="#E5E5E5")
toplabel.grid(row=0, column=0, columnspan=2, sticky='new', padx=0, pady=0)
toplabel.config(font="Arial 10 bold")


#username
user_label = tk.Label(mainframe, text="Username:")
user_label.grid(row=1, column=0, sticky='e', padx=4, pady=6)
user_entry = tk.Entry(mainframe, textvariable=username)
user_entry.grid(row=1, column=1, sticky='e', padx=4, pady=6)
user_entry.focus_set()

#password
pass_label = tk.Label(mainframe, text="Password:")
pass_label.grid(row=2, column=0, sticky='e', padx=4, pady=6)
pass_entry = tk.Entry(mainframe, textvariable=password, show="*")
pass_entry.grid(row=2, column=1, sticky='e', padx=4, pady=6)

status_label = tk.Label(mainframe, text="", anchor='e', 
                        fg="#7F7F7F", bd=0, relief='sunken')
status_label.grid(row=4, column=0, sticky='e', padx=4, pady=4)


#buttons
cancel_button = tk.Button(mainframe, text="Cancel", command=root.destroy)
cancel_button.grid(row=3, column=1, sticky='w', padx=4, pady=4)
cancel_button.bind("<Return>", (lambda event: root.destroy()))

login_button = tk.Button(mainframe, text="Login ", command=check_entry)
login_button.grid(row=3, column=1, sticky='e', padx=4, pady=4)
login_button.bind("<Return>", (lambda event: check_entry()))



app = MainApp(root)
root.mainloop()
