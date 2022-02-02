#!usr/bin/env python3
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import exceptions

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)
wait = WebDriverWait(driver, 10)

def login(username, password):

    driver.get('https://queue.tudelft.nl/login')
    
    us = wait.until(EC.presence_of_element_located((By.NAME, 'username')))
    ps = wait.until(EC.presence_of_element_located((By.NAME, 'password')))
    us.send_keys(username)
    ps.send_keys(password + '\n')
    
    return True

def enroll(course):
    
    driver.get('https://queue.tudelft.nl/editions')
    
    search_field = wait.until(EC.presence_of_element_located((By.NAME, 'nameSearch')))
    search_field.send_keys(course.name + '\n')

    wait.until(EC.presence_of_element_located((By.LINK_TEXT, 'enrol'))).click()

def register(courses):
    
    driver.get('https://queue.tudelft.nl/...')
    
    for course in courses:
        
        try:
            wait.until(EC.presence_of_element_located(()) # Course appeaers (by name)
        except BaseException as err:
            enroll(course)
