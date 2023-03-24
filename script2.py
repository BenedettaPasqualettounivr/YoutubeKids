from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

#open Firefox
driver = webdriver.Firefox()

#go to the link
driver.get('https://www.youtube.com/')

# wait for the page to load everything (works without it)
for i in range(10):
    print(i)
    time.sleep(1)

#go to the search bar
search_bar = driver.find_element(By.NAME, "search_query")
search_bar.send_keys("Teddy Ranunculaceae and his friends")
search_bar.submit()
time.sleep(10)

#scroll the page
driver.execute_script("window.scrollBy(0, 500)")
time.sleep(2)
driver.execute_script("window.scrollBy(0, -500)")




#close the browser
time.sleep(20)
driver.close()
