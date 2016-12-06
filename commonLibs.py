from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys



def browser():
   browser = webdriver.Chrome("/Users/fivestars/Desktop/chromedriver")


def writePassed(testName):
    testPassed = open("/Users/fivestars/Desktop/testresults.txt", 'a')
    testPassed.write(" " + testName + " " + "passed" "\n")
    testPassed.close()

def writeFailed(testName):
    testFailed = open("/Users/fivestars/Desktop/testresults.txt", 'a')
    testFailed.write(" " + testName + " " + "failed" "\n")
    testFailed.close()

testName = "testname"

