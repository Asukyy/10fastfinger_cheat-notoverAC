import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

# Créer un lien vers mon navigateur
browser = webdriver.Chrome()

# Charger le site web
browser.get("https://www.mcrpg.com/kohi-click-test/")

# Cliquer sur le bouton "Accepter tous les cookies
time.sleep(2)

# Trouver le bouton et le stocker dans une variable
button = browser.find_element(By.CLASS_NAME, "btn-default")

# Créer une action de clic sur le bouton et la répéter plusieurs fois
action = ActionChains(browser)
# appuie le plus vite possible sur le bouton
action.click(button)
action.perform()
# appuie 100 fois sur le bouton
for i in range(100):
    action.click(button)
    action.perform()
    time.sleep(0.1)

time.sleep(20000)
