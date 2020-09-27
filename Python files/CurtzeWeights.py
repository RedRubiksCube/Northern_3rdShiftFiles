import pyautogui
import time 
import datetime
import logging
import os

logging.basicConfig(level=logging.INFO, filename= '../Logs/Logs.log') # Debug, Info, Warn,  Error


#Get Date as int
#Monday = 0 
#Sunday = 6

day = datetime.datetime.today().weekday()
#day = 0
file_run_time = datetime.datetime.now()


#Rout lists
Day_list = []
Mon_routes = ['193','194','195'] 	# This will run if the day value is equal to 0
Tues_routes = ['293','294','295']	# This will run if the day value is equal to 1
Wed_routes = ['393','394','395'] 	# This will run if the day value is equal to 2
Thurs_routes = ['492','494','495'] 	# This will run if the day value is equal to 3
Fri_routes = ['593','594','595'] 	# This will run if the day value is equal to 4


#This is the users questions portion 
USR = pyautogui.prompt('What is your username?')
PW = pyautogui.prompt('What is your password?')
day_ran = pyautogui.prompt('Is this being ran after midnight? \n IE - If product is being shipped on Monday, is today technically Monday? \n Answer yes if true, Answer no if false.')



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




#Logging information
logging.info('Program was ran at ' + str(file_run_time))
#logging.info('Day value program was ran for: ' + str(day))
logging.info('Entery: ' + USR)
logging.info('Entery: ' + PW)


#This section begins typing the the routes

#Opens server2
pyautogui.press('win')
pyautogui.typewrite('Notepad')#, duration=1)
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
	time.sleep(1)

time.sleep(10)
pyautogui.typewrite('exit')
pyautogui.press('enter')