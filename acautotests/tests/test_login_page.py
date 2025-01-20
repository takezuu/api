import time

import pytest

from Pages.LoginPage import LoginPage
from locators import LoginLocators, TopBars, APIMonitor, DevicesLocators, AdminLocators, \
    Notifications
from data import LoginData
from verification import LoginVerif, CasesVerif, AdminVerif
import allure
from tests.decorators import DUsers, DEntities


@pytest.mark.login
@pytest.mark.noload
class TestLoginPage:

    @allure.feature('Authorization page')
    @allure.title('Clean monitor')
    @DUsers.logout_all_users()
    @DEntities.delete_all_entities()
    def test_0_clean_monitor(self, browser, url):
        pass

    @allure.feature('Authorization page')
    @allure.title('Log in with correct password and login/status administrator')
    @DUsers.add_delete_user()
    @DUsers.login_logout_user(user_login=LoginData.ADMIN_LOGIN, user_password=LoginData.PASSWORD, page_name='login')
    def test_login_001(self, page, url):
        """https://knoxygen.atlassian.net/wiki/spaces/WA/pages/3576856588"""
        page.wait_visability_element(element=TopBars.USER_STATUS)
        text_element = page.get_text_element(element=TopBars.USER_STATUS)
        page.check_logged_status(text_element=text_element, check_string=CasesVerif.ADMIN_STATUS)
        page.check_name_of_tab(name_of_tab=CasesVerif.NAME_OF_TAB)
        page.wait_visability_element(element=TopBars.ANALYTIC_BAR)
        page.check_available_bars(arg1=TopBars.DATA_BAR, arg2=TopBars.ANALYTIC_BAR, arg3=TopBars.TOOLS_BAR,
                                  arg4=TopBars.REPORT_BAR, arg5=TopBars.VIEW_BAR, arg6=TopBars.SEARCH_BAR)
        return page

    @allure.feature('Authorization page')
    @allure.title('Log in with correct login and wrong password')
    @DUsers.add_delete_user()
    def test_login_002(self, browser, url):
        """https://knoxygen.atlassian.net/wiki/spaces/WA/pages/3576856599"""
        page = LoginPage(browser)

        page.open_url(url=url)

        page.wait_visability_element(element=LoginLocators.LOGIN_FIELD)
        page.write_in_element(element=LoginLocators.LOGIN_FIELD, text=LoginData.ADMIN_LOGIN)
        page.write_in_element(element=LoginLocators.PASSWORD_FIELD,
                              text=LoginData.INVALID_PASSWORD)

        page.click_element(element=LoginLocators.LOGIN_BUTTON)
        page.wait_visability_element(element=LoginLocators.NOTIFICATION)
        element_text = page.get_text_element(element=LoginLocators.NOTIFICATION)

        page.compare_text(element_text=element_text, message=LoginVerif.LOGIN_PAGE_NOTIFICATION)

    @allure.feature('Authorization page')
    @allure.title('Log in with wrong login and correct password')
    @DUsers.add_delete_user()
    def test_login_003(self, browser, url):
        """https://knoxygen.atlassian.net/wiki/spaces/WA/pages/3653894175"""
        page = LoginPage(browser)

        page.open_url(url=url)

        page.wait_visability_element(element=LoginLocators.LOGIN_FIELD)
        page.write_in_element(element=LoginLocators.LOGIN_FIELD, text=LoginData.INVALID_LOGIN)
        page.write_in_element(element=LoginLocators.PASSWORD_FIELD, text=LoginData.PASSWORD)

        page.click_element(element=LoginLocators.LOGIN_BUTTON)

        page.wait_visability_element(element=LoginLocators.NOTIFICATION)
        element_text = page.get_text_element(element=LoginLocators.NOTIFICATION)
        page.compare_text(element_text=element_text, message=LoginVerif.LOGIN_PAGE_NOTIFICATION)

    @allure.feature('Authorization page')
    @allure.title('Log in with wrong login and password')
    @DUsers.add_delete_user()
    def test_login_004(self, browser, url):
        """https://knoxygen.atlassian.net/wiki/spaces/WA/pages/3576856621"""
        page = LoginPage(browser)

        page.open_url(url=url)

        page.wait_visability_element(element=LoginLocators.LOGIN_FIELD)
        page.write_in_element(element=LoginLocators.LOGIN_FIELD, text=LoginData.INVALID_LOGIN)
        page.write_in_element(element=LoginLocators.PASSWORD_FIELD, text=LoginData.INVALID_PASSWORD)

        page.click_element(element=LoginLocators.LOGIN_BUTTON)

        page.wait_visability_element(element=LoginLocators.NOTIFICATION)
        element_text = page.get_text_element(element=LoginLocators.NOTIFICATION)
        page.compare_text(element_text=element_text, message=LoginVerif.LOGIN_PAGE_NOTIFICATION)

    @allure.feature('Authorization page')
    @allure.title('Log in with dbadmin')
    @DUsers.login_logout_user(user_login=LoginData.SUPER_LOGIN, user_password=LoginData.SUPER_PASSWORD,
                              page_name='login')
    def test_login_005(self, page, url):
        """https://knoxygen.atlassian.net/wiki/spaces/WA/pages/3576856632"""
        page.wait_visability_element(element=TopBars.USER_STATUS)
        text_element = page.get_text_element(element=TopBars.USER_STATUS)
        page.check_logged_status(text_element=text_element, check_string=CasesVerif.SUPER_STATUS)
        page.check_name_of_tab(name_of_tab=AdminVerif.NAME_OF_TAB)
        page.check_available_bars(arg1=TopBars.DATA_BAR, arg2=TopBars.ANALYTIC_BAR, arg3=TopBars.TOOLS_BAR,
                                  arg4=TopBars.REPORT_BAR, arg5=TopBars.ADMIN_BAR, arg6=TopBars.SEARCH_BAR,
                                  arg7=TopBars.VIEW_BAR)
        return page

    @allure.feature('Authorization page')
    @allure.title('Log in with expert')
    @DUsers.add_delete_user(user_status='expert')
    @DUsers.login_logout_user(user_login=LoginData.EXPERT_LOGIN, user_password=LoginData.PASSWORD, page_name='login')
    def test_login_006(self, page, url):
        """https://knoxygen.atlassian.net/wiki/spaces/WA/pages/3576856654"""
        page.wait_visability_element(element=TopBars.USER_STATUS)
        text_element = page.get_text_element(element=TopBars.USER_STATUS)
        page.check_logged_status(text_element=text_element, check_string=CasesVerif.EXPERT_STATUS)
        page.check_name_of_tab(name_of_tab=CasesVerif.NAME_OF_TAB)
        page.check_available_bars(arg1=TopBars.DATA_BAR, arg2=TopBars.ANALYTIC_BAR, arg3=TopBars.TOOLS_BAR,
                                  arg4=TopBars.REPORT_BAR, arg5=TopBars.VIEW_BAR, arg6=TopBars.SEARCH_BAR)
        return page

    @allure.feature('Authorization page')
    @allure.title('Log in with loader')
    @DUsers.add_delete_user(user_status='load')
    @DUsers.login_logout_user(user_login=LoginData.LOAD_LOGIN, user_password=LoginData.PASSWORD, page_name='login')
    def test_login_007(self, page, url):
        """https://knoxygen.atlassian.net/wiki/spaces/WA/pages/3576856665"""
        page.wait_visability_element(element=TopBars.USER_STATUS)
        text_element = page.get_text_element(element=TopBars.USER_STATUS)
        page.check_logged_status(text_element=text_element, check_string=CasesVerif.LOAD_STATUS)
        page.check_name_of_tab(name_of_tab=CasesVerif.NAME_OF_TAB)
        page.check_available_bars(arg=TopBars.DATA_BAR)

        page.hover_on_element(element=TopBars.RIGHT_BAR_LOAD)
        page.wait_visability_element(element=TopBars.EXIT_BUTTON)
        page.click_element(element=TopBars.EXIT_BUTTON)
        page.wait_visability_element(element=LoginLocators.LOGIN_BUTTON)

    @allure.feature('Authorization page')
    @allure.title('Log out with dbadmin + api/monitor')
    def test_login_008(self, browser, url):
        """https://knoxygen.atlassian.net/wiki/spaces/WA/pages/3576856720"""
        page = LoginPage(browser)
        page.open_url(url=url, api=APIMonitor.MONITOR)
        page.get_browser_screenshot()
        condition = True
        while condition:
            condition = page.clear_monitor(element=APIMonitor.LOGOUT)
            if condition:
                page.click_element(element=APIMonitor.LOGOUT)
                page.refresh_page()

        page.open_url(url=url)

        page.wait_visability_element(element=LoginLocators.LOGIN_FIELD)
        page.write_in_element(element=LoginLocators.LOGIN_FIELD, text=LoginData.SUPER_LOGIN)
        page.write_in_element(element=LoginLocators.PASSWORD_FIELD, text=LoginData.SUPER_PASSWORD)

        page.click_element(element=LoginLocators.LOGIN_BUTTON)

        page.open_new_tab()
        page.open_url(url=url, api=APIMonitor.MONITOR)

        page.check_element_contains_text(element=APIMonitor.SUPER_USER)
        browser_tabs = page.get_all_tabs()
        page.select_tab_number(1, browser_tabs)

        page.hover_on_element(element=TopBars.RIGHT_BAR)
        page.wait_visability_element(element=TopBars.EXIT_BUTTON)
        page.click_element(element=TopBars.EXIT_BUTTON)
        page.wait_visability_element(element=LoginLocators.LOGIN_BUTTON)

        browser_tabs = page.get_all_tabs()
        page.select_tab_number(2, browser_tabs)
        page.refresh_page()
        page.refresh_page()

        page.check_element_contains_text_disappeared(element=APIMonitor.SUPER_USER)

    @allure.feature('Authorization page')
    @allure.title('Log out with administrator + api/monitor')
    @DUsers.add_delete_user()
    def test_login_009(self, browser, url):
        """https://knoxygen.atlassian.net/wiki/spaces/WA/pages/3576856731"""
        page = LoginPage(browser)
        page.open_url(url=url, api=APIMonitor.MONITOR)
        page.get_browser_screenshot()
        condition = True
        while condition:
            condition = page.clear_monitor(element=APIMonitor.LOGOUT)
            if condition:
                page.click_element(element=APIMonitor.LOGOUT)
                page.refresh_page()

        page.open_url(url=url)

        page.wait_visability_element(element=LoginLocators.LOGIN_FIELD)
        page.write_in_element(element=LoginLocators.LOGIN_FIELD, text=LoginData.ADMIN_LOGIN)
        page.write_in_element(element=LoginLocators.PASSWORD_FIELD, text=LoginData.PASSWORD)

        page.click_element(element=LoginLocators.LOGIN_BUTTON)

        page.open_new_tab()
        page.open_url(url=url, api=APIMonitor.MONITOR)

        page.check_element_contains_text(element=APIMonitor.ADMIN)
        browser_tabs = page.get_all_tabs()
        page.select_tab_number(1, browser_tabs)
        page.wait_visability_element(element=TopBars.RIGHT_BAR)

        page.hover_on_element(element=TopBars.RIGHT_BAR)
        page.wait_visability_element(element=TopBars.EXIT_BUTTON)
        page.click_element(element=TopBars.EXIT_BUTTON)
        page.wait_visability_element(element=LoginLocators.LOGIN_BUTTON)

        browser_tabs = page.get_all_tabs()
        page.select_tab_number(2, browser_tabs)
        page.refresh_page()
        page.refresh_page()

        page.check_element_contains_text_disappeared(element=APIMonitor.ADMIN)

    @allure.feature('Authorization page')
    @allure.title('Log out with expert + api/monitor')
    @DUsers.add_delete_user(user_status='expert')
    def test_login_010(self, browser, url):
        """https://knoxygen.atlassian.net/wiki/spaces/WA/pages/3576856742"""
        page = LoginPage(browser)
        page.open_url(url=url, api=APIMonitor.MONITOR)
        page.get_browser_screenshot()
        condition = True
        while condition:
            condition = page.clear_monitor(element=APIMonitor.LOGOUT)
            if condition:
                page.click_element(element=APIMonitor.LOGOUT)
                page.refresh_page()

        page.open_url(url=url)

        page.wait_visability_element(element=LoginLocators.LOGIN_FIELD)
        page.write_in_element(element=LoginLocators.LOGIN_FIELD, text=LoginData.EXPERT_LOGIN)
        page.write_in_element(element=LoginLocators.PASSWORD_FIELD, text=LoginData.PASSWORD)

        page.click_element(element=LoginLocators.LOGIN_BUTTON)

        page.open_new_tab()
        page.open_url(url=url, api=APIMonitor.MONITOR)

        page.check_element_contains_text(element=APIMonitor.EXPERT)
        browser_tabs = page.get_all_tabs()
        page.select_tab_number(1, browser_tabs)
        page.wait_visability_element(element=TopBars.RIGHT_BAR)

        page.hover_on_element(element=TopBars.RIGHT_BAR)
        page.wait_visability_element(element=TopBars.EXIT_BUTTON)
        page.click_element(element=TopBars.EXIT_BUTTON)
        page.wait_visability_element(element=LoginLocators.LOGIN_BUTTON)

        browser_tabs = page.get_all_tabs()
        page.select_tab_number(2, browser_tabs)
        page.refresh_page()
        page.refresh_page()

        page.check_element_contains_text_disappeared(element=APIMonitor.EXPERT)

    @allure.feature('Authorization page')
    @allure.title('Log out with loader + api/monitor')
    @DUsers.add_delete_user(user_status='load')
    def test_login_011(self, browser, url):
        """https://knoxygen.atlassian.net/wiki/spaces/WA/pages/3576856753"""
        page = LoginPage(browser)

        page.open_url(url=url)

        page.wait_visability_element(element=LoginLocators.LOGIN_FIELD)
        page.write_in_element(element=LoginLocators.LOGIN_FIELD, text=LoginData.LOAD_LOGIN)
        page.write_in_element(element=LoginLocators.PASSWORD_FIELD, text=LoginData.PASSWORD)

        page.click_element(element=LoginLocators.LOGIN_BUTTON)

        page.open_new_tab()
        page.open_url(url=url, api=APIMonitor.MONITOR)

        page.check_element_contains_text(element=APIMonitor.LOAD)
        browser_tabs = page.get_all_tabs()
        page.select_tab_number(1, browser_tabs)
        page.wait_visability_element(element=TopBars.RIGHT_BAR_LOAD)

        page.hover_on_element(element=TopBars.RIGHT_BAR_LOAD)
        page.wait_visability_element(element=TopBars.EXIT_BUTTON)
        page.click_element(element=TopBars.EXIT_BUTTON)
        page.wait_visability_element(element=LoginLocators.LOGIN_BUTTON)

        browser_tabs = page.get_all_tabs()
        page.select_tab_number(2, browser_tabs)
        page.refresh_page()
        page.refresh_page()

        page.check_element_contains_text_disappeared(element=APIMonitor.LOAD)

    @allure.feature('Authorization page')
    @allure.title('Log out with several opened tabs + api/monitor')
    @DUsers.add_delete_user(user_status='admin')
    def test_login_012(self, browser, url):
        """https://knoxygen.atlassian.net/wiki/spaces/WA/pages/3576856764"""
        page = LoginPage(browser)

        page.open_url(url=url)

        page.wait_visability_element(element=LoginLocators.LOGIN_FIELD)
        page.write_in_element(element=LoginLocators.LOGIN_FIELD, text=LoginData.ADMIN_LOGIN)
        page.write_in_element(element=LoginLocators.PASSWORD_FIELD, text=LoginData.PASSWORD)

        page.click_element(element=LoginLocators.LOGIN_BUTTON)

        page.wait_visability_element(element=TopBars.DATA_BAR)
        page.hover_on_element(element=TopBars.DATA_BAR)
        page.wait_visability_element(element=TopBars.DROP_BLOCK_DEVICES)

        page.open_page_in_new_tab(element=TopBars.DROP_BLOCK_DEVICES)

        browser_tabs = page.get_all_tabs()
        page.select_tab_number(2, browser_tabs)
        page.wait_visability_element(element=DevicesLocators.COUNTER_SECTION)

        page.open_new_tab()
        page.open_url(url=url, api=APIMonitor.MONITOR)

        browser_tabs = page.get_all_tabs()
        page.select_tab_number(1, browser_tabs)

        page.hover_on_element(element=TopBars.RIGHT_BAR)
        page.wait_visability_element(element=TopBars.EXIT_BUTTON)
        page.click_element(element=TopBars.EXIT_BUTTON)
        page.wait_visability_element(element=LoginLocators.LOGIN_BUTTON)
        # проверяю вкладку, где страница логина
        page.check_name_of_tab(name_of_tab=LoginVerif.NAME_OF_TAB)
        element = page.find_element(element=LoginLocators.LOGIN_BUTTON)
        page.check_disable_element(element=element)
        # проверяю вкладку, где была откыта страница устройства
        browser_tabs = page.get_all_tabs()
        page.select_tab_number(2, browser_tabs)
        page.wait_visability_element(element=LoginLocators.LOGIN_BUTTON)
        element = page.find_element(element=LoginLocators.LOGIN_BUTTON)
        page.check_disable_element(element=element)
        page.check_name_of_tab(name_of_tab=LoginVerif.NAME_OF_TAB)

        # проверяю вкладку где, открыта страница монитора
        browser_tabs = page.get_all_tabs()
        page.select_tab_number(3, browser_tabs)
        page.refresh_page()
        page.check_element_contains_text_disappeared(element=APIMonitor.ADMIN)

    @allure.feature('Authorization page')
    @allure.title('Log in after deletion with administrator')
    @DUsers.add_delete_user(user_status='admin')
    @DUsers.login_logout_user(user_login=LoginData.SUPER_LOGIN, user_password=LoginData.SUPER_PASSWORD,
                              page_name='login')
    def test_login_013(self, page, url):
        """https://knoxygen.atlassian.net/wiki/spaces/WA/pages/3576856676"""

        page.wait_not_visability_element(element=Notifications.PRELOADER)
        page.wait_visability_element(element=AdminLocators.SEARCH)
        page.write_in_element(element=AdminLocators.SEARCH, text=LoginData.ADMIN_LOGIN)
        page.press_enter()

        page.wait_visability_element(element=AdminLocators.SELECTED_LINE)
        page.hover_on_element(element=AdminLocators.SELECTED_LINE)
        page.hover_on_element(element=AdminLocators.BASKET)
        page.click_element(element=AdminLocators.BASKET)

        page.wait_visability_element(element=AdminLocators.BASKET_MESSAGE)
        element_text = page.get_text_element(element=AdminLocators.BASKET_MESSAGE)
        page.check_warning_message(element_text=element_text, message=AdminVerif.DELETE_MESSAGE)

        page.click_element(element=AdminLocators.BASKET_YES_BUTTON)
        page.wait_visability_element(element=Notifications.BLUE_NOTIFI)
        element_text = page.get_text_element(element=Notifications.BLUE_NOTIFI)
        page.compare_text(element_text=element_text, message=AdminVerif.FINAL_DELETE_MESSAGE)
        page.click_element(element=Notifications.NOTIFI_CLOSE)
        page.write_in_element(element=AdminLocators.SEARCH, text=LoginData.ADMIN_LOGIN)
        page.press_enter()
        page.check_element_contains_text_disappeared(element=AdminLocators.ADMIN_IN_TABLE)

        page.hover_on_element(element=TopBars.RIGHT_BAR)
        page.wait_visability_element(element=TopBars.EXIT_BUTTON)
        page.click_element(element=TopBars.EXIT_BUTTON)
        page.wait_visability_element(element=LoginLocators.LOGIN_FIELD)

        page.write_in_element(element=LoginLocators.LOGIN_FIELD, text=LoginData.ADMIN_LOGIN)
        page.write_in_element(element=LoginLocators.PASSWORD_FIELD, text=LoginData.PASSWORD)

        page.click_element(element=LoginLocators.LOGIN_BUTTON)

        page.wait_visability_element(element=Notifications.RED_NOTIFI)
        element_text = page.get_text_element(element=Notifications.RED_NOTIFI)
        page.compare_text(element_text=element_text, message=AdminVerif.WRONG_LOGIN_PASSWORD)

    @allure.feature('Authorization page')
    @allure.title('Log in after deletion with expert')
    @DUsers.add_delete_user(user_status='expert')
    @DUsers.login_logout_user(user_login=LoginData.SUPER_LOGIN, user_password=LoginData.SUPER_PASSWORD,
                              page_name='login')
    def test_login_014(self, page, url):
        """https://knoxygen.atlassian.net/wiki/spaces/WA/pages/3576856687"""
        page.wait_visability_element(element=AdminLocators.SEARCH)
        page.write_in_element(element=AdminLocators.SEARCH, text=LoginData.EXPERT_LOGIN)
        page.press_enter()

        page.wait_visability_element(element=AdminLocators.SELECTED_LINE)
        page.hover_on_element(element=AdminLocators.SELECTED_LINE)
        page.hover_on_element(element=AdminLocators.BASKET)
        page.click_element(element=AdminLocators.BASKET)

        page.wait_visability_element(element=AdminLocators.BASKET_MESSAGE)
        element_text = page.get_text_element(element=AdminLocators.BASKET_MESSAGE)
        page.check_warning_message(element_text=element_text, message=AdminVerif.DELETE_MESSAGE)

        page.click_element(element=AdminLocators.BASKET_YES_BUTTON)

        page.wait_visability_element(element=Notifications.BLUE_NOTIFI)
        element_text = page.get_text_element(element=Notifications.BLUE_NOTIFI)
        page.compare_text(element_text=element_text, message=AdminVerif.FINAL_DELETE_MESSAGE)
        page.click_element(element=Notifications.NOTIFI_CLOSE)

        page.write_in_element(element=AdminLocators.SEARCH, text=LoginData.EXPERT_LOGIN)
        page.press_enter()

        page.check_element_contains_text_disappeared(element=AdminLocators.EXPERT_IN_TABLE)

        page.hover_on_element(element=TopBars.RIGHT_BAR)
        page.wait_visability_element(element=TopBars.EXIT_BUTTON)
        page.click_element(element=TopBars.EXIT_BUTTON)

        page.wait_visability_element(element=LoginLocators.LOGIN_FIELD)
        page.write_in_element(element=LoginLocators.LOGIN_FIELD, text=LoginData.EXPERT_LOGIN)
        page.write_in_element(element=LoginLocators.PASSWORD_FIELD, text=LoginData.PASSWORD)
        page.click_element(element=LoginLocators.LOGIN_BUTTON)

        page.wait_visability_element(element=Notifications.RED_NOTIFI)
        element_text = page.get_text_element(element=Notifications.RED_NOTIFI)
        page.compare_text(element_text=element_text, message=AdminVerif.WRONG_LOGIN_PASSWORD)

    @allure.feature('Authorization page')
    @allure.title('Log in after deletion with loader')
    @DUsers.add_delete_user(user_status='load')
    @DUsers.login_logout_user(user_login=LoginData.SUPER_LOGIN, user_password=LoginData.SUPER_PASSWORD,
                              page_name='login')
    def test_login_015(self, page, url):
        """https://knoxygen.atlassian.net/wiki/spaces/WA/pages/3576856698"""
        page.wait_visability_element(element=AdminLocators.SEARCH)
        page.write_in_element(element=AdminLocators.SEARCH, text=LoginData.LOAD_LOGIN)
        page.press_enter()

        page.wait_visability_element(element=AdminLocators.SELECTED_LINE)
        page.hover_on_element(element=AdminLocators.SELECTED_LINE)
        page.hover_on_element(element=AdminLocators.BASKET)
        page.click_element(element=AdminLocators.BASKET)

        page.wait_visability_element(element=AdminLocators.BASKET_MESSAGE)
        element_text = page.get_text_element(element=AdminLocators.BASKET_MESSAGE)
        page.check_warning_message(element_text=element_text, message=AdminVerif.DELETE_MESSAGE)

        page.click_element(element=AdminLocators.BASKET_YES_BUTTON)

        page.wait_visability_element(element=Notifications.BLUE_NOTIFI)
        element_text = page.get_text_element(element=Notifications.BLUE_NOTIFI)
        page.compare_text(element_text=element_text, message=AdminVerif.FINAL_DELETE_MESSAGE)
        page.click_element(element=Notifications.NOTIFI_CLOSE)

        page.write_in_element(element=AdminLocators.SEARCH, text=LoginData.LOAD_LOGIN)
        page.press_enter()

        page.check_element_contains_text_disappeared(element=AdminLocators.LOAD_IN_TABLE)

        page.hover_on_element(element=TopBars.RIGHT_BAR)
        page.wait_visability_element(element=TopBars.EXIT_BUTTON)
        page.click_element(element=TopBars.EXIT_BUTTON)

        page.wait_visability_element(element=LoginLocators.LOGIN_FIELD)
        page.write_in_element(element=LoginLocators.LOGIN_FIELD, text=LoginData.LOAD_LOGIN)
        page.write_in_element(element=LoginLocators.PASSWORD_FIELD, text=LoginData.PASSWORD)

        page.click_element(element=LoginLocators.LOGIN_BUTTON)

        page.wait_visability_element(element=Notifications.RED_NOTIFI)
        element_text = page.get_text_element(element=Notifications.RED_NOTIFI)
        page.compare_text(element_text=element_text, message=AdminVerif.WRONG_LOGIN_PASSWORD)

    @allure.feature('Authorization page')
    @allure.title('Check work of loggin button')
    def test_login_016(self, browser, url):
        """https://knoxygen.atlassian.net/wiki/spaces/WA/pages/3576856775"""
        page = LoginPage(browser)

        page.open_url(url=url)

        page.wait_visability_element(element=LoginLocators.LOGIN_FIELD)
        page.write_in_element(element=LoginLocators.LOGIN_FIELD, text=LoginData.SUPER_LOGIN)
        page.write_in_element(element=LoginLocators.PASSWORD_FIELD, text=LoginData.SUPER_PASSWORD)

        element = page.find_element(element=LoginLocators.LOGIN_BUTTON)

        page.check_able_element(element=element)

    @allure.feature('Authorization page')
    @allure.title('Check work of hid/show password\'s button')
    def test_login_017(self, browser, url):
        """https://knoxygen.atlassian.net/wiki/spaces/WA/pages/3582197778"""
        page = LoginPage(browser)

        page.open_url(url=url)

        page.wait_visability_element(element=LoginLocators.LOGIN_FIELD)
        page.write_in_element(element=LoginLocators.LOGIN_FIELD, text=LoginData.SUPER_LOGIN)
        page.write_in_element(element=LoginLocators.PASSWORD_FIELD, text=LoginData.SUPER_PASSWORD)

        element = page.find_element(element=LoginLocators.EYE)
        page.check_element_attribute(element=element, name_of_attribute='title', state=LoginVerif.EYE)

        element = page.find_element(element=LoginLocators.PASSWORD_FIELD)
        page.check_element_attribute(element=element, name_of_attribute='type', state=LoginVerif.PASSWORD)

        page.click_element(element=LoginLocators.EYE)

        element = page.find_element(element=LoginLocators.EYE)
        page.check_element_attribute(element=element, name_of_attribute='title', state=LoginVerif.HIDE_EYE)

        element = page.find_element(element=LoginLocators.PASSWORD_FIELD)
        page.check_element_attribute(element=element, name_of_attribute='type', state=LoginVerif.PASSWORD_HIDE)

    @allure.feature('Authorization page')
    @allure.title('Clean monitor')
    @DUsers.logout_all_users()
    def test_z_clean_monitor(self, browser, url):
        pass
