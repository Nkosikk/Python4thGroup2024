from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class YourCartPage:
    viewToCart_xpath = "//span[contains(@class,'shopping_cart_badge')]"
    checkoutButton_id = 'checkout'

    def __init__(self, driver):
        self.driver = driver


    def viewToCart(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, self.viewToCart_xpath)))
        element.click()

    def clickCheckoutButton(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.ID, self.checkoutButton_id)))
        element.click()
