import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

#Scenario Goal: login

class TestTest():

  def setup_method(self, method):
    self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    self.vars = {}

  def teardown_method(self, method):
    self.driver.quit()

  def test_test(self):
    #### Background steps ####

    # Precondition Steps
    self.driver.get('https://www.amazon.com/')

    #### Scenario steps ####

    # Precondition Steps
    self.driver.get('https://www.clientam.com/sso/Login')

    # Scenario Steps
    self.driver.find_element(By.ID, 'user_name').click()
    self.driver.find_element(By.ID, 'user_name').send_keys('uname')
    self.driver.find_element(By.ID, 'password').click()
    self.driver.find_element(By.ID, 'password').send_keys('pass')
    self.driver.find_element(By.ID, 'submitForm').click()

    # Scenario Step / Result
    assert WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.ID, 'ERRORMSG'))).get_attribute("innerHTML") == 'Invalid username password combination'

    self.driver.close()