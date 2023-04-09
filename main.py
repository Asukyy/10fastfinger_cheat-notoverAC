import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


# Créer un lien vers mon navigateur
browser = webdriver.Chrome()

# Charger le site web
browser.get("https://10fastfingers.com/login")

# Cliquer sur le bouton "Accepter tous les cookies"
browser.find_element(By.ID, "CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll").click()
time.sleep(2)
email_field = browser.find_element(By.ID, "UserEmail")
email_field.send_keys("tonMDP")
password_field = browser.find_element(By.ID, "UserPassword")
password_field.send_keys("tonemail")
time.sleep(2)
browser.find_element(By.ID, "login-form-submit").click()


# Trouver la liste de mots et les stocker dans une variable
words_list = browser.find_element(By.ID, "row1").find_elements(By.TAG_NAME, "span")

# Écrire chaque mot dans le champ de saisie
input_field = browser.find_element(By.ID, "inputfield")
for word in words_list:
    input_field.send_keys(word.text + " ")
    time.sleep(0.3)


time.sleep(20000)
