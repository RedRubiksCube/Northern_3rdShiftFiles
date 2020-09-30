import pyautogui, time

pyautogui.press('win')
pyautogui.typewrite('notepad')#, duration=1)
pyautogui.press('enter')
time.sleep(5)
pyautogui.press('win', 'left')