__author__ = 'O Adeleye'
import os
import pandas as pd

class TestData(object):
    CHROME_EXECUTABLE_PATH = "C:/Users/HP 1040 G2/PycharmProjects/WebDevTest/Drivers/chromedriver.exe";
    base_url = ".cmslamp14.aut.ac.nz/assign1/"
    VALID_STATUS_CODES = [9200]
    INVALID_STATUS_CODES = ["A8213", "S)2", "S001"]
    STATUS_TEXT = ["testing"]
    VALID_SEARCH_TEXT = ["test"]
    INVALID_SEARCH_STRING =["%%*@"]
    INVALID_STATUS_TEXT = ["", "%%@"]
    HOME_PAGE_TITLE = "Amazon.in"
    NO_RESULTS_TEXT = "No results found."
    INDEX_INFO = ["I declare that this assignment is my individual work", "Name", "ID", "Email"]
    POST_LINK = "Post a new status"
    SEARCH_LINK = "Search Status"
    FILE_NAMES = ["poststatusform.html", "about.html", "poststatusform.php", "poststatusprocess.php",
                  "searchstatus.html", "searchstatusprocess.php"]
    error_message = ["Please enter a different Status Code as it must be unique.",
                     "Sorry, your Status Code must start with the letter 'S' and be followed by exactly 4 numbers.",
                     "Post unsuccessful, status code field is empty!", "Post unsuccessful, status field is empty!",
                     "Sorry, your Status can only contain alphanumeric characters including spaces, commas, periods (full stop), exclamation points and question marks.",
                     "Post unsuccessful, Status can only contain alphanumeric characters.",
                     "Search Unsuccessful!, status does not exit in DB.",
                     "Search Unsuccessful!, search field is empty!",
                     "Not Found", "No status found", "already exist", "not exist"
                     "Sorry, it looks like something went wrong with your search query."]
    error_message_keywords = ["unsuccessful","used","duplicate","already exist", "duplication", "not valid", "not correct", "error", "invalid","something wrong", "empty", "incorrect", "failed",
                              "Not Found", "No found", "no exit", "No status found", "already exist", "not exist"]

    ABOUT_QUE = ["What special features have you done"
        , "Which parts did you have trouble with", "What would you like to do better next time", "What you have learnt along the way"]

    def __init__(self, username):
        self.username = username
        # print(self.username)

    def base_urls(self):
        return "http://" + "".join((self.username, TestData.base_url))

    def home_urls(self):
        return self.base_urls()

    def search_urls_php(self):
        return self.base_urls() + "searchstatusform.php"

    def search_urls(self):
        return self.base_urls() + "searchstatusform.html"

    def about_urls(self):
        return self.base_urls() + "about.html"

    def index_urls(self):
        return self.base_urls() + "index.html"

    def search_result_url(self):
        return self.base_urls() + "searchstatusprocess.php"

    def post_url(self):
        return self.base_urls() + "poststatusform.php"

    def post_process_url(self):
        return self.base_urls() + "poststatusprocess.php"

    def URLS(self):
        URL = []
        srl = self.search_urls()
        URL.append(srl)
        URL.extend((str(self.base_urls()).strip(''), self.index_urls(), self.about_urls(), self.post_url(),
                    self.post_process_url(), self.home_urls()))
        return URL

    def HOMEPAGE_URLS(self):
        URL = []
        srl = self.search_urls()
        URL.append(srl)
        URL.extend((self.about_urls(), self.post_url()))
        return URL

    @staticmethod

    def read_username():
        translation ={39: None}
        current_dir = os.path.dirname(__file__)
        _names = os.path.join(current_dir, "std.csv")
        df = pd.read_csv(_names)
       # try:
         #   with open(_names, "+a") as f:
          #      Lines = f.readlines()
           #     usernames = ["("+line.strip()+","+")" for line in Lines]
      #  except IOError:
        #    print("File not accessible")
      #  return str(usernames).translate(translation)
