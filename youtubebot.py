import pyautogui
import time
time.sleep(3)
a = int(input("How much times would you like the video to be viewed: "))
b = input("Link to youtube video: ")
for i in range(a):
    #Giving the user 5 seconds to open the browser and let it be
    time.sleep(5)
    pyautogui.hotkey('ctrl', 't')#Opening a new tab
    pyautogui.write(b)#Writing the youtube video link
    pyautogui.press('enter')
    time.sleep(35)#You need at least 30 seconds of wathcing time to make it count aas a view
    pyautogui.hotkey('ctrl', 'w')#Closing the tab than repeating it again

