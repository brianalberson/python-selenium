from selenium import webdriver
import time
from Selenium import writing

browser = webdriver.Chrome("/Users/fivestars/Desktop/chromedriver")
browser.get("http://localhost:8030/connect/#/login")
testName = "login was successful"
browser.implicitly_wait("5")
businessid = browser.find_element_by_name("business_id")
businessid.send_keys("BRIANTEST")
email = browser.find_element_by_name("email")
email.send_keys("brian.alberson@fivestars.com")
password = browser.find_element_by_name("password")
password.send_keys("fivestars")
sign_in = browser.find_element_by_id("signin_button")
browser.implicitly_wait(5)
sign_in.click()


time.sleep(5)
"""
ids = browser.find_elements_by_xpath('//*[@href]')

for ii in ids:
    print(ii.get_attribute('href'))
"""
"""
checkin = browser.find_element_by_xpath('html/body/ion-side-menus/ion-nav-view/div[2]/ion-side-menu-content/ion-view/ion-header-bar/div/div[3]/div')
checkin.click()"""

try:
    loginLogo = browser.find_element_by_xpath('/html/body/ion-side-menus/ion-nav-view/div[2]/ion-side-menu-content/ion-view/ion-header-bar/div/div[2]/img')
    if (loginLogo.is_displayed() == True):
        writing.writePassed(testName)
        browser.close()
except:
    writing.writeFailed(testName)
    browser.close()







