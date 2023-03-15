from selenium.webdriver.common.by import By


from Utilities.Baseclass import Baseclass
from pageObject.CheckoutPage import CheckoutPage
from pageObject.ConfirmPage import Confirmpage
from pageObject.HomePage import HomePage


class Testone(Baseclass):

    def test_e2e(self):
        log = self.getLogger()
        homePage = HomePage(self.driver)
        checkoutPage = homePage.shopItems()
        products = checkoutPage.getProductItems()
        log.info("Getting all the card titles")

        for product in products:
            productname = checkoutPage.getProductName(product).text
            log.info(productname)
            if productname == "Nokia Edge":
                checkoutPage.addItemIntoCart(product).click()

        checkoutPage.checkoutButton().click()
        confirmPage = checkoutPage.checkoutItems()
        log.info("Entering country name Ind")
        confirmPage.Search().send_keys("Ind")
        self.VerifyLinkPresence("India")
        confirmPage.Select().click()
        confirmPage.GetCheckbox().click()
        confirmPage.GetPurchase().click()
        finalMsg = confirmPage.GetSuccessMsg().text
        log.info("Alert message received is"+finalMsg)
        assert "Success!" in finalMsg
        print("Order successful!!!")
