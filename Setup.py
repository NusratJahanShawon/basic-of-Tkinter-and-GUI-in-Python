import tkinter as tk

# widgets = GUI elements: buttons, labels, text boxes, images  etc.
# windows = GUI windows: main window, dialog boxes, popups etc.

mainWindow = tk.Tk() #instantiate an instance of a window
mainWindow.geometry("600x450-8-400") #set the size of the window
mainWindow.title("My First GUI") #set the title of the window

#adding labels
label=tk.Label(mainWindow, text="Hello World!") #create a label widget
label.grid(row=0, column=0) #place the label in the window using grid
# label.pack(side='top') #add the label to the window


leftFrame = tk.Frame(mainWindow) #create a frame widget
leftFrame.grid(row=1, column=1) #place the frame in the window using grid
# leftFrame.pack(side='left', anchor='n', fill=tk.Y, expand=False) #add the frame to the window

canvas= tk.Canvas(leftFrame, relief='raised', borderwidth=1) #create a canvas widget
# canvas.pack(side='left', anchor='n') #add the canvas to the window
canvas.grid(row=1, column=0) #place the canvas in the window using grid


rightFrame = tk.Frame(mainWindow)
# rightFrame.pack(side='right', anchor='n', fill=tk.Y, expand=True) #add the frame to the window
rightFrame.grid(row=1, column=2) #place the frame in the window using grid


#creating a button
button1 = tk.Button(rightFrame, text="Click Me!") 
button2 = tk.Button(rightFrame, text="Exit") 
button3= tk.Button(rightFrame, text="Don't Click Me!") 

# button1.pack(side='top', ) 
# button2.pack(side='top') 
# button3.pack(side='top') 

button1.grid(row=0, column=0) #place the button in the window using grid
button2.grid(row=1, column=0) #place the button in the window using grid
button3.grid(row=2, column=0) #place the button in the window using grid

#configure grid columns 
mainWindow.columnconfigure(0, weight=1) #column 0 expands with window
mainWindow.columnconfigure(1, weight=1) #column 1 expands with window
mainWindow.grid_columnconfigure(2, weight=1) #column 2 expands with window

leftFrame.config(relief='sunken', borderwidth=1) #add border to frame
rightFrame.config(relief='sunken', borderwidth=1) #add border to frame
leftFrame.grid(sticky='ns') #make the frame stick to north and south
rightFrame.grid(sticky='new') #make the frame stick to all sides

rightFrame.columnconfigure(0, weight=1) #column 0 expands with window   
button2.grid(sticky='ew') #make the button stick to east and west
mainWindow.mainloop() # placce window on computer screen, listen for events, wait for user input


