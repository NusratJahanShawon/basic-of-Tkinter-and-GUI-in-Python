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

# frame for the radio buttons
optionFrame = tk.LabelFrame(mainWindow, text="File Details")
optionFrame.grid(row=1, column=2, sticky='ne')

rbValue = tk.IntVar()
rbValue.set(3) # the numbe of the default selected radio button here 3

#radio buttons
radio1 = tk.Radiobutton(optionFrame, text="Filename", value=1, variable=rbValue)
radio2 = tk.Radiobutton(optionFrame, text="Path", value=2, variable=rbValue)
radio3 = tk.Radiobutton(optionFrame, text="Timestamp", value=3, variable=rbValue)
radio1.grid(row=0, column=0, sticky='w')
radio2.grid(row=1, column=0, sticky='w')    
radio3.grid(row=2, column=0, sticky='w')

#widget to desplay tge result
resultLabel = tk.Label(mainWindow, text="Result")
resultLabel.grid(row=2, column=2, sticky='nw')
result=tk.Entry(mainWindow)
result.grid(row=2, column=2, sticky='sw')

#frame for the time spinners
timeFrame = tk.LabelFrame(mainWindow, text="Time")  
timeFrame.grid(row=3, column=0, sticky='new')

#time spinners
hourSpinner = tk.Spinbox(timeFrame, width=2, values=tuple(range(0,24)))
minuteSpinner = tk.Spinbox(timeFrame, width=2, from_=0, to=59)
secondSpinner = tk.Spinbox(timeFrame, width=2, from_=0, to= 59)
hourSpinner.grid(row=0, column=0)
tk.Label(timeFrame, text=":").grid(row=0, column=1)
minuteSpinner.grid(row=0, column=2)
tk.Label(timeFrame, text=":").grid(row=0, column=3)
secondSpinner.grid(row=0, column=4)
timeFrame['padx'] = 36

#frame for the date spinners
dateFrame = tk.LabelFrame(mainWindow, text="Date")
dateFrame.grid(row=4, column=0, sticky='new')
#date llabels
dayLabel = tk.Label(dateFrame, text="Day")
monthLabel = tk.Label(dateFrame, text="Month")
yearLabel = tk.Label(dateFrame, text="Year")
dayLabel.grid(row=0, column=0,sticky='w')                       
monthLabel.grid(row=0, column=1,sticky='w')
yearLabel.grid(row=0, column=2,sticky='w')

#date spinners
daySpinner = tk.Spinbox(dateFrame, width=4, from_=1, to=31)
monthSpinner = tk.Spinbox(dateFrame, width=4, values=("Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"))
yearSpinner = tk.Spinbox(dateFrame, width=6, from_=2000, to=2099)
daySpinner.grid(row=1, column=0)    
monthSpinner.grid(row=1, column=1)
yearSpinner.grid(row=1, column=2)
dateFrame['padx'] = 36



mainWindow.mainloop()     
# print(rbValue.get())                                     