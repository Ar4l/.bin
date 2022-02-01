#!usr/bin/env python3
import time

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

    driver.get('https://my.tudelft.nl')
    
    us = wait.until(EC.presence_of_element_located((By.NAME, 'username')))
    ps = wait.until(EC.presence_of_element_located((By.NAME, 'password')))
    us.send_keys(username)
    ps.send_keys(password + '\n')
    
    # driver.find_element(By.ID, 'submit_button').click()
    # TODO: Return confirmation/error
    return True
   
def register_for_course(course):
    
    # TODO: Attempt to enroll again if fails
    driver.refresh()
    driver.get('https://my.tudelft.nl/#/inschrijven/cursus/')

    search_bar = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'searchbar-input')))
    search_bar.send_keys(course + '\n')
    time.sleep(1.5) # TODO: Poll for course ID instead

    wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'osi-ion-item'))).click()
        
    try: # Confirm Enrollment

        fixed = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'fixed-content')))
        fixed.find_element(By.TAG_NAME, 'button').click()
    
    except exceptions.NoSuchElementException: # Enrollment Failed

        warning_message = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'warning-text-container')))
        time.sleep(1) # TODO: Remove
        print(f'{course} enrolment failed: {warning_message.text}.')


def register_for_test(course):

    driver.get('https://my.tudelft.nl/#/inschrijven/toets/:id')
    # wait.until(document_initialised)
    driver.find_element(By.CLASS_NAME, 'searchbar-input').send_keys(course)


