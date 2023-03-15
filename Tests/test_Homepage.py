import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium import webdriver
from selenium.webdriver.support.select import Select

from TestData.HomePageData import HomePageData
from Utilities.Baseclass import Baseclass
from pageObject.HomePage import HomePage


class TestHomePage(Baseclass):

    def test_formSubmission(self, GetData):
        log = self.getLogger()
        homepage = HomePage(self.driver)
        log.info("First name is"+GetData["FirstName"])
        homepage.GetName().send_keys(GetData["FirstName"])
        homepage.GetEmail().send_keys(GetData["LastName"])
        homepage.GetCheckbox().click()
        self.selectOptionByText(homepage.GetDropdown(), GetData["Gender"])
        homepage.GetSubmitBtn().click()
        Msg = homepage.GetAlertText().text
        assert "Success!" in Msg
        print(Msg)
        self.driver.refresh()

    @pytest.fixture(params=HomePageData.test_Homepage_Data)
    def GetData(self, request):
        return request.param
