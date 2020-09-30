import pyautogui, time

Route_QTY = pyautogui.prompt('How many routes are we processing? \n Must enter a integer')
QTY_range = (1, int(Route_QTY))

print(Route_QTY)
print(QTY_range)
#for i in QTY_R:
#	print(QTY_range)
