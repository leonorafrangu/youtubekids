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

#open Firefox
driver = webdriver.Firefox()

#go to the link
driver.get('https://www.youtube.com/')

# Wait for the cookies pop up to appear, or continue execution after 10 seconds
try:
        cookies_popup = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'cookies-popup')))
        accept_button = cookies_popup.find_element(By.ID, 'accept-button')
        accept_button.click()
except:
        print('Cookies pop up not found within 10 seconds')

button = driver.find_element(By.XPATH, "/html/body/ytd-app/ytd-consent-bump-v2-lightbox/tp-yt-paper-dialog/div[4]/div[2]/div[6]/div[1]/ytd-button-renderer[2]/yt-button-shape/button/yt-touch-feedback-shape/div/div[2]")
button.click()
print("click")

# wait for the page to load everything (works without it)
for i in range(10):
    print(i)
    time.sleep(1)

#go to the search bar
search_bar = driver.find_element(By.NAME, "search_query")
search_bar.send_keys("\"all about toys store\"")
search_bar.submit()
time.sleep(10)

#scroll the page
#driver.execute_script("window.scrollBy(0, 500)")
#time.sleep(2)
#driver.execute_script("window.scrollBy(0, -500)")

#move the mouse
element = driver.find_element(By.ID, "title")
actions = ActionChains(driver)
actions.move_to_element(element).perform()

#/html/body/ytd-app/div[1]/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer[1]/div[3]/ytd-video-renderer/div[1]/div/div[1]/div/h3/a/yt-formatted-string
button = driver.find_element(By.XPATH, "/html/body/ytd-app/div[1]/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer[1]/div[3]/ytd-video-renderer/div[1]/div/div[1]/div/h3/a/yt-formatted-string")
button.click()
print("click")


#play the video
video = driver.find_element (By.ID, 'movie_player')
try:
    video.send_keys(Keys.SPACE) #hits space
except:
    video.send_keys(Keys.SPACE) #hits space
print("spero che sia la fine")
#close the browser
sl=random.randint(67,130)
print("hh")
time.sleep(sl)
print("jj")
driver.close()
print("fine")
