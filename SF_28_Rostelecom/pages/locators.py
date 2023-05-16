from selenium.webdriver.common.by import By

class BaseLocators:
    BODY = (By.XPATH, "//body")
    LEFT = (By.XPATH,"//section[@id='page-left']")
    RIGHT = (By.XPATH, "//section[@id='page-right']")

class AuthPageLocators:
    AUTH_HEADING = (By.XPATH, "//h1[contains(text(),'Авторизация')]")
    AUTH_MENU = (By.XPATH, "//section[@id='page-left']/*//h1[contains(text(),'Авторизация')]")
    AUTH_SLOGAN = (By.XPATH,
                   "//section[@id='page-right']/*//p[contains(text(),'Персональный помощник в цифровом мире Ростелекома')]")
    AUTH_TAB_MENU = (By.XPATH,
                     "//section[@id='page-right']/*//div[@id='t-btn-tab-phone' or @id='t-btn-tab-mail' or "
                     "@id='t-btn-tab-login' or @id='t-btn-tab-ls']")
    AUTH_USERNAME_INPUT_PLACEHOLDER_TELEPHONE = (By.XPATH, "//span[contains(text(),'Мобильный телефон')]")
    AUTH_USERNAME_INPUT = (By.XPATH, "//input[@id='username']")
    AUTH_USERNAME_INPUT_ACTIV_EMAIL = (By.XPATH, "//span[contains(text(),'Электронная почта')]")
    AUTH_USERNAME_INPUT_ACTIV_LOGIN = (By.XPATH, "//span[contains(text(),'Логин')]")
    AUTH_USERNAME_INPUT_ACTIV_LS = (By.XPATH, "//span[contains(text(),'Лицевой счёт')]")
    AUTH_FORGOT_PASSWORD_LINK = (By.XPATH, "//a[@id='forgot_password']")
    AUTH_REGISTER_LINK = (By.XPATH, "//a[@id='kc-register']")
    AUTH_TAB_PHONE = (By.XPATH, "//div[@id='t-btn-tab-phone']")
    AUTH_TAB_EMAIL = (By.XPATH, "//div[@id='t-btn-tab-mail']")
    AUTH_TAB_LOGIN = (By.XPATH, "//div[@id='t-btn-tab-login']")
    AUTH_TAB_LS = (By.XPATH, "//div[@id='t-btn-tab-ls']")
    AUTH_ENTER_BUTTON = (By.XPATH, "//button[@id='kc-login']")
    AUTH_ERROR_ENTER_PHONE_NUMBER = (By.CSS_SELECTOR, '.rt-input-container__meta--error')
    AUTH_ERROR_FORM = (By.XPATH, "//span[@id='form-error-message']")
    AUTH_PASSWORD_INPUT = (By.XPATH, "//input[@id='password']")
    AUTH_COD = (By.XPATH, "//button[@id='back_to_otp_btn']")
    AUTH_FORM_COD = (By.XPATH, "//h1[contains(text(),'Авторизация по коду')]")
    CHANGE_PASS_HEADING = (By.XPATH, "//h1[contains(text(),'Восстановление пароля')]")
    REG_HEADING = (By.XPATH, "//h1[contains(text(),'Регистрация')]")
