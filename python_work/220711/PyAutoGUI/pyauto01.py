import pyautogui

# python -m pip install -U pip setuptoools
# pip install pyautogui

print(pyautogui.size())
print(pyautogui.position())

# pyautogui.screenshot('icon.png', region=(492, 9, 20, 44))
# pyautogui.click('icon.png')

# pyautogui.moveTo(x=548,y=19)
# pyautogui.click()
img = pyautogui.locateOnScreen('./python_work/220711/help.png', confidence=0.9)
# pyautogui.click('./python_work/220711/help.png')
pyautogui.click(img)
# pip install opencv-python
