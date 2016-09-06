# -*- coding: utf-8 -*-
import sys
import time
#import requests
#import lxml
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
#from element import BasePageElement
import re
from locators import MainPageLocators, \
    SignInPageLocators, ShoppingCartLocators, \
    PDPLocators, PLPLocators, CheckoutLocators, \
    OrderConfPageLocators, OrderHistoryLocators, \
    PersonalDetailsLocators
from utils import TestTools

class BasePage(object):
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 30)
        self.tt = TestTools()

class MainPage(BasePage):

    def is_title_match(self):
        return u"Benevita Site|ホームページ" in self.driver.title

    def go_to_benevita_home_dropdown(self):
        try:
            self.driver.find_element(*MainPageLocators.HEADER_PRODSERVICES).click()
            self.driver.find_element(*MainPageLocators.BENEVITA_DROPDOWN_LINK).click()
        except:
            print sys._getframe().f_code.co_name + ": Failed to click Benevita Logo in home page.", sys.exc_info()[0]
            raise

        return True

    def go_to_benevita_home_logo(self):
        try:
            self.driver.find_element(*MainPageLocators.BENEVITA_LOGO).click()
        except:
            print sys._getframe().f_code.co_name + ": Failed to click Benevita Logo in home page.", sys.exc_info()[0]
            raise

        return True
    def click_signin_link(self):
        find_signInLink = lambda: self.driver.find_element(*MainPageLocators.SIGNIN_LINK)
        verify_signInLink = self.tt.wait_for(find_signInLink, 20)
        visible_signInLink = self.tt.is_showing(verify_signInLink, 3)
        try:
            verify_signInLink.click()
        except:
            return False
        return True

    def click_my_account(self):
        find_myAccount = lambda: self.driver.find_element(*MainPageLocators.MY_ACCOUNT)
        verify_myAccount = self.tt.wait_for(find_myAccount, 10)
        visible_myAccount = self.tt.is_showing(verify_myAccount, 1)
        try:
            verify_myAccount.click()
        except:
            return False

        return True

    def click_order_history(self, time_out):
        find_orderHistory = lambda: self.driver.find_element(*MainPageLocators.MY_ACCOUNT_ORDER_HISTORY)
        verify_orderHistory = self.tt.wait_for(find_orderHistory, time_out)
        visible_orderHistory = self.tt.is_showing(verify_orderHistory, 1)
        try:
            verify_orderHistory.click()
        except:
            return False

        return True

    def click_update_personal_details(self, time_out):
        find_personalDetails = lambda: self.driver.find_element(*MainPageLocators.MY_ACCOUNT_PERSONAL_DETAILS)
        verify_personalDetails = self.tt.wait_for(find_personalDetails, time_out)
        visible_personalDetails = self.tt.is_showing(verify_personalDetails, 1)
        try:
            verify_personalDetails.click()
        except:
            return False

        return True

    def click_log_out(self):
        find_logOutLink = lambda: self.driver.find_element(*MainPageLocators.MY_ACCOUNT_LOGOUT)
        verify_logOutLink = self.tt.wait_for(find_logOutLink, 15)
        visible_logOutLink = self.tt.is_showing(verify_logOutLink, 1)
        try:
            verify_logOutLink.click()
        except:
            return False

        return True


    def get_num_cart_items(self):
        return self.driver.find_element(*MainPageLocators.MINI_CART_COUNT).get_attribute('innerHTML')

    def open_mini_cart(self):
        try:
            time.sleep(10)
            self.driver.find_element(*MainPageLocators.MINI_CART).click()
        except:
            raise Exception ("Mini cart didn't get clicked.")
        return True

    def click_checkout_on_mini_cart(self):
        try:
            time.sleep(3)
            self.driver.find_element(*MainPageLocators.MINI_CART_CHECKOUT_BUTTON).click()
        except:
            raise Exception ("Checkout button on mini cart didn't get clicked.")
        return True


    def click_continue_shopping_from_mini_cart(self):
        try:
            time.sleep(5)
            self.driver.find_element(*MainPageLocators.MINI_CART_CONTSHOP_BUTTON).click()
        except:
            raise Exception (sys._getframe().f_code.co_name + ": Checkout button on mini cart didn't get clicked.", sys.exc_info()[0])
        return True

    def click_category_link(self, category, isIBO, time_out):
        find_category_dropdown = lambda: self.driver.find_element(*MainPageLocators.CATEGORY_DROPDOWN)
        verify_category_dropdown = self.tt.wait_for(find_category_dropdown, time_out)
        visible_category_dropdown = self.tt.is_showing(verify_category_dropdown, 1)
        try:
            verify_category_dropdown.click()
        except:
            raise Exception (sys._getframe().f_code.co_name + ": Failed to click category dropdown.", sys.exc_info()[0])

        categories = \
        {'ENROLLMENT': self.driver.find_element(*MainPageLocators.ENROLLMENT),
         'NUTRITION': self.driver.find_element(*MainPageLocators.NUTRITION)}

        if isIBO:
            categories['SALES_TOOLS'] = self.driver.find_element(*MainPageLocators.SALES_TOOLS)
        try:
            categories.get(category).click()
        except:
            raise Exception (sys._getframe().f_code.co_name + ": Failed to select category.", sys.exc_info()[0])
        return True

    def verify_header_msg(self, msg_type):
        """
        msg_type takes the following:
        NEWUSER - for new enrollment message.
        """
        new_enrollment_msg = u'ご登録ありがとうございます.'
        msg = ''

        if msg_type == "NEWUSER":
            msg = new_enrollment_msg

        return re.search(msg, self.driver.find_element(*MainPageLocators.ALERT).text)

    def click_product_in_home(self, prd_name, time_out):
        """
        :param prd_name:
        '211-JP' etc.  See the dictionary below.
        :param time_out:
        seconds

        :return: bool
        """
        #locators = MainPageLocators()
        products = \
            {'211-JP': self.driver.find_element(*MainPageLocators.PRODUCT_GO),
             '212-JP':self.driver.find_element(*MainPageLocators.PRODUCT_REST),
             '201-JP':self.driver.find_element(*MainPageLocators.PRODUCT_SHAKEIT),
             '701-JP':self.driver.find_element(*MainPageLocators.PRODUCT_BALANCE_KIT),
             '610-JP':self.driver.find_element(*MainPageLocators.PRODUCT_ACN_STICKER),
             '401-JP':self.driver.find_element(*MainPageLocators.PRODUCT_ENROLLMENT_KIT),
             '501-JP':self.driver.find_element(*MainPageLocators.PRODUCT_SHAKER_BOTTLE1),
             '502-JP':self.driver.find_element(*MainPageLocators.PRODUCT_SHAKER_BOTTLE2)}
        try:
            find_product = lambda: products.get(prd_name)
            verify_product = self.tt.wait_for(find_product, time_out)
            visible_product = self.tt.is_showing(verify_product, 1)
            verify_product.click()
            return True
        except:
            print sys._getframe().f_code.co_name + ": Failed to click product in home page.", sys.exc_info()[0]
            raise

