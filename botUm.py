import pyautogui
from selenium import webdriver
from selenium import By

# pyautogui.PAUSE = 0.5

# pyautogui.press("win")
# pyautogui.write("Chrome")
# pyautogui.press("backspace")
# pyautogui.press("Enter")
navegador = webdriver.Chrome()
navegador.get("https://www.youtube.com/")
navegador.driver.find_element(By.XPATH, "/html/body/ytd-app/div[1]/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div[1]/div[1]/div/div[2]/input").send_keys("Veja Baby - Lagum")

# navegador.get("https://www.youtube.com/")
# navegador.find_element_by_xpath('/html/body/ytd-app/div[1]/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div[1]/div[1]/div/div[2]/input').click()
# navegador.find_element_by_xpath('/html/body/ytd-app/div[1]/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div[1]/div[1]/div/div[2]/input').send_keys("Veja Baby - Lagum")
# navegador.send_element_by_xpath("/html/body/ytd-app/div[1]/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/button").click()

# chrome -> chromedriver