import pyautogui
import time

while(True):
    try:
        buttonx, buttony = pyautogui.locateCenterOnScreen('btn.png', confidence=0.9)
        pyautogui.click(buttonx, buttony) 

        time.sleep(1.5)

        buttonx, buttony = pyautogui.locateCenterOnScreen('btn2.png', confidence=0.9)
        pyautogui.click(buttonx, buttony) 

        time.sleep(1.5)
        
        buttonx, buttony = pyautogui.locateCenterOnScreen('btnclose.png', confidence=0.9)
        pyautogui.click(buttonx, buttony)
    except TypeError:
        print("A TypeError has been occured!")