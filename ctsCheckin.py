from selenium import webdriver
import time
from Selenium import writing

testName = "Cts Checkin Appears"
browser = webdriver.Chrome("/Users/fivestars/Desktop/chromedriver")
ctsbrowser = webdriver.Chrome("/Users/fivestars/Desktop/chromedriver")
browser.get("http://localhost:8030/connect/#/login")
browser.implicitly_wait(5)
browser.implicitly_wait(5)
businessid = browser.find_element_by_name("business_id")
businessid.send_keys("BRIANTEST")
email = browser.find_element_by_name("email")
email.send_keys("brian.alberson@fivestars.com")
password = browser.find_element_by_name("password")
password.send_keys("fivestars")
sign_in = browser.find_element_by_id("signin_button")
browser.implicitly_wait(5)
sign_in.click()
browser.implicitly_wait(5)
time.sleep(10)

ctsbrowser.get('http://localhost:8030/cts/#/login')
ctsbrowser.implicitly_wait(5)
ctsbrowser.implicitly_wait(5)
ctsBID = ctsbrowser.find_element_by_name('business_id')
ctsBID.send_keys('BRIANTEST')
ctsEmail = ctsbrowser.find_element_by_name('email')
ctsEmail.send_keys('brian.alberson@fivestars.com')
ctsPass = ctsbrowser.find_element_by_name('password')
ctsPass.send_keys('fivestars')
cts_sign_in = ctsbrowser.find_element_by_id('signin_button')
ctsbrowser.implicitly_wait(5)
cts_sign_in.click()
ctsOneButton = ctsbrowser.find_element_by_xpath('/html/body/ion-side-menus/ion-nav-view/ion-view[2]/ng-include/ion-content/div/div[1]/div[2]/div[1]/fs-phonepad/div[1]/div[1]/button')
ctsTwoButton = ctsbrowser.find_element_by_xpath('/html/body/ion-side-menus/ion-nav-view/ion-view[2]/ng-include/ion-content/div/div[1]/div[2]/div[1]/fs-phonepad/div[1]/div[2]/button')
ctsThreeButton = ctsbrowser.find_element_by_xpath('/html/body/ion-side-menus/ion-nav-view/ion-view[2]/ng-include/ion-content/div/div[1]/div[2]/div[1]/fs-phonepad/div[1]/div[3]/button')
ctsFourButton = ctsbrowser.find_element_by_xpath('/html/body/ion-side-menus/ion-nav-view/ion-view[2]/ng-include/ion-content/div/div[1]/div[2]/div[1]/fs-phonepad/div[2]/div[1]/button')
ctsFiveButton = ctsbrowser.find_element_by_xpath('/html/body/ion-side-menus/ion-nav-view/ion-view[2]/ng-include/ion-content/div/div[1]/div[2]/div[1]/fs-phonepad/div[2]/div[2]/button')
ctsSixButton = ctsbrowser.find_element_by_xpath('/html/body/ion-side-menus/ion-nav-view/ion-view[2]/ng-include/ion-content/div/div[1]/div[2]/div[1]/fs-phonepad/div[2]/div[3]/button')
ctsSevenButton = ctsbrowser.find_element_by_xpath('/html/body/ion-side-menus/ion-nav-view/ion-view[2]/ng-include/ion-content/div/div[1]/div[2]/div[1]/fs-phonepad/div[3]/div[1]/button')
ctsEightButton = ctsbrowser.find_element_by_xpath('/html/body/ion-side-menus/ion-nav-view/ion-view[2]/ng-include/ion-content/div/div[1]/div[2]/div[1]/fs-phonepad/div[3]/div[2]/button')
ctsNineButton = ctsbrowser.find_element_by_xpath('/html/body/ion-side-menus/ion-nav-view/ion-view[2]/ng-include/ion-content/div/div[1]/div[2]/div[1]/fs-phonepad/div[3]/div[3]/button')
ctsZeroButton = ctsbrowser.find_element_by_xpath('/html/body/ion-side-menus/ion-nav-view/ion-view[2]/ng-include/ion-content/div/div[1]/div[2]/div[1]/fs-phonepad/div[4]/div[2]/button')
ctsGoButton = ctsbrowser.find_element_by_xpath('/html/body/ion-side-menus/ion-nav-view/ion-view[2]/ng-include/ion-content/div/div[1]/div[2]/div[1]/fs-phonepad/div[4]/div[3]/div/button')

ctsFiveButton.click()
ctsOneButton.click()
ctsZeroButton.click()
ctsThreeButton.click()
ctsFiveButton.click()
ctsEightButton.click()
ctsFiveButton.click()
ctsNineButton.click()
ctsFourButton.click()
ctsThreeButton.click()
ctsGoButton.click()
time.sleep(10)

try:
    browser.refresh()
    browser.implicitly_wait(6)
    time.sleep(2)
    cts_is_checkedin = browser.find_element_by_xpath('/html/body/ion-side-menus/ion-nav-view/div[2]/ion-side-menu-content/ion-view/ion-content/div/div/div[2]/div/div/div[2]')
    if(cts_is_checkedin.is_displayed() == True):
        writing.writePassed(testName)
        browser.close()
        ctsbrowser.close()

except:
    writing.writeFailed(testName)
    browser.close()
    ctsbrowser.close()

