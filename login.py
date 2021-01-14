#!/usr/bin/python
# Login Window
# David Lawson


try:
    import Tkinter as tk
except:
    import tkinter as tk
 

root = tk.Tk()
root.title("\tLogin")
root.geometry("272x152")
root.option_add("*Font", "TkDefaultFont 9")
root.columnconfigure(0, weight=1)


#Main Frame
mainframe = tk.Frame(root, highlightcolor="#BFBFBF", 
                    highlightthickness=1, 
                    relief='sunken')
mainframe.grid(sticky='n', padx=4, pady=4)


username = tk.StringVar()
password = tk.StringVar()


def check_entry():
    if username.get() == 'smitty' and password.get() == 'pencil':
        print ("Access Granted")
        status_label.grid_remove()
        stat1 = tk.Label(root, text=" Access: Granted ", anchor='w', 
                        fg="#7F7F7F", bd=1, relief='sunken')
        stat1.grid(row=4, column=0, sticky='ew', padx=5, pady=2)
    else:
        print ("Access Denied")
        status_label.grid_remove()
        stat2 = tk.Label(root, text=" Access: Denied ", anchor='w', 
                        fg="#7F7F7F", bd=1, relief='sunken')
        stat2.grid(row=4, column=0, sticky='ew', padx=5, pady=2)


#username
user_label = tk.Label(mainframe, text="Username:")
user_label.grid(row=0, column=0, sticky='w', padx=6, pady=8)
user_entry = tk.Entry(mainframe, textvariable=username)
user_entry.grid(row=0, column=1, sticky='e', padx=6, pady=8)
user_entry.focus_set()

#password
pass_label = tk.Label(mainframe, text="Password:")
pass_label.grid(row=1, column=0, sticky='w', padx=6, pady=8)
pass_entry = tk.Entry(mainframe, textvariable=password, show="*")
pass_entry.grid(row=1, column=1, sticky='e', padx=6, pady=8)

status_label = tk.Label(root, text=" Access: Pending", anchor='w', 
                        fg="#7F7F7F", bd=1, relief='sunken')
status_label.grid(row=4, column=0, sticky='ew', padx=5, pady=2)


#buttons
cancel_button = tk.Button(mainframe, text="Cancel", command=root.destroy)
cancel_button.grid(row=3, column=1, sticky='w', padx=6, pady=8)
cancel_button.bind("<Return>", (lambda event: root.destroy()))

login_button = tk.Button(mainframe, text="Login ", command=check_entry)
login_button.grid(row=3, column=1, sticky='e', padx=6, pady=8)
login_button.bind("<Return>", (lambda event: check_entry()))



root.protocol("WM_DELETE_WINDOW")
root.mainloop()
