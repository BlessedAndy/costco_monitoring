'''
Created on Mar 27, 2020

@author: Administrator
'''
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from com.tools.notify import send_SMS_message

'''
Configuration block
'''
#Change to False when the script works
Debug = True

#------------------------------------------------------------
options = webdriver.ChromeOptions() 
options.add_argument("start-maximized")
options.add_argument('disable-infobars')

if(Debug == False):
    options.headless = True # set to headless without opening browser

#Your account and password for Costco
userEmail = 'xxx'
userPassword = 'xxx'
zipcode = 19087

def login_costco():
    driver = webdriver.Chrome(options=options, executable_path=r'C:/stock/chromedriver.exe')
    
    #Change the checkout URL as yours
    URL = 'https://sameday.costco.com/store/checkout_v3'
    driver.get(URL)
    
    #input userEmail and password
    input_zipcode = driver.find_element_by_id('signup-zipcode')
    input_zipcode.clear()
    input_zipcode.send_keys(zipcode)
    input_zipcode.send_keys(Keys.ENTER)
    
    sleep(7)
    #input userEmail and password
    input_userEmail = driver.find_element_by_id('logonId')
    input_userEmail.clear()
    input_userEmail.send_keys(userEmail)
     
    input_userPassword = driver.find_element_by_id('logonPassword')
    input_userPassword.clear()
    input_userPassword.send_keys(userPassword)
    input_userPassword.send_keys(Keys.ENTER)
    
    sleep(7)
    #go to cart
    driver.get('https://sameday.costco.com/store/checkout_v3')
    sleep(12)
    
    while True:
        driver.refresh()
        sleep(7)
        
        try:
            Delivery_options = driver.find_element_by_id('Delivery options').text
            print(Delivery_options)
        except Exception:
            print('There is time slot available now ...')
            send_SMS_message('There is time slot available now ...')
            
        if(Delivery_options != 'No delivery times available. Right now, all shoppers are busy and working hard to get to every order. Please check back later to see if deliveries are available.'):
            print('There is time available now ...')
            send_SMS_message('There is time available now ...')
            
    driver.close()
    
login_costco()

#TODO:
#auto purchase
'''
click continue:

<button type="submit" data-radium="true" style="touch-action: manipulation; cursor: pointer; border: 1px solid transparent; border-radius: 4px; font-weight: 600; white-space: nowrap; user-select: none; -webkit-font-smoothing: antialiased; background-image: none; display: inline-flex; align-items: center; padding-left: 16px; padding-right: 16px; font-size: 16px; height: 40px; background-color: rgb(48, 113, 169); color: rgb(238, 238, 238);">Continue</button>


place order:
<button type="button" data-radium="true" style="touch-action: manipulation; cursor: pointer; border: 1px solid transparent; border-radius: 4px; font-weight: 600; white-space: nowrap; user-select: none; -webkit-font-smoothing: antialiased; background-image: none; display: block; align-items: center; padding-left: 24px; padding-right: 24px; font-size: 18px; height: 48px; background-color: rgb(48, 113, 169); color: rgb(238, 238, 238); width: 100%;">Place order</button>
'''