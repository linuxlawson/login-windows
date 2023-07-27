#!/usr/bin/env python3
# Login Window #5

import tkinter as tk

root = tk.Tk()
root.title("Login")
root.geometry("263x186")
root.option_add("*Font", "TkDefaultFont 9")
root.resizable(0,0)

#Main Frame
mainframe = tk.Frame(root, highlightcolor="#1A1A1A",
                    highlightbackground="#7F7F7F", 
                    highlightthickness=1, 
                    relief='flat')
mainframe.grid(padx=5, pady=2, sticky='nsew')

username = tk.StringVar()
password = tk.StringVar()


def check_entry(event=None):
    if username.get() == 'smitty' and password.get() == 'pencil':
        status_label.config(text="\nAccess Granted\n", fg="#15DD15")
    else:
        status_label.config(text="##############\n#    Access Denied    #\n##############", fg="#15DD15")


#username
user_label = tk.Label(mainframe, text="Username:")
user_label.grid(column=0, row=0, padx=4, pady=10, sticky='e')
user_entry = tk.Entry(mainframe, textvariable=username)
user_entry.grid(column=1, row=0, padx=4, pady=10, sticky='e')
user_entry.focus_set()

#password
pass_label = tk.Label(mainframe, text="Password:")
pass_label.grid(column=0, row=1, padx=4, pady=6, sticky='e')
pass_entry = tk.Entry(mainframe, textvariable=password, show="*")
pass_entry.grid(column=1, row=1, padx=4, pady=6, sticky='e')
pass_entry.bind('<Return>', check_entry)

status_label = tk.Label(mainframe, text="\nAuthorized Users Only\n", anchor='n', 
                        bg="#000000", fg="#E5E5E5", bd=1, relief='sunken')
status_label.grid(column=0, row=3, padx=4, pady=6, columnspan=2, sticky='ew')

#buttons
cancel_button = tk.Button(mainframe, text="Cancel", command=root.destroy)
cancel_button.grid(column=1, row=2, padx=4, pady=8, sticky='w')
cancel_button.bind("<Return>", (lambda event: root.destroy()))

login_button = tk.Button(mainframe, text="Login ", command=check_entry)
login_button.grid(column=1, row=2, padx=4, pady=8, sticky='e')
login_button.bind("<Return>", (lambda event: check_entry()))


root.protocol("WM_DELETE_WINDOW")
root.mainloop()
