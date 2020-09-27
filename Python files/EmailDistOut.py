import pyautogui, time


USR = pyautogui.prompt('What is your username?')
PW = pyautogui.prompt('What is your password?')

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

pyautogui.typewrite('cd /users/data/curtze1')
pyautogui.press('enter')

#District 2
pyautogui.typewrite('drun')
pyautogui.press('enter')
time.sleep(1)
pyautogui.typewrite('dailyoutstk')
pyautogui.press('enter')
time.sleep(15)

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
