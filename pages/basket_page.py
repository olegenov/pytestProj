from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_empty_basket_message(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_MESSAGE), \
               'Empty basket message is not presented'
    
    def should_not_be_basket_items(self):
        assert not self.is_element_present(*BasketPageLocators.BASKET_ITEMS), \
                   'Basket items are presented'
