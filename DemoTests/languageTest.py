# pip install webdriver-manager
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

s = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)
driver.maximize_window()
driver.get("https://demo.betgames.tv/")
languageButton = driver.find_element(By.ID, "language")
languageButton.click()
driver.implicitly_wait(100)
languageLT = driver.find_element(By.XPATH, "//*[contains(text(), 'Lithuanian')]")
languageLT.click()
driver.implicitly_wait(10)
contactUsField = driver.find_element(By.ID, "contact")
assert contactUsField.text == 'SUSISIEKITE SU MUMIS'
languageButton = driver.find_element(By.ID, "language")
assert languageButton.text == "LITHUANIAN"
driver.close()
