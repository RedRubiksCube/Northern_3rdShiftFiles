from tkinter import *

#This is the code for the opening page
#main page = MP
MP = Tk()
MP.title('Daily Routing')
MP.geometry('500x500')
MP.iconbitmap('C:/Users/TRedinger/Documents/Py/squarelogo.ico')


welcome_Label = Label(MP, text='Welcome to Northerns Routing Program. \n This will assist you in automating commands being sent to Tiny Terms.')
welcome_Label.grid(row=1, column=0)




MP.mainloop()