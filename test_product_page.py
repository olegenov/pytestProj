import pytest

from .pages.basket_page import BasketPage
from .pages.main_page import MainPage
from .pages.product_page import ProductPage
from .pages.login_page import LoginPage

from .utils import generate_email, generate_password


@pytest.fixture
def link():
    return 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/'


def test_guest_should_see_login_link_on_product_page(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()

    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser, link): 
    page = ProductPage(browser, link)
    page.open()
    page.add_to_purchase()
    page.should_be_right_success_alert()
    page.should_be_right_basket_price()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_basket_page(browser, link):
    page = MainPage(browser, link)
    page.open()
    page.go_to_basket_page()

    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_not_be_basket_items()
    basket_page.should_be_empty_basket_message()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.add_to_purchase()
    page.should_disappear_success_alert()


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.add_to_purchase()
    page.should_not_be_success_alert()


class TestUserAddToBasketFromProductPage():
    def setup(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/'

        page = MainPage(browser, link)
        page.open()
        page.go_to_login_page()

        page = LoginPage(browser, browser.current_url)
        page.register_new_user(generate_email(), generate_password())
        page.should_be_authorized_user()

        yield

    def test_user_cant_see_success_message(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/'

        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_alert()
    
    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser): 
        link = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/'

        page = ProductPage(browser, link)
        page.open()
        page.add_to_purchase()
        page.should_be_right_success_alert()
        page.should_be_right_basket_price()
