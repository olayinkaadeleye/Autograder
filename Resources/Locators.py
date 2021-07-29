__author__ = 'O Adeleye'
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class Locators():
    # --- Home Page Locators ---
    POST_LINK_TEXT = (By.PARTIAL_LINK_TEXT, "Post a new status")
    SEARCH_LINK_TEXT = (By.PARTIAL_LINK_TEXT, "Search status")
    #HOMEPAGE_LINKS = (By.XPATH, "//a[@href]")driver.find_elements_by_xpath("//a[@href]")
    HOMEPAGE_LINKS = (By.XPATH, "//a[@href]")

    # ---Post Form Elements Locators----
    #STATUSCODE_INPUT = (By.XPATH,"//form//input[translate(@name, 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxy') = 'statuscode' or //label[contains(text(),'Status Code')]]")
    STATUSCODE_INPUT = (By.XPATH, "//form//input[contains(translate(@name, 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxy'),'code') or contains(translate(@name, 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxy'),'code')]")
    STATUS_INPUT = (By.XPATH,"//*[translate(@name, 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxy') = 'status']")
    SEARCH_STATUS_INPUT =(By.XPATH,"//form//input[contains(translate(@name, 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxy'), 'search') or contains(translate(@name, 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxy'),'status')]")
    SHARE_CHECK_ONLY = (By.XPATH, "//*[@type='checkbox' or @value='Only Me']")
    SHARE_CHECK_FRIEND = (By.XPATH, "//*[@type='checkbox' or @value='Friends']")
    SHARE_CHECK_PUBLIC = (By.XPATH,"//*[@type='checkbox' or @value='Public']")
    #DATE = (By.XPATH, "//form//input[translate(@type, 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxy') ='date']")
    DATE= (By.XPATH, "//form//input[contains(translate(@name, 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxy'),'date')]")
    ALLOW_LIKE = (By.XPATH, "//form//input[@value='Allow Like' or @type='checkbox']")
    ALLOW_COMMENT = (By.XPATH, "//form//input[@value='Allow Comment' or @type='checkbox']")
    ALLOW_SHARE = (By.XPATH, "//form//input[@value='Allow Share' or @type='checkbox']")
    SUBMIT_POST = (By.XPATH, "//*[translate(@type,'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxy')='submit' or contains(translate(@name, 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxy'),'post')]")
    SUBMIT_SEARCH = (By.XPATH, "//*[translate(@type, 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxy') ='submit' ]")
    POST_FORM = (By.TAG_NAME, "form")
    SEARCH_FORM = (By.TAG_NAME, "form")
    POST_MESSAGE = (By.TAG_NAME, "body")
    SEARCH_RESULT = (By.TAG_NAME, "body")
    ABOUT_PAGE = (By.TAG_NAME, "body")


