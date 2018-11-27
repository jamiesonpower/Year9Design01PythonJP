#This imports the tkinter "tool box" this contains
#all the support material to make GUI elements.
#by including "as tk" we are giving a short name to use.
import tkinter as tk


#Main Window
root = tk.Tk() #creates the standard main window.


#Three stages to build elements/objects
#1. Construct the Object: We build and configure it.
#2. Configure the Object: We specify behaviours and settings (OPTIONAL)
#3. Pack the Object: Put it in the window
output = tk.Text(root,height = 10, width = 30) #Parametres are what we send to the function. 
#ordered parametres: the order we send them matters. (COMMON)
#name parametres - JavaScript and Python specific: order doesn't matter but name does
output.config(state = "disable", background = "light blue")
output.grid(row = 1, column = 1, rowspan = 3)


#************WIDGET 2,3,4 (Labels)**************
labInput1 = tk.Label(root, text = "Outfits")
labInput1.grid(row = 1, column = 0)

labInput2 = tk.Label(root, text = "Pickaxes")
labInput2.grid(row = 2, column = 0)

labInput3 = tk.Label(root, text = "Gliders")
labInput3.grid(row = 3, column = 0)

#***********WIDGET 5,6 (Checkboxes)***********

cHC = tk.Checkbutton(root, text="Expand", variable=var1)
cHC.grid(row = 0, column = 1)



cLF = tk.Checkbutton(root, text="Expand", variable=var2)
cLF.grid(row = 1, column = 1)

#We are writing an EVENT DRIVE PROGRAM.
#Build the GUI
#Start it running
#Wait for "EVENT"
root.mainloop() #Starts the program.




