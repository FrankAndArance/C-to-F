import pyautogui
from time import sleep, time
import keyboard
from IPython.display import clear_output

# 設定每一個動作，都暫停若干秒
pyautogui.PAUSE = 0.05


def click_first():    
    
     # 比對所有圖片，取得顯示在桌面的圖片物件 (pillow / PIL Image)
    btn_fastfight_location = pyautogui.locateOnScreen('images/fastfight.png', confidence=0.8)              
    # 取得每一個圖片的中心點
    btn_fastfight_point = pyautogui.center(btn_fastfight_location)    
    # 點擊圖片
    pyautogui.click(btn_fastfight_point)
        
    sleep(0.1)
        
    while True:
        try:        
            sleep(0.1)
        
            btn_continues_location = pyautogui.locateOnScreen('images/continues.png', confidence=0.8)
        
            btn_continues_point = pyautogui.center(btn_continues_location)
        
            pyautogui.click(btn_continues_point)
            
        except TypeError:
            break

def click_second():       
    sleep(0.1)
        
    btn_open_location = pyautogui.locateOnScreen('images/open.png', confidence=0.8)
        
    btn_open_point = pyautogui.center(btn_open_location)
        
    pyautogui.click(btn_open_point)
    

def click_third():
    sleep(0.1)
                 
    btn_getfewpower_location = pyautogui.locateOnScreen('images/getfewpower.png', confidence=0.8)        
            
    btn_getfewpower_point = pyautogui.center(btn_getfewpower_location)
    
    pyautogui.click(btn_getfewpower_point)
    
    sleep(0.1)
    
    while True:
        try:        
            sleep(0.1)
        
            btn_clickspace_location = pyautogui.locateOnScreen('images/clickspace.png', confidence=0.8)
        
            btn_clickspace_point = pyautogui.center(btn_clickspace_location)
        
            pyautogui.click(btn_clickspace_point)
            
        except TypeError:
            break
    
       
def click_fourth():
    sleep(0.1)
            
    btn_getmorepower_location = pyautogui.locateOnScreen('images/getmorepower.png', confidence=0.8)        
            
    btn_getmorepower_point = pyautogui.center(btn_getmorepower_location)
    
    pyautogui.click(btn_getmorepower_point)
    
    sleep(0.1)
    
    while True:
        try:        
            sleep(0.1)
        
            btn_clickspace_location = pyautogui.locateOnScreen('images/clickspace.png', confidence=0.8)
        
            btn_clickspace_point = pyautogui.center(btn_clickspace_location)
        
            pyautogui.click(btn_clickspace_point)
            
        except TypeError:
            break
                 
                    
def click_fifth():
    sleep(0.1)
             
    btn_getlotpower_location = pyautogui.locateOnScreen('imagess/getlotpower.png', confidence=0.8)        
            
    btn_getlotpower_point = pyautogui.center(btn_getlotpower_location)
    
    pyautogui.click(btn_getlotpower_point)
    
    sleep(0.1)
    
    while True:
        try:        
            sleep(0.1)
        
            btn_clickspace_location = pyautogui.locateOnScreen('images/clickspace.png', confidence=0.8)
        
            btn_clickspace_point = pyautogui.center(btn_clickspace_location)
        
            pyautogui.click(btn_clickspace_point)
            
        except TypeError:
            break

    
def click_sixth():
    sleep(0.1)
             
    btn_search_location = pyautogui.locateOnScreen('imagess/search.png', confidence=0.8)        
            
    btn_search_point = pyautogui.center(btn_search_location)
    
    pyautogui.click(btn_search_point)           

    
    
while True:
    print('start')
    if pyautogui.locateOnScreen('images/fastfight.png', confidence=0.8) != None:
        print('test1')
        click_first()
                        
    if pyautogui.locateOnScreen('images/open.png', confidence=0.8) != None:
        print('test2')
        click_second()
                   
    if pyautogui.locateOnScreen('images/getfewpower.png', confidence=0.8) != None:
        print('test3')
        click_third()
               
    if pyautogui.locateOnScreen('images/getmorepower.png', confidence=0.8) != None:
        print('test4')
        click_fourth()
                 
    if pyautogui.locateOnScreen('images/getlotpower.png', confidence=0.8) != None:
        print('test5')
        click_fifth()

    if pyautogui.locateOnScreen('images/search.png', confidence=0.8) != None:
        print('test6')
        click_sixth()
        
    # 按 alt 結束迴圈
    if keyboard.is_pressed('alt'):
        break
        
    else:
        continue