class OrderHistory(BasePage):

    def __init__(self, driver, order_number, grand_total, shipping_fee):
        self.driver = driver
        self.order_number = order_number
        self.grand_total = grand_total
        self.shipping_fee = shipping_fee
        self.tt = TestTools()

    def click_order_number(self):
        try:
            self.driver.find_element_by_link_text(self.order_number).click()
        except:
            raise

        return True

    def check_order(self, num_items, items):
        """
        :param num_items: number of items purchased.  integer.
        items: an array of item skus
        :return:
        """

        assert self.driver.find_element(*OrderHistoryLocators.BC_ORDER_NO).get_attribute('innerHTML') == u"注文 " + self.order_number, "Order Number in Breadcrumb is incorrect."
        assert self.driver.find_element(*OrderHistoryLocators.ORDER_NO).get_attribute('innerHTML') == self.order_number, "Order Number is incorrect."
        grand_total = self.driver.find_element(*OrderHistoryLocators.GRAND_TOTAL_LINE).text
        assert re.search(self.grand_total, grand_total), "Grand Total is incorrect."
        shipping = self.driver.find_element(*OrderHistoryLocators.SHIP_CHARGE).get_attribute('innerHTML')
        assert re.search(self.shipping_fee, shipping), "Shipping is incorrect."
        displayed_items = self.driver.find_elements(*OrderHistoryLocators.ORDER_ITEMS)
        num_item_displayed = len(displayed_items)
        assert num_item_displayed == num_items, "Number of item is wrong. It is " + str(num_item_displayed)
        assert self.tt.check_ordered_items(displayed_items, items), "Ordered items are not in order history."

        return True

