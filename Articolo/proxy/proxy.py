import csv
import random
from selenium import webdriver
from selenium.webdriver.common.proxy import Proxy, ProxyType

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
browser = webdriver.Firefox(proxy=proxy_socks5)
browser.get('https://www.google.com')
