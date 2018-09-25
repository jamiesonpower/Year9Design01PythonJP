import tkinter as tk


root = tk.Tk()
root.title("Volume of a Cylinder")

labr = tk.Label(root, text="radius") #stage 1 create widget or element
labr.pack() #Stage 3: pack the widget 

entr =  tk.Entry(root)
entr.pack()

labh = tk.Label(root, text="height")
labh.pack()

enth =  tk.Entry(root)
enth.pack()

btn = tk.Button(root, text="Submit")
btn.pack()

output = tk.Text(root, width=50, height=10, borderwidth=3, relief=tk.GROOVE)
output.config(state="disabled")
output.pack()  

root.mainloop() 