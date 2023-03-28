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

p=False 
proxies=["45.77.56.114", "45.77.56.114"]
for i in range(len(proxies)):
    time.sleep(randint(5,15))
    options = Options()
    options.set_preference('network.cookie.cookieBehavior', 2) # disable cookies


    proxy= Proxy({
        'proxyType': ProxyType.MANUAL,
        'httpProxy': proxies[i]
    })
    if p:
        driver = webdriver.Firefox(options=options, proxy=proxy)
    else:
        driver = webdriver.Firefox(options=options)

        
    # Navigate to the page with the cookies pop up
    driver.get('https://www.youtube.com/watch?v=DXUAyRRkI6k')

    # Wait for the cookies pop up to appear, or continue execution after 10 seconds
    try:
        cookies_popup = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'cookies-popup')))
        accept_button = cookies_popup.find_element(By.ID, 'accept-button')
        accept_button.click()
    except:
        print('Cookies pop up not found within 10 seconds')


    #scroll the page
    driver.execute_script("window.scrollBy(0, 500)")
    time.sleep(10)
    driver.execute_script("window.scrollBy(0, -500)")

    #move the mouse
    element = driver.find_element(By.ID, "title")
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()

    #play the video
    video = driver.find_element (By.ID, 'movie_player')
    video.send_keys(Keys.SPACE) #hits space

    #close the browser
    time.sleep(50)
    driver.close()
