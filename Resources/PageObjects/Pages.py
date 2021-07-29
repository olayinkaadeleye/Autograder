__author__ = 'O Adeleye'

import sys
import time
import html2text
import re
import random
from datetime import datetime
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from Resources.Locators import Locators
from Resources.TestData import TestData


class BasePage():
    """This class is the parent class for all the pages in our application."""
    """It contains all common elements and functionalities available to all pages."""

    # this function is called every time a new object of the base class is created.
    def __init__(self, driver):
        self.driver = driver

    # this function performs click on web element whose locator is passed to it.
    def click(self, by_locator):
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(by_locator)).click()

    def post(self, by_locator):
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(by_locator)).send_keys(Keys.RETURN)

    # this function asserts comparison of a web element's text with passed in text.
    def assert_element_text(self, by_locator, element_text):
        web_element = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(by_locator))
        assert web_element.text == element_text

    # this function performs text entry of the passed in text, in a web element whose locator is passed to it.
    def enter_text(self, by_locator, text):
        return WebDriverWait(self.driver, 2).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    # this function checks if the web element whose locator has been passed to it, is enabled or not and returns
    # web element if it is enabled.
    def is_enabled(self, by_locator):
        return WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(by_locator))

    # this function checks if the web element whose locator has been passed to it, is visible or not and returns
    # true or false depending upon its visibility.
    def is_visible(self, by_locator):
        element = WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(by_locator))
        return bool(element)

    # this function moves the mouse pointer over a web element whose locator has been passed to it.
    def hover_to(self, by_locator):
        element = WebDriverWait(self.driver, 2).until(EC.visibility_of_element_located(by_locator))
        ActionChains(self.driver).move_to_element(element).perform()

    def word_count(self, str):
        counts = dict()
        words = str.split()
        for word in words:
            if word in counts:
                counts[word] += 1
            else:
                counts[word] = 1
        return counts


class HomePage(BasePage):
    """Home Page Assignment-1 (index.html)"""

    def __init__(self, driver, name):
        super().__init__(driver)
        self.name = name
        self.driver.get(TestData(name).base_urls())
        print(".....Beginning TASK 1: Index Page........")

    """TASK 1"""

    def verify_index_page_info(self):
        global missing_urls
        html = self.driver.page_source
        mark = 2
        c = html2text.html2text(html).lower()
        # print (c)
        links = self.driver.find_elements(*Locators.HOMEPAGE_LINKS)
        window_before = self.driver.window_handles[0]
        print("Task 1(a)...Summary....................:")
        for info in TestData.INDEX_INFO:
            m = re.search((info + ".*").lower(), c.lower())
            if m:
                # include student details in the feedback
                print("{} information is included".format(m.group()))
            else:
                mark = mark - 0.5
                print("{} is required page information but missing: (-0.5 marks)".format(info))
        print("Task (1a) mark received = {}".format(mark))
        i = 0
        urls = []
        irregular_url = []
        """Test if all the links on index page is working"""
        print("Task 1(b)...Summary....................:")
        mark = 3
        for link in links:
            urls.append(link.get_attribute('href'))
            self.driver.execute_script("window.open('" + link.get_attribute('href') + "');")
            self.driver.switch_to.window(self.driver.window_handles[i])
            i = i + 1
            """check if link addressing follows required syntax"""
            if self.driver.current_url not in TestData(self.name).URLS():
                irregular_url.append(self.driver.current_url)
            self.driver.switch_to.window(window_before)

        if irregular_url:
            irregular_url = [x for x in irregular_url if "https" not in x]
            print(" The following addressing: {} appear(s) not follow the required syntax (-2 marks)".format(
                set(irregular_url)))
            mark = mark - (len(set(irregular_url)) * 0.5)

        else:
            print("Links worked for using the relative addressing.")

        """check if necessary links are included on the page"""
        # print(urls)
        global page_urls;
        p_urls = set(urls)  # webpage urls
        missing_url = sorted(set(TestData(self.name).HOMEPAGE_URLS()) - p_urls)
        if not urls and not irregular_url:
            print("Please upload your assign1 on cmslamp14.aut.ac.nz")
            print("URL list is empty?{}".format(urls))
            mark = 0
        elif missing_url:
            print("  Either the following required link(s) are missing on this page {}:".format(
                missing_url) + "OR  " + "wrong file name/extension used")
            mark = mark - (len(missing_url) * 0.5)
        print("Task (1b) mark received = {}".format(mark))
        # global variable for reuse
        missing_urls = missing_url
        page_urls = p_urls

    """TASK 2:"""


