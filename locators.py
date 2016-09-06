# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By

class MainPageLocators(object):
    #HEADER
    BENEVITA_LOGO = (By.CSS_SELECTOR, '.sub-site-logo > a:nth-child(1) > img:nth-child(1)')
    HEADER_PRODSERVICES = (By.CSS_SELECTOR, '.clearfix.auto.has-sub.js-enquire-has-sub > a')
    BENEVITA_DROPDOWN_LINK = (By.LINK_TEXT, 'Benevita')
    SIGNIN_LINK = (By.LINK_TEXT, u"ログイン／ユーザ登録")
    WELCOME_MSG = (By.CLASS_NAME, 'logged_in')
    MY_ACCOUNT = (By.LINK_TEXT, 'My Account')
    MY_ACCOUNT_PERSONAL_DETAILS = (By.CSS_SELECTOR,'.open > div:nth-child(2) > ul:nth-child(1) > li:nth-child(3) > div:nth-child(1) > a:nth-child(1)')

    MY_ACCOUNT_ORDER_HISTORY = (By.CSS_SELECTOR, '.open > div:nth-child(2) > ul:nth-child(1) > li:nth-child(6) > div:nth-child(1) > a:nth-child(1)')
    MY_ACCOUNT_LOGOUT = (By.CSS_SELECTOR, '.liOffcanvas.logout-link>a')
    MINI_CART = (By.CSS_SELECTOR, '.glyphicon-shopping-cart')
    MINI_CART_COUNT = (By.CSS_SELECTOR, '.mini-cart-count > span:nth-child(1)')
    MINI_CART_CHECKOUT_BUTTON = (By.LINK_TEXT, u"確認してチェックアウト")
    MINI_CART_CONTSHOP_BUTTON =  (By.LINK_TEXT, u"ショッピングを続ける")
    ALERT = (By.CSS_SELECTOR, '.alert')
    CATEGORY_DROPDOWN = (By.CSS_SELECTOR, 'ul.visible-md > li:nth-child(1) > div:nth-child(1) > button:nth-child(1) > span:nth-child(1) > a:nth-child(1)')
    ENROLLMENT = (By.LINK_TEXT, 'Enrollment')
    NUTRITION = (By.LINK_TEXT, 'Nutrition')
    SALES_TOOLS = (By.LINK_TEXT, 'Sales Tools')

    PRODUCT_GO = (By.CSS_SELECTOR,'div.owl-item:nth-child(2) > div:nth-child(1) > a:nth-child(1)')
    PRODUCT_SHAKEIT = (By.CSS_SELECTOR,'div.owl-item:nth-child(1) > div:nth-child(1) > a:nth-child(1)')
    PRODUCT_REST = (By.CSS_SELECTOR,'div.owl-item:nth-child(3) > div:nth-child(1) > a:nth-child(1)')
    PRODUCT_SHAKER_BOTTLE1 = (By.CSS_SELECTOR,'div.owl-item:nth-child(4) > div:nth-child(1) > a:nth-child(1)')
    PRODUCT_SHAKER_BOTTLE2 = (By.CSS_SELECTOR,'div.owl-item:nth-child(5) > div:nth-child(1) > a:nth-child(1)')
    PRODUCT_BALANCE_KIT = (By.CSS_SELECTOR,'div.owl-item:nth-child(6) > div:nth-child(1) > a:nth-child(1)')
    PRODUCT_ENROLLMENT_KIT = (By.CSS_SELECTOR,'div.owl-item:nth-child(7) > div:nth-child(1) > a:nth-child(1)')
    PRODUCT_ACN_STICKER = (By.CSS_SELECTOR,'div.owl-item:nth-child(8) > div:nth-child(1) > a:nth-child(1)')

class PersonalDetailsLocators(object):
    LAST_NAME_FURIGANA = (By.ID, 'profile.furiganaLastName')
    FIRST_NAME_FURIGANA = (By.ID, 'profile.furiganaFirstName')
    LAST_NAME_JAPANESE = (By.ID, 'profile.japaneseLastName')
    FIRST_NAME_JAPANESE = (By.ID, 'profile.japaneseFirstName')
    LAST_NAME_ENGLISH = (By.ID, 'profile.lastName')
    FIRST_NAME_ENGLISH = (By.ID, 'profile.firstName')
    UPDATE_BUTTON = (By.CSS_SELECTOR,'.btn-primary')


class SignInPageLocators(object):

    #FOR REGISTERED/IBO USERS
    USER_EMAIL_FIELD = (By.ID, 'j_username')
    USER_PASSWORD_FIELD = (By.ID, 'j_password')
    SIGNIN_BUTTON = (By.XPATH, ".//*[@id='loginForm']/button")

    #FOR GUEST USER CHECKOUT
    GUEST_EMAIL_FIELD = (By.ID, 'guest.email')
    GUEST_CONRIRM_EMAIL_FIELD = (By.ID, 'guest.confirm.email')

    # FOR NEW ENROLLMENT
    LAST_NAME_FIELD = (By.ID, 'register.lastName')
    FIRST_NAME_FIELD = (By.ID, 'register.firstName')
    ENROLLMENT_EMAIL_FIELD = (By.ID, 'register.email')
    ENROLLMENT_PASSWORD1_FIELD = (By.ID, 'password')
    ENROLLMENT_PASSWORD2_FIELD = (By.ID, 'register.checkPwd')
    REGISTER_BUTTON = (By.XPATH, ".//*[@id='registerForm']/div[6]/button")

