import unittest
from selenium import webdriver
from time import sleep
from Search import SearchPage


class CaseRun(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        sleep(3)
        self.driver.implicitly_wait(30)
        self.url = "http://www.baidu.com"
        sleep(3)
        self.content = "CMBC"

    def test_search(self):
        baidu_page = SearchPage(self.driver, self.url)
        baidu_page.open()
        baidu_page.search_content(self.content)
        baidu_page.btn_click()

    def tearDown(self):
        pass
        #self.driver.quit()


if __name__ == "__main__":
    unittest.main()