class PostForm(BasePage):
    def __init__(self, driver, name):
        super().__init__(driver)
        self.name = name
        m_url = [m_url for m_url in missing_urls if "post" in m_url]
        if m_url:
            print("missing some url")
            global post_urlg
            post_url = [purl for purl in page_urls if "post" in purl]
            post_url = (str(post_url)[1:-1])
            self.pst_url = post_url.replace("'", "")
            self.driver.get(self.pst_url)
        else:
            self.driver.get(TestData(self.name).post_url())
        print("\n" + ".....Beginning TASK 2: PostStatusForm........" + "\n")

    def check_postForm_elements(self):
        print("Task 2(a)...Summary....................:")
        # print(missing_urls)
        mark = 0
        if self.is_enabled(Locators.STATUSCODE_INPUT):
            print("status code field is visible and attribute name is ok")
            mark = mark + 1
        if not self.is_visible(Locators.STATUSCODE_INPUT):
            print("'statuscode' is not used? ")
        if self.is_enabled(Locators.STATUS_INPUT):
            print("status text field is enabled/visible and attribute name is ok")
            mark = mark + 1
        if self.click(Locators.SHARE_CHECK_PUBLIC) or self.click(Locators.SHARE_CHECK_FRIEND) or self.click(
                Locators.SHARE_CHECK_ONLY):
            print("check buttons are visible, can be clicked and correct attribute/type used")
            mark = mark + 0
        if self.click(Locators.ALLOW_LIKE) or self.click(Locators.ALLOW_SHARE) or self.click(Locators.ALLOW_COMMENT):
            print("check buttons are visible, can be clicked and correct attribute/type used")
            mark = mark + 0
        print("Task (2a) mark received = {}".format(mark))

    """ b.	Date field contained the server date (4 marks) 
        Use client date will also do 
        c.	Web page used the POST method (2 marks)
        d.  Links worked using relative addressing (2 marks)
        """

    def check_post_method(self):
        mark = 0
        self.enter_text(Locators.STATUS_INPUT, TestData.STATUS_TEXT[0])
        sample_text_code = "S" + str(TestData.VALID_STATUS_CODES[0] + 2)
        self.enter_text(Locators.STATUSCODE_INPUT, sample_text_code)
        self.click(Locators.SHARE_CHECK_PUBLIC)
        self.click(Locators.SHARE_CHECK_FRIEND)
        self.click(Locators.SHARE_CHECK_ONLY)

        # Current date time in local system
        selected_date = self.is_enabled(Locators.DATE).get_attribute('value')
        # expected_date = (datetime.date(datetime.now())).strftime("%d-%m-%Y")
        if selected_date:
            mark = mark + 4
            print("Good!, date field is populated with server date({})".format(selected_date))

        else:
            mark = 0
            print("(-4 marks): Either date did not follow format of server date is different from selected date")
            print("Either date field is empty or did not contain server date : " + selected_date)
        print("Task (2b) mark received = {}".format(mark))

        # check post method
        self.click(Locators.ALLOW_LIKE)
        self.click(Locators.ALLOW_COMMENT)
        self.click(Locators.ALLOW_SHARE)
        mark = 0
        method = self.is_enabled(Locators.POST_FORM).get_attribute("method")
        if method != "post":
            print(" You are expected to use POST method to send data to the server and not " + method)
        else:
            print("Good!, POST method was used!")
            mark = mark + 2
        print("Task (2c) mark received = {}".format(mark))
        mark = 0
        if self.driver.current_url != TestData(self.name).post_url():
            print(" This relative addressing: " + self.driver.current_url + " " +
                  "does not follow the required syntax ")
        else:
            print("Good!, Links worked using relative addressing")
            mark = mark + 2
        self.post(Locators.SUBMIT_POST)
        time.sleep(1)
        print("Task (2d) mark received = {}".format(mark))

    """TASK 3:"""


