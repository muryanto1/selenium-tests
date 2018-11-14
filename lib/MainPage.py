import time

from BasePage import BasePage
from BasePage import InvalidPageException

from selenium.common.exceptions import NoSuchElementException

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MainPage(BasePage):

    def __init__(self, driver):
        super(MainPage, self).__init__(driver)
        
    def _validate_page(self):
        # validate Main page is displaying a 'Home' tab
        print("xxx in MainPage.validatePage() ...REVISIT...")

