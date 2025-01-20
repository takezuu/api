import time
from functools import wraps

import allure

import API
import operation_system
import pytest
from Pages.AdminPage import AdminPage
from data import LoginData, LoadImagesData, STAND_PATH, DevicesData, WorkspaceData, CasesData, HashesData, TagsData, \
    KeywordsSetsData, WatchListsData
from locators import LoginLocators, TopBars, Notifications, AdminLocators, LoadImagesLocators, \
    DevicesLocators, HashesLocators, TagsLocators, KeywordsSetsLocators, WatchListsLocators, WorkspaceLocators
from verification import LoginVerif, AdminVerif, CasesVerif, LoadImagesVerif, LicenseVerif
from tests.decorators import DUsers, DDevices, DLicense, DEntities, DTags, DHashsets, DKeywordSets, DTime, DWathlists


@pytest.mark.license
class TestLicense:

    @staticmethod
    def add_delete_user_test_004(user_status=LoginData.STATUS_ADMIN, user_login=None, user_name=None,
                                 user_lastname=None, position=None):
        """Декоратор для добавления и удаления ползователя"""

        def setup(func):
            wraps(func)

            def inner(self, browser, url):
                headers = None

                try:
                    user_id = None
                    try:
                        headers = API.api_user_login(url=url)
                        user_id = API.api_add_entity(url=url, headers=headers, entity_type='user',
                                                     user_status=user_status,
                                                     user_login=user_login,
                                                     user_name=user_name, user_lastname=user_lastname,
                                                     position=position)
                        func(self, browser, url)
                    finally:
                        API.api_delete_entity(url=url, entity_type='user', entity_id=user_id + 1, headers=headers)

                finally:
                    API.api_user_logout(url=url, headers=headers)

            return inner

        return setup

    @allure.feature('License')
    @allure.title('Clean monitor')
    @pytest.mark.noload
    @DUsers.logout_all_users()
    @DLicense.put_new_license(folder_name='1')
    @DEntities.delete_all_entities()
    def test_0_clean_monitor(self, browser, url):
        pass

    @allure.feature('License')
    @allure.title('Activate system/ log in/ check full version')
    @pytest.mark.noload
    @DUsers.delete_user(user_login=LoginData.ADMIN_LOGIN)
    def test_license_001(self, browser, url):
        """https://knoxygen.atlassian.net/wiki/spaces/WA/pages/3794468986/Auto+License.001"""
        page = AdminPage(browser)
        page.open_url(url=url)
        page.wait_visability_element(element=LoginLocators.LOGIN_FIELD)

        page.check_name_of_tab(name_of_tab=LoginVerif.NAME_OF_TAB)
        page.find_element(element=LoginLocators.LOGIN_CARD_VERSION)

        element_text = page.get_text_element(element=LoginLocators.LOGIN_CARD_LICENSE_NUM)
        page.compare_text(element_text=element_text, message=LoginVerif.LICENSE_NUM)

        element_text = page.get_text_element(element=LoginLocators.LOGIN_CARD_LICENSE_DATE)
        page.compare_text(element_text=element_text, message=LoginVerif.LICENSE_DATE1)

        page.write_in_element(element=LoginLocators.LOGIN_FIELD, text=LoginData.SUPER_LOGIN)
        page.write_in_element(element=LoginLocators.PASSWORD_FIELD,
                              text=LoginData.SUPER_PASSWORD)
        page.click_element(element=LoginLocators.LOGIN_BUTTON)

        page.wait_visability_element(element=TopBars.DATA_BAR)
        page.wait_not_visability_element(element=Notifications.PRELOADER)

        page.check_name_of_tab(name_of_tab=AdminVerif.NAME_OF_TAB)

        page.hover_on_element(element=TopBars.ANALYTIC_BAR)
        page.find_element(element=TopBars.DROP_BLOCK_TEXT_ANALYZER)
        page.hover_on_element(element=TopBars.ADMIN_BAR)
        page.find_element(element=TopBars.DROP_BLOCK_STATISCTICS)

        page.hover_on_element(element=TopBars.RIGHT_BAR)
        page.wait_visability_element(element=TopBars.EXIT_BUTTON)
        page.click_element(element=TopBars.EXIT_BUTTON)
        page.wait_visability_element(element=LoginLocators.LOGIN_BUTTON)

    @allure.feature('License')
    @allure.title('Create max users')
    @DUsers.logout_all_users()
    @pytest.mark.noload
    @DUsers.delete_user(user_login=LoginData.ADMIN_LOGIN)
    def test_license_002(self, browser, url):
        """https://knoxygen.atlassian.net/wiki/spaces/WA/pages/3794469002/Auto+License.002"""
        page = AdminPage(browser)
        page.open_url(url=url)
        page.wait_visability_element(element=LoginLocators.LOGIN_FIELD)

        page.check_name_of_tab(name_of_tab=LoginVerif.NAME_OF_TAB)

        page.write_in_element(element=LoginLocators.LOGIN_FIELD, text=LoginData.SUPER_LOGIN)
        page.write_in_element(element=LoginLocators.PASSWORD_FIELD, text=LoginData.SUPER_PASSWORD)
        page.click_element(element=LoginLocators.LOGIN_BUTTON)

        page.wait_visability_element(element=TopBars.DATA_BAR)
        page.wait_not_visability_element(element=Notifications.PRELOADER)

        page.check_name_of_tab(name_of_tab=AdminVerif.NAME_OF_TAB)

        page.wait_visability_element(element=AdminLocators.ADD_BUTTON)
        page.wait_visability_element(element=AdminLocators.COUNTER)
        counter = page.find_element(element=AdminLocators.COUNTER)
        first_counter = page.get_counter(element=counter)

        page.click_element(element=AdminLocators.ADD_BUTTON)
        page.wait_visability_element(element=AdminLocators.ADD_SECTION)

        page.write_in_element(element=AdminLocators.LOGIN_FIELD, text=LoginData.ADMIN_LOGIN)
        element = page.find_element(element=AdminLocators.SELECT_STATUS)
        page.select_status(element=element, ind=1)
        page.write_in_element(element=AdminLocators.FIRST_NAME, text=LoginData.FIRST_NAME)
        page.write_in_element(element=AdminLocators.LAST_NAME, text=LoginData.LAST_NAME)
        page.write_in_element(element=AdminLocators.PASSWORD_FIELD, text=LoginData.PASSWORD)
        page.write_in_element(element=AdminLocators.PASSWORD_COPY_FIELD, text=LoginData.PASSWORD)

        page.click_element(element=AdminLocators.FINAL_ADD)
        page.wait_visability_element(element=Notifications.BLUE_NOTIFI)
        element_text = page.get_text_element(element=Notifications.BLUE_NOTIFI)
        page.compare_text(element_text=element_text, message=AdminVerif.ADDED_USER)
        page.click_element(element=Notifications.NOTIFI_CLOSE)

        page.write_in_element(element=AdminLocators.SEARCH, text=LoginData.ADMIN_LOGIN)
        page.press_enter()
        page.wait_visability_element(AdminLocators.GRID_LOGIN)
        param_list = page.get_grid_user_parameters(arg1=AdminLocators.GRID_LOGIN,
                                                   arg2=AdminLocators.GRID_STATUS,
                                                   arg3=AdminLocators.GRID_FNAME,
                                                   arg4=AdminLocators.GRID_LNAME)
        page.check_grid_user_parameters(parameters=param_list, check_parameters=AdminVerif.ADMIN_PARAM)
        counter = page.find_element(element=AdminLocators.COUNTER)
        second_counter = page.get_counter(element=counter)
        page.check_counter_plus(first_counter=first_counter, second_counter=second_counter)

        page.hover_on_element(element=TopBars.RIGHT_BAR)
        page.wait_visability_element(element=TopBars.EXIT_BUTTON)
        page.click_element(element=TopBars.EXIT_BUTTON)
        page.wait_visability_element(element=LoginLocators.LOGIN_BUTTON)

    @allure.feature('License')
    @allure.title('Connection with max users')
    @pytest.mark.noload
    @DUsers.logout_all_users()
    @DUsers.add_delete_user(user_login=LoginData.ADMIN_LOGIN)
    def test_license_003(self, browser, url):
        """https://knoxygen.atlassian.net/wiki/spaces/WA/pages/3794469018/Auto+License.003"""
        page = AdminPage(browser)
        page.open_url(url=url)
        page.wait_visability_element(element=LoginLocators.LOGIN_FIELD)

        page.check_name_of_tab(name_of_tab=LoginVerif.NAME_OF_TAB)

        page.write_in_element(element=LoginLocators.LOGIN_FIELD, text=LoginData.ADMIN_LOGIN)
        page.write_in_element(element=LoginLocators.PASSWORD_FIELD, text=LoginData.PASSWORD)
        page.click_element(element=LoginLocators.LOGIN_BUTTON)

        page.wait_visability_element(element=TopBars.DATA_BAR)
        page.wait_not_visability_element(element=Notifications.PRELOADER)

        page.check_name_of_tab(name_of_tab=CasesVerif.NAME_OF_TAB)
        page.check_available_bars(arg1=TopBars.DATA_BAR, arg2=TopBars.ANALYTIC_BAR, arg3=TopBars.TOOLS_BAR,
                                  arg4=TopBars.REPORT_BAR, arg5=TopBars.VIEW_BAR, arg6=TopBars.SEARCH_BAR)
        text_element = page.get_text_element(element=TopBars.USER_STATUS)
        page.check_logged_status(text_element=text_element, check_string=CasesVerif.ADMIN_STATUS)
        page.check_element_absent(element=TopBars.ADMIN_BAR)

        page.hover_on_element(element=TopBars.RIGHT_BAR)
        page.wait_visability_element(element=TopBars.EXIT_BUTTON)
        page.click_element(element=TopBars.EXIT_BUTTON)
        page.wait_visability_element(element=LoginLocators.LOGIN_BUTTON)

    @allure.feature('License')
    @allure.title('Delete user with max users and create new user and authorization')
    @pytest.mark.noload
    @DUsers.logout_all_users()
    @add_delete_user_test_004(user_login=LoginData.ADMIN_LOGIN)
    @DUsers.login_logout_user(user_login=LoginData.SUPER_LOGIN, user_password=LoginData.SUPER_PASSWORD,
                              page_name='admin')
    def test_license_004(self, page, url):
        """https://knoxygen.atlassian.net/wiki/spaces/WA/pages/3794469034/Auto+License.004"""
        page.wait_not_visability_element(element=Notifications.PRELOADER)
        page.wait_visability_element(element=AdminLocators.SEARCH)
        page.write_in_element(element=AdminLocators.SEARCH, text=LoginData.ADMIN_LOGIN)
        page.press_enter()

        page.wait_visability_element(element=AdminLocators.SELECTED_LINE)
        page.hover_on_element(element=AdminLocators.SELECTED_LINE)
        page.hover_on_element(element=AdminLocators.BASKET)
        page.click_element(element=AdminLocators.BASKET)

        page.wait_visability_element(element=AdminLocators.BASKET_MESSAGE)

        page.click_element(element=AdminLocators.BASKET_YES_BUTTON)
        page.wait_visability_element(element=Notifications.BLUE_NOTIFI)
        element_text = page.get_text_element(element=Notifications.BLUE_NOTIFI)
        page.compare_text(element_text=element_text, message=AdminVerif.FINAL_DELETE_MESSAGE)
        page.click_element(element=Notifications.NOTIFI_CLOSE)

        page.wait_visability_element(element=AdminLocators.ADD_BUTTON)
        page.wait_visability_element(element=AdminLocators.COUNTER)
        counter = page.find_element(element=AdminLocators.COUNTER)
        first_counter = page.get_counter(element=counter)

        page.click_element(element=AdminLocators.ADD_BUTTON)
        page.wait_visability_element(element=AdminLocators.ADD_SECTION)

        page.write_in_element(element=AdminLocators.LOGIN_FIELD, text=LoginData.ADMIN_LOGIN)
        element = page.find_element(element=AdminLocators.SELECT_STATUS)
        page.select_status(element=element, ind=1)
        page.write_in_element(element=AdminLocators.FIRST_NAME, text=LoginData.FIRST_NAME)
        page.write_in_element(element=AdminLocators.LAST_NAME, text=LoginData.LAST_NAME)
        page.write_in_element(element=AdminLocators.PASSWORD_FIELD, text=LoginData.PASSWORD)
        page.write_in_element(element=AdminLocators.PASSWORD_COPY_FIELD, text=LoginData.PASSWORD)

        page.click_element(element=AdminLocators.FINAL_ADD)
        page.wait_visability_element(element=Notifications.BLUE_NOTIFI_2)
        element_text = page.get_text_element(element=Notifications.BLUE_NOTIFI_2)
        page.compare_text(element_text=element_text, message=AdminVerif.ADDED_USER)
        page.click_element(element=Notifications.NOTIFI_CLOSE_2)

        counter = page.find_element(element=AdminLocators.COUNTER)
        second_counter = page.get_counter(element=counter)
        page.check_counter_plus(first_counter=first_counter, second_counter=second_counter)

        page.hover_on_element(element=TopBars.RIGHT_BAR)
        page.wait_visability_element(element=TopBars.EXIT_BUTTON)
        page.click_element(element=TopBars.EXIT_BUTTON)
        page.wait_visability_element(element=LoginLocators.LOGIN_BUTTON)

        page.wait_visability_element(element=LoginLocators.LOGIN_FIELD)
        page.write_in_element(element=LoginLocators.LOGIN_FIELD, text=LoginData.ADMIN_LOGIN)
        page.write_in_element(element=LoginLocators.PASSWORD_FIELD,
                              text=LoginData.PASSWORD)
        page.click_element(element=LoginLocators.LOGIN_BUTTON)

        page.wait_not_visability_element(element=Notifications.PRELOADER)
        page.wait_visability_element(element=TopBars.DATA_BAR)

        text_element = page.get_text_element(element=TopBars.USER_STATUS)
        page.check_logged_status(text_element=text_element, check_string=CasesVerif.ADMIN_STATUS)
        page.check_element_absent(element=TopBars.ADMIN_BAR)

        page.check_name_of_tab(name_of_tab=CasesVerif.NAME_OF_TAB)

        return page

    @allure.feature('License')
    @allure.title('Create user with max users')
    @pytest.mark.noload
    @DEntities.delete_all_entities()
    @DUsers.logout_all_users()
    @DUsers.add_delete_users(users_data=[(LoginData.EXPERT_LOGIN, LoginData.FIRST_NAME),
                                         (LoginData.EXPERT_LOGIN_2, LoginData.NEW_FIRST_NAME)])
    @DUsers.login_logout_user(user_login=LoginData.SUPER_LOGIN, user_password=LoginData.SUPER_PASSWORD,
                              page_name='admin')
    def test_license_005(self, page, url):
        """https://knoxygen.atlassian.net/wiki/spaces/WA/pages/3794469050/Auto+License.005"""
        page.wait_not_visability_element(element=Notifications.PRELOADER)
        page.wait_visability_element(element=AdminLocators.ADD_BUTTON)

        page.click_element(element=AdminLocators.ADD_BUTTON)
        page.wait_visability_element(element=AdminLocators.ADD_SECTION)

        page.write_in_element(element=AdminLocators.LOGIN_FIELD, text=LoginData.ADMIN_LOGIN)
        element = page.find_element(element=AdminLocators.SELECT_STATUS)
        page.select_status(element=element, ind=1)
        page.write_in_element(element=AdminLocators.FIRST_NAME, text=LoginData.FIRST_NAME)
        page.write_in_element(element=AdminLocators.LAST_NAME, text=LoginData.LAST_NAME)
        page.write_in_element(element=AdminLocators.PASSWORD_FIELD, text=LoginData.PASSWORD)
        page.write_in_element(element=AdminLocators.PASSWORD_COPY_FIELD, text=LoginData.PASSWORD)

        page.click_element(element=AdminLocators.FINAL_ADD)

        page.wait_visability_element(element=Notifications.RED_NOTIFI)
        element_text = page.get_text_element(element=Notifications.RED_NOTIFI)
        page.compare_text(element_text=element_text, message=AdminVerif.MAX_USERS)
        page.click_element(element=Notifications.RED_NOTIFI_CLOSE)

        page.click_element(element=AdminLocators.CANCEL_BUTTON)

        return page

    @allure.feature('License')
    @allure.title('Log in with max connections')
    @pytest.mark.noload
    @DUsers.logout_all_users()
    @DUsers.add_delete_user(user_login=LoginData.ADMIN_LOGIN)
    @DUsers.api_login_logout(data_for_login=LoginData.ADMIN_LOGIN)
    def test_license_006(self, browser, url):
        """https://knoxygen.atlassian.net/wiki/spaces/WA/pages/3794469066/Auto+License.006"""
        page = AdminPage(browser)
        page.open_url(url=url)
        page.wait_visability_element(element=LoginLocators.LOGIN_FIELD)

        page.write_in_element(element=LoginLocators.LOGIN_FIELD, text=LoginData.SUPER_LOGIN)
        page.write_in_element(element=LoginLocators.PASSWORD_FIELD, text=LoginData.SUPER_PASSWORD)
        page.click_element(element=LoginLocators.LOGIN_BUTTON)

        page.wait_visability_element(element=Notifications.RED_NOTIFI)
        element_text = page.get_text_element(element=Notifications.RED_NOTIFI)
        page.compare_text(element_text=element_text, message=AdminVerif.MAX_CONNECTIONS)

        return page

    @allure.feature('License')
    @allure.title('Upload 1 backup via import')
    @DUsers.logout_all_users()
    @DUsers.login_logout_user(user_login=LoginData.SUPER_LOGIN, user_password=LoginData.SUPER_PASSWORD,
                              page_name='admin')
    def test_license_008(self, page, url):
        """https://knoxygen.atlassian.net/wiki/spaces/WA/pages/3794469098/Auto+License.008"""

        page.wait_visability_element(element=TopBars.DATA_BAR)

        page.open_url(url=url, api=LoadImagesData.PAGE)

        page.wait_not_visability_element(element=Notifications.PRELOADER)
        page.wait_visability_element(element=LoadImagesLocators.ADD_BUTTON)
        page.wait_element_is_clickable(element=LoadImagesLocators.ADD_BUTTON)

        page.wait_not_visability_element(element=Notifications.PRELOADER)
        page.click_element(element=LoadImagesLocators.ADD_BUTTON)

        page.wait_visability_element(element=LoadImagesLocators.ADD_SECTION)

        page.upload_file(file_dir=STAND_PATH + '\\1', file_name='test.ofbx',
                         element=LoadImagesLocators.INPUT_FILE_OFBX_OFBR)

        page.click_element(element=LoadImagesLocators.CHECKBOX_NOFILES)

        page.click_element(element=LoadImagesLocators.FINAL_ADD)

        while True:
            page.wait_visability_element(element=Notifications.IMAGE_UPLOAD)
            element_text = page.get_text_element(Notifications.IMAGE_UPLOAD)[:13]
            if len(element_text) > 0:
                page.compare_text(element_text=element_text, message=LoadImagesVerif.IMAGE_UPLOAD)
                if page.check_element_is_appeared(element=LoadImagesLocators.OFBX):
                    break

        element_text = page.get_text_element(Notifications.IMAGE_UPLOAD_PROCESS)
        page.compare_text(element_text=element_text, message=LoadImagesVerif.IMAGE_SUCCESS_UPLOAD)

        while True:
            page.refresh_page()
            page.wait_not_visability_element(element=Notifications.PRELOADER)
            time.sleep(60)
            if page.check_element_is_appeared(element=LoadImagesLocators.OFBX):
                element_text = page.get_upload_badge(element=LoadImagesLocators.UPLOAD_BADGE)
                page.compare_badge_in_while(element_text=element_text)
                element_text = page.get_text_element(LoadImagesLocators.GRID_NOTIFI)
                page.check_text_not_in(element_text=element_text, message=LoadImagesVerif.GRID_NOTIFI)
            else:
                break

        page.wait_not_visability_element(element=Notifications.PRELOADER)
        page.check_element_contains_text_disappeared(element=LoadImagesLocators.OFBX)
        return page

    @allure.feature('License')
    @allure.title('Upload max devices delete device and upload')
    @pytest.mark.skip(reason='Log out')
    @DUsers.logout_all_users()
    @DDevices.delete_several_devices()
    @DLicense.put_new_license(folder_name='2')
    @DUsers.login_logout_user(user_login=LoginData.SUPER_LOGIN, user_password=LoginData.SUPER_PASSWORD,
                              page_name='admin')
    def test_license_009_010(self, page, url):
        """https://knoxygen.atlassian.net/wiki/spaces/WA/pages/3794469114/Auto+License.009
        https://knoxygen.atlassian.net/wiki/spaces/WA/pages/3794469130/Auto+License.010"""
        page.wait_visability_element(element=TopBars.DATA_BAR)

        page.open_url(url=url, api=LoadImagesData.PAGE)

        page.wait_visability_element(element=LoadImagesLocators.ADD_BUTTON)
        page.wait_element_is_clickable(element=LoadImagesLocators.ADD_BUTTON)

        page.wait_not_visability_element(element=Notifications.PRELOADER)
        page.click_element(element=LoadImagesLocators.ADD_BUTTON)

        page.wait_visability_element(element=LoadImagesLocators.ADD_SECTION)

        page.upload_file(file_dir=STAND_PATH + '\\1', file_name='test.ofbx',
                         element=LoadImagesLocators.INPUT_FILE_OFBX_OFBR)

        page.click_element(element=LoadImagesLocators.CHECKBOX_NOFILES)

        page.click_element(element=LoadImagesLocators.FINAL_ADD)

        while True:
            page.wait_visability_element(element=Notifications.IMAGE_UPLOAD)
            element_text = page.get_text_element(Notifications.IMAGE_UPLOAD)[:13]
            if len(element_text) > 0:
                page.compare_text(element_text=element_text, message=LoadImagesVerif.IMAGE_UPLOAD)
                if page.check_element_is_appeared(element=LoadImagesLocators.OFBX):
                    break

        element_text = page.get_text_element(Notifications.IMAGE_UPLOAD_PROCESS)
        page.compare_text(element_text=element_text, message=LoadImagesVerif.IMAGE_SUCCESS_UPLOAD)

        while True:
            page.refresh_page()
            page.wait_not_visability_element(element=Notifications.PRELOADER)
            time.sleep(60)
            if page.check_element_is_appeared(element=LoadImagesLocators.OFBX):
                element_text = page.get_upload_badge(element=LoadImagesLocators.UPLOAD_BADGE)
                page.compare_badge_in_while(element_text=element_text)
                element_text = page.get_text_element(LoadImagesLocators.GRID_NOTIFI)
                page.check_text_not_in(element_text=element_text, message=LoadImagesVerif.GRID_NOTIFI)
            else:
                break

        page.wait_not_visability_element(element=Notifications.PRELOADER)
        page.check_element_contains_text_disappeared(element=LoadImagesLocators.OFBX)

        page.open_url(url=url, api=DevicesData.PAGE)

        page.wait_not_visability_element(element=Notifications.PRELOADER)
        page.wait_visability_element(element=DevicesLocators.OPEN_BUTTON)
        page.wait_element_is_clickable(element=DevicesLocators.OPEN_BUTTON)

        page.write_in_element(element=DevicesLocators.SEARCH, text=DevicesData.DEVICE)
        page.press_enter()

        page.wait_visability_element(element=DevicesLocators.GRID_DEVICE_NAME)

        page.wait_visability_element(element=AdminLocators.SELECTED_LINE)
        page.hover_on_element(element=AdminLocators.SELECTED_LINE)
        page.hover_on_element(element=AdminLocators.BASKET)
        page.click_element(element=AdminLocators.BASKET)

        page.wait_visability_element(element=DevicesLocators.BASKET_MESSAGE)
        page.click_element(element=DevicesLocators.BASKET_OK_BUTTON)
        page.wait_visability_element(element=DevicesLocators.BASKET_YES_BUTTON)
        page.click_element(element=DevicesLocators.BASKET_YES_BUTTON)

        page.wait_visability_element(element=Notifications.BLUE_NOTIFI)
        element_text = page.get_text_element(element=Notifications.BLUE_NOTIFI)
        page.compare_text(element_text=element_text, message=AdminVerif.FINAL_DELETE_MESSAGE)
        page.click_element(element=Notifications.NOTIFI_CLOSE)

        page.open_url(url=url, api=LoadImagesData.PAGE)

        page.wait_not_visability_element(element=Notifications.PRELOADER)
        page.wait_visability_element(element=LoadImagesLocators.ADD_BUTTON)
        page.wait_element_is_clickable(element=LoadImagesLocators.ADD_BUTTON)

        page.wait_not_visability_element(element=Notifications.PRELOADER)
        page.click_element(element=LoadImagesLocators.ADD_BUTTON)

        page.wait_visability_element(element=LoadImagesLocators.ADD_SECTION)

        page.upload_file(file_dir=STAND_PATH + '\\1', file_name='test.ofbx',
                         element=LoadImagesLocators.INPUT_FILE_OFBX_OFBR)

        page.click_element(element=LoadImagesLocators.FINAL_ADD)

        while True:
            page.wait_visability_element(element=Notifications.IMAGE_UPLOAD)
            element_text = page.get_text_element(Notifications.IMAGE_UPLOAD)[:13]
            if len(element_text) > 0:
                page.compare_text(element_text=element_text, message=LoadImagesVerif.IMAGE_UPLOAD)
                if page.check_element_is_appeared(element=LoadImagesLocators.OFBX):
                    break

        element_text = page.get_text_element(Notifications.IMAGE_UPLOAD_PROCESS)
        page.compare_text(element_text=element_text, message=LoadImagesVerif.IMAGE_SUCCESS_UPLOAD)

        while True:
            page.refresh_page()
            page.wait_not_visability_element(element=Notifications.PRELOADER)
            time.sleep(60)
            if page.check_element_is_appeared(element=LoadImagesLocators.OFBX):
                element_text = page.get_upload_badge(element=LoadImagesLocators.UPLOAD_BADGE)
                page.compare_badge_in_while(element_text=element_text)
                element_text = page.get_text_element(LoadImagesLocators.GRID_NOTIFI)
                page.check_text_not_in(element_text=element_text, message=LoadImagesVerif.GRID_NOTIFI)
            else:
                break

        page.wait_not_visability_element(element=Notifications.PRELOADER)
        page.check_element_contains_text_disappeared(element=LoadImagesLocators.OFBX)

        return page

    @allure.feature('License')
    @allure.title('Check upload over max devices')
    @pytest.mark.noload
    @DUsers.logout_all_users()
    @DDevices.delete_several_devices()
    @DLicense.put_new_license(folder_name='3')
    @DUsers.login_logout_user(user_login=LoginData.SUPER_LOGIN, user_password=LoginData.SUPER_PASSWORD,
                              page_name='admin')
    def test_license_011(self, page, url):
        """https://knoxygen.atlassian.net/wiki/spaces/WA/pages/3794469146/Auto+License.011"""
        page.wait_visability_element(element=TopBars.DATA_BAR)

        page.open_url(url=url, api=LoadImagesData.PAGE)

        page.wait_not_visability_element(element=Notifications.PRELOADER)
        page.wait_visability_element(element=LoadImagesLocators.ADD_BUTTON)
        page.wait_element_is_clickable(element=LoadImagesLocators.ADD_BUTTON)

        page.wait_not_visability_element(element=Notifications.PRELOADER)
        page.click_element(element=LoadImagesLocators.ADD_BUTTON)

        page.wait_visability_element(element=Notifications.RED_NOTIFI)
        element_text = page.get_text_element(element=Notifications.RED_NOTIFI)
        page.compare_text(element_text=element_text, message=LoadImagesVerif.MAX_DEVICES)
        page.click_element(element=Notifications.RED_NOTIFI_CLOSE)

        return page

    @allure.feature('License')
    @allure.title('Check invalid hardware id')
    @pytest.mark.noload
    @DUsers.logout_all_users()
    @DLicense.put_new_license(folder_name='4')
    def test_license_014(self, browser, url):
        """https://knoxygen.atlassian.net/wiki/spaces/WA/pages/3794469190/Auto+License.014+hardware+id+id"""
        page = AdminPage(browser)
        page.open_url(url=url)
        page.wait_visability_element(element=LoginLocators.LOGIN_FIELD)

        page.check_name_of_tab(name_of_tab=LoginVerif.NAME_OF_TAB)

        page.wait_visability_element(element=LoginLocators.LOGIN_FIELD)
        page.write_in_element(element=LoginLocators.LOGIN_FIELD, text=LoginData.SUPER_LOGIN)
        page.write_in_element(element=LoginLocators.PASSWORD_FIELD, text=LoginData.SUPER_PASSWORD)
        page.click_element(element=LoginLocators.LOGIN_BUTTON)

        page.wait_visability_element(element=Notifications.RED_NOTIFI)
        element_text = page.get_text_element(element=Notifications.RED_NOTIFI)
        page.compare_text(element_text=element_text, message=LoginVerif.IVALID_HID)

    @allure.feature('License')
    @allure.title('Login day before license expiration')
    @pytest.mark.skip(reason='Time confuse')
    @pytest.mark.noload
    @DTime.change_time_before()
    @DLicense.put_new_license(folder_name='13')
    @DUsers.login_logout_user(user_login=LoginData.SUPER_LOGIN, user_password=LoginData.SUPER_PASSWORD,
                              page_name='admin')
    def test_license_015(self, page, url):
        page.wait_visability_element(element=TopBars.DATA_BAR)
        page.wait_not_visability_element(element=Notifications.PRELOADER)

        page.check_name_of_tab(name_of_tab=AdminVerif.NAME_OF_TAB)

        return page

    @allure.feature('License')
    @allure.title('Login on day license expiration')
    @pytest.mark.skip(reason='Time confuse')
    @pytest.mark.noload
    @DTime.change_time_today()
    @DUsers.login_logout_user(user_login=LoginData.SUPER_LOGIN, user_password=LoginData.SUPER_PASSWORD,
                              page_name='admin')
    def test_license_016(self, page, url):
        page.wait_visability_element(element=TopBars.DATA_BAR)
        page.wait_not_visability_element(element=Notifications.PRELOADER)

        page.check_name_of_tab(name_of_tab=AdminVerif.NAME_OF_TAB)

        page.hover_on_element(element=TopBars.RIGHT_BAR)
        page.wait_visability_element(element=TopBars.EXIT_BUTTON)
        page.click_element(element=TopBars.EXIT_BUTTON)
        page.wait_visability_element(element=LoginLocators.LOGIN_BUTTON)

        operation_system.execute_time_script_day_after()
        time.sleep(2)

        page.write_in_element(element=LoginLocators.LOGIN_FIELD, text=LoginData.SUPER_LOGIN)
        page.write_in_element(element=LoginLocators.PASSWORD_FIELD,
                              text=LoginData.SUPER_PASSWORD)
        page.click_element(element=LoginLocators.LOGIN_BUTTON)

        page.wait_visability_element(element=Notifications.RED_NOTIFI)
        element_text = page.get_text_element(element=Notifications.RED_NOTIFI)
        page.compare_text(element_text=element_text, message=LicenseVerif.LICENSE_EXPIRATION)

    @pytest.mark.test
    @allure.feature('License')
    @allure.title('Access denied check after expiration license')
    @pytest.mark.noload
    @DUsers.logout_all_users()
    @DLicense.put_new_license(folder_name='6')
    def test_license_017(self, browser, url):
        page = AdminPage(browser)
        page.open_url(url=url)
        page.wait_visability_element(element=LoginLocators.LOGIN_FIELD)

        page.check_name_of_tab(name_of_tab=LoginVerif.NAME_OF_TAB)

        page.write_in_element(element=LoginLocators.LOGIN_FIELD, text=LoginData.SUPER_LOGIN)
        page.write_in_element(element=LoginLocators.PASSWORD_FIELD,
                              text=LoginData.SUPER_PASSWORD)
        page.click_element(element=LoginLocators.LOGIN_BUTTON)

        page.wait_visability_element(element=Notifications.RED_NOTIFI)
        element_text = page.get_text_element(element=Notifications.RED_NOTIFI)
        page.compare_text(element_text=element_text, message=LicenseVerif.LICENSE_EXPIRATION)

    @allure.feature('License')
    @allure.title('Delete license file during using system')
    @pytest.mark.noload
    @DUsers.logout_all_users()
    @DLicense.put_new_license(folder_name='1')
    def test_license_018(self, browser, url):
        """https://knoxygen.atlassian.net/wiki/spaces/WA/pages/3794469270/Auto+License.018"""
        page = AdminPage(browser)
        page.open_url(url=url)
        page.wait_visability_element(element=LoginLocators.LOGIN_FIELD)

        page.check_name_of_tab(name_of_tab=LoginVerif.NAME_OF_TAB)

        page.write_in_element(element=LoginLocators.LOGIN_FIELD, text=LoginData.SUPER_LOGIN)
        page.write_in_element(element=LoginLocators.PASSWORD_FIELD,
                              text=LoginData.SUPER_PASSWORD)
        page.click_element(element=LoginLocators.LOGIN_BUTTON)

        page.wait_visability_element(element=TopBars.DATA_BAR)
        page.wait_not_visability_element(element=Notifications.PRELOADER)

        page.check_name_of_tab(name_of_tab=AdminVerif.NAME_OF_TAB)

        page.open_url(url=url, api=WorkspaceData.PAGE)

        page.wait_not_visability_element(element=Notifications.PRELOADER)
        page.wait_visability_element(element=WorkspaceLocators.LEFT_SIDEBAR)

        operation_system.delete_license()
        operation_system.reload_backend()

        time.sleep(60)

        page.open_url(url=url, api=CasesData.PAGE)

        page.wait_not_visability_element(element=Notifications.PRELOADER)
        page.wait_visability_element(element=Notifications.RED_NOTIFI)
        element_text = page.get_text_element(element=Notifications.RED_NOTIFI)
        page.compare_text(element_text=element_text, message=LicenseVerif.LICENSE_ERROR)

    @allure.feature('License')
    @allure.title('Exclude dbadmin from users list')
    @pytest.mark.noload
    @DUsers.logout_all_users()
    @DLicense.put_new_license(folder_name='10')
    @DUsers.add_delete_user(user_login=LoginData.EXPERT_LOGIN, user_status=LoginData.STATUS_EXPERT)
    @DUsers.add_delete_user(user_login=LoginData.EXPERT_LOGIN_2, user_status=LoginData.STATUS_EXPERT)
    @DUsers.login_logout_user(user_login=LoginData.SUPER_LOGIN, user_password=LoginData.SUPER_PASSWORD,
                              page_name='admin')
    def test_license_023(self, page, url):
        """https://knoxygen.atlassian.net/wiki/spaces/WA/pages/3794469350/Auto+License.023+dbadmin"""
        page.wait_visability_element(element=AdminLocators.ADD_BUTTON)
        page.wait_visability_element(element=AdminLocators.COUNTER)

        page.click_element(element=AdminLocators.ADD_BUTTON)
        page.wait_visability_element(element=AdminLocators.ADD_SECTION)

        page.write_in_element(element=AdminLocators.LOGIN_FIELD, text=LoginData.ADMIN_LOGIN)
        element = page.find_element(element=AdminLocators.SELECT_STATUS)
        page.select_status(element=element, ind=1)
        page.write_in_element(element=AdminLocators.FIRST_NAME, text=LoginData.FIRST_NAME)
        page.write_in_element(element=AdminLocators.LAST_NAME, text=LoginData.LAST_NAME)
        page.write_in_element(element=AdminLocators.PASSWORD_FIELD, text=LoginData.PASSWORD)
        page.write_in_element(element=AdminLocators.PASSWORD_COPY_FIELD, text=LoginData.PASSWORD)

        page.click_element(element=AdminLocators.FINAL_ADD)

        page.wait_visability_element(element=Notifications.RED_NOTIFI)
        element_text = page.get_text_element(element=Notifications.RED_NOTIFI)
        page.compare_text(element_text=element_text, message=AdminVerif.MAX_USERS)
        page.click_element(element=Notifications.RED_NOTIFI_CLOSE)

        page.click_element(element=AdminLocators.CANCEL_BUTTON)

        return page

    @allure.feature('License')
    @allure.title('Access check after expiration license')
    @pytest.mark.noload
    @DUsers.logout_all_users()
    @DLicense.put_new_license(folder_name='5')
    @DUsers.login_logout_user(user_login=LoginData.SUPER_LOGIN, user_password=LoginData.SUPER_PASSWORD,
                              page_name='admin')
    def test_license_024(self, page, url):
        page.wait_visability_element(element=TopBars.DATA_BAR)
        page.wait_not_visability_element(element=Notifications.PRELOADER)

        page.check_name_of_tab(name_of_tab=AdminVerif.NAME_OF_TAB)

        page.open_url(url=url, api=LoadImagesData.PAGE)

        page.wait_not_visability_element(element=Notifications.PRELOADER)
        page.wait_visability_element(element=LoadImagesLocators.ADD_BUTTON)
        page.wait_element_is_clickable(element=LoadImagesLocators.ADD_BUTTON)

        page.click_element(element=LoadImagesLocators.ADD_BUTTON)

        page.wait_visability_element(element=Notifications.RED_NOTIFI)
        element_text = page.get_text_element(element=Notifications.RED_NOTIFI)
        page.compare_text(element_text=element_text, message=LicenseVerif.LICENSE_EXPIRATION)

        return page

    @allure.feature('License')
    @allure.title('Check education license')
    @pytest.mark.noload
    @DUsers.logout_all_users()
    @DLicense.put_new_license(folder_name='8')
    @DTags.add_delete_tags(
        tags_name_list=['tag1', 'tag2', 'tag3', 'tag4', 'tag5', 'tag6', 'tag7', 'tag8', 'tag9', 'tag10',
                        'tag11', 'tag12', 'tag13', 'tag14', 'tag15', 'tag16', 'tag17', 'tag18', 'tag19', 'tag20'])
    @DKeywordSets.add_delete_keywords_sets(
        keywords_sets_name_list=['keyword_set1', 'keyword_set2', 'keyword_set3', 'keyword_set4',
                                 'keyword_set5', 'keyword_set6', 'keyword_set7', 'keyword_set8', 'keyword_set9',
                                 'keyword_set10', 'keyword_set11', 'keyword_set12', 'keyword_set13', 'keyword_set14',
                                 'keyword_set15', 'keyword_set16', 'keyword_set17', 'keyword_set18', 'keyword_set19',
                                 'keyword_set20'])
    @DHashsets.add_delete_hashes(
        hashes_name_list=['hashset1', 'hashset2', 'hashset3', 'hashset4', 'hashset5', 'hashset6',
                          'hashset7', 'hashset8', 'hashset9', 'hashset10', 'hashset11', 'hashset12', 'hashset13',
                          'hashset14', 'hashset15', 'hashset16', 'hashset17', 'hashset18', 'hashset19', 'hashset20'])
    @DWathlists.add_delete_watchlists(
        watchlists_name_list=['watchlist1', 'watchlist2', 'watchlist3', 'watchlist4', 'watchlist5', 'watchlist6',
                              'watchlist7', 'watchlist8', 'watchlist9', 'watchlist10', 'watchlist11', 'watchlist12',
                              'watchlist13', 'watchlist14', 'watchlist15', 'watchlist16', 'watchlist17', 'watchlist18',
                              'watchlist19', 'watchlist20'])
    @DUsers.login_logout_user(user_login=LoginData.SUPER_LOGIN, user_password=LoginData.SUPER_PASSWORD,
                              page_name='admin')
    def test_license_025(self, page, url):
        page.wait_not_visability_element(element=Notifications.PRELOADER)
        page.wait_visability_element(element=TopBars.DATA_BAR)

        page.hover_on_element(element=TopBars.DATA_BAR)
        page.check_element_absent(element=TopBars.DROP_BLOCK_TEXT_ANALYZER)
        page.check_element_absent(element=TopBars.DROP_BLOCK_LOAD_IMAGES)

        page.hover_on_element(element=TopBars.ADMIN_BAR)
        page.check_element_absent(element=TopBars.DROP_BLOCK_STATISCTICS)

        page.open_url(url=url, api=HashesData.PAGE)

        page.wait_not_visability_element(element=Notifications.PRELOADER)
        page.wait_visability_element(element=HashesLocators.ADD_BUTTON)

        page.click_element(element=HashesLocators.ADD_BUTTON)

        page.wait_visability_element(element=Notifications.RED_NOTIFI)
        element_text = page.get_text_element(element=Notifications.RED_NOTIFI)
        page.compare_text(element_text=element_text, message=LicenseVerif.LICENSE_LIMIT_HASHES)
        page.click_element(element=Notifications.RED_NOTIFI_CLOSE)

        page.open_url(url=url, api=TagsData.PAGE)

        page.wait_not_visability_element(element=Notifications.PRELOADER)
        page.wait_visability_element(element=TagsLocators.ADD_BUTTON)

        page.click_element(element=TagsLocators.ADD_BUTTON)

        page.wait_visability_element(element=Notifications.RED_NOTIFI)
        element_text = page.get_text_element(element=Notifications.RED_NOTIFI)
        page.compare_text(element_text=element_text, message=LicenseVerif.LICENSE_LIMIT_TAGS)
        page.click_element(element=Notifications.RED_NOTIFI_CLOSE)

        page.open_url(url=url, api=KeywordsSetsData.PAGE)

        page.wait_not_visability_element(element=Notifications.PRELOADER)
        page.wait_visability_element(element=KeywordsSetsLocators.ADD_BUTTON)

        page.click_element(element=KeywordsSetsLocators.ADD_BUTTON)

        page.wait_visability_element(element=Notifications.RED_NOTIFI)
        element_text = page.get_text_element(element=Notifications.RED_NOTIFI)
        page.compare_text(element_text=element_text, message=LicenseVerif.LICENSE_LIMIT_KEYWORDS_SETS)
        page.click_element(element=Notifications.RED_NOTIFI_CLOSE)

        page.open_url(url=url, api=WatchListsData.PAGE)

        page.wait_not_visability_element(element=Notifications.PRELOADER)
        page.wait_visability_element(element=WatchListsLocators.ADD_BUTTON)

        page.click_element(element=WatchListsLocators.ADD_BUTTON)

        page.wait_visability_element(element=Notifications.RED_NOTIFI)
        element_text = page.get_text_element(element=Notifications.RED_NOTIFI)
        page.compare_text(element_text=element_text, message=LicenseVerif.LICENSE_LIMIT_KEYWORDS_WACHLISTS)
        page.click_element(element=Notifications.RED_NOTIFI_CLOSE)

        return page

    @allure.feature('License')
    @allure.title('Access check after expiration education license')
    @pytest.mark.noload
    @DUsers.logout_all_users()
    @DLicense.put_new_license(folder_name='5')
    @DUsers.login_logout_user(user_login=LoginData.SUPER_LOGIN, user_password=LoginData.SUPER_PASSWORD,
                              page_name='admin')
    def test_license_026(self, page, url):
        page.wait_visability_element(element=TopBars.DATA_BAR)
        page.wait_not_visability_element(element=Notifications.PRELOADER)

        page.check_name_of_tab(name_of_tab=AdminVerif.NAME_OF_TAB)

        page.open_url(url=url, api=LoadImagesData.PAGE)

        page.wait_not_visability_element(element=Notifications.PRELOADER)
        page.wait_visability_element(element=LoadImagesLocators.ADD_BUTTON)
        page.wait_element_is_clickable(element=LoadImagesLocators.ADD_BUTTON)

        page.click_element(element=LoadImagesLocators.ADD_BUTTON)

        page.wait_visability_element(element=Notifications.RED_NOTIFI)
        element_text = page.get_text_element(element=Notifications.RED_NOTIFI)
        page.compare_text(element_text=element_text, message=LicenseVerif.LICENSE_EXPIRATION)

        return page

    @allure.feature('License')
    @allure.title('Access denied check after expiration education license')
    @pytest.mark.noload
    @DUsers.logout_all_users()
    @DLicense.put_new_license(folder_name='12')
    def test_license_027(self, browser, url):
        page = AdminPage(browser)
        page.open_url(url=url)
        page.wait_visability_element(element=LoginLocators.LOGIN_FIELD)

        page.check_name_of_tab(name_of_tab=LoginVerif.NAME_OF_TAB)

        page.write_in_element(element=LoginLocators.LOGIN_FIELD, text=LoginData.SUPER_LOGIN)
        page.write_in_element(element=LoginLocators.PASSWORD_FIELD,
                              text=LoginData.SUPER_PASSWORD)
        page.click_element(element=LoginLocators.LOGIN_BUTTON)

        page.wait_visability_element(element=Notifications.RED_NOTIFI)
        element_text = page.get_text_element(element=Notifications.RED_NOTIFI)
        page.compare_text(element_text=element_text, message=LicenseVerif.LICENSE_EXPIRATION)

    @allure.feature('License')
    @allure.title('Clean monitor')
    @pytest.mark.noload
    @DUsers.logout_all_users()
    def test_z_clean_monitor(self, browser, url):
        pass