class ProcessPostStatus(BasePage):
    """ a.	(-10 marks) Check  manually Database table exist checked before storing
        must have code to check table existence (e.g., query the INFORMATION_SCHEMA.TABLES)
         and if not exist create the table """
    appro_error_message = 0

    def __init__(self, driver, name):
        super().__init__(driver)
        self.name = name
        m_url = [m_url for m_url in missing_urls if "post" in m_url]
        if m_url:
            print("missing some url")
            post_url = [purl for purl in page_urls if "post" in purl]
            post_url = (str(post_url)[1:-1])
            self.pst_url = post_url.replace("'", "")
            self.driver.get(self.pst_url)
        else:
            self.driver.get(TestData(self.name).post_url())
        # self.driver.get(TestData(self.name).post_url())
        print("\n" + ".....Beginning TASK 3: Processing PostStatusForm........" + "\n")

    def status_code_validation(self):
        global appro_error_message
        mark = 0
        pst_url = self.driver.current_url
        self.post(Locators.SUBMIT_POST)
        if pst_url == self.driver.current_url:
            print("status code validation is seems to done on the client or server side")
            mark = mark + 5
            print("Task (3b) mark received = {}".format(mark))
            self.driver.refresh()
        else:
            self.driver.back()
            self.driver.refresh()
            for sample_text_code in TestData.INVALID_STATUS_CODES:
                mark = 0
                self.enter_text(Locators.STATUS_INPUT, TestData.STATUS_TEXT[0])
                self.enter_text(Locators.STATUSCODE_INPUT, sample_text_code)
                user_code_input = self.is_enabled(Locators.STATUSCODE_INPUT).get_attribute('value')
                self.post(Locators.SUBMIT_POST)
                post_message = self.is_enabled(Locators.POST_MESSAGE).text
                html = self.driver.page_source
                if post_message in TestData.error_message:
                    _message = "Status code validation is done!"
                    mark = mark + 5
                    print("Task (3b) mark received = {}".format(mark))
                elif html:
                    c = html2text.html2text(html).lower()
                    if any(word in c for word in TestData.error_message_keywords):
                        _message = "validation is done with error message "
                        mark = mark + 5
                else:
                    print("appropriate error message not included")
                    mark = 0
                    print("Task (3b) mark received = {}".format(mark))
                if self.driver.current_url != pst_url:
                    time.sleep(1)
                    self.driver.back()
                    self.driver.refresh()
            print(_message)
            print("Task (3b) mark received = {}".format(mark))
            if mark == 5:
                appro_error_message = 2.5
            if not Locators.SUBMIT_POST:
                print("Post button is neither enabled nor visible")
                print("Either page not displaying error message or error_message not appropriate enough!")
                self.driver.refresh()

            # back to previous page with back()

    def status_validation(self):
        global appro_error_message
        n = random.randint(10, 100)
        mark = 0
        self.driver.refresh()
        pst_url = self.driver.current_url
        sample_status_code = "S" + str(TestData.VALID_STATUS_CODES[0] + n)
        self.enter_text(Locators.STATUSCODE_INPUT, sample_status_code)
        self.enter_text(Locators.STATUS_INPUT, TestData.INVALID_STATUS_TEXT[0])
        self.post(Locators.SUBMIT_POST)
        if pst_url == self.driver.current_url:
            print("status validation seems to have been done on the client side")
            mark = mark + 5
            print("Task (3b) mark received = {}".format(mark))
            self.driver.refresh()
        else:
            self.driver.back()
            self.driver.refresh()
            for sample_text in TestData.STATUS_TEXT:
                self.enter_text(Locators.STATUS_INPUT, sample_text)
                sample_status_code = "S" + str(TestData.VALID_STATUS_CODES[0] + 2)
                self.enter_text(Locators.STATUSCODE_INPUT, sample_status_code)
                self.post(Locators.SUBMIT_POST)
                post_message = self.is_enabled(Locators.POST_MESSAGE).text
                html = self.driver.page_source
                if post_message in TestData.error_message:
                    _message = "Status validation is done!"
                    mark = mark + 5
                    print("Task (3b) mark received = {}".format(mark))
                elif html:
                    c = html2text.html2text(html).lower()
                    if any(word in c for word in TestData.error_message_keywords):
                        _message = "status validation seems to have been done with error message "
                        mark = mark + 5
                else:
                    print("seems you did not include appropriate error message")
                    mark = 0
                    print("Task (3b) mark received = {}".format(mark))
                if self.driver.current_url != pst_url:
                    time.sleep(1)
                    self.driver.back()
                    self.driver.refresh()
            print(_message)
            print("Task (3b) mark received = {}".format(mark))
            if mark == 5:
                appro_error_message = 2 + appro_error_message
            if not Locators.SUBMIT_POST:
                print("Post button is neither enabled nor visible")
                print("Either page not displaying error message or error_message not appropriate enough!")
                self.driver.refresh()

    def is_address_relative(self):
        n = random.randint(1, 199)
        mark = 0
        self.driver.refresh()
        pst_url = self.driver.current_url
        sample_status_code = "S" + str(TestData.VALID_STATUS_CODES[0] + 5)
        self.enter_text(Locators.STATUSCODE_INPUT, sample_status_code)
        self.enter_text(Locators.STATUS_INPUT, TestData.STATUS_TEXT[0])
        self.post(Locators.SUBMIT_POST)
        if self.driver.current_url == TestData(self.name).post_process_url():
            print("Link follows specification and worked using relative addressing")
            mark = 5
            print("Task (3e) mark received = {}".format(mark))
        else:
            print(" Your addressing either did not follows specification or did not worked using relative addressing")
            print("Task (3e) mark received = {}".format(mark))

    def scode_uniqueness(self):
        mark = 0
        a_mark = 0
        self.driver.refresh()
        pst_url = self.driver.current_url
        SampleText = ["u test", "test u"]
        for text in SampleText:
            sample_status_code = "S" + str(TestData.VALID_STATUS_CODES[0])
            self.enter_text(Locators.STATUSCODE_INPUT, sample_status_code)
            self.enter_text(Locators.STATUS_INPUT, text)
            self.post(Locators.SUBMIT_POST)
            self.driver.back()
            self.driver.refresh()

        sample_status_code = "S" + str(TestData.VALID_STATUS_CODES[0])
        self.enter_text(Locators.STATUSCODE_INPUT, sample_status_code)
        self.enter_text(Locators.STATUS_INPUT, SampleText[1])
        self.post(Locators.SUBMIT_POST)
        html = self.driver.page_source
        if pst_url == self.driver.current_url:
            print("status code uniqueness validation appears done on the client")
            mark = mark + 10
            print("Task (3b) mark received = {}".format(mark))
            a_mark = 5
            self.driver.refresh()
        else:
            if html:
                c = html2text.html2text(html).lower()
                if any(word in c for word in TestData.error_message_keywords):
                    _message = "status code uniqueness validation is done with error message "
                    mark = mark + 10
                    a_mark = 5
                else:
                    print("appropriate error message not included")
                    mark = 0
                    print("Task (3c) mark received = {}".format(mark))
                if self.driver.current_url != pst_url:
                    time.sleep(1)
                    self.driver.back()
                    self.driver.refresh()
                print(_message)
                print("Task (3c) mark received = {}".format(mark))
                print("Task (3d) mark received = {}".format(a_mark))


