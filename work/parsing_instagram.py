from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import selenium.common.exceptions
import time
import random
 
# Login Credentials
username = 'dairon_evg'
password = 'Walterkovach1'
url = 'https://instagram.com/' + '_irina.demi_'

def path():
        global chrome   
        # starts a new chrome session
        # driver = webdriver.Chrome(ChromeDriverManager().install())
        chrome = webdriver.Chrome(r'C:\Users\79215\Downloads\chromedriver_win32\chromedriver.exe') # Add path if required

def url_name(url):
  chrome.get(url)  
  # adjust sleep if you want
  time.sleep(4)

def login(username, your_password):
    log_but = chrome.find_element_by_class_name("L3NKy")
    time.sleep(2)
    log_but.click()
    time.sleep(4)
     
    # finds the username box
    usern = chrome.find_element_by_name("username")
     
    # sends the entered username
    usern.send_keys(username)
 
    # finds the password box
    passw = chrome.find_element_by_name("password")
 
    # sends the entered password
    passw.send_keys(your_password)
     
    # press enter after sending password
    passw.send_keys(Keys.RETURN)
    time.sleep(5.5)
     
    # Finding Not Now button
    notk = chrome.find_element_by_class_name("yWX7d") 
    notk.click()
    time.sleep(3)

def send_message():
   
    # Find message button
    message = chrome.find_element_by_class_name('L3NKy ')
    message.click()
    time.sleep(2)
    # chrome.find_element_by_class_name('HoLwm ').click()
    # time.sleep(1)
    l = ['hello', 'Hi', 'How are You', 'Hey', 'Bro whats up']
    
    mbox = chrome.find_element_by_tag_name('textarea')
    mbox.send_keys("Готово, отослал посылку)")
    mbox.send_keys(Keys.RETURN)
    time.sleep(1.2)


path()
time.sleep(1)
url_name(url)
login(username, password)
send_message()
chrome.close()