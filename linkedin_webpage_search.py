import os
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pandas as pd

# LinkedIn credentials from environment variables
linkedin_email = os.getenv('LINKEDIN_EMAIL')
linkedin_password = os.getenv('LINKEDIN_PASSWORD')

# Setup WebDriver
driver = webdriver.Safari()

# Log in to LinkedIn
driver.get('https://www.linkedin.com/login')

email_field = driver.find_element(By.ID, 'username')
email_field.send_keys(linkedin_email)
password_field = driver.find_element(By.ID, 'password')
password_field.send_keys(linkedin_password)
password_field.send_keys(Keys.RETURN)

time.sleep(5)
print("Login Successful!")

# Navigate to the search page
driver.get("https://www.linkedin.com/search/results/people/")
time.sleep(5)

# Perform search
search_box = driver.find_element(By.XPATH, "//input[@placeholder='Search']")
search_box.send_keys("Graphic Design")
search_box.send_keys(Keys.RETURN)
time.sleep(5)

# Extract data
profiles = driver.find_elements(By.CLASS_NAME, "entity-result__title-text")
data = []

for profile in profiles:
    name = profile.text.split('\n')[0]
    data.append({"Name": name})

# Save data
df = pd.DataFrame(data)
df.to_csv('linkedin_profiles.csv', index=False)

print("Data extraction complete. Data saved to linkedin_profiles.csv")

# Keep Safari open
print("You can manually close Safari when done.")