import pyautogui
import time

side = 1
loopern = 0

def start():
    time.sleep(2)
    pyautogui.click(3813, 52) #øye
    #(1888, 58)
    time.sleep(0.5)
    pyautogui.press('winleft')
    time.sleep(1)
    pyautogui.write('klipp', interval=0.25)
    pyautogui.press('enter')
    time.sleep(1)
#start er injected inn i whole

def utoginn():
    pyautogui.click(3813, 52)#øye
    time.sleep(0.5)
    pyautogui.click(1977, 51)#pilH
    time.sleep(0.5)
    pyautogui.click(3813, 52)#øye
#utoginn er injected inn i sc_page1

def sc_page1():
    pyautogui.hotkey('ctrl', 'n') #ny SC
    time.sleep(1)
    pyautogui.moveTo(340, 37) #top left
    pyautogui.moveTo(340, 37)
    time.sleep(0.5)
    pyautogui.dragTo(3497, 2119, 0.2, button='left') #bottom right
    time.sleep(1.5)
    #pyautogui.moveTo(420, 2132)
    #time.sleep(1)
    pyautogui.moveTo(-844,741)
    pyautogui.click(-844,741) #snipp (denne er for å gå ut av brett)
    pyautogui.hotkey('ctrl', 's')
    time.sleep(1)
    global side
    pyautogui.write('side ' + str(side))
    time.sleep(0.5)
    pyautogui.press('enter')
    time.sleep(1)
    side += 2
    pyautogui.moveTo(512, 2132) #flytte musen til brett
    time.sleep(1)
    pyautogui.click(512, 2132) #brett (gå inn i brett)
    time.sleep(1)
    utoginn()
    time.sleep(0.5)
    pyautogui.moveTo(-844,741)
    pyautogui.click(-844,741) #snipp (denne er for å gå ut av brett)(420, 2132)(-844,741)
    time.sleep(0.5)


def alle():
    start()
    sc_page1()
    sc_page1()

def whole():
    start()
    global loopern
    while loopern < 320:
        sc_page1()
        if loopern == 319:
            break
        loopern += 1


whole()
#alle()


print(pyautogui.position())

