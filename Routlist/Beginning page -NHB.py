from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from datetime import date
import sqlite3
import os


root = Tk()
root.title('Routing')
root.geometry('400x400')

#Below is code essential to creating the database
today = date.today()
year = str(today)[0:4]
month = str(today)[5:7]
day = str(today)[8:10]
dir_year = 'T:/Information Technology Drive/Automation/Routing' + '/' + year
dir_month = 'T:/Information Technology Drive/Automation/Routing' + '/' + year + '/' + month
dir_day = 'T:/Information Technology Drive/Automation/Routing' + '/' + year + '/' + month + '/' + day
if not os.path.exists(dir_year):
	os.mkdir(dir_year)
if not os.path.exists(dir_month):
	os.mkdir(dir_month)

database = sqlite3.connect(str(dir_day) + '.db')
c = database.cursor() 

#Frames
day_frame = Frame(root)
day_frame.grid(row=0, column=0)
routing_frame = Frame(root)


#Instead of changing the windows, I will have code be inside frames, and we can change them in there 

welcome_label = Label(day_frame, text='Welcome to Northern Haserots Routing program. \n Please select the ship date.')
welcome_label.grid(row=0, column=0)

ship_days= [
	"Monday",
	"Tuesday",
	"Wednesday",
	"Thursday",
	"Friday",
	"Saturday"
]

day_selected = ttk.Combobox(day_frame, value=ship_days)
day_selected.current(0)
day_selected.grid(row=1, column=0)

#Remove if Route_LF works in EXE
def P2():
	day_frame.grid_forget()
	routing_frame.grid(row=0, column=0)

def choose_day_button():
	global response
	response = messagebox.askyesno('Confirm Day', 'You have selected ' + day_selected.get() +', is this the correct day?')
	#display_day_Confirm_deny=Label(root, text=str(response))
	#display_day_Confirm_deny.grid(row=3, column=0)
	
	if str(response) == 'True':
		P2()
	else:
		messagebox.showinfo('Incorrect day', 'Please select the correct day')

def day_return():
	routing_frame.grid_forget()
	day_frame.grid(row=1, column=0)

day_selected_button = Button(day_frame, text="Select day", command=choose_day_button)
day_selected_button.grid(row=2, column=0)


#Below is the routes to be selected
select_routes_label = Label(routing_frame, text='Please check the routes you would like to route')
select_routes_label.grid(row=0, column=0, columnspan=5)

return_to_day_select_button = Button(routing_frame, text='Return to select day', command=day_return)
return_to_day_select_button.grid(row=12, column=0, columnspan=3)




#Column one of checkboxes
RTV1 = StringVar()
RT1 = Checkbutton(routing_frame, text='1', variable=RTV1, onvalue="R", offvalue="DR")
RT1.deselect()
RT1.grid(row=2, column=0)

RTV2 = StringVar()
RT2 = Checkbutton(routing_frame, text='2', variable=RTV2, onvalue="R", offvalue="DR")
RT2.deselect()
RT2.grid(row=3, column=0)

RTV3 = StringVar()
RT3 = Checkbutton(routing_frame, text='3', variable=RTV3, onvalue="R", offvalue="DR")
RT3.deselect()
RT3.grid(row=4, column=0)

RTV4 = StringVar()
RT4 = Checkbutton(routing_frame, text='4', variable=RTV4, onvalue="R", offvalue="DR")
RT4.deselect()
RT4.grid(row=5, column=0)

RTV5 = StringVar()
RT5 = Checkbutton(routing_frame, text='5', variable=RTV5, onvalue="R", offvalue="DR")
RT5.deselect()
RT5.grid(row=6, column=0)

RTV6 = StringVar()
RT6 = Checkbutton(routing_frame, text='6', variable=RTV6, onvalue="R", offvalue="DR")
RT6.deselect()
RT6.grid(row=7, column=0)

RTV7 = StringVar()
RT7 = Checkbutton(routing_frame, text='7', variable=RTV7, onvalue="R", offvalue="DR")
RT7.deselect()
RT7.grid(row=8, column=0)

RTV8 = StringVar()
RT8 = Checkbutton(routing_frame, text='8', variable=RTV8, onvalue="R", offvalue="DR")
RT8.deselect()
RT8.grid(row=9, column=0)

RTV9 = StringVar()
RT9 = Checkbutton(routing_frame, text='9', variable=RTV9, onvalue="R", offvalue="DR")
RT9.deselect()
RT9.grid(row=10, column=0)

