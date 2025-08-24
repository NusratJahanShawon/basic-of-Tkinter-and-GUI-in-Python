import os
import tkinter as tk
mainWindow = tk.Tk() 


mainWindow.geometry("640x480-8-200") 
mainWindow.title("Grid Demo") 

label=tk.Label(mainWindow, text="TKinter Grid Demo")
label.grid(row=0, column=0, columnspan=3)




mainWindow.columnconfigure(0, weight=1) 
mainWindow.columnconfigure(1, weight=1)     
mainWindow.columnconfigure(2, weight=3)
mainWindow.columnconfigure(3, weight=3)
mainWindow.columnconfigure(4, weight=3)

mainWindow.rowconfigure(0, weight=1)
mainWindow.rowconfigure(1, weight=10)
mainWindow.rowconfigure(2, weight=1)
mainWindow.rowconfigure(3, weight=3)
mainWindow.rowconfigure(4, weight=3)

#making the list view
fileList = tk.Listbox(mainWindow)
fileList.grid(row=1, column=0, sticky='nsew', rowspan=2)
fileList.config(border=2, relief='sunken')

for zone in os.listdir('C:/Windows/System32'):
    fileList.insert(tk.END, zone)

listScroll = tk.Scrollbar(mainWindow, orient=tk.VERTICAL, command=fileList.yview)
listScroll.grid(row=1, column=1, sticky='nsw', rowspan=2)
fileList['yscrollcommand'] = listScroll.set



mainWindow.mainloop()                                          