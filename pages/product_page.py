from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_purchase(self):
        self.should_be_basket_button()

        basket_button = self.browser.find_element(
            *ProductPageLocators.ADD_TO_BASKET_BUTTON
        )
        basket_button.click()

    def should_be_right_success_alert(self):
        self.should_be_success_alert()

        alert = self.browser.find_element(
            *ProductPageLocators.SUCCESS_ALERT
        )
        product_name = self.browser.find_element(
            *ProductPageLocators.PRODUCT_NAME
        )

        assert product_name.text in alert.text, \
               'There is no product name in success alert'
    
    def should_be_right_basket_price(self):
        self.should_be_info_alert()

        alert = self.browser.find_element(
            *ProductPageLocators.INFO_ALERT
        )
        product_price = self.browser.find_element(
            *ProductPageLocators.PRODUCT_PRICE
        )

        assert product_price.text in alert.text, \
               'There is invalid price in info alert'

    def should_be_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BUTTON), \
               'Basket button is not presented'

    def should_be_success_alert(self):
        assert self.is_element_present(*ProductPageLocators.SUCCESS_ALERT), \
               'Success Alert is not presented'

    def should_be_info_alert(self):
        assert self.is_element_present(*ProductPageLocators.INFO_ALERT), \
               'Info Alert is not presented'

    def should_not_be_success_alert(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_ALERT), \
               'Info Alert is presented'
    
    def should_disappear_success_alert(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_ALERT), \
               'Info Alert hasnt disappeared'
