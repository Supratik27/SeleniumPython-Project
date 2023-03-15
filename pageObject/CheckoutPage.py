from selenium.webdriver.common.by import By

from pageObject.ConfirmPage import Confirmpage


class CheckoutPage:
    products = (By.CSS_SELECTOR, "div[class='card h-100']")
    productName = (By.CSS_SELECTOR, "div h4 a")
    addProduct = (By.CSS_SELECTOR, "div button")
    checkout1 = (By.CSS_SELECTOR, "a[class*=btn-primary]")
    checkout2 = (By.CSS_SELECTOR, ".btn.btn-success")

    def __init__(self, driver):
        self.driver = driver

    def getProductItems(self):
        return self.driver.find_elements(*CheckoutPage.products)
        # driver.find_elements(By.CSS_SELECTOR, "div[class='card h-100']")

    def getProductName(self, product):
        return product.find_element(*CheckoutPage.productName)
        # product.find_element(By.CSS_SELECTOR, "div h4 a")

    def addItemIntoCart(self, product):
        return product.find_element(*CheckoutPage.addProduct)
        # product.find_element(By.CSS_SELECTOR, "div button")

    def checkoutButton(self):
        return self.driver.find_element(*CheckoutPage.checkout1)

    def checkoutItems(self):
        self.driver.find_element(*CheckoutPage.checkout2).click()
        confirmPage = Confirmpage(self.driver)
        return confirmPage
