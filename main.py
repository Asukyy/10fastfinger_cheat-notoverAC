import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


browser = webdriver.Chrome()

browser.get("https://10fastfingers.com/login")
time.sleep(2)
browser.find_element(By.ID, "CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll").click()
time.sleep(2)
email_field = browser.find_element(By.ID, "UserEmail")
email_field.send_keys("YOUR_Email")
password_field = browser.find_element(By.ID, "UserPassword")
password_field.send_keys("YOUR_PassWord")
time.sleep(2)
browser.find_element(By.ID, "login-form-submit").click()
time.sleep(2)
# browser.find_element(By.ID, "typing-test").click()  #à enlever ou non celon si il se connecte directement au typing test
time.sleep(3)

words_list = browser.find_element(By.ID, "row1").find_elements(By.TAG_NAME, "span")

input_field = browser.find_element(By.ID, "inputfield")
for word in words_list:
    input_field.send_keys(word.text + " ")
    time.sleep(0.2)


time.sleep(20000)
