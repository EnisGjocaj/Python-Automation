from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time


path = r"C:\Users\Admin\Downloads\chromedriver-win64\chromedriver-win64/chromedriver.exe"
website = "https://www.google.com/"

service = Service(executable_path=path)
driver = webdriver.Chrome(service=service)


driver.get(website)


WebDriverWait(driver, 5).until(
	EC.presence_of_element_located((By.CLASS_NAME, "gLFyf"))
)


input_element = driver.find_element(By.CLASS_NAME, "gLFyf")
input_element.clear()
input_element.send_keys("Github" + Keys.ENTER)

WebDriverWait(driver, 5).until(
	EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "GitHub"))
)


link = driver.find_element(By.PARTIAL_LINK_TEXT, "GitHub")
link.click()

time.sleep(10)

driver.quit()