# Setting up Module
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

# Opening the browser
browser=webdriver.Chrome(executable_path='Chromedriver\\chromedriver.exe')
browser.get('https://playtennis.usta.com/palencia/Booking/BookByDate')

# SighIn Process
browser.find_element_by_xpath('/html/body/header/div/div/div[2]/div[3]/div/ul/li[2]').click()
browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div[2]/div[2]/div[2]/div/form/div[1]/input').send_keys('marwan.zakaria@gmail.com')
browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div[2]/div[2]/div[2]/div/form/div[2]/input').send_keys('xhd6UPR.veh7gtv*cmh')
browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div[2]/div[2]/div[2]/div/form/input[3]').click()

# Going three days from today
for i in range(3):
    try:
        browser.find_element_by_xpath('/html/body/div[4]/div[2]/div/div/div/form/div/div/div[1]/div/div[1]/a[3]').click()
    except:
        browser.implicitly_wait(3)
        browser.find_element_by_xpath('/html/body/div[4]/div[2]/div/div/div/form/div/div/div[1]/div/div[1]/a[3]').click()
        continue

#Finding the Pickle A or B
while True:
    try:
        browser.find_element_by_xpath('/html/body/div[4]/div[2]/div/div/div/form/div/div/div[2]/div[2]/a[1]').click()
        
        # Seleting the timing in the court
        courtName=browser.find_element_by_xpath('/html/body/div[4]/div[2]/div/div/div/form/div/div/div[2]/div[2]/ul/li[%s]/div/div/div[1]/h3'%('11'))
        if (courtName=='Pickle A') or (courtName=="Pickle B"):

            browser.find_element_by_xpath('/html/body/div[4]/div[2]/div/div/div/form/div/div/div[2]/div[2]/ul/li[11]/div/div/div[2]/div[1]/div[2]').click()

            browser.find_element_by_xpath('/html/body/div[8]/div/div/div/div[1]/form/div[1]/div[1]/div[2]/div/div/div/span/span/span[2]').click()
            browser.find_element_by_xpath('/html/body/div[8]/div/div/div/div[1]/form/div[1]/div[1]/div[2]/div/div/div/span/ul/li[4]').click()
            # browser.find_element_by_xpath('/html/body/div[8]/div/div/div/div[1]/form/div[2]/div/button').click()
            break
    except:
        break

