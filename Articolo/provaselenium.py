import sys
sys.path.append("/Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10/site-packages")

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.firefox.options import Options
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.proxy import Proxy, ProxyType
from random import *

import csv
import random
from selenium import webdriver
from selenium.webdriver.common.proxy import Proxy, ProxyType

#cambia sto numero qui per farlo rimanere in esecuzione più a lungo
for i in range(0,100):
    # Read proxy list from CSV file
    with open('proxylist.csv', newline='') as csvfile:
        proxyreader = csv.DictReader(csvfile)
        proxies = []
        for row in proxyreader:
            proxies.append(row)

# Select a random proxy from the list
proxy = random.choice(proxies)

 # Set up the proxy configuration for Selenium
proxy_address = proxy['IP Address'] + ':' + proxy['Port Number']
proxy_socks5 = Proxy({
    'proxyType': ProxyType.MANUAL,
    'socksProxy': proxy_address,
    'socksVersion': 5,
})

# Launch the browser with the selected proxy configuration
driver = webdriver.Firefox(proxy=proxy_socks5)
#driver.get('https://www.google.com')

    #p=False 
    #proxies=["45.77.56.114", "45.77.56.114"]
    #for i in range(len(proxies)):
        #time.sleep(randint(5,15))
        #options = Options()
        #options.set_preference('network.cookie.cookieBehavior', 2) # disable cookies


        #proxy= Proxy({
            #'proxyType': ProxyType.MANUAL,
            #'httpProxy': proxies[i]
        
        #if p:
            #driver = webdriver.Firefox(options=options, proxy=proxy)
        #else:
            #driver = webdriver.Firefox(options=options)

            
        # Navigate to the page with the cookies pop up
        #driver.get('https://www.youtube.com/watch?v=DXUAyRRkI6k')
driver.get("https://www.youtube.com/watch?v=Jo9El3rF0z8")

# Wait for the cookies pop up to appear, or continue execution after 10 seconds
try:
        cookies_popup = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'cookies-popup')))
        accept_button = cookies_popup.find_element(By.ID, 'accept-button')
        accept_button.click()
except:
        print('Cookies pop up not found within 10 seconds')

#for i in range(0,100):
#i += 1
print("prima sleep")
#scroll the page
time.sleep(10)
print("dopo sleep")
driver.execute_script("window.scrollBy(0, 500)")


#click

button = driver.find_element(By.XPATH, "/html/body/c-wiz/div/div/div/div[2]/div[1]/div[3]/div[1]/form[2]/div/div/button/span")
button.click()
print("click")

#move the mouse
element = driver.find_element(By.ID, "title")
actions = ActionChains(driver)
actions.move_to_element(element).perform()

#play the video
video = driver.find_element (By.ID, 'movie_player')
video.send_keys(Keys.SPACE) #hits space

#close the browser
sl=random.randint(67,130)
time.sleep(sl)