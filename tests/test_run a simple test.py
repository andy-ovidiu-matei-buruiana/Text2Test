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

#Scenario Goal: run a simple test

class TestTest():

  def setup_method(self, method):
    self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    self.vars = {}

  def teardown_method(self, method):
    self.driver.quit()

  def test_test(self):


    #### Scenario steps ####

    # Precondition Steps
    self.driver.get('https://www.amazon.com/')

    # Scenario Steps
    self.driver.find_element(By.ID, 'twotabsearchtextbox').click()
    self.driver.find_element(By.ID, 'twotabsearchtextbox').send_keys('J.K. Rowling')
    self.driver.find_element(By.ID, 'nav-search-submit-button').click()

    self.driver.close()