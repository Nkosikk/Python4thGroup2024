import decimal

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutOverviewPage:
    checkoutTitle_xpath = "//span[@class='title']"
    itemTotal_xpath = "//div[contains(@class,'summary_subtotal_label')]"
    TotalPrice_xpath = "//div[contains(@class,'summary_total_label')]"
    cartList_class_name = "cart_list"
    cartItem_class_name = "cart_item"
    finishButton_id = "finish"
    cancelButton_xpath = "//button[@id='cancel']"

    def __init__(self, driver):
        self.driver = driver

    def verifyCheckoutTitle(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.checkoutTitle_xpath)))

    def calculateCartItems(self):
        cart = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, self.cartList_class_name))
        )
    def calculateCartItems(self):
        cart = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, self.cartList_class_name))
        )

        # Ensure there are cart items
        items = cart.find_elements(By.CLASS_NAME, self.cartItem_class_name)

        if len(items) > 0:
            # Assuming the total item price and grand total are shown with "$" symbol
            try:
                itemTot = float(cart.find_element(By.XPATH, self.itemTotal_xpath).text.split("$")[1])
                grandTot = float(cart.find_element(By.XPATH, self.TotalPrice_xpath).text.split("$")[1])

                # Calculate the item total after tax
                tax = 0.08
                itemTotAfterTax = itemTot * (1 + tax)  # itemTot + itemTot * tax
                tempTotal = round(itemTotAfterTax, 2)

                # Compare calculated total with the grand total
                # Allow for a small tolerance due to floating point precision
                tolerance = 0.01  # tolerance in dollars (you can adjust this)

                if abs(tempTotal + 10000) <= tolerance:
                    element = self.driver.find_element(By.ID, self.finishButton_id)
                    element.click()
                    assert True
                else:
                    element = self.driver.find_element(By.XPATH, self.cancelButton_xpath)
                    element.click()
                    assert False, f"Expected total: {grandTot}, but calculated: {tempTotal}"

            except Exception as e:
                print(f"Error calculating totals: {e}")
                element = self.driver.find_element(By.XPATH, self.cancelButton_xpath)
                element.click()
                #assert False
        else:
            print("No items in the cart.")
            assert False

