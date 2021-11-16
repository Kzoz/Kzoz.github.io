from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

#Open Chrome browser and maximize the size of the window
keyw = input('What are you looking for on Youtube: ')
googling = input('Google Search: ')
driver = webdriver.Chrome()
driver.maximize_window()
time.sleep(1)

#Websites to open
youtube = 'https://www.youtube.com/'
theverge = 'https://www.theverge.com/'
bbcnews = 'https://www.bbc.com/news'
japantimes = 'https://www.japantimes.co.jp'
google = 'https://www.google.com/'
new_tabs = [theverge,bbcnews,japantimes,google]

#Opening websites + doing searches on YT and Google
driver.get(youtube)
search_box = driver.find_element_by_xpath('//*[@id="search"]')
search_box.send_keys(keyw)
search_button = driver.find_element_by_xpath('//*[@id="search-icon-legacy"]')
search_button.click()

counter = 1
for i in new_tabs:

    driver.execute_script("window.open('');")
    driver.switch_to_window(driver.window_handles[counter])
    driver.get(i)
    time.sleep(1)
    counter+=1

search_google = driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input')
search_google.send_keys(googling)
search_google.send_keys(Keys.ENTER)