RTV10 = StringVar()
RT10 = Checkbutton(routing_frame, text='10', variable=RTV10, onvalue="R", offvalue="DR")
RT10.deselect()
RT10.grid(row=11, column=0)

#Column 2 of checkboxes

RTV11 = StringVar()
RT11 = Checkbutton(routing_frame, text='11', variable=RTV11, onvalue="R", offvalue="DR")
RT11.deselect()
RT11.grid(row=2, column=1)

RTV12 = StringVar()
RT12 = Checkbutton(routing_frame, text='12', variable=RTV12, onvalue="R", offvalue="DR")
RT12.deselect()
RT12.grid(row=3, column=1)

RTV13 = StringVar()
RT13 = Checkbutton(routing_frame, text='13', variable=RTV13, onvalue="R", offvalue="DR")
RT13.deselect()
RT13.grid(row=4, column=1)

RTV14 = StringVar()
RT14 = Checkbutton(routing_frame, text='14', variable=RTV14, onvalue="R", offvalue="DR")
RT14.deselect()
RT14.grid(row=5, column=1)

RTV15 = StringVar()
RT15 = Checkbutton(routing_frame, text='15', variable=RTV15, onvalue="R", offvalue="DR")
RT15.deselect()
RT15.grid(row=6, column=1)

RTV16 = StringVar()
RT16 = Checkbutton(routing_frame, text='16', variable=RTV16, onvalue="R", offvalue="DR")
RT16.deselect()
RT16.grid(row=7, column=1)

RTV17 = StringVar()
RT17 = Checkbutton(routing_frame, text='17', variable=RTV17, onvalue="R", offvalue="DR")
RT17.deselect()
RT17.grid(row=8, column=1)

RTV18 = StringVar()
RT18 = Checkbutton(routing_frame, text='18', variable=RTV18, onvalue="R", offvalue="DR")
RT18.deselect()
RT18.grid(row=9, column=1)

RTV19 = StringVar()
RT19 = Checkbutton(routing_frame, text='19', variable=RTV19, onvalue="R", offvalue="DR")
RT19.deselect()
RT19.grid(row=10, column=1)

RTV20 = StringVar()
RT20 = Checkbutton(routing_frame, text='20', variable=RTV20, onvalue="R", offvalue="DR")
RT20.deselect()
RT20 .grid(row=11, column=1)

RTV21 = StringVar()
RT21 = Checkbutton(routing_frame, text='21', variable=RTV21, onvalue="R", offvalue="DR")
RT21.deselect()
RT21.grid(row=2, column=2)

#Starts third column
RTV22 = StringVar()
RT22 = Checkbutton(routing_frame, text='22', variable=RTV22, onvalue="R", offvalue="DR")
RT22.deselect()
RT22.grid(row=3, column=2)

RTV23 = StringVar()
RT23 = Checkbutton(routing_frame, text='23', variable=RTV23, onvalue="R", offvalue="DR")
RT23.deselect()
RT23.grid(row=4, column=2)

RTV24 = StringVar()
RT24 = Checkbutton(routing_frame, text='24', variable=RTV24, onvalue="R", offvalue="DR")
RT24.deselect()
RT24.grid(row=5, column=2)

RTV25 = StringVar()
RT25 = Checkbutton(routing_frame, text='25', variable=RTV25, onvalue="R", offvalue="DR")
RT25.deselect()
RT25.grid(row=6, column=2)

RTV26 = StringVar()
RT26 = Checkbutton(routing_frame, text='26', variable=RTV26, onvalue="R", offvalue="DR")
RT26.deselect()
RT26.grid(row=7, column=2)

RTV27 = StringVar()
RT27 = Checkbutton(routing_frame, text='27', variable=RTV27, onvalue="R", offvalue="DR")
RT27.deselect()
RT27.grid(row=8, column=2)

RTV28 = StringVar()
RT28 = Checkbutton(routing_frame, text='28', variable=RTV28, onvalue="R", offvalue="DR")
RT28.deselect()
RT28.grid(row=9, column=2)

RTV29 = StringVar()
RT29 = Checkbutton(routing_frame, text='29', variable=RTV29, onvalue="R", offvalue="DR")
RT29.deselect()
RT29.grid(row=10, column=2)