class ShoppingCartLocators(object):
    CHECKOUT_BUTTON = (By.CSS_SELECTOR, 'div.container:nth-child(6) > div:nth-child(3) > div:nth-child(2) > div:nth-child(1) > button:nth-child(1)')
    REMOVE_BUTTON_0 = (By.CSS_SELECTOR, '#removeEntry_0 > span:nth-child(1)')

class CheckoutLocators(object):
    TEAM_ID_FIELD = (By.ID, 'teamID')
    TEAM_ID_NEXT_BUTTON = (By.CSS_SELECTOR, '.checkout-next')
    SHIP_SURENAME = (By.ID, 'address.surname')
    SHIP_FIRSTNAME = (By.ID, 'address.firstName')
    SHIP_POSTALCODE = (By.ID, 'address.postalcode')
    SHIP_ADDRESS1 = (By.ID, 'address.line1')
    SHIP_ADDRESS2 = (By.ID, 'address.line2')
    SHIP_TOWNCITY = (By.ID, 'address.townCity')
    SHIP_PREFECTURE = (By.ID, 'address.region')
    SHIP_PHONE = (By.ID, 'address.phone')
    SHIP_SUBMIT_BUTTON = (By.ID, 'addressSubmit')
    DELV_METHOD = (By.ID, 'delivery_method')
    DELV_TIME = (By.ID, 'delivery_time')
    DELV_SUBMIT_BUTTON  = (By.ID, 'deliveryMethodSubmit')
    USE_SHIP_ADDRESS_CHKBX = (By.ID, 'deliveryMethodSubmit')
    BILLING_SURENAME = (By.ID, 'billingAddress.lastName')
    BILLING_FIRSTNAME = (By.ID, 'billingAddress.firstName')
    BILLING_POSTALCODE = (By.ID, 'billingAddress.postcode')
    BILLING_PREFECTURE = (By.ID, 'billingAddress.region')
    BILLING_TOWNCITY = (By.ID, 'billingAddress.townCity')
    BILLING_ADDRESS2 = (By.ID, 'billingAddress.line2')
    BILLING_ADDRESS1 = (By.ID, 'billingAddress.line1')
    BILLING_TERMS_CHKBX = (By.ID, 'Terms1')
    BILLING_SUBMIT_BUTTON = (By.CSS_SELECTOR, 'button.btn.btn-primary.btn-block.submit_worldpayHopForm.checkout-next')
    SUMMARY_SUBTOTAL = (By.CSS_SELECTOR, '.subtotal>span')
    SUMMARY_SHIPPING = (By.CSS_SELECTOR, '.shipping>span')
    SUMMARY_GRANDTOTAL = (By.CSS_SELECTOR, '.totals>span')
    IFRAME = (By.TAG_NAME, 'iframe')
    CC_NUMBER = (By.CSS_SELECTOR, '#cardNumber')
    CC_NAME = (By.CSS_SELECTOR, '#cardholderName')
    CC_EXP_MONTH = (By.CSS_SELECTOR, '#expiryMonth')
    CC_EXP_YEAR = (By.CSS_SELECTOR, '#expiryYear')
    CC_SEC_CODE = (By.CSS_SELECTOR, '#securityCode')
    CC_SUBMIT_BUTTON = (By.CSS_SELECTOR, '#submitButton')

class OrderConfPageLocators(object):
    HEADER = (By.CSS_SELECTOR, '.confirmation-header>h2')
    EMAIL = (By.CSS_SELECTOR, 'div.confirmation-header > p:nth-of-type(1) > strong')
    TEAMID = (By.CSS_SELECTOR, '.confirmation-header > strong:nth-child(4)')
    ORDER_DATETIME = (By.CSS_SELECTOR, '.confirmation-header > p:nth-child(5) > strong:nth-child(1)')
    GRAND_TOTAL = (By.CSS_SELECTOR, '.confirmation-header > p:nth-child(8) > strong:nth-child(1)')
    ORDER_NUMBER = (By.CSS_SELECTOR, '.confirmation-header > p:nth-child(3) > strong:nth-child(1)')
    ORDER_ITEMS = (By.CSS_SELECTOR, '.item-details')

class OrderHistoryLocators(object):
    BC_ORDER_NO = (By.CSS_SELECTOR, '.active')
    ORDER_NO = (By.CSS_SELECTOR, '.account-order-header_data > div:nth-child(1) > strong:nth-child(1)')
    GRAND_TOTAL_LINE = (By.CSS_SELECTOR, '.col-md-7.text-right-md')
    SHIP_CHARGE = (By.CSS_SELECTOR, '#orderTotals > tbody:nth-child(3) > tr:nth-child(2) > td:nth-child(2)')
    ORDER_ITEMS = (By.CSS_SELECTOR, '.account-orderdetail-item-section-body > ul')

class PDPLocators(object):
    ADD_TO_CART_BUTTON = (By.ID, 'addToCartButton')
    ADD_TO_AUTOSHIP_BUTTON = (By.CSS_SELECTOR, 'button.btn:nth-child(5)')

class PLPLocators(object):
    LIST_SECTION = (By.CSS_SELECTOR, 'div.container:nth-child(7)')
    ADD_TO_BUTTONS = (By.TAG_NAME, 'button')