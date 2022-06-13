class TestCase:
    def __init__(self, name):
        self.name = name
    def run(self):
        result = TestResult()
        result.testStarted()
        self.setUp()
        method = getattr(self, self.name)
        method()
        self.tearDown()
        return result
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
    # def setUp(self):
    #     self.test = WasRun("testMethod")
    # def testRunning(self):
        # test = WasRun("testMethod")
        # assert(not test.wasRun)
        # self.test.run()
        # assert (self.test.wasRun)
    def testTemplateMethod(self):
        test = WasRun("testMethod")
        test.run()
        assert ("setUp testMethod tearDown " == test.log)
    def testResult(self):
        test = WasRun("testMethod")
        result = test.run()
        assert ("1 run, 0 failed" == result.summary())
    def testFailedResult(self):
        test = WasRun("testBrokenMethod")
        result = test.run()
        assert("1 run, 1 failed" == result.summary())

class TestResult:
    def __init__(self):
        self.runCount = 0
    def testStarted(self):
        self.runCount = self.runCount + 1
    def summary(self):
        return "%d run, 0 failed" % self.runCount

# TestCaseTest("testRunning").run()
TestCaseTest("testTemplateMethod").run()
TestCaseTest("testResult").run()
# TestCaseTest("testFailedResult").run()