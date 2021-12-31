import pyautogui
import os
import re
import keyboard
import time

def create_screenshots():
    my_screenshot = pyautogui.screenshot()
    path_to_save = 'C:\\Users\\79215\\Documents'
    files = [f for f in os.listdir(path_to_save) if os.path.isfile(os.path.join(path_to_save, f))]
    scr_template = {'head': 'screenshot_', 'tail':'.jpg'}
    RE_SCREENSHOT = re.compile('^'+scr_template["head"]+r'(\d+)'+scr_template["tail"]+'$')
    # print(re.findall('(1)\s+(2)', '1  2 1  2'))
    jpgs = [0]
    for f in files:
        f1 = RE_SCREENSHOT.findall(f)
        if f1:
            try: 
                jpgs.append(int(f1[0]))
            except ValueError:
                pass

    jpgs.sort() 
    new_file_name = f'{scr_template["head"]}{jpgs[-1] + 1}{scr_template["tail"]}'
    new_file_path = os.path.join(path_to_save, new_file_name)
    my_screenshot.save(new_file_path)



while True:
    try:
        if keyboard.read_key() == 'ctrl':         
            print('create screenshot')
            create_screenshots()
            time.sleep(0.5)
    except:
        pass

    