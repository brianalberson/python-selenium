from selenium import webdriver
import time
from Selenium import writing
from Selenium import commonLibs


testName = "login was successful"
businessid = login.browser().find_element_by_name("business_id")
email = login.browser().find_element_by_name("email")
password = login.browser().find_element_by_name("password")
sign_in = login.browser().find_element_by_id("signin_button")
login = commonLibs.browser().getMtab()


login.getMtab()
login.implicitly_wait("5")
businessid.send_keys("BRIANTEST")
email.send_keys("brian.alberson@fivestars.com")
password.send_keys("fivestars")
login.implicitly_wait(5)
sign_in.click()
time.sleep(5)

try:
    loginLogo = browser.find_element_by_xpath('/html/body/ion-side-menus/ion-nav-view/div[2]/ion-side-menu-content/ion-view/ion-header-bar/div/div[2]/img')
    if (loginLogo.is_displayed() == True):
        writing.writePassed(testName)
        browser.close()
except:
    writing.writeFailed(testName)
    browser.close()