from selenium import webdriver
import time
from Selenium import writing

testName = "reward redeemed successfully"
browser = webdriver.Chrome("/Users/fivestars/Desktop/chromedriver")
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
time.sleep(3)
checkInbutton = browser.find_element_by_xpath('/html/body/ion-side-menus/ion-nav-view/div[2]/ion-side-menu-content/ion-view/ion-header-bar/div/div[3]/div')
checkInbutton.click()
browser.implicitly_wait(5)
oneButton = browser.find_element_by_xpath('/html/body/ion-side-menus/ion-nav-view/div[2]/ion-side-menu-content/ion-view/ion-content/div/div/div/fs-phonepad/div[1]/div[1]/button')
twoButton = browser.find_element_by_xpath('/html/body/ion-side-menus/ion-nav-view/div[2]/ion-side-menu-content/ion-view/ion-content/div/div/div/fs-phonepad/div[1]/div[2]/button')
threeButton = browser.find_element_by_xpath('/html/body/ion-side-menus/ion-nav-view/div[2]/ion-side-menu-content/ion-view/ion-content/div/div/div/fs-phonepad/div[1]/div[3]/button')
fourButton = browser.find_element_by_xpath('/html/body/ion-side-menus/ion-nav-view/div[2]/ion-side-menu-content/ion-view/ion-content/div/div/div/fs-phonepad/div[2]/div[1]/button')
fiveButton = browser.find_element_by_xpath('/html/body/ion-side-menus/ion-nav-view/div[2]/ion-side-menu-content/ion-view/ion-content/div/div/div/fs-phonepad/div[2]/div[2]/button')
sixButton = browser.find_element_by_xpath('/html/body/ion-side-menus/ion-nav-view/div[2]/ion-side-menu-content/ion-view/ion-content/div/div/div/fs-phonepad/div[2]/div[3]/button')
sevenButton = browser.find_element_by_xpath('/html/body/ion-side-menus/ion-nav-view/div[2]/ion-side-menu-content/ion-view/ion-content/div/div/div/fs-phonepad/div[3]/div[1]/button')
eightButton = browser.find_element_by_xpath('/html/body/ion-side-menus/ion-nav-view/div[2]/ion-side-menu-content/ion-view/ion-content/div/div/div/fs-phonepad/div[3]/div[2]/button')
nineButton = browser.find_element_by_xpath('/html/body/ion-side-menus/ion-nav-view/div[2]/ion-side-menu-content/ion-view/ion-content/div/div/div/fs-phonepad/div[3]/div[3]/button')
zeroButton = browser.find_element_by_xpath('/html/body/ion-side-menus/ion-nav-view/div[2]/ion-side-menu-content/ion-view/ion-content/div/div/div/fs-phonepad/div[4]/div[2]/button')
goButton = browser.find_element_by_xpath('/html/body/ion-side-menus/ion-nav-view/div[2]/ion-side-menu-content/ion-view/ion-content/div/div/div/fs-phonepad/div[4]/div[3]/div/button')
fiveButton.click()
oneButton.click()
zeroButton.click()
threeButton.click()
fiveButton.click()
eightButton.click()
fiveButton.click()
nineButton.click()
fourButton.click()
threeButton.click()
time.sleep(2)
goButton.click()
browser.implicitly_wait(5)
time.sleep(1)
reward = browser.find_element_by_xpath('//*[@id="reward_list"]/fs-reward[1]/div/div/div[3]/div/div/div')
reward.click()
done = browser.find_element_by_xpath('//*[@id="main_content"]/div[2]/div/div[2]/button')
done.click()
time.sleep(6)
try:
    loginLogo = browser.find_element_by_xpath('/html/body/ion-side-menus/ion-nav-view/div[2]/ion-side-menu-content/ion-view/ion-header-bar/div/div[2]/img')
    if(loginLogo.is_displayed() == True):
        writing.writePassed(testName)
        browser.close()
except:
    writing.writeFailed(testName)
    browser.close()