class PersonalDetailsPage(BasePage):
    """
    change_last_names requires last_names to be an array:
    last_name[0] = furigana last name
    last_name[1] = Japanese last name
    last_name[2] = English last name
    """
    def change_last_names(self, last_names):
        if len(last_names) == 3:
            try:
                self.driver.find_element(*PersonalDetailsLocators.LAST_NAME_FURIGANA).clear()
                self.driver.find_element(*PersonalDetailsLocators.LAST_NAME_FURIGANA).send_keys(last_name[0])
                self.driver.find_element(*PersonalDetailsLocators.LAST_NAME_JAPANESE).clear()
                self.driver.find_element(*PersonalDetailsLocators.LAST_NAME_JAPANESE).send_keys(last_name[1])
                self.driver.find_element(*PersonalDetailsLocators.LAST_NAME_ENGLISH).clear()
                self.driver.find_element(*PersonalDetailsLocators.LAST_NAME_ENGLISH).send_keys(last_name[2])
                self.driver.find_element(*PersonalDetailsLocators.UPDATE_BUTTON).click()
            except:
                raise Exception (sys._getframe().f_code.co_name + ": The last names couldn't be changed.")
        else:
            print ("last_name has to be an array of 3 elements, furigana, Japanese, English names")
            return False

        return True

    def validate_all_names(self, first_names, last_names):
        if len(last_names) == 3 and len(first_names) == 3:
            assert self.driver.find_element(*PersonalDetailsLocators.LAST_NAME_FURIGANA).get_attribute('value') == (last_name[0]), "Furigana last name is not matched"
            assert self.driver.find_element(*PersonalDetailsLocators.LAST_NAME_JAPANESE).get_attribute('value') == (last_name[1]), "Japanese last name is not matched"
            assert self.driver.find_element(*PersonalDetailsLocators.LAST_NAME_ENGLISH).get_attribute('value') == (last_name[2]), "English last name is not matched"
            assert self.driver.find_element(*PersonalDetailsLocators.FIRST_NAME_FURIGANA).get_attribute('value') == (first_name[0]), "Furigana first name is not matched"
            assert self.driver.find_element(*PersonalDetailsLocators.FIRST_NAME_JAPANESE).get_attribute('value') == (first_name[1]), "Japanese first name is not matched"
            assert self.driver.find_element(*PersonalDetailsLocators.FIRST_NAME_ENGLISH).get_attribute('value') == (first_name[2]), "English first name is not matched"

        else:
            print ("last_names and first_names have to be an array of 3 elements, furigana, Japanese, English names")
            return False

        return True


