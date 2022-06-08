class TestCase:
    def __init__(self, name):
        self.name = name
    def run(self):
        self.setUp()
        method = getattr(self, self.name)
        method()
        self.tearDown()
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

# TestCaseTest("testRunning").run()
TestCaseTest("testTemplateMethod").run()