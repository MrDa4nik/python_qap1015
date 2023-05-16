# Запуск теста: python -m pytest -v --tb=line tests/test_auth_page.py
import time

from pages.auth_page import AuthPage
from settings import url_base_page

class TestAuthPage():
    def test_RT_001_open_page(self, browser):
        auth_page = AuthPage(browser, url_base_page)
        auth_page.open()
        auth_page.open_page()

    def test_RT_002_locator_left_right(self, browser):
        auth_page = AuthPage(browser, url_base_page)
        auth_page.open()
        time.sleep(5)
        auth_page.locator_left_right()

    def test_RT_003_locator_menu_left(self, browser):
        auth_page = AuthPage(browser, url_base_page)
        auth_page.open()
        auth_page.locator_menu_left()

    def test_RT_004_locator_menu_right(self, browser):
        auth_page = AuthPage(browser, url_base_page)
        auth_page.open()
        auth_page.locator_menu_right()

    def test_RT_005_locator_tab_menu(self, browser):
        auth_page = AuthPage(browser, url_base_page)
        auth_page.open()
        auth_page.locator_tab_menu()

    def test_RT_006_locator_phone_imput(self, browser):
        auth_page = AuthPage(browser, url_base_page)
        auth_page.open()
        auth_page.locator_phone_imput()

    def test_RT_007_authentication_phone_pass(self, browser):
        auth_page = AuthPage(browser, url_base_page)
        auth_page.open()
        time.sleep(5)
        auth_page.authentication_phone_pass()

    def test_RT_008_authentication_email_pass(self, browser):
        auth_page = AuthPage(browser, url_base_page)
        auth_page.open()
        time.sleep(5)
        auth_page.authentication_email_pass()

    def test_RT_009_authentication_login_pass(self, browser):
        auth_page = AuthPage(browser, url_base_page)
        auth_page.open()
        time.sleep(5)
        auth_page.authentication_login_pass()

    def test_RT_010_authentication_ls_pass(self, browser):
        auth_page = AuthPage(browser, url_base_page)
        auth_page.open()
        time.sleep(5)
        auth_page.authentication_ls_pass()

    def test_RT_011_tab_email(self, browser):
        auth_page = AuthPage(browser, url_base_page)
        auth_page.open()
        auth_page.tab_email()

    def test_RT_012_tab_login(self, browser):
        auth_page = AuthPage(browser, url_base_page)
        auth_page.open()
        auth_page.tab_login()

    def test_RT_013_tab_ls(self, browser):
        auth_page = AuthPage(browser, url_base_page)
        auth_page.open()
        auth_page.tab_ls()

    def test_RT_014_recovery_form(self, browser):
        auth_page = AuthPage(browser, url_base_page)
        auth_page.open()
        auth_page.recovery_form()

    def test_RT_015_authentication_cod(self, browser):
        auth_page = AuthPage(browser, url_base_page)
        auth_page.open()
        time.sleep(5)
        auth_page.authentication_cod()

    def test_RT_016_registration_form(self, browser):
        auth_page = AuthPage(browser, url_base_page)
        auth_page.open()
        auth_page.registration_form()

    def test_RT_017_authorization_blank_fields(self, browser):
        auth_page = AuthPage(browser, url_base_page)
        auth_page.open()
        auth_page.authorization_blank_fields()

    def test_RT_018_fake_phone_pass(self, browser):
        auth_page = AuthPage(browser, url_base_page)
        auth_page.open()
        time.sleep(5)
        auth_page.fake_phone_pass()

    def test_RT_019_fake_email_pass(self, browser):
        auth_page = AuthPage(browser, url_base_page)
        auth_page.open()
        time.sleep(5)
        auth_page.fake_email_pass()

    def test_RT_020_fake_login_pass(self, browser):
        auth_page = AuthPage(browser, url_base_page)
        auth_page.open()
        time.sleep(5)
        auth_page.fake_login_pass()

    def test_RT_021_fake_ls_pass(self, browser):
        auth_page = AuthPage(browser, url_base_page)
        auth_page.open()
        time.sleep(5)
        auth_page.fake_ls_pass()