class SearchStatusForm(BasePage):

    def __init__(self, driver, name):
        super().__init__(driver)
        self.name = name
        m_url = [m_url for m_url in missing_urls if "search" in m_url]
        if m_url:
            print("missing some url")
            global search_urlg
            search_url = [surl for surl in page_urls if "search" in surl]
            search_url = (str(search_url)[1:-1])
            self.s_url = search_url.replace("'", "")
            self.driver.get(self.s_url)
        else:
            self.driver.get(TestData(self.name).search_urls())
        print("\n" + ".....Beginning TASK 4: Processing SearchStatusForm........" + "\n")

    "a.	Form contained all information shown in the screen shot (2 marks)"
    "b. Web page used the GET  method (2 marks)"
    "c.	Links worked using relative addressing  (1 marks)"

    def check_searchForm(self):
        mark = 0
        if self.is_enabled(Locators.SEARCH_STATUS_INPUT) and self.is_enabled(Locators.SUBMIT_SEARCH):
            mark = mark + 2
            print("Search elements are enabled and ok ")
            print("Task (4a) mark received = {}".format(mark))
        else:
            print(" Either Search input field or button is not named as specified or not enabled")
        method = self.is_enabled(Locators.SEARCH_FORM).get_attribute("method")
        mark = 0
        if method == "get":
            mark = mark + 2
            print("Get method is used")
            print("Task (4b) mark received = {}".format(mark))
        else:
            print(" You are expected to use GET method to send data to the server and not " + method)
        mark = 0
        if self.driver.current_url in TestData(self.name).search_urls():
            mark = mark + 1
            print("gOOD!, Links worked using relative addressing")
            print("Task (4c) mark received = {}".format(mark))
        else:
            print("This relative addressing: " + self.driver.current_url + " " +
                  "does not follow the required syntax ")
        time.sleep(1)