class SignInPage(BasePage):

    email = ''
    password = ''

    new_user_last_name = u"英士"
    new_user_first_name = u"得尾"
    new_user_email = "akikom.10000+"+time.strftime("%d%m%Y%I%M%S")+"@gmail.com"
    new_user_password = "Site1234@1"

    def get_new_user_email(self):
        return self.new_user_email

    def get_new_user_password(self):
        return self.new_user_password


    #def is_title_matched(self):
    #    return u"ログイン|Benevita Site" in self.driver.title

    def create_new_user(self):
        ending_page_url = "https://acn-hq-aws01.siteworx.com:9102/acngoodsstorefront/benevita/ja/"
        func_name = sys._getframe().f_code.co_name

        find_lastNameField = lambda: self.driver.find_element(*SignInPageLocators.LAST_NAME_FIELD)
        verify_lastNameField = self.tt.wait_for(find_lastNameField, 10)
        visible_lastNameField = self.tt.is_showing(verify_lastNameField, 3)

        verify_lastNameField.send_keys(self.new_user_last_name)
        assert self.driver.find_element(*SignInPageLocators.FIRST_NAME_FIELD).is_displayed(), func_name + ": first name field is missing."
        assert self.driver.find_element(*SignInPageLocators.ENROLLMENT_EMAIL_FIELD).is_displayed(), func_name + ": email field is missing."
        assert self.driver.find_element(*SignInPageLocators.ENROLLMENT_PASSWORD1_FIELD).is_displayed(), func_name + ": password1 field is missing."
        assert self.driver.find_element(*SignInPageLocators.ENROLLMENT_PASSWORD2_FIELD).is_displayed(), func_name + ": password2 field is missing."
        assert self.driver.find_element(*SignInPageLocators.REGISTER_BUTTON).is_displayed(), func_name + ": register button is missing."

        try:
            self.driver.find_element(*SignInPageLocators.FIRST_NAME_FIELD).send_keys(self.new_user_first_name)
            self.driver.find_element(*SignInPageLocators.ENROLLMENT_EMAIL_FIELD).send_keys(self.new_user_email)
            self.driver.find_element(*SignInPageLocators.ENROLLMENT_PASSWORD1_FIELD).send_keys(self.new_user_password)
            self.driver.find_element(*SignInPageLocators.ENROLLMENT_PASSWORD2_FIELD).send_keys(self.new_user_password)
            self.driver.find_element(*SignInPageLocators.REGISTER_BUTTON).click()
        except:
            raise Exception(func_name + ": form entry failed.")

        return  bool(self.driver.current_url == ending_page_url)

    """
        TBD: user_type takes "REGISTERED" or "IBO"
    """
    #def user_sign_in(self, user_type, email, password):
    def user_sign_in(self, email, password):

        try:
            self.driver.find_element(*SignInPageLocators.USER_EMAIL_FIELD).send_keys(email)
            self.driver.find_element(*SignInPageLocators.USER_PASSWORD_FIELD).send_keys(password)
            self.driver.find_element(*SignInPageLocators.SIGNIN_BUTTON).click()
        except:
            raise Exception ("Sign in failed")

        return True

    def guest_user_sign_in(self, email):
        try:
            self.driver.find_element(*SignInPageLocators.GUEST_EMAIL_FIELD).send_keys(email)
            self.driver.find_element(*SignInPageLocators.GUEST_CONRIRM_EMAIL_FIELD).send_keys(email + '\n')
        except:
            raise Exception ("Sign in failed")

        return True

class ShoppingCart(BasePage):

    def click_checkout_buttn(self, time_out):
        find_CheckoutButton = lambda: self.driver.find_element(*ShoppingCartLocators.CHECKOUT_BUTTON)
        verify_CheckoutButton = self.tt.wait_for(find_CheckoutButton, time_out)
        visible_Checkout_CheckoutButton = self.tt.is_showing(verify_CheckoutButton, 1)
        try:
            verify_CheckoutButton.click()
        except:
            raise
        return True

    def clear_cart(self):
        mp = MainPage(self.driver)
        numItems = int(mp.get_num_cart_items())
        if numItems > 0:
            try:
                assert mp.open_mini_cart(), "mini cart didn't open."
                assert mp.click_checkout_on_mini_cart(), "couldn't go to the shopping cart."
                for x in xrange(0, numItems):
                    self.driver.implicitly_wait(5)
                    self.driver.find_element(*ShoppingCartLocators.REMOVE_BUTTON_0).click()
                    self.driver.implicitly_wait(5)
                self.driver.implicitly_wait(5)
            except:
                raise
        return bool(int(mp.get_num_cart_items()) == 0)

