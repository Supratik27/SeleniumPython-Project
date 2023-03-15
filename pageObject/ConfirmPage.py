from selenium.webdriver.common.by import By


class Confirmpage:
    CountrySearch = (By.ID, "country")
    CountrySelect = (By.LINK_TEXT, "India")
    Checkbox = (By.CSS_SELECTOR, "div[class*=checkbox]")
    Purchase = (By.CSS_SELECTOR, "input[class*=btn]")
    SuccessMsg = (By.CSS_SELECTOR, "div[class*=alert]")

    def __init__(self, driver):
        self.driver = driver

    def Search(self):
        return self.driver.find_element(*Confirmpage.CountrySearch)

    def Select(self):
        return self.driver.find_element(*Confirmpage.CountrySelect)

    def GetCheckbox(self):
        return self.driver.find_element(*Confirmpage.Checkbox)

    def GetPurchase(self):
        return self.driver.find_element(*Confirmpage.Purchase)

    def GetSuccessMsg(self):
        return self.driver.find_element(*Confirmpage.SuccessMsg)