class SearchStatusResult(BasePage):
    def __init__(self, driver, name):
        super().__init__(driver)
        self.name = name
        m_url = [m_url for m_url in missing_urls if "search" in m_url]
        if m_url:
            print("missing some url")
            global search_urlg
            search_url = [surl for surl in page_urls if "search" in surl]
            search_url = (str(search_url)[1:-1])
            self.s_url = search_url.replace("'", "")
            self.driver.get(self.s_url)
        else:
            self.driver.get(TestData(self.name).search_urls())

        print("\n" + ".....Beginning TASK 5: Processing Status Search Result........" + "\n")

    "a.	Search string, and database table existence validated (manually) (8 marks)"
    """Note that we only test if search is correct format(e.g. empty character) and multiple results of sample text 
    returned """
    "b. Search performed correctly and multiple matches displayed (8 marks)"
    "c. Appropriate error messages generated if errors occur  (8 marks)"
    """Pre-defined error statements required"""
    "d.	Links worked using relative addressing  (1 marks)"

    def check_searchResult(self):
        mark = 0
        self.driver.refresh()
        for sample_text in TestData.VALID_SEARCH_TEXT:
            self.enter_text(Locators.SEARCH_STATUS_INPUT, sample_text)
            self.click(Locators.SUBMIT_SEARCH)
            search_results = self.is_enabled(Locators.SEARCH_RESULT).text
            result_base_url = self.driver.current_url.rsplit('=', 1)[0]
            if TestData(self.name).search_result_url() in result_base_url:
                mark = mark + 1
                print("Task (5d) mark received = {}".format(mark))
            else:
                print(" This relative addressing: " + self.driver.current_url + " " +
                      "does not follow the required syntax ")
            self.driver.back()
            self.is_enabled(Locators.SEARCH_STATUS_INPUT).clear()
            self.driver.refresh()
            text_count = (self.word_count(search_results))
            mark = 0
            """ All valid test cases must include the Testing in this case
            as we are interested in related matches"""
            if text_count.get("test") is not None and (int(text_count.get("test"))) > 1:
                mark = mark + 8
                print("Task (5b) mark received = {}".format(mark))
                print("Successful multiple result!: " + (str(text_count.get("test"))) + "  results returned")

            elif text_count.get("test") is not None and (int(text_count.get("test"))) == 1:
                print("(-8 marks) The status: " + sample_text + " should return multiple results as it appears in DB "
                                                                "multiple times")
            elif text_count.get("test") is None and not search_results:
                print("(-8) Seems your search procedure is problematic")

            elif "search" not in self.driver.current_url:
                print("(-8) Seems search page not responding")
            else:
                print("check student search part manually")

    def search_string_validation(self):
        mark = 0
        a_mark = 0
        self.driver.refresh()
        s_url = self.driver.current_url
        self.enter_text(Locators.SEARCH_STATUS_INPUT, TestData.INVALID_SEARCH_STRING)
        self.post(Locators.SUBMIT_SEARCH)
        search_results = self.is_enabled(Locators.SEARCH_RESULT).text
        html = self.driver.page_source
        _message =""
        if s_url == self.driver.current_url:
            print("search string validation seems to have been done on the client side")
            mark = mark + 4
            print("Task (5a(i)) mark received = {}".format(mark))
            a_mark = 8
            print("Task (5c) mark received = {}".format(a_mark))
        else:
            if search_results in TestData.error_message:
                _message = "String validation is done!"
                mark = mark + 4
                print("Task (5a(i)) mark received = {}".format(mark))
                a_mark = 8
            elif html:
                c = html2text.html2text(html).lower()
                if any(word in c for word in TestData.error_message_keywords):
                    _message = "status validation is done with error message "
                    mark = mark + 4
                    a_mark = 8
            else:
                print ("seems you did not include appropriate error message")
                mark = 0
                a_mark = 0
                print("Task (5a(i)) mark received = {}".format(mark))
            if self.driver.current_url != s_url:
                time.sleep(2)
                self.driver.back()
                self.driver.refresh()
        print(_message)
        print("Task (5a(i)) mark received = {}".format(mark))
        print("Task (5c) mark received = {}".format(a_mark))