class Checkout(BasePage):

    def manage_teamID(self, isURLOn, team_id, time_out):
        find_TeamIDField = lambda: self.driver.find_element(*CheckoutLocators.TEAM_ID_FIELD)
        verify_TeamIDField = self.tt.wait_for(find_TeamIDField, time_out)
        visible_TeamIDField = self.tt.is_showing(verify_TeamIDField, 1)

        try:
            if not isURLOn:
                verify_TeamIDField.clear()
                verify_TeamIDField.send_keys(team_id)
            else:
                assert verify_TeamIDField.get_attribute('value') == team_id, "the team id is not present."
                assert verify_TeamIDField.get_attribute('readOnly'), "the team id field is not readonly."

            self.driver.find_element(*CheckoutLocators.TEAM_ID_NEXT_BUTTON).click()
        except:
            raise

        return True

    def manual_fill_delivery_info(self, deliv_info,time_out):
        """
        :param deliv_info: takes dictionary consists of surename, firstname, postalcode, address1, address2, townCity, prefecture, phone
        :param time_out: seconds for finding the first item.
        :return:
        """
        try:
            find_AddressSurname = lambda: self.driver.find_element(*CheckoutLocators.SHIP_SURENAME)
            verify_AddressSurname = self.tt.wait_for(find_AddressSurname, time_out)
            visible_AddressSurname = self.tt.is_showing(verify_AddressSurname, 1)
            verify_AddressSurname.send_keys(deliv_info.get('surename'))

            self.driver.find_element(*CheckoutLocators.SHIP_FIRSTNAME).send_keys(deliv_info.get('firstname'))
            self.driver.find_element(*CheckoutLocators.SHIP_POSTALCODE).send_keys(deliv_info.get('postalcode') + '\n')
            self.driver.find_element(*CheckoutLocators.SHIP_ADDRESS1).send_keys(deliv_info.get('address1'))
            self.driver.find_element(*CheckoutLocators.SHIP_ADDRESS2).send_keys(deliv_info.get('address2'))
            time.sleep(5)
            assert self.driver.find_element(*CheckoutLocators.SHIP_TOWNCITY).get_attribute('value') == deliv_info.get('townCity'), "The city field has wrong data."
            assert Select(self.driver.find_element(*CheckoutLocators.SHIP_PREFECTURE)).first_selected_option.text == deliv_info.get('prefecture'), "The prefecture field has wrong data."

            self.driver.find_element(*CheckoutLocators.SHIP_PHONE).send_keys(deliv_info.get('phone'))

            self.driver.find_element(*CheckoutLocators.SHIP_SUBMIT_BUTTON).click()
        except:
            raise

        return True

    def set_delivery_options(self, type, time,time_out):

        find_DeliveryMethod = lambda: self.driver.find_element(*CheckoutLocators.DELV_METHOD)
        verify_DeliveryMethod = self.tt.wait_for(find_DeliveryMethod, time_out)
        visible_DeliveryMethod = self.tt.is_showing(verify_DeliveryMethod, 1)

        try:
            Select(verify_DeliveryMethod).select_by_index(type)
            if type != 0:
                Select(self.driver.find_element(*CheckoutLocators.DELV_TIME)).select_by_index(time)
            self.driver.find_element(*CheckoutLocators.DELV_SUBMIT_BUTTON).click()
        except:
            raise

        return True

    def auto_fill_billing_info(self, deliv_info,time_out):

        find_wpUseDeliveryAddressCheckBox = lambda: self.driver.find_element_by_id("wpUseDeliveryAddress")
        verify_wpUseDeliveryAddressCheckBox = self.tt.wait_for(find_wpUseDeliveryAddressCheckBox, time_out)
        visible_wpUseDeliveryAddressCheckBox = self.tt.is_showing(verify_wpUseDeliveryAddressCheckBox, 1)
        verify_wpUseDeliveryAddressCheckBox.click()
        time.sleep(5)
        assert self.driver.find_element(*CheckoutLocators.BILLING_SURENAME).get_attribute("value") == deliv_info.get("surename"), "The billing surname field is blank."
        assert self.driver.find_element(*CheckoutLocators.BILLING_FIRSTNAME).get_attribute("value") == deliv_info.get("firstname"), "The billing first name field is blank."
        time.sleep(5)
        assert self.driver.find_element(*CheckoutLocators.BILLING_POSTALCODE).get_attribute("value") == deliv_info.get("postalcode"), "The billing postal code field is blank."
        assert Select(self.driver.find_element(*CheckoutLocators.BILLING_PREFECTURE)).first_selected_option.text == deliv_info.get('prefecture'), "The prefecture field has wrong data."
        assert self.driver.find_element(*CheckoutLocators.BILLING_TOWNCITY).get_attribute("value") == deliv_info.get("townCity"), "The billing townCity code field is blank."
        assert self.driver.find_element(*CheckoutLocators.BILLING_ADDRESS2).get_attribute("value") == deliv_info.get("address1"), "The billing address2 code field is blank."
        assert self.driver.find_element(*CheckoutLocators.BILLING_ADDRESS1).get_attribute("value") == deliv_info.get("address2"), "The billing address1 code field is blank."
        assert self.driver.find_element(*CheckoutLocators.BILLING_TERMS_CHKBX).get_attribute("value") == 'true', "The terms checkbox is already checked."

        try:
            self.driver.find_element(*CheckoutLocators.BILLING_TERMS_CHKBX).click()
            self.driver.find_element(*CheckoutLocators.BILLING_SUBMIT_BUTTON).click()
        except:
            raise

        return True


    def check_order_summary(self, subtotal, shipping_charge, grand_total):
        find_subTotal = lambda: self.driver.find_element(*CheckoutLocators.SUMMARY_SUBTOTAL)
        verify_subTotal = self.tt.wait_for(find_subTotal, 5)
        visible_subTotal = self.tt.is_showing(verify_subTotal, 5)
        time.sleep(10)
        assert verify_subTotal.text != subtotal, "Content Type text didn't match: |%s| returned" % verify_subTotal.text
        assert self.driver.find_element(*CheckoutLocators.SUMMARY_SHIPPING).text != shipping_charge, "Content Type text didn't match: |%s| returned" % self.driver.find_element(*CheckoutLocators.SUMMARY_SHIPPING).text
        assert self.driver.find_element(*CheckoutLocators.SUMMARY_GRANDTOTAL).text != grand_total, "Content Type text didn't match: |%s| returned" % self.driver.find_element(*CheckoutLocators.SUMMARY_GRANDTOTAL).text
        return True

    def assign_cc_number_by_type (self, cc_type):
        cc_numbers = \
            {'visa': (4917610000000000, 123),
             'master': (5454545454545454, 1234),
             'jcb': (3528000700000000, 123),
             'amex': (34343434343434, 123)
            }
        return cc_numbers.get(cc_type)

    def fill_cc_form(self, card_type, surename, firstname, month, year, time_out):

        cc_numbers = self.assign_cc_number_by_type(card_type)
        cc_number = cc_numbers[0]
        sec_code = cc_numbers[1]

        find_frame = lambda: self.driver.find_element(*CheckoutLocators.IFRAME)
        verify_frame = self.tt.wait_for(find_frame, time_out)
        self.driver.switch_to_frame(verify_frame)

        try:
            self.driver.find_element(*CheckoutLocators.CC_NUMBER).send_keys(cc_number)
            if surename != 'NONE' and firstname != 'NONE':
                name_element = self.driver.find_element(*CheckoutLocators.CC_NAME)
                name_element.clear()
                name_element.send_keys(surename+firstname)
            Select(self.driver.find_element(*CheckoutLocators.CC_EXP_MONTH)).select_by_visible_text(month)
            Select(self.driver.find_element(*CheckoutLocators.CC_EXP_YEAR)).select_by_visible_text(year)
            self.driver.find_element(*CheckoutLocators.CC_SEC_CODE).send_keys(sec_code)
            self.driver.find_element(*CheckoutLocators.CC_SUBMIT_BUTTON).click()
        except:
            raise

        return True

    def check_order_conf_page(self, email, team_id, grand_total, time_out):

        conf_header = u"ご注文が完了しました"
        time.sleep(time_out)
        assert re.search('orderConfirmation',self.driver.current_url), "Order Confirmation page is not found."
        #print self.driver.find_element(*OrderConfPageLocators.HEADER).get_attribute('innerHTML')
        assert self.driver.find_element(*OrderConfPageLocators.HEADER).get_attribute('innerHTML') == conf_header, "Conf header text is missing."
        assert self.driver.find_element(*OrderConfPageLocators.EMAIL).get_attribute('innerHTML')== email, "Email shown is wrong."
        assert self.driver.find_element(*OrderConfPageLocators.TEAMID).get_attribute('innerHTML') == team_id, "Team ID is wrong."
        assert len(self.driver.find_element(*OrderConfPageLocators.ORDER_DATETIME).get_attribute('innerHTML')) > 12, "Order Date and Time seem not right."
        assert self.driver.find_element(*OrderConfPageLocators.GRAND_TOTAL).get_attribute('innerHTML')== grand_total, "Grand total is wrong"

        return True

    def get_order_number(self):
        return self.driver.find_element(*OrderConfPageLocators.ORDER_NUMBER).get_attribute('innerHTML')


