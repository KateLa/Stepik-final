from selenium.webdriver.common.by import By


class MainPageLocators(object):
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators(object):
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "register_form")
    
class ProductPageLocators(object):
    ADD_BUTTON = (By.CLASS_NAME, 'btn-add-to-basket')
    LANG_EN_GB = (By.XPATH, '//html')
    SUCCESS_ADDITION_ALERT = (By.CSS_SELECTOR, '.alert-success')
    ALERT_PRICE = (By.CSS_SELECTOR, '.alert-info strong')
    PRODUCT_NAME_ADDITION_ALERT = (By.CSS_SELECTOR, '.alert-success strong')
