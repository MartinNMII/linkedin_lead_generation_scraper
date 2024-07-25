import os
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

linkedin_email = os.getenv('LINKEDIN_EMAIL')
linkedin_password = os.getenv('LINKEDIN_PASSWORD')

driver = webdriver.Safari()

driver.get('https://www.linkedin.com/login')

email_field = driver.find_element(By.ID, 'username')
email_field.send_keys(linkedin_email)
password_field = driver.find_element(By.ID, 'password')
password_field.send_keys(linkedin_password)

password_field.send_keys(Keys.RETURN)

time.sleep(5)

print("Login Successful!")



