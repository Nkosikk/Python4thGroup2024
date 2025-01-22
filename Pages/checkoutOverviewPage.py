import decimal

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutOverviewPage:
    checkoutTitle_xpath = "//span[@class='title']"
    itemTotal_xpath = "//div[contains(@class,'summary_subtotal_label')]"
    TotalPrice_xpath = "//div[contains(@class,'summary_total_label')]"
    cartList = "cart_list"
    cartItem = "cart_item"
    finishButton_id = "finish"
    cancelButton_xpath = "//button[@id='cancel']"

    def __init__(self, driver):
        self.driver = driver

    def verifyCheckoutTitle(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.checkoutTitle_xpath)))

    def calculateCartItems(self):
        cart = WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located((By.CLASS_NAME, self.cartList)))
        items = cart.find_elements(By.CLASS_NAME, self.cartItem)
        if items.__len__() > 0:
            item_tot = float(cart.find_element(By.XPATH, self.itemTotal_xpath).text.split("$")[1])
            grand_tot = float(cart.find_element(By.XPATH, self.TotalPrice_xpath).text.split("$")[1])
            tax = 0.08
            item_tot_after_tax = item_tot * tax
            temp_total = item_tot + item_tot_after_tax

            # Set a tolerance (epsilon) for floating-point comparison
            epsilon = 0.01

            # Compare with a tolerance to avoid precision issues
            if abs(temp_total - grand_tot) <= epsilon:
                element = self.driver.find_element(By.ID, self.finishButton_id)
                element.click()
                assert True
            else:
                element = self.driver.find_element(By.XPATH, self.cancelButton_xpath)
                element.click()
                assert False
