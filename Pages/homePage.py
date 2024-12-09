from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage:
    product_label_xpath = "//div[@class='product_label'][contains(.,'Products')]"


    def __init__(self, driver):
        self.driver = driver

    def verifyThatUserIsLoggedIn(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.product_label_xpath)))
        element.is_displayed()