from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage:
    product_label_xpath = "//span[@class='title'][contains(.,'Products')]"
    addBackPack_id = "add-to-cart-sauce-labs-backpack"
    viewToCart_xpath = "//span[contains(@class,'shopping_cart_badge')]"
    checkoutButton_id = 'checkout'

    def __init__(self, driver):
        self.driver = driver

    def verifyThatUserIsLoggedIn(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.product_label_xpath)))
        element.is_displayed()

    def selectBackPack(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.ID, self.addBackPack_id)))
        element.click()

