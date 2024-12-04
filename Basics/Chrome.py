import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.maximize_window()
driver.get("https://www.saucedemo.com/")

driver.find_element(By.ID, "user-name").send_keys("standard_user")

driver.find_element(By.XPATH, "//input[@id='password']").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()

driver.find_element(By.XPATH, "//span[@class='title'][contains(.,'Products')]").is_displayed()
driver.save_screenshot('/Users/nkosi/PycharmProjects/Python4thGroup2024/Basics/Screenshot/nkosi.png')
# driver.get_screenshot_as_file('/Users/nkosi/PycharmProjects/Python4thGroup2024/Screenshot/home.png')

# if productText == 'Productsf':
#     print('Product is displayed')
#     assert True
# else:
#     print('Product is not displayed')
#     assert False


time.sleep(3)
