from selenium.webdriver.common.by import By

from pageObject.CheckoutPage import CheckoutPage


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    shop = (By.CSS_SELECTOR, "a[href*=shop]")  # in a tuple
    name = (By.NAME, "name")
    email = (By.NAME, "email")
    checkbox = (By.ID, "exampleCheck1")
    Dropdown = (By.ID, "exampleFormControlSelect1")
    SubmitBtn = (By.CSS_SELECTOR, "input[class*='btn']")
    AlertText = (By.CSS_SELECTOR, "div[class*='alert-success']")

    def shopItems(self):
        self.driver.find_element(*HomePage.shop).click()
        checkoutPage = CheckoutPage(self.driver)
        return checkoutPage

    def GetName(self):
        return self.driver.find_element(*HomePage.name)

    def GetEmail(self):
        return self.driver.find_element(*HomePage.email)

    def GetCheckbox(self):
        return self.driver.find_element(*HomePage.checkbox)

    def GetDropdown(self):
        return self.driver.find_element(*HomePage.Dropdown)

    def GetSubmitBtn(self):
        return self.driver.find_element(*HomePage.SubmitBtn)

    def GetAlertText(self):
        return self.driver.find_element(*HomePage.AlertText)

