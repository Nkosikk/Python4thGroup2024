from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    textbox_username_xpath = "//input[contains(@id,'user-name')]"
    textbox_password_xpath = "//input[contains(@id,'password')]"
    button_login_xpath = "//input[contains(@id,'login-button')]"

    def __init__(self, driver):
        self.driver = driver

    def enterUsername(self, username):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.textbox_username_xpath)))
        element.send_keys(username)

    def enterPassword(self, password):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.textbox_password_xpath)))
        element.send_keys(password)


    # Please delete the comment applicableto u when done writing your code
    #ToDo Sandile to do the method to enter password

    def clickLoginButton(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.button_login_xpath)))
        element.click()

    # Please delete the comment applicableto u when done writing your code

    #ToDo Tman to do the method to enter clicklogin button
    #ToDo Tlhogi to do the method to dothe code to verity that we are logged in
    #ToDo Simo to do the method to select any item
    #ToDo Ezekiel to do the method to verify that item is selected
    #ToDo Diphofa to do the method to click the cart

