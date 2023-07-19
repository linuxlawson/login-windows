#!/usr/bin/python3
# Login Window

import tkinter as tk
 
root = tk.Tk()
root.title("Login")
root.geometry("272x152")
root.option_add("*Font", "TkDefaultFont 9")
root.columnconfigure(0, weight=1)
root.resizable(0,0)

#Main Frame
mainframe = tk.Frame(root, highlightcolor="#BFBFBF", 
                    highlightbackground="#7F7F7F", 
                    highlightthickness=1, 
                    relief='sunken')
mainframe.grid(padx=4, pady=4, sticky='nsew')

username = tk.StringVar()
password = tk.StringVar()


def check_entry(event=None):
    if username.get() == 'smitty' and password.get() == 'pencil':
        status_label.config(text=" Access: Granted")
    else:
        status_label.config(text=" Access: Denied")

#username
user_label = tk.Label(mainframe, text="Username:")
user_label.grid(column=0, row=0, padx=6, pady=8, sticky='w')
user_entry = tk.Entry(mainframe, textvariable=username)
user_entry.grid(column=1, row=0, padx=6, pady=8, sticky='e')
user_entry.focus_set()

#password
pass_label = tk.Label(mainframe, text="Password:")
pass_label.grid(column=0, row=1, padx=6, pady=8, sticky='w')
pass_entry = tk.Entry(mainframe, textvariable=password, show="*")
pass_entry.grid(column=1, row=1, padx=6, pady=8, sticky='e')
pass_entry.bind('<Return>', check_entry)

status_label = tk.Label(root, text=" Access: Pending", anchor='w', 
                        fg="#7F7F7F", bd=1, relief='sunken')
status_label.grid(column=0, row=4, padx=4, pady=2, sticky='ew')


#buttons
cancel_button = tk.Button(mainframe, text="Cancel", command=root.destroy)
cancel_button.grid(column=1, row=3, padx=6, pady=6, sticky='w')
cancel_button.bind("<Return>", (lambda event: root.destroy()))

login_button = tk.Button(mainframe, text="Login ", command=check_entry)
login_button.grid(column=1, row=3, padx=6, pady=6, sticky='e')
login_button.bind("<Return>", (lambda event: check_entry()))


root.protocol("WM_DELETE_WINDOW")
root.mainloop()
