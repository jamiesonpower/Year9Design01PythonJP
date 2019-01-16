#This imports the tkinter "tool box" this contains
#all the support material to make GUI elements.
#by including "as tk" we are giving a short name to use.
import tkinter as tk


#Variables: Store data about my program 
#		[un,r,e,l]
outfit = [0,0,0,0]
pickaxes = [1,2,3,4]
gliders = [5,6,7,8]

#list data[0] == 0 outfits data[0] = 1 pickaxes data[0] = 2 gliders
data = [0]

#Step 1: bind a focus on function, and a focus out
#Step 2: Create a write to file program 

def clicked1(event):
	#How do I decide who I have clicked on?
	print("Outfits")
	labInput1.config(background = "red", foreground = "white")
	labInput3.config(background = "grey", foreground = "red")
	labInput2.config(background = "grey", foreground = "red")
	labInput6.config(text = "Uncommon Skins: "+str(outfit[0]))
	labInput7.config(text = "Rare Skins: "+str(outfit[1]))
	labInput8.config(text = "Epic Skins: "+str(outfit[2]))
	labInput9.config(text = "Legendary Skins: "+str(outfit[3]))

	EntUC.delete(0,tk.END)
	EntR.delete(0,tk.END)
	EntE.delete(0,tk.END)
	EntL.delete(0,tk.END)
	data[0] = 0

	EntUC.insert(tk.END,"0")
	EntR.insert(tk.END,"0")
	EntE.insert(tk.END,"0")
	EntL.insert(tk.END,"0")

def clicked2(event):
	#How do I decide who I have clicked on?
	print("Pickaxes")
	labInput2.config(background = "red", foreground = "white")
	labInput1.config(background = "grey", foreground = "red")
	labInput3.config(background = "grey", foreground = "red")
	labInput6.config(text = "Uncommon Skins: "+str(pickaxes[0]))
	labInput7.config(text = "Rare Skins: "+str(pickaxes[1]))
	labInput8.config(text = "Epic Skins: "+str(pickaxes[2]))
	labInput9.config(text = "Legendary Skins: "+str(pickaxes[3]))
	data[0] = 1

def clicked3(event):
	#How do I decide who I have clicked on?
	print("Gliders")
	labInput3.config(background = "red", foreground = "white")
	labInput2.config(background = "grey", foreground = "red")
	labInput1.config(background = "grey", foreground = "red")
	labInput6.config(text = "Uncommon Skins: "+str(gliders[0]))
	labInput7.config(text = "Rare Skins: "+str(gliders[1]))
	labInput8.config(text = "Epic Skins: "+str(gliders[2]))
	labInput9.config(text = "Legendary Skins: "+str(gliders[3]))
	data[0] = 2
def BtnPlusUCFNC():
	print ("+1 Uncommon")
	tv = EntUC.get()
	tv = int(tv)
	tv = tv + 1
	EntUC.delete(0,tk.END)
	EntUC.insert(0,str(tv))



def BtnMinusUCFNC():
	print ("-1 Uncommon")
	tv = EntUC.get()
	tv = int(tv)
	if (tv - 1 >= 0):
		tv = tv - 1
		EntUC.delete(0,tk.END)
		EntUC.insert(0,str(tv))

def BtnPlusRFNC():
	print ("+1 Rare")
	tv = EntR.get()
	tv = int(tv)
	tv = tv + 1
	EntR.delete(0,tk.END)
	EntR.insert(0,str(tv))

def BtnMinusRFNC():
	print ("-1 Rare")
	tv = EntR.get()
	tv = int(tv)
	if (tv - 1 >= 0):
		tv = tv - 1
		EntR.delete(0,tk.END)
		EntR.insert(0,str(tv))

def BtnPlusEFNC():
	print ("+1 Epic")
	tv = EntE.get()
	tv = int(tv)
	tv = tv + 1
	EntE.delete(0,tk.END)
	EntE.insert(0,str(tv))

def BtnMinusEFNC():
	print ("-1 Epic")
	tv = EntE.get()
	tv = int(tv)
	if (tv - 1 >= 0):
		tv = tv - 1
		EntE.delete(0,tk.END)
		EntE.insert(0,str(tv))

def BtnPlusLFNC():
	print ("+1 Legendary")
	tv = EntL.get()
	tv = int(tv)
	tv = tv + 1
	EntL.delete(0,tk.END)
	EntL.insert(0,str(tv))

def BtnMinusLFNC():
	print ("-1 Legendary")
	tv = EntL.get()
	tv = int(tv)
	if (tv - 1 >= 0):
		tv = tv - 1
		EntL.delete(0,tk.END)
		EntL.insert(0,str(tv))

def BtnSaveFNC():
	print ("Saved")
	#Step 1: figure out who is selected?
	print(data[0])


	#Step 2: Take value from each entry change it to an int
	#if data[0] == 0:
		#update outfits
	#if data[0] == 1:
		#update pick
	#if data[0] == 2:
		#update gliders


	#Step 3: Add that to the right list

#def on_entry_click(event):
    #"""function that gets called whenever entry is clicked"""
 #   if entry.get() == '':
   #    entry.delete(0, "end") # delete all the text in the entry
    #   entry.insert(0, '') #Insert blank for user input
     #  entry.config(fg = 'black')


