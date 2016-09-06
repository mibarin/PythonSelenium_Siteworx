# -*- coding: utf-8 -*-
import unittest
import time
from selenium import webdriver
import page
from utils import Timeout
from utils import log_errors
from utils import TestTools

class GuestUserCheckout(unittest.TestCase):

    def setUp(self):
        #self.driver = webdriver.Firefox()
        #self.driver.delete_all_cookies()
        service_args=['--ignore-ssl-errors=true']
        self.driver = webdriver.PhantomJS("C:/phantomjs/bin/phantomjs.exe", service_args=service_args)
        self.teamID = '1234567890'
        self.driver.get("https://acn-hq-aws01.siteworx.com:9102/acngoodsstorefront/benevita/ja/")
        self.driver.set_window_size(1580,1050)

    @log_errors
    def testGuestUserCheckout(self):
        with Timeout(360, "Akiko Michibayashi - QA"):
            email = 'akiko.guest@gmail.com'
            password = 'Site1234@'
            is_ibo = False
            user_type = 'GUEST'
            category = 'NUTRITION'
            items_to_order = ['211-JP', '502-JP']
            num_items = 2
            deliv_info = \
                {'surename': u"山田",
                 'firstname': u"花子",
                 'postalcode': '0611124',
                 'address1': u"稲穂町西",
                 'address2': u"1-1-1",
                 'townCity': u"北広島市",
                 'prefecture': u"北海道",
                 'phone': '0113733828'}
            deliv_type = 0  #pick up
            deliv_time = 'NONE' #deliv option shouldn't be available for pick up
            subtotal = u"¥3,900"
            shipping_charge = 0
            card_type = 'visa'
            exp_month = '01'
            exp_year = '2020'
            oh_shipping_charge = u"無料"


            home_page = page.MainPage(self.driver)
            time.sleep(5)
            assert home_page.click_signin_link(), "couldn't click the sign in link."

            assert home_page.go_to_benevita_home_dropdown(), "Failed to go to Benevita Home."
            assert home_page.click_product_in_home(items_to_order[0], 15)
            pdp = page.PDP(self.driver)
            assert pdp.click_add_to_cart(5), "Failed to add to cart from PDP."
            assert home_page.click_continue_shopping_from_mini_cart(), "Failed to click Continue Shopping button from PDP."

            assert home_page.click_category_link(category, is_ibo, 5)
            time.sleep(5)
            plp = page.PLP(self.driver)
            assert plp.click_add_to_cart(user_type, category, items_to_order[1]), "Failed to click PLP Add to Cart."
            assert home_page.click_checkout_on_mini_cart(), "Failed to open Mini Cart."
            shopping_cart = page.ShoppingCart(self.driver)
            assert shopping_cart.click_checkout_buttn(5), "Failed to click checkout button."

            sign_in_page = page.SignInPage(self.driver)
            time.sleep(5)
            assert sign_in_page.guest_user_sign_in(email), "The sign in form couldn't be submitted."

            checkout = page.Checkout(self.driver)
            assert checkout.manage_teamID(False, self.teamID, 5), "TeamID case failed."
            assert checkout.set_delivery_options(deliv_type, deliv_time,5), "Delivery options couldn't be selected."
            assert checkout.manual_fill_delivery_info(deliv_info, 10), "Delivery info couldn't be filled."
            assert checkout.auto_fill_billing_info(deliv_info, 5), "Billing info couldn't be filled."
            assert checkout.check_order_summary(subtotal, shipping_charge, subtotal), "Order summary seems incorrect."
            assert checkout.fill_cc_form(card_type, deliv_info.get('surename'), deliv_info.get('firstname'), exp_month, exp_year, 10), "CC form couldn't be filled."
            assert checkout.check_order_conf_page(email, self.teamID, subtotal, 10), "Order confirmation page seems incorrect."

    def tearDown(self):
        #print ("done")
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()