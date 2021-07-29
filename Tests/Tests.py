__author__ = 'O Adeleye'

import time
from parameterized import parameterized, parameterized_class
import unittest
import pandas as pd
from selenium import webdriver
from Resources.Locators import Locators
from Resources.PageObjects.Pages import AboutQuestions, HomePage, PostForm, ProcessPostStatus, SearchStatusForm, \
    SearchStatusResult
from Resources.TestData import TestData
from Resources.Write import Write


# Base Class for the tests
class Test_Base(unittest.TestCase):

    def setUp(self):
        "Setting up how we want Chrome to run"
        chrome_options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(TestData.CHROME_EXECUTABLE_PATH, options=chrome_options)
        # browser should be loaded in maximized window
        self.driver.maximize_window()

    def tearDown(self):
        "To do the cleanup after test has executed."
        self.driver.close()
        self.driver.quit()


# names = TestData.read_username()
# df = pd.read_csv(r"C:\Users\HP 1040 G2\PycharmProjects\WebDevTest\Resources\std.csv", encoding='utf-8')
# df = df["username"].type(str)

# @parameterized_class(('n',), names)
def write_result():
    Write.results()

#@parameterized_class(('n',), [("gqk9788",),("fsc3111",),("zvq1157",),("njm7162",),("zjj1672",),("vqv8807",),("pxq6189",),("nnk6362",),("xbn4166",),("jff7367",),("ggh9947",),("sgk6741",),("frs9688",),("kdr1283",),("wxx6957",)])
#@parameterized_class(('n',), [("qfw3690",), ("pwm1057",), ("jpn5953",),("wcj0143",),("kyk7346",),("jsj6212",),("msc0848",), ("ybn3442",),("pbm0950",),("bss5188",)])
#@parameterized_class(('n',), [("knw9556",),("kwg5145",),("pgv1165",),("hmy5518",), ("wrc0329",), ("dkp5561",),("grg3725",),("pqh3376",),("ghq8692",)])
#@parameterized_class(('n',), [("cdk7156",),("ngp9017",), ("ytk0657",),("svc3366",),("gdt5133",), ("kyj3313",), ("xsn0308",),("xtv5949",),("jvz2508",),("cpc5502",)])
#@parameterized_class(('n',), [("bcc9954",),("ryp7807",),("wsx3714",),("cqf3154",),("hdv4639",),("sfr2717",),("krx3446",),("qvw4247",),("gkv0170",),("nnr8218",),("cvb1418",),("kxt7346",),("nsw2205",),("cvz0516",)])
@parameterized_class(('n',), [("kdm4487",),("cfq6450",),("cgm7577",),("qmj0723",),("knp3972",),("xks8166",),("hmp1716",),("nmb2927",),("wfh1924",),("hyp9617",),("xpt4616",),("vvn0316",)])


# Test Class containing all tests
class Test_Cases(Test_Base):
    def setUp(self):
        super().setUp()

    def test_home_page_loaded_successfully(self):
        # instantiate an object of HomePage class. Remember when the constructor of HomePage class is called
        # it opens up the browser and navigates to Home Page of the site under test.
        self.homePage = HomePage(self.driver, self.n)
        self.homePage.verify_index_page_info()

    def test_post_form(self):
        self.postForm = PostForm(self.driver, self.n)
        self.postForm.check_postForm_elements()
        print("SUMMARY: ")
        self.postForm.check_post_method()

    # specify path where the HTML reports for testcase execution are to be generated

    def test_post_process(self):
        self.postProcess = ProcessPostStatus(self.driver, self.n)
        print("SUMMARY: ")
        self.postProcess.status_code_validation()
        print("SUMMARY: ")
        self.postProcess.status_validation()
        print("SUMMARY: ")
        self.postProcess.scode_uniqueness()
        print("SUMMARY: ")
        self.postProcess.is_address_relative()

    def test_search_status_form(self):
        self.statusForm = SearchStatusForm(self.driver, self.n)
        print("SUMMARY: ")
        self.statusForm.check_searchForm()

    def test_search_status_result(self):
        self.search_statusResult = SearchStatusResult(self.driver, self.n)
        print("SUMMARY: ")
        self.search_statusResult.check_searchResult()
        print("SUMMARY: ")
        self.search_statusResult.search_string_validation()

    def test_t_about_page(self):
        self.about_page = AboutQuestions(self.driver, self.n)
        print("SUMMARY: ")
        self.about_page.check_about_url_and_question()


if __name__ == '__main__':
    # unittest.main()

    log_file = 'log_file'
    with open(log_file, "+w") as f:
        runner = unittest.TextTestRunner(f)
        unittest.main(testRunner=runner)
    f.close()