#def on_focusout(event):
 #   if entry.get() == '':
   #     entry.insert(0, 'Enter your username...')
    #    entry.config(fg = 'grey')



#label = tk.Label(root, text="User: ")
#label.pack(side="left")

#entry = tk.Entry(root, bd=1)
#entry.insert(0, 'Enter your user name...')
#entry.bind('<FocusIn>', on_entry_click)
#entry.bind('<FocusOut>', on_focusout)
#entry.config(fg = 'grey')
#entry.pack(side="left")


root = tk.Tk()





#Three stages to build elements/objects
#1. Construct the Object: We build and configure it.
#2. Configure the Object: We specify behaviours and settings (OPTIONAL)
#3. Pack the Object: Put it in the window
#Parametres are what we send to the function. 
#ordered parametres: the order we send them matters. (COMMON)
#name parametres - JavaScript and Python specific: order doesn't matter but name does



#Add a section a code that highlights
#the appropriate section - Outfits, Pickaxes or Gliders
#************WIDGET 2,3,4 (Labels)**************
labInput1 = tk.Label(root, text = "Outfits")
labInput1.config(background = "red", foreground = "white")
labInput1.grid(row = 0, column = 0, sticky = "NESW")
labInput1.bind("<Button-1>",clicked1)

labInput2 = tk.Label(root, text = "Pickaxes")
labInput2.config(background = "grey", foreground = "red")
labInput2.grid(row = 1, column = 0, sticky = "NESW")
labInput2.bind("<Button-1>",clicked2)

labInput3 = tk.Label(root, text = "Gliders")
labInput3.config(background = "grey", foreground = "red")
labInput3.grid(row = 2, column = 0, sticky = "NESW")
labInput3.bind("<Button-1>",clicked3)

#Add a label that you can put an image in
labImg1 = tk.Label(root, background = "light blue")
labImg1.grid(row = 0, column = 4, rowspan = 3, sticky = "NESW")


labInput4 = tk.Label(root, text = "Total = ___", background = "light blue")
labInput4.grid(row = 3, column = 4, sticky = "NESW")

labInput6 = tk.Label(root, text = "Uncommon Skins: "+str(outfit[0]), background = "light green")
labInput6.grid(row = 5, column = 0, sticky = "NESW")

labInput7 = tk.Label(root, text = "Rare Skins: "+str(outfit[1]), background = "blue", foreground = "white")
labInput7.grid(row = 6, column = 0,  sticky = "NESW")

labInput8 = tk.Label(root, text = "Epic Skins: "+str(outfit[2]), background = "purple", foreground = "white")
labInput8.grid(row = 7, column = 0, sticky = "NESW")

labInput9 = tk.Label(root, text = "Legendary Skins: "+str(outfit[3]), background = "Gold")
labInput9.grid(row = 8, column = 0, sticky = "NESW")

labImg2 = tk.Label(root, background = "Green")
labImg2.grid(row = 5, column = 4, rowspan = 3, sticky = "NESW")

labInput10 = tk.Label(root, text = "Total = ____/100", background = "Green")
labInput10.grid(row = 8, column = 4, sticky = "NESW")

labInput11 = tk.Label(root, text = "V-Convert", background = "black", foreground = "red")
labInput11.grid(row = 0, column = 1, rowspan = 3, columnspan = 3, sticky = "NESW")

#Save
BtnSave = tk.Button(root, text = "Save", command = BtnSaveFNC)
BtnSave.grid(row = 9, column = 1)

#Uncommon +/-
EntUC = tk.Entry(root)
EntUC.insert(0,"0")
EntUC.grid(row = 5, column = 1)

BtnPlusUC = tk.Button(root, text = "+", command = BtnPlusUCFNC)
BtnPlusUC.grid(row = 5, column = 2)

BtnMinusUC = tk.Button(root, text = "-", command = BtnMinusUCFNC)
BtnMinusUC.grid(row = 5, column = 3)

#Rare +/-
EntR = tk.Entry(root)
EntR.insert(0,"0")
EntR.grid(row = 6, column = 1)

BtnPlusR = tk.Button(root, text = "+", command = BtnPlusRFNC)
BtnPlusR.grid(row = 6, column = 2)

BtnMinusR = tk.Button(root, text = "-", command = BtnMinusRFNC)
BtnMinusR.grid(row = 6, column = 3)

#Epic +/-
EntE = tk.Entry(root)
EntE.insert(0,"0")
EntE.grid(row = 7, column = 1)

BtnPlusE = tk.Button(root, text = "+", command = BtnPlusEFNC)
BtnPlusE.grid(row = 7, column = 2)

BtnMinusE = tk.Button(root, text = "-", command = BtnMinusEFNC)
BtnMinusE.grid(row = 7, column = 3)

#Legendary +/-
EntL = tk.Entry(root)
EntL.insert(0,"0")
EntL.grid(row = 8, column = 1)

BtnPlusL = tk.Button(root, text = "+", command = BtnPlusLFNC)
BtnPlusL.grid(row = 8, column = 2)

BtnMinusL = tk.Button(root, text = "-", command = BtnMinusLFNC)
BtnMinusL.grid(row = 8, column = 3)


root.mainloop()