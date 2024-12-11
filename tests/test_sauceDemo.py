import time

import allure
import pytest
from allure_commons.types import AttachmentType

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
        allure.attach(self.driver.get_screenshot_as_png(),name="login page",attachment_type=AttachmentType.PNG)
        self.login.clickLoginButton()
        allure.attach(self.driver.get_screenshot_as_png(), name="Inventory page", attachment_type=AttachmentType.PNG)


        time.sleep(3)