RTV30 = StringVar()
RT30 = Checkbutton(routing_frame, text='30', variable=RTV30, onvalue="R", offvalue="DR")
RT30.deselect()
RT30.grid(row=11, column=2)

#Starts 4th column 

RTV31 = StringVar()
RT31 = Checkbutton(routing_frame, text='31', variable=RTV31, onvalue="R", offvalue="DR")
RT31.deselect()
RT31.grid(row=2, column=3)

RTV32 = StringVar()
RT32 = Checkbutton(routing_frame, text='32', variable=RTV32, onvalue="R", offvalue="DR")
RT32.deselect()
RT32.grid(row=3, column=3)

RTV32 = StringVar()
RT32 = Checkbutton(routing_frame, text='33', variable=RTV32, onvalue="R", offvalue="DR")
RT32.deselect()
RT32.grid(row=4, column=3)

RTV33 = StringVar()
RT33 = Checkbutton(routing_frame, text='34', variable=RTV33, onvalue="R", offvalue="DR")
RT33.deselect()
RT33.grid(row=5, column=3)

RTV34 = StringVar()
RT34 = Checkbutton(routing_frame, text='35', variable=RTV34, onvalue="R", offvalue="DR")
RT34.deselect()
RT34.grid(row=6, column=3)

RTV35 = StringVar()
RT35 = Checkbutton(routing_frame, text='36', variable=RTV35, onvalue="R", offvalue="DR")
RT35.deselect()
RT35.grid(row=7, column=3)

RTV36 = StringVar()
RT36= Checkbutton(routing_frame, text='37', variable=RTV36, onvalue="R", offvalue="DR")
RT36.deselect()
RT36.grid(row=8, column=3)

RTV37 = StringVar()
RT37 = Checkbutton(routing_frame, text='38', variable=RTV37, onvalue="R", offvalue="DR")
RT37.deselect()
RT37.grid(row=9, column=3)

RTV38 = StringVar()
RT38 = Checkbutton(routing_frame, text='39', variable=RTV38, onvalue="R", offvalue="DR")
RT38.deselect()
RT38.grid(row=10, column=3)

RTV39 = StringVar()
RT39 = Checkbutton(routing_frame, text='40', variable=RTV39, onvalue="R", offvalue="DR")
RT39.deselect()
RT39.grid(row=11, column=3)

#Starts 5th column

RTV40 = StringVar()
RT40 = Checkbutton(routing_frame, text='41', variable=RTV40, onvalue="R", offvalue="DR")
RT40.deselect()
RT40.grid(row=2, column=4)

RTV41 = StringVar()
RT41 = Checkbutton(routing_frame, text='42', variable=RTV41, onvalue="R", offvalue="DR")
RT41.deselect()
RT41.grid(row=3, column=4)

RTV42 = StringVar()
RT42 = Checkbutton(routing_frame, text='43', variable=RTV42, onvalue="R", offvalue="DR")
RT42.deselect()
RT42.grid(row=4, column=4)

RTV43 = StringVar()
RT43 = Checkbutton(routing_frame, text='44', variable=RTV43, onvalue="R", offvalue="DR")
RT43.deselect()
RT43.grid(row=5, column=4)

RTV44 = StringVar()
RT44 = Checkbutton(routing_frame, text='45', variable=RTV44, onvalue="R", offvalue="DR")
RT44.deselect()
RT44.grid(row=6, column=4)

RTV45 = StringVar()
RT45 = Checkbutton(routing_frame, text='46', variable=RTV45, onvalue="R", offvalue="DR")
RT45.deselect()
RT45.grid(row=7, column=4)

RTV46 = StringVar()
RT46 = Checkbutton(routing_frame, text='47', variable=RTV46, onvalue="R", offvalue="DR")
RT46.deselect()
RT46.grid(row=8, column=4)

RTV47 = StringVar()
RT47 = Checkbutton(routing_frame, text='48', variable=RTV47, onvalue="R", offvalue="DR")
RT47.deselect()
RT47.grid(row=9, column=4)

RTV48 = StringVar()
RT48 = Checkbutton(routing_frame, text='49', variable=RTV48, onvalue="R", offvalue="DR")
RT48.deselect()
RT48.grid(row=10, column=4)

RTV49 = StringVar()
RT49 = Checkbutton(routing_frame, text='50', variable=RTV49, onvalue="R", offvalue="DR")
RT49.deselect()
RT49.grid(row=11, column=4)

database.commit()
database.close()
root.mainloop()

