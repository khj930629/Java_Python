import pyautogui

pyautogui.keyDown('command')
pyautogui.press('space')
pyautogui.keyUp('command')
pyautogui.write('excel')
pyautogui.hotkey('enter')

pyautogui.sleep(2)
pyautogui.hotkey('enter')
