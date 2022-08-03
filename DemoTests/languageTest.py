# pip install webdriver-manager

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
languageLT = driver.find_element(By.XPATH, "//*[contains(text(), 'Lithuanian')]")
languageLT.click()
contactUsField = driver.find_element(By.ID, "contact")
assert contactUsField.text == 'SUSISIEKITE SU MUMIS'
languageButton = driver.find_element(By.ID, "language")
assert languageButton.text == "LITHUANIAN"
navBarRight = driver.find_element(By.CLASS_NAME, "navbar-right")
elementList = navBarRight.find_elements(By.TAG_NAME, "li")
assert elementList[0].text == "DARBALAUKIS"
assert elementList[1].text == "PLANŠETĖ"
assert elementList[2].text == "MOBILUS"
assert elementList[3].text == "REAGUOJANTIS"
assert elementList[4].text == "MINI ŽAIDIMAS"
driver.close()
