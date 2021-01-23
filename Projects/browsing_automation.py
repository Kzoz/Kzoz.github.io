from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

keyw = input('What are you looking for on Youtube: ')
driver = webdriver.Chrome()
driver.maximize_window()
time.sleep(5)

youtube = 'https://www.youtube.com/'
theverge = 'https://www.theverge.com/'
bbcnews = 'https://www.bbc.com/news'
japantimes = 'https://www.japantimes.co.jp'

driver.get(youtube)

search_box = driver.find_element_by_xpath('//*[@id="search"]')
search_box.send_keys(keyw)

search_button = driver.find_element_by_xpath('//*[@id="search-icon-legacy"]')
search_button.click()

driver.execute_script("window.open('');")
driver.switch_to_window(driver.window_handles[1])
driver.get(theverge)
time.sleep(1)

driver.execute_script("window.open('');")
driver.switch_to_window(driver.window_handles[2])
driver.get(bbcnews)
time.sleep(1)

driver.execute_script("window.open('');")
driver.switch_to_window(driver.window_handles[3])
driver.get(japantimes)
# The colab automation is not trusted by Chrome thus requires an credentials.

#driver.get('https://colab.research.google.com/drive/1DisWLq2mESaqQc4wpowOwCPj08_Kgcy2')
#launchcode = driver.find_element_by_xpath('//*[@id="cell-matNcb0UC5gj"]/div[2]/div[2]/div[1]/div[1]/div/colab-run-button//div/div[2]/iron-icon')
#launchcode.click()
#launchcode2 = driver.find_element_by_xpath('//*[@id="cell-bi1HB7A2EBqA"]/div[2]/div[2]/div[1]/div[1]/div/colab-run-button//div/div[2]/iron-icon')
#launchcode2.click()
#launchcode3 = driver.find_element_by_xpath('//*[@id="cell-3N9iYJC_Glpc"]/div[2]/div[2]/div[1]/div[1]/div/colab-run-button//div/div[2]/iron-icon')
#launchcode3.click()
#def automate(lst):
#    for i in lst:
#        i
#        i.click()
