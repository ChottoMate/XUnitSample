class TestCase:
    def __init__(self, name):
        self.name = name
    def run(self):
        self.setUp()
        method = getattr(self, self.name)
        method()
    def setUp(self):
        pass

class WasRun(TestCase):
    # def __init__(self, name):
    #     self.wasRun = None
    #     super().__init__(name)
    def testMethod(self):
        self.wasRun = 1
    def setUp(self):
        self.wasRun = None
        self.wasSetUp = 1

class TestCaseTest(TestCase):
    def setUp(self):
        self.test = WasRun("testMethod")
    def testRunning(self):
        # test = WasRun("testMethod")
        # assert(not test.wasRun)
        self.test.run()
        assert (self.test.wasRun)
    def testSetUp(self):
        # test = WasRun("testMethod")
        self.test.run()
        assert (self.test.wasSetUp)

TestCaseTest("testRunning").run()
TestCaseTest("testSetUp").run()