class AboutQuestions(BasePage):
    def __init__(self, driver, name):
        super().__init__(driver)
        self.name = name
        self.driver.get(TestData(self.name).about_urls())
        time.sleep(2)
        print("\n" + ".....Beginning TASK 6: Processing About page questions........" + "\n")

    def check_intersection(self, Que, content):
        mark = 0

        attempted_que = [que for que in Que if que in content]
        if set(Que).intersection(set(content)):
            mark = mark + 4
            print("Task (6a) mark received = {}".format(mark))
            print("Question attempted")
        elif len(attempted_que) > 2:
            mark = mark + 4
            print("Task (6a) mark received = {}".format(mark))
            print("Question attempted")
            
        elif content and self.driver.current_url == TestData(self.name).about_urls():
            mark = mark + 3
            print("Not all questions are well attempted ")
            print("Task (6a) mark received = {}".format(mark))
        else:
            print("You have not properly answered the questions")
            print("Task (6a) mark received = {}".format(mark))

    def check_about_url_and_question(self):
        mark = 0
        about_content = self.is_enabled(Locators.ABOUT_PAGE).text
        self.check_intersection(TestData.ABOUT_QUE, about_content)
        if self.driver.current_url == TestData(self.name).about_urls():
            mark = mark + 1
            print("Task (6b) mark received = {}".format(mark))
        else:
            print(" (-1 marks): This relative addressing: " + self.driver.current_url + " " +
                  "does not follow the required syntax ")
