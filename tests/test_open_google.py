import unittest
import os 
import sys
import time

this_dir = os.path.abspath(os.path.dirname(__file__))
lib_dir = os.path.join(this_dir, '..', 'lib')
sys.path.append(lib_dir)

#print("xxx xxx lib_dir: {d}".format(d=lib_dir))

# from BaseTestCase import BaseTestCase
from BaseTestCase import BaseTestCase
from BasePage import InvalidPageException
from MainPage import MainPage

class BrowserTest(BaseTestCase):
    def test_open_google(self):
        print("xxx test_open_google xxx")
        main_page = MainPage(self.driver)
        main_page.load_page("www.google.com")
        # main_page.load_page("locahost:8888")
        print("xxx after loading page xxx")

if __name__ == '__main__':
    unittest.main(verbosity=2)

