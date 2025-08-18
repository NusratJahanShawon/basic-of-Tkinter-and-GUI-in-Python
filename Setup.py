import tkinter as tk

# widgets = GUI elements: buttons, labels, text boxes, images  etc.
# windows = GUI windows: main window, dialog boxes, popups etc.

mainWindow = tk.Tk() #instantiate an instance of a window
mainWindow.geometry("600x450+8+400") #set the size of the window
mainWindow.title("My First GUI") #set the title of the window

#adding labels
label=tk.Label(mainWindow, text="Hello World!") #create a label widget
label.pack(side='top') #add the label to the window

canvas= tk.Canvas(mainWindow, relief='raised', borderwidth=1) #create a canvas widget
canvas.pack(side='left')

mainWindow.mainloop() # placce window on computer screen, listen for events, wait for user input


