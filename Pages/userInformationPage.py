from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class UserInformationPage:
    firstName_id = "first-name"
    lastName_id = "last-name"
    zipCode_id = "postal-code"
    continueButton_id = "continue"
    

    def __init__(self, driver):
        self.driver = driver

    def enterFirstName(self, firstname):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.ID, self.firstName_id)))
        element.send_keys(firstname)

    def enterLastName(self, lastname):
        element = self.driver.find_element(By.ID, self.lastName_id)
        element.send_keys(lastname)

    def enterZipCode(self, zipcode):
        element = self.driver.find_element(By.ID, self.zipCode_id)
        element.send_keys(zipcode)

    def clickContinueButton(self):
        element = self.driver.find_element(By.ID, self.continueButton_id)
        element.click()
