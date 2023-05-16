import time

from settings import *
from .base_page import BasePage
from .locators import BaseLocators, AuthPageLocators


class AuthPage(BasePage):
    # RT_001 проверка перехода на страницу и наличие формы Авторизации
    def open_page(self):
        assert self.is_element_present(AuthPageLocators.AUTH_HEADING)
        assert "https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth" in self.browser.current_url, \
            "url do not match"

    # RT_002 проверка наличие правого и левого блока
    def locator_left_right(self):
        assert self.is_element_present(BaseLocators.LEFT), "element not found"
        assert self.is_element_present(BaseLocators.RIGHT), "element not found"

    # RT_003 проверка наличия формы Авторизации в левом блоке
    def locator_menu_left(self):
        assert self.is_element_present(AuthPageLocators.AUTH_MENU), "element not found"

    # RT_004 проверка наличия слогана в правом блоке
    def locator_menu_right(self):
        assert self.is_element_present(AuthPageLocators.AUTH_SLOGAN), "element not found"

    # RT_005 проверка расположения меню выбора типа аутентификации
    def locator_tab_menu(self):
        assert self.is_element_present(AuthPageLocators.AUTH_TAB_MENU), "element not found"

    # RT_006 проверка типа аутентификации по умолчанию поле imput
    def locator_phone_imput(self):
        assert self.is_element_present(AuthPageLocators.AUTH_USERNAME_INPUT_PLACEHOLDER_TELEPHONE), \
            "element not found"

    # RT_007 проверка аутентификации по телефону и паролю
    def authentication_phone_pass(self):
        self.find_element(AuthPageLocators.AUTH_USERNAME_INPUT).send_keys(valid_phone)
        self.find_element(AuthPageLocators.AUTH_PASSWORD_INPUT).send_keys(valid_password)
        self.find_element(AuthPageLocators.AUTH_ENTER_BUTTON).click()
        assert "https://b2c.passport.rt.ru/account_b2c" in self.browser.current_url, "url do not match"

    # RT_008 проверка аутентификации оп электронной почте и паролю
    def authentication_email_pass(self):
        self.find_element(AuthPageLocators.AUTH_USERNAME_INPUT).send_keys(valid_email)
        self.find_element(AuthPageLocators.AUTH_PASSWORD_INPUT).send_keys(valid_password)
        self.find_element(AuthPageLocators.AUTH_ENTER_BUTTON).click()
        assert "https://b2c.passport.rt.ru/account_b2c" in self.browser.current_url, "url do not match"

    # RT_009 проверка аутентификации по логину и паролю
    def authentication_login_pass(self):
        self.find_element(AuthPageLocators.AUTH_USERNAME_INPUT).send_keys(valid_login)
        self.find_element(AuthPageLocators.AUTH_PASSWORD_INPUT).send_keys(valid_password)
        self.find_element(AuthPageLocators.AUTH_ENTER_BUTTON).click()
        assert "https://b2c.passport.rt.ru/account_b2c" in self.browser.current_url, "url do not match"

    # RT_010 проверка аутентификации по лицевому счету и паролю (тест провал нет валидных данных)
    def authentication_ls_pass(self):
        self.find_element(AuthPageLocators.AUTH_USERNAME_INPUT).send_keys(valid_ls)
        self.find_element(AuthPageLocators.AUTH_PASSWORD_INPUT).send_keys(valid_password)
        self.find_element(AuthPageLocators.AUTH_ENTER_BUTTON).click()
        assert "https://b2c.passport.rt.ru/account_b2c" in self.browser.current_url, "url do not match"

    # RT_011 проверка переключения на email при вводе в поле телефона
    def tab_email(self):
        self.find_element(AuthPageLocators.AUTH_USERNAME_INPUT).send_keys(valid_email)
        self.find_element(AuthPageLocators.AUTH_PASSWORD_INPUT).click()
        assert self.is_element_present(AuthPageLocators.AUTH_USERNAME_INPUT_ACTIV_EMAIL), "element not found"

    # RT_012 проверка переключения на login при вводе в поле телефона
    def tab_login(self):
        self.find_element(AuthPageLocators.AUTH_USERNAME_INPUT).send_keys(valid_login)
        self.find_element(AuthPageLocators.AUTH_PASSWORD_INPUT).click()
        assert self.is_element_present(AuthPageLocators.AUTH_USERNAME_INPUT_ACTIV_LOGIN), "element not found"

    # RT_013 проверка переключения на email при вводе в поле телефона
    def tab_ls(self):
        self.find_element(AuthPageLocators.AUTH_USERNAME_INPUT).send_keys(valid_ls)
        self.find_element(AuthPageLocators.AUTH_PASSWORD_INPUT).click()
        assert self.is_element_present(AuthPageLocators.AUTH_USERNAME_INPUT_ACTIV_LS), "element not found"

    # RT_014 проверка ссылки на форму восстановления пароля
    def recovery_form(self):
        self.find_element(AuthPageLocators.AUTH_FORGOT_PASSWORD_LINK).click()
        assert "https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/reset-credentials" \
               in self.browser.current_url, "url do not match"
        assert self.is_element_present(AuthPageLocators.CHANGE_PASS_HEADING), "element not found"

    # RT_015 проверка ссылки на форму восстановления пароля
    def authentication_cod(self):
        self.find_element(AuthPageLocators.AUTH_COD).click()
        assert self.is_element_present(AuthPageLocators.AUTH_FORM_COD), "element not found"

    # RT_016 проверка ссылки на форму регистрации
    def registration_form(self):
        self.find_element(AuthPageLocators.AUTH_REGISTER_LINK).click()
        assert self.is_element_present(AuthPageLocators.REG_HEADING), "element not found"

    # RT_017 проверка авторизации с незаполненными полями
    def authorization_blank_fields(self):
        self.find_element(AuthPageLocators.AUTH_TAB_PHONE).click()
        self.find_element(AuthPageLocators.AUTH_ENTER_BUTTON).click()
        assert self.is_element_present(AuthPageLocators.AUTH_ERROR_ENTER_PHONE_NUMBER), "element not found"

    # RT_018 проверка авторизации с некорректными данными (телефон, пароль)
    def fake_phone_pass(self):
        self.find_element(AuthPageLocators.AUTH_USERNAME_INPUT).send_keys(fake_phone)
        self.find_element(AuthPageLocators.AUTH_PASSWORD_INPUT).send_keys(fake_password)
        self.find_element(AuthPageLocators.AUTH_ENTER_BUTTON).click()
        assert self.is_element_present(AuthPageLocators.AUTH_ERROR_FORM), "element not found"

    # RT_019 проверка авторизации с некорректными данными (почта, пароль)
    def fake_email_pass(self):
        self.find_element(AuthPageLocators.AUTH_TAB_EMAIL).click()
        self.find_element(AuthPageLocators.AUTH_USERNAME_INPUT).send_keys(fake_email)
        self.find_element(AuthPageLocators.AUTH_PASSWORD_INPUT).send_keys(fake_password)
        self.find_element(AuthPageLocators.AUTH_ENTER_BUTTON).click()
        assert self.is_element_present(AuthPageLocators.AUTH_ERROR_FORM), "element not found"

    # RT_020 проверка авторизации с некорректными данными (логин, пароль)
    def fake_login_pass(self):
        self.find_element(AuthPageLocators.AUTH_TAB_LOGIN).click()
        self.find_element(AuthPageLocators.AUTH_USERNAME_INPUT).send_keys(fake_email)
        self.find_element(AuthPageLocators.AUTH_PASSWORD_INPUT).send_keys(fake_password)
        self.find_element(AuthPageLocators.AUTH_ENTER_BUTTON).click()
        assert self.is_element_present(AuthPageLocators.AUTH_ERROR_FORM), "element not found"

    # RT_021 проверка авторизации с некорректными данными (лицевой счет, пароль)
    def fake_ls_pass(self):
        self.find_element(AuthPageLocators.AUTH_TAB_LS).click()
        self.find_element(AuthPageLocators.AUTH_USERNAME_INPUT).send_keys(fake_email)
        self.find_element(AuthPageLocators.AUTH_PASSWORD_INPUT).send_keys(fake_password)
        self.find_element(AuthPageLocators.AUTH_ENTER_BUTTON).click()
        assert self.is_element_present(AuthPageLocators.AUTH_ERROR_FORM), "element not found"





