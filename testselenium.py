from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

#open Firefox
driver = webdriver.Firefox()

#go to the link
driver.get('https://www.youtube.com/watch?v=DXUAyRRkI6k')

# wait for the page to load everything (works without it)
for i in range(10):
    print(i)
    time.sleep(1)

#scroll the page
driver.execute_script("window.scrollBy(0, 500)")
time.sleep(10)
driver.execute_script("window.scrollBy(0, -500)")

#move the mouse
element = driver.find_element(By.ID, "search-icon-legacy")
actions = ActionChains(driver)
actions.move_to_element(element).perform()

#play the video
video = driver.find_element (By.ID, 'movie_player')
video.send_keys(Keys.SPACE) #hits space

#close the browser
time.sleep(20)
driver.close()