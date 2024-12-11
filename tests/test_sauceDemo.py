import time

import allure
import pytest

from Pages.loginPage import LoginPage
from Utils.ReadProperties_loginDetails import ReadLoginProperties


class Test_SauceDemo:
    sauceDemoURL = ReadLoginProperties().getSauceDemoURL()
    username = ReadLoginProperties().getUsername()
    password = ReadLoginProperties().getPassword()

    @pytest.mark.nkosi
    @allure.severity(allure.severity_level.CRITICAL)
    def test_loginToSauceDemo(self, setup):
        self.driver = setup
        self.driver.get(self.sauceDemoURL)
        self.driver.maximize_window()
        self.login = LoginPage(self.driver)
        self.login.enterUsername(self.username)
        self.login.enterPassword(self.password)
        self.login.clickLoginButton()

        time.sleep(3)
