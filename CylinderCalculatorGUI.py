import tkinter as tk
import math

def calculate():

	print("Calculate pressed")
	r = float(entr.get())
	h = float(enth.get())

	v = math.pi*r*r*h
	v = round(v,3)

	output.config(state="normal")

	outputValue = "Given\nradius:"+str(r)+" cm\nheight:"+str(h)+" cm\nThe volume is:"+str(v)+" cm cubed\n\n"

	output.delete(1.0,tk.END)
	output.insert(tk.INSERT,outputValue)
	output.config(state="disabled") 

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

btn = tk.Button(root, text="Calculate", command=calculate)
btn.pack()

output = tk.Text(root, width=50, height=10, borderwidth=3, relief=tk.GROOVE)
output.config(state="disabled")
output.pack()  

root.mainloop() 