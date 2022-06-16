class TestCase:
    def __init__(self, name):
        self.name = name
    def run(self, result):
        # result = TestResult()
        result.testStarted()
        self.setUp()
        try:
            method = getattr(self, self.name)
            method()
        except:
            result.testFailed()
        self.tearDown()
        # return result
    def setUp(self):
        pass
    def tearDown(self):
        pass

class WasRun(TestCase):
    # def __init__(self, name):
    #     self.wasRun = None
    #     super().__init__(name)
    def testMethod(self):
        # self.wasRun = 1
        self.log = self.log + "testMethod "
    def testBrokenMethod(self):
        raise Exception
    def setUp(self):
        # self.wasRun = None
        # self.wasSetUp = 1
        self.log = "setUp "
    def tearDown(self):
        self.log = self.log + "tearDown "

class TestCaseTest(TestCase):
    def setUp(self):
        self.result = TestResult()
    #     self.test = WasRun("testMethod")
    # def testRunning(self):
        # test = WasRun("testMethod")
        # assert(not test.wasRun)
        # self.test.run()
        # assert (self.test.wasRun)
    def testTemplateMethod(self):
        test = WasRun("testMethod")
        # result = TestResult()
        test.run(self.result)
        assert ("setUp testMethod tearDown " == test.log)
    def testResult(self):
        test = WasRun("testMethod")
        # result = TestResult()
        test.run(self.result)
        assert ("1 run, 0 failed" == self.result.summary())
    def testFailedResult(self):
        test = WasRun("testBrokenMethod")
        # result = TestResult()
        test.run(self.result)
        assert("1 run, 1 failed" == self.result.summary())
    def testFailedResultFormatting(self):
        # result = TestResult()
        self.result.testStarted()
        self.result.testFailed()
        assert ("1 run, 1 failed" == self.result.summary())
    def testSuite(self):
        suite = TestSuite()
        suite.add(WasRun("testMethod"))
        suite.add(WasRun("testBrokenMethod"))
        # result = TestResult()
        suite.run(self.result)
        assert ("2 run, 1 failed" == self.result.summary())

class TestSuite:
    def __init__(self):
        self.tests = []
    def add(self, test):
        self.tests.append(test)
    def run(self, result):
        # result = TestResult()
        for test in self.tests:
            test.run(result)
        # return result

class TestResult:
    def __init__(self):
        self.runCount = 0
        self.errorCount = 0
    def testStarted(self):
        self.runCount = self.runCount + 1
    def testFailed(self):
        self.errorCount = self.errorCount + 1
    def summary(self):
        return "%d run, %d failed" % (self.runCount, self.errorCount)

# TestCaseTest("testRunning").run()
# print(TestCaseTest("testTemplateMethod").run().summary())
# print(TestCaseTest("testResult").run().summary())
# print(TestCaseTest("testFailedResult").run().summary())
# print(TestCaseTest("testFailedResultFormatting").run().summary())
# print(TestCaseTest("testSuite").run().summary())

suite = TestSuite()
suite.add(TestCaseTest("testTemplateMethod"))
suite.add(TestCaseTest("testResult"))
suite.add(TestCaseTest("testFailedResult"))
suite.add(TestCaseTest("testFailedResultFormatting"))
suite.add(TestCaseTest("testSuite"))
result = TestResult()
suite.run(result)
print(result.summary())