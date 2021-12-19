from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time


print('Whatsapp Bot, Version 1.0')

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://web.whatsapp.com/')
time.sleep(20)
driverx = '//div[contains(@class, "copyable-text selectable-text")]'

contacts = ['Alan']

message = 'Good Morning of Good Afternoom, your whatsapp was hacked, please send me credit card number and password, thanks!'

def SearchContacts(contacts):
    searching = driver.find_element_by_xpath(driverx)
    time.sleep(2)
    searching.click()
    time.sleep(2)
    searching.send_keys(contacts)
    time.sleep(2)
    searching.send_keys(Keys.ENTER)
    time.sleep(2)

def MessageUpload(message):
    fieldBoxMesage = driver.find_elements_by_xpath(driverx)
    fieldBoxMesage[1].click()
    time.sleep(2)
    fieldBoxMesage[1].send_keys(message)
    fieldBoxMesage[1].send_keys(Keys.ENTER)
    time.sleep(2)

for contact in contacts:
    SearchContacts(contact)
    MessageUpload(message)


print('Finished code')
print('=============================================')
print('Created by @starkzinho and @howstrangeoficial')
print('=============================================')
