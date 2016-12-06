

def writePassed(testName):
    testPassed = open("/Users/fivestars/Desktop/testresults.txt", 'a')
    testPassed.write(" " + testName + " " + "passed" "\n")
    testPassed.close()

def writeFailed(testName):
    testFailed = open("/Users/fivestars/Desktop/testresults.txt", 'a')
    testFailed.write(" " + testName + " " + "failed" "\n")
    testFailed.close()

testName = "testname"



