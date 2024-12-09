from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    textbox_username_xpath = "//input[contains(@id,'user-name')]"
    textbox_password_xpath = "//input[contains(@id,'password')]"

    addBackPack_id = "add-to-cart-sauce-labs-backpack"

    def __init__(self, driver):
        self.driver = driver

    def enterUsername(self, username):
        wait = WebDriverWait(self.driver, 15)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.textbox_username_xpath)))
        element.send_keys(username)

        def enterPassword(self, password):
            wait = WebDriverWait(self.driver, 10)
            element = wait.until(EC.visibility_of_element_located((By.XPATH, self.textbox_password_xpath)))
            element.send_keys(password)

    def selectBackPack(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.ID, self.addBackPack_id)))
        element.click()

    # Please delete the comment applicableto u when done writing your code

    #ToDo Tman to do the method to enter clicklogin button
    #ToDo Tlhogi to do the method to dothe code to verity that we are logged in
    #ToDo Ezekiel to do the method to verify that item is selected
    #ToDo Diphofa to do the method to click the cart

