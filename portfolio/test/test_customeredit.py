import unittest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class test_customeredit(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def teardown_method(self, method):
        self.driver.quit()

    def test_customeredit(self):
        self.driver.get("http://127.0.0.1:8000/login/")
        self.driver.set_window_size(1280, 656)
        self.driver.find_element(By.ID, "id_username").send_keys("instructor")
        self.driver.find_element(By.ID, "id_password").send_keys("maverick1a")
        self.driver.find_element(By.CSS_SELECTOR, ".btn-success").click()
        time.sleep(2)
        self.driver.find_element(By.LINK_TEXT, "View Details").click()
        time.sleep(2)
        self.driver.find_element(By.LINK_TEXT, "Edit").click()
        self.driver.find_element(By.ID, "id_address").click()
        self.driver.find_element(By.ID, "id_address").send_keys("123 street1")
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, ".save").click()
        time.sleep(2)
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
