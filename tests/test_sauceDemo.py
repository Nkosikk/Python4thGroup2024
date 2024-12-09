import time

import allure
import pytest

from Pages.loginPage import LoginPage
from Utils.ReadProperties_loginDetails import ReadLoginProperties


class Test_SauceDemo:
    sauceDemoURL = ReadLoginProperties().getSauceDemoURL()

    @pytest.mark.nkosi
    @allure.severity(allure.severity_level.CRITICAL)
    def test_loginToSauceDemo(self, setup):
        self.driver = setup
        self.driver.get(self.sauceDemoURL)
        self.driver.maximize_window()
        self.login = LoginPage(self.driver)
        self.login.enterUsername("standard_user")
        self.login.enterPassword("secret_sauce")
        self.login.clickLoginButton()

        time.sleep(3)
