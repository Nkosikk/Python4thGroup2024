import time

import allure
import pytest

from Utils.ReadProperties_loginDetails import ReadLoginProperties


class Test_SauceDemo:
    sauceDemoURL = ReadLoginProperties().getSauceDemoURL()

    @pytest.mark.nkosi
    @allure.severity(allure.severity_level.CRITICAL)
    def test_loginToSauceDemo(self, setup):
        self.driver = setup
        time.sleep(3)
