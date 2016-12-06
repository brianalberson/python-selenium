from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time

import unittest

class LoginTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("/Users/fivestars/Desktop/chromedriver")
        self.driver.get("http://localhost:8030/connect/#/login")
        self.driver.implicitly_wait("10")

    def test_login(self):
        driver = self.driver
        bIDField = "business_id"
        emailFieldID    = "email"
        passFieldID = "fivestars"
        loginFieldID = "signin_button"

        bIDElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_name(bIDField))
        emailElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_name(emailFieldID))
        passElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_name(passFieldID))
        loginElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_name(loginFieldID))


        bIDElement.clear()
        bIDElement.send_keys(BRIANTEST)
        emailElement.clear()
        emailElement.send_keys("brian.alberson@fivestars.com")
        passElement.clear()
        passElement.send_keys(fivestars)
        loginElement.click()
        WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(""))



    def tearDown(self):
        self.driver = webdriver.Chrome("/Users/fivestars/Desktop/chromedriver")
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()