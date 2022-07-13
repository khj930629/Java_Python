import pyautogui

print(pyautogui.position())
# pyautogui.click(x=496, y=8, duration=2)

pyautogui.keyDown('command')
pyautogui.press('space')
pyautogui.keyUp('command')
pyautogui.write('calc')
pyautogui.hotkey('enter')

pyautogui.sleep(1)
img = pyautogui.locateOnScreen('./pyauto_work/7.png', confidence=0.9)
pyautogui.click(img)
# pyautogui.write('7')

pyautogui.sleep(2)
win1 = pyautogui.getActiveWindow()
win1.close()
