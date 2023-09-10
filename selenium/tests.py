import os
import pathlib
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By

def file_uri(filename):
    return pathlib.Path(os.path.abspath(filename)).as_uri()

#  Trocar os chamados, update do selenium 
#  https://stackoverflow.com/questions/72773206/selenium-python-attributeerror-webdriver-object-has-no-attribute-find-el
#  https://bobbyhadz.com/blog/python-attributeerror-webdriver-object-has-no-attribute-find-element-by-id

driver = webdriver.Chrome()

class WebPageTests(unittest.TestCase):
    
    def test_title(self):
        driver.get(file_uri("counter.html"))
        self.assertEqual(driver.title, 'Counter')

    def test_increase(self):
        driver.get(file_uri("counter.html"))
        increase = driver.find_element("id", "increase")
        increase.click()
        self.assertEqual(driver.find_element(By.TAG_NAME, "h1").text, '1')
    def test_decrease(self):
        driver.get(file_uri("counter.html"))
        decrease = driver.find_element("id","decrease")
        decrease.click()
        self.assertEqual(driver.find_element(By.TAG_NAME, "h1").text, "-1")

    def test_multiple_increase(self):
        driver.get(file_uri("counter.html"))
        increase = driver.find_element("id","increase")
        for i in range(3):
            increase.click()
        self.assertEqual(driver.find_element(By.TAG_NAME, "h1").text, "3")

if __name__ == "__main__":
    unittest.main()        
