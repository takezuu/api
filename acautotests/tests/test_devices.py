import time

import allure
import pytest

from data import LoadImagesData, STAND_PATH, DevicesData, LoginData
from locators import TopBars, LoadImagesLocators, Notifications, DevicesLocators
from tests.decorators import DUsers, DEntities
from verification import LoadImagesVerif, DevicesVerif


@pytest.mark.devices
@pytest.mark.noload
class TestDevicesPage:

    @allure.feature('Devices page')
    @allure.title('Clean monitor')
    @DUsers.logout_all_users()
    @DEntities.delete_all_entities()
    @DUsers.login_logout_user(user_login=LoginData.SUPER_LOGIN, user_password=LoginData.SUPER_PASSWORD,
                              page_name='load_images')
    def test_0_clean_monitor(self, page, url):
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

    @allure.feature('Devices page')
    @allure.title('Edit device')
    @DUsers.logout_all_users()
    @DUsers.login_logout_user(user_login=LoginData.SUPER_LOGIN, user_password=LoginData.SUPER_PASSWORD,
                              page_name='devices')
    def test_devices_001(self, page, url):
        """https://knoxygen.atlassian.net/wiki/spaces/WA/pages/3775955137/Auto+Devices.001"""
        page.wait_not_visability_element(element=Notifications.PRELOADER)

        page.open_url(url=url, api=DevicesData.PAGE)

        page.wait_not_visability_element(element=Notifications.PRELOADER)
        page.wait_visability_element(element=DevicesLocators.OPEN_BUTTON)
        page.wait_element_is_clickable(element=DevicesLocators.OPEN_BUTTON)
        page.get_browser_screenshot()
        page.write_in_element(element=DevicesLocators.SEARCH, text=DevicesData.DEVICE)
        page.press_enter()

        page.wait_visability_element(element=DevicesLocators.GRID_DEVICE_NAME)

        page.click_element(element=DevicesLocators.EDIT_ACCEPT_BUTTON)

        page.wait_visability_element(element=DevicesLocators.RIGHT_SIDEBAR_DEVICE_NAME_INPUT)
        page.clear_element(element=DevicesLocators.RIGHT_SIDEBAR_DEVICE_NAME_INPUT)

        page.write_in_element(element=DevicesLocators.RIGHT_SIDEBAR_DEVICE_NAME_INPUT, text=DevicesData.DEVICE_NAME)

        page.click_element(element=DevicesLocators.EDIT_ACCEPT_BUTTON)

        page.wait_visability_element(element=Notifications.BLUE_NOTIFI)
        element_text = page.get_text_element(element=Notifications.BLUE_NOTIFI)
        page.compare_text(element_text=element_text, message=DevicesVerif.ALIAS_SAVED)
        page.click_element(element=Notifications.NOTIFI_CLOSE)

        page.write_in_element(element=DevicesLocators.SEARCH, text=DevicesData.DEVICE_NAME)
        page.press_enter()

        page.wait_visability_element(element=DevicesLocators.GRID_DEVICE_NAME)

        grid_name = page.get_text_element(element=DevicesLocators.GRID_DEVICE_NAME)
        right_sidebar_name = page.get_text_element(element=DevicesLocators.RIGHT_SIDEBAR_DEVICE_NAME)

        page.compare_text(elment=grid_name, message=DevicesVerif.DEVICE_NAME)
        page.compare_text(element=right_sidebar_name, message=DevicesVerif.DEVICE_NAME)

        return page
