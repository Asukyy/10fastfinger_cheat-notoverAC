import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


browser = webdriver.Chrome()

browser.get("https://10fastfingers.com/login")

browser.find_element(By.ID, "CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll").click()
time.sleep(2)
email_field = browser.find_element(By.ID, "UserEmail")
email_field.send_keys("tonMDP")
password_field = browser.find_element(By.ID, "UserPassword")
password_field.send_keys("tonemail")
time.sleep(2)
browser.find_element(By.ID, "login-form-submit").click()


words_list = browser.find_element(By.ID, "row1").find_elements(By.TAG_NAME, "span")

input_field = browser.find_element(By.ID, "inputfield")
for word in words_list:
    input_field.send_keys(word.text + " ")
    time.sleep(0.3)


time.sleep(20000)