class PDP(BasePage):

    def click_add_to_cart(self, time_out):
        find_addToCartBtn = lambda: self.driver.find_element(*PDPLocators.ADD_TO_CART_BUTTON)
        verify_addToCartBtn = self.tt.wait_for(find_addToCartBtn, time_out)
        visible_addToCartBtn = self.tt.is_showing(verify_addToCartBtn, 5)
        try:
            verify_addToCartBtn.click()
        except:
            print sys._getframe().f_code.co_name + ":  Add To Cart button couldn't be clicked.", sys.exc_info()[0]
            raise

        return True

    def click_add_to_autoship(self, time_out):
        find_addToAutoShipBtn = lambda: self.driver.find_element(*PDPLocators.ADD_TO_AUTOSHIP_BUTTON)
        verify_addToAutoShipBtn = self.tt.wait_for(find_addToAutoShipBtn, time_out)
        visible_addToAutoShipBtn = self.tt.is_showing(verify_addToAutoShipBtn, 1)
        try:
            verify_addToAutoShipBtn.click()
        except:
            raise Exception (sys._getframe().f_code.co_name + ": Add To Autoship button couldn't be clicked.")

        return True

class PLP(BasePage):

    def __init__(self, driver):
        self.driver = driver
        self.buttons = self.driver.find_elements(*PLPLocators.ADD_TO_BUTTONS)
        #print self.buttons
        self.add_to_cart_btns = {}
        self.add_to_autoship_btns = {}

    def init_buttons(self, user_type, category):
        if user_type == 'GUEST':
            self.init_buttons_for_guest(category)
        else:
            self.init_buttons_for_reg_user(category)

    def init_buttons_for_guest(self, category):
        if category == "NUTRITION":
            self.add_to_cart_btns = \
                {'502-JP':self.buttons[10],
                 '212-JP':self.buttons[11],
                 '601-JP':self.buttons[12],
                 '211-JP':self.buttons[13],
                 '701-JP':self.buttons[14],
                 '201-JP':self.buttons[15],
                 '501-JP':self.buttons[16]}

        elif category == "ENROLLMENT":
            self.add_to_cart_btns = {'401-JP': self.buttons[11]}

    def init_buttons_for_reg_user(self, category):
        if category == "NUTRITION":
            self.add_to_cart_btns = \
                {'502-JP':self.buttons[10],
                 '212-JP':self.buttons[12],
                 '501-JP':self.buttons[14],
                 '601-JP':self.buttons[15],
                 '211-JP':self.buttons[18],
                 '701-JP':self.buttons[20],
                 '201-JP':self.buttons[22]}

            self.add_to_autoship_btns = \
                {'502-JP':self.buttons[11],
                 '212-JP':self.buttons[13],
                 '601-JP':self.buttons[16],
                 #'701-JP':self.buttons[13],
                 '211-JP':self.buttons[19],
                 '701-JP':self.buttons[21],
                 '201-JP':self.buttons[23]}

        elif category == "ENROLLMENT":
            self.add_to_cart_btns = {'401-JP': self.buttons[6]}
            self.add_to_autoship_btns = {'401-JP': self.buttons[7]}

        elif category == "SALES_TOOLS":
            self.add_to_cart_btns = \
                {'602-JP': self.buttons[10],
                 '608-JP': self.buttons[12],
                 '610-JP': self.buttons[14],
                 '699-JP': self.buttons[16]}

            self.add_to_autoship_btns = \
                {'602-JP': self.buttons[11],
                 '608-JP': self.buttons[13],
                 '610-JP': self.buttons[15],
                 '699-JP': self.buttons[17]}

        else:
            raise Exception(sys._getframe().f_code.co_name + ":  Buttons couldn't be initialized.", sys.exc_info()[0])



    def click_add_to_cart(self, user_type, category, product):
        try:
            self.init_buttons(user_type, category)
            self.add_to_cart_btns.get(product).click()
        except:
            raise Exception(sys._getframe().f_code.co_name + ": Add To Cart button couldn't be clicked.", sys.exc_info()[0])

        return True

    def click_add_to_autoship(self, product):
        try:
            self.add_to_autoship_btns.get(product).click()
        except:
            raise Exception(sys._getframe().f_code.co_name + ": Add To Cart button couldn't be clicked.", sys.exc_info()[0])

        return True





