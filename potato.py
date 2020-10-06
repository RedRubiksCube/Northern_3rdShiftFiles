from datetime import date
from tkinter import *
import pyautogui, time, csv, os, datetime, logging

#logging.basicConfig(level=logging.INFO, filename= '../Logs/Logs.log')

root = Tk()
root.title("Routing List")
root.geometry("800x600")

#Below is code essential to creating the CSV file
today = date.today()
year = str(today)[0:4]
month = str(today)[5:7]
day = str(today)[8:10]
#dir_year = 'T:/Information Technology Drive/Automation/Routing' + '/' + year
#dir_month = 'T:/Information Technology Drive/Automation/Routing' + '/' + year + '/' + month
#dir_day = 'T:/Information Technology Drive/Automation/Routing' + '/' + year + '/' + month + '/' + day
#if not os.path.exists(dir_year):
#	os.mkdir(dir_year)
#if not os.path.exists(dir_month):
#	os.mkdir(dir_month)

#Get Date as int
#Monday = 0 
#Sunday = 6

day = datetime.datetime.today().weekday()
#day = 0
file_run_time = datetime.datetime.now()


#FRAMES
welcome_frame = Frame(root)
welcome_frame.grid(row=0, column=0)
	#The button frame should appear on each page
buttons_frame = Frame(root, bg="#0e0a80") #width=200, height=200, bd=1,
buttons_frame.grid(row=2, column=0)
	#Use format below to create new frames, use functions to call and forget frames
assign_routes_frame = Frame(root)
	#Used to run Buffa's produce report
produce_report_frame = Frame(root)

#LISTS

#Route lists
#These lists are used for the Curtze Weight 
Day_list = []
Mon_routes = ['193','194','195'] 	# This will run if the day value is equal to 0
Tues_routes = ['293','294','295']	# This will run if the day value is equal to 1
Wed_routes = ['393','394','395'] 	# This will run if the day value is equal to 2
Thurs_routes = ['492','494','495'] 	# This will run if the day value is equal to 3
Fri_routes = ['593','594','595'] 	# This will run if the day value is equal to 4

#INTRO LABEL
welcome_label = Label(welcome_frame, text='Welcome to Northern Haserots Routing program. \n What would you like to do?')
welcome_label.grid(row=0, column=0)

#FUNCTIONS
def P2():
	welcome_frame.grid_forget()
	asign_routes_frame.grid(row=0, column=0)

def ass_routes():
	pass

def N_TT_login():
	USR = pyautogui.prompt("Logging into Northerns's system. \n What is your username?")
	PW = pyautogui.prompt('What is your Northern password?')

	#Opens server2
	pyautogui.press('win')
	pyautogui.typewrite('notepad')#, duration=1)
	pyautogui.press('enter')

	time.sleep(5)
	pyautogui.typewrite(USR)
	pyautogui.press('enter')

	pyautogui.typewrite(PW)
	pyautogui.press('enter')
	pyautogui.press('enter')
	time.sleep(5)

def C_TT_login():
	USR = pyautogui.prompt("Logging into Curtze's system. \n What is your username?")
	PW = pyautogui.prompt('What is your Curtze password?')
	pyautogui.press('win')
	pyautogui.typewrite('notepad')#, duration=1) curtze.tpx
	pyautogui.press('enter')


	#USR = pyautogui.prompt('What is your username?')
	time.sleep(5)
	pyautogui.typewrite(USR)
	pyautogui.press('enter')

	#PW = USR = pyautogui.prompt('What is your passwocd')
	pyautogui.typewrite(PW)
	pyautogui.press('enter')
	pyautogui.press('enter')
	time.sleep(5)

	pyautogui.typewrite('cd /users/data/curtze1')
	pyautogui.press('enter')

def close_TT():
	pyautogui.typewrite("exit")
	pyautogui.press('enter')

def produce_report():
	N_TT_login()
	pyautogui.typewrite('cd /users/data/curtze1')
	pyautogui.press('enter')

	pyautogui.typewrite('drun')
	pyautogui.press('enter')
	time.sleep(1)
	pyautogui.typewrite('produce')
	pyautogui.press('enter')
	time.sleep(2)
	pyautogui.typewrite('12')
	pyautogui.press('enter')
	time.sleep(2)

	pyautogui.typewrite('lpr -dprinter53 prt-produce')
	pyautogui.press('enter')
	time.sleep(5)
	close_TT()

def distOut_email():
	N_TT_login()
	pyautogui.typewrite('drun')
	pyautogui.press('enter')
	time.sleep(1)
	pyautogui.typewrite('dailyoutstk')
	pyautogui.press('enter')
	time.sleep(2)
	pyautogui.press('enter')
	time.sleep(15)

	dist = 2
	dist = 2
	while dist < 13:
		pyautogui.typewrite('drun')
		pyautogui.press('enter')
		time.sleep(1)
		pyautogui.typewrite('distoutstk')
		pyautogui.press('enter')
		time.sleep(1)
		pyautogui.typewrite(str(dist))
		pyautogui.press('enter')
		time.sleep(3)
		if dist == 9:
			dist = dist + 2
		else:
			dist = dist + 1

	#Runs the clear
	pyautogui.typewrite('cd /users/bin')
	pyautogui.press('enter')
	time.sleep(2)
	pyautogui.typewrite('proc-clrcustrnet')
	pyautogui.press('enter')
	time.sleep(5)

	pyautogui.typewrite('l /usr/roadnet/rnetcust.txt')
	pyautogui.press('enter')
	time.sleep(5)
	close_TT()

def curtzeweights():
	day_ran = pyautogui.prompt('Is this being ran before midnight? \n IE - If product is being shipped on Monday, is today technically Monday? \n Answer yes if true, Answer no if false.')
		#Selects corret day values
	if str(day_ran.lower()) == 'yes' or str(day_ran.lower()) == 'no':
		if day_ran.lower() == 'yes':
			if day == 6:
				Day_list = Mon_routes
				logging.info('Routes ran for Monday') 
			else:
				day = day + 1
				if day == 1:
					Day_list = Tues_routes
					logging.info('Routes ran for Tuesday')	
				elif day == 2:
					Day_list = Wed_routes
					logging.info('Routes ran for Wednesday')	
				elif day == 3:
					Day_list = Thurs_routes
					logging.info('Routes ran for Thursday')	
				elif day == 4:
					Day_list = Fri_routes
					logging.info('Routes ran for Friday')	
	else:
		if day == 0:
			Day_list = Mon_routes
			logging.info('Routes ran for Monday') 
		elif day == 1:
			Day_list = Tues_routes
			logging.info('Routes ran for Tuesday')	
		elif day == 2:
			Day_list = Wed_routes
			logging.info('Routes ran for Wednesday')	
		elif day == 3:
			Day_list = Thurs_routes
			logging.info('Routes ran for Thursday')	
		elif day == 4:
			Day_list = Fri_routes
			logging.info('Routes ran for Friday')

	#Runs program
	C_TT_login()
	for route in Day_list:
	#This runs the catg-prt section
		pyautogui.typewrite('jrun')
		pyautogui.press('enter')
		time.sleep(1)
		pyautogui.typewrite('catg-prt')
		pyautogui.press('enter')
		time.sleep(1)
		pyautogui.typewrite('98')
		pyautogui.press('enter')
		time.sleep(1)
		pyautogui.typewrite('1')
		pyautogui.press('enter')
		time.sleep(1)
		pyautogui.typewrite(route)
		pyautogui.press('enter')
		time.sleep(1)
		pyautogui.press('enter')
		time.sleep(1)
		pyautogui.press('enter')
		time.sleep(1)
		pyautogui.press('enter')
		time.sleep(15)
		#This runs the catg-sss portion
		pyautogui.typewrite('jrun')
		pyautogui.press('enter')
		time.sleep(1)
		pyautogui.typewrite('catg-sss')
		pyautogui.press('enter')
		time.sleep(1)
		pyautogui.typewrite('98')
		pyautogui.press('enter')
		time.sleep(1)
		pyautogui.typewrite(route)
		pyautogui.press('enter')
		time.sleep(2)
		pyautogui.press('enter')
		time.sleep(5)

	pyautogui.typewrite('jrun')
	pyautogui.press('enter')
	time.sleep(1)
	pyautogui.typewrite('nffitems')
	pyautogui.press('enter')
	close_TT()


#BUTTONS
#Choose_routes_Button = Button(routing_frame, text="Run Routes", command=run_routes)
#Choose_routes_Button.grid(row=14 ,column=2)

assign_routes_button = Button(buttons_frame, text="Assign Routes", command=ass_routes)
assign_routes_button.grid(row=0 ,column=0, columnspan=1)#, padx=20, pady=20)

email_out_button = Button(buttons_frame, text="Email District Outs", command=distOut_email)
email_out_button.grid(row=1 ,column=0, columnspan=1)#, padx=20, pady=20)

produce_report_button = Button(buttons_frame, text="Produce Report", command=produce_report)
produce_report_button.grid(row=0 ,column=1, columnspan=2)#, padx=20, pady=20)

#Not active
	#change_driver_info_button = Button(buttons_frame, text="Update Driver Information", command=ass_routes)
	#change_driver_info_button.grid(row=0 ,column=1, padx=20, pady=20)


root.mainloop()