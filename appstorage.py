import tkinter as tk

def submit():
	#next step is to take all the inputs 
	#then you need error check

	username.append(nameIn.get())
	nameIn.delete(0,tk.END)
	print(username)

	password.append(passwordIn.get())
	passwordIn.delete(0,tk.END)
	print(password)

username = []
password = []

#Main Window
root = tk.Tk() #creates the standard main window.

root.mainloop()