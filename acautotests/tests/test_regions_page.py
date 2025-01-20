import pytest

from tests.decorators import DRegions, DCases, DUsers, DEntities
from locators import TopBars, Notifications, RegionsLocators, \
    CasesLocators
from data import LoginData, RegionsData, CasesData
from verification import RegionsVerif, CasesVerif
import allure


@pytest.mark.regions
@pytest.mark.noload
class TestRegionsPage:

    @allure.feature('Regions page')
    @allure.title('Clean monitor')
    @DUsers.logout_all_users()
    @DEntities.delete_all_entities()
    def test_0_clean_monitor(self, browser, url):
        pass

    @allure.feature('Regions page')
    @allure.title('Create new region')
    @DRegions.delete_region(region_name=RegionsData.REG1)
    @DUsers.login_logout_user(user_login=LoginData.SUPER_LOGIN, user_password=LoginData.SUPER_PASSWORD,
                              page_name='regions')
    def test_regions_001(self, page, url):
        """https://knoxygen.atlassian.net/wiki/spaces/WA/pages/3775955315/Auto+Regions.001"""
        page.wait_visability_element(element=TopBars.DATA_BAR)

        page.open_url(url=url, api=RegionsData.PAGE)
        page.wait_not_visability_element(element=Notifications.PRELOADER)

        page.wait_visability_element(element=RegionsLocators.ADD_BUTTON)

        counter = page.find_element(element=RegionsLocators.COUNTER)
        first_counter = page.get_counter(element=counter)

        page.click_element(element=RegionsLocators.ADD_BUTTON)

        page.write_in_element(element=RegionsLocators.REGION_NAME, text=RegionsData.REG1)

        page.click_element(element=RegionsLocators.FINAL_ADD)

        page.wait_visability_element(element=Notifications.BLUE_NOTIFI)
        element_text = page.get_text_element(element=Notifications.BLUE_NOTIFI)
        page.compare_text(element_text=element_text, message=RegionsVerif.ADDED_REGION)
        page.click_element(element=Notifications.NOTIFI_CLOSE)

        counter = page.find_element(element=RegionsLocators.COUNTER)
        second_counter = page.get_counter(element=counter)
        page.check_counter_plus(first_counter=first_counter, second_counter=second_counter)

        page.write_in_element(element=RegionsLocators.SEARCH, text=RegionsData.REG1)
        page.press_enter()
        page.wait_visability_element(RegionsLocators.GRID_REGION)

        element_text = page.get_text_element(element=RegionsLocators.GRID_REGION)
        page.compare_text(element_text=element_text, message=RegionsVerif.REG1)

        return page

    @allure.feature('Regions page')
    @allure.title('Create new region and attach to case')
    @DRegions.add_delete_region(region_name=RegionsData.REG1)
    @DCases.add_delete_case(case_name=CasesData.CASE)
    @DUsers.login_logout_user(user_login=LoginData.SUPER_LOGIN, user_password=LoginData.SUPER_PASSWORD,
                              page_name='regions')
    def test_regions_002(self, page, url):
        """https://knoxygen.atlassian.net/wiki/spaces/WA/pages/3775955326/Auto+Regions.002"""
        page.wait_visability_element(element=TopBars.DATA_BAR)

        page.open_url(url=url, api=RegionsData.PAGE)
        page.wait_not_visability_element(element=Notifications.PRELOADER)

        page.wait_visability_element(element=RegionsLocators.ADD_BUTTON)

        element = page.find_element(element=RegionsLocators.RIGHT_SIDEBAR_COUNTER)
        element_text = page.get_counter(element=element)
        page.compare_text(element_text=element_text, message=RegionsVerif.ZERO_COUNT)

        element_text = page.get_text_element(element=RegionsLocators.RIGHT_SIDEBAR_NOCASES)
        page.compare_text(element_text=element_text, message=RegionsVerif.NOCASES)

        page.open_url(url=url, api=CasesData.PAGE)
        page.wait_not_visability_element(element=Notifications.PRELOADER)

        page.wait_visability_element(element=CasesLocators.RIGHT_SIDEBAR_EDIT_BUTTON)
        page.click_element(element=CasesLocators.RIGHT_SIDEBAR_EDIT_BUTTON)

        page.wait_visability_element(element=CasesLocators.ADD_SECTION)
        page.click_element(element=CasesLocators.REGIONS_DROPDOWN)

        page.wait_visability_element(element=CasesLocators.REGION_1ST)
        page.click_element(element=CasesLocators.REGION_1ST)

        page.click_element(element=CasesLocators.FINAL_ADD)

        page.wait_visability_element(element=Notifications.BLUE_NOTIFI)
        element_text = page.get_text_element(element=Notifications.BLUE_NOTIFI)
        page.compare_text(element_text=element_text, message=CasesVerif.SAVE_CHANGES)
        page.click_element(element=Notifications.NOTIFI_CLOSE)

        page.wait_visability_element(element=Notifications.BLUE_NOTIFI)
        page.click_element(element=Notifications.NOTIFI_CLOSE)

        page.wait_visability_element(element=Notifications.BLUE_NOTIFI)
        page.click_element(element=Notifications.NOTIFI_CLOSE)

        page.open_url(url=url, api=RegionsData.PAGE)
        page.wait_not_visability_element(element=Notifications.PRELOADER)

        page.wait_visability_element(element=TopBars.DATA_BAR)

        page.check_name_of_tab(name_of_tab=RegionsVerif.NAME_OF_TAB)

        page.wait_visability_element(element=RegionsLocators.RIGHT_SIDEBAR_COUNTER)
        element = page.find_element(element=RegionsLocators.RIGHT_SIDEBAR_COUNTER)
        element_text = page.get_counter(element=element)
        page.compare_text(element_text=element_text, message=RegionsVerif.HAVE_CASE)

        element_text = page.get_text_element(element=RegionsLocators.RIGHT_SIDEBAR_NOCASES)
        page.compare_text(element_text=element_text, message=CasesVerif.CASE)

        return page

    @allure.feature('Regions page')
    @allure.title('Change region')
    @DRegions.add_delete_region(region_name=RegionsData.REG1)
    @DCases.add_delete_case(case_name=CasesData.CASE)
    @DUsers.login_logout_user(user_login=LoginData.SUPER_LOGIN, user_password=LoginData.SUPER_PASSWORD,
                              page_name='regions')
    def test_regions_003(self, page, url):
        """https://knoxygen.atlassian.net/wiki/spaces/WA/pages/3775955337/Auto+Regions.003"""
        page.wait_visability_element(element=TopBars.DATA_BAR)

        page.open_url(url=url, api=CasesData.PAGE)
        page.wait_not_visability_element(element=Notifications.PRELOADER)

        page.wait_visability_element(element=CasesLocators.RIGHT_SIDEBAR_EDIT_BUTTON)
        page.click_element(element=CasesLocators.RIGHT_SIDEBAR_EDIT_BUTTON)

        page.wait_visability_element(element=CasesLocators.ADD_SECTION)
        page.click_element(element=CasesLocators.REGIONS_DROPDOWN)
        page.wait_visability_element(element=CasesLocators.REGION_1ST)
        page.click_element(element=CasesLocators.REGION_1ST)
        page.click_element(element=CasesLocators.FINAL_ADD)

        page.open_url(url=url, api=RegionsData.PAGE)
        page.wait_not_visability_element(element=Notifications.PRELOADER)

        page.wait_visability_element(element=RegionsLocators.RIGHT_SIDEBAR_EDIT_BUTTON)
        page.click_element(element=RegionsLocators.RIGHT_SIDEBAR_EDIT_BUTTON)

        page.clear_element(element=RegionsLocators.REGION_NAME)
        page.write_in_element(element=RegionsLocators.REGION_NAME, text=RegionsData.REG2)

        page.click_element(element=RegionsLocators.FINAL_ADD)

        page.wait_visability_element(element=Notifications.BLUE_NOTIFI)
        element_text = page.get_text_element(element=Notifications.BLUE_NOTIFI)
        page.compare_text(element_text=element_text, message=RegionsVerif.SAVE_CHANGES)
        page.click_element(element=Notifications.NOTIFI_CLOSE)

        element_text = page.get_text_element(element=RegionsLocators.RIGHT_SIDEBAR_REGION_NAME)
        page.compare_text(element_text=element_text, message=RegionsVerif.REG2)

        element_text = page.get_text_element(element=RegionsLocators.GRID_REGION)
        page.compare_text(element_text=element_text, message=RegionsVerif.REG2)

        page.open_url(url=url, api=CasesData.PAGE)
        page.wait_not_visability_element(element=Notifications.PRELOADER)

        page.wait_visability_element(element=CasesLocators.RIGHT_SIDEBAR_EDIT_BUTTON)
        page.click_element(element=CasesLocators.RIGHT_SIDEBAR_EDIT_BUTTON)

        page.wait_visability_element(element=CasesLocators.ADD_SECTION)
        page.click_element(element=CasesLocators.REGIONS_DROPDOWN)

        page.wait_visability_element(element=CasesLocators.REGION_1ST)
        element_text = page.get_text_element(element=CasesLocators.REGION_1ST)

        page.compare_text(element_text=element_text, message=RegionsVerif.REG2)

        page.click_element(element=CasesLocators.CANCEL_BUTTON)

        return page

    @allure.feature('Regions page')
    @allure.title('Delete region')
    @DRegions.add_delete_region(region_name=RegionsData.REG1)
    @DUsers.login_logout_user(user_login=LoginData.SUPER_LOGIN, user_password=LoginData.SUPER_PASSWORD,
                              page_name='regions')
    def test_regions_004(self, page, url):
        """https://knoxygen.atlassian.net/wiki/spaces/WA/pages/3775955348/Auto+Regions.004"""
        page.wait_visability_element(element=TopBars.DATA_BAR)

        page.open_url(url=url, api=RegionsData.PAGE)
        page.wait_not_visability_element(element=Notifications.PRELOADER)

        page.wait_visability_element(element=RegionsLocators.ADD_BUTTON)

        page.hover_on_element(element=RegionsLocators.GRID_REGION)
        page.hover_on_element(element=RegionsLocators.BASKET)
        page.click_element(element=RegionsLocators.BASKET)

        page.wait_visability_element(element=RegionsLocators.BASKET_MESSAGE)
        page.click_element(element=RegionsLocators.BASKET_YES_BUTTON)

        page.wait_visability_element(element=Notifications.BLUE_NOTIFI)
        element_text = page.get_text_element(element=Notifications.BLUE_NOTIFI)
        page.compare_text(element_text=element_text, message=RegionsVerif.FINAL_DELETE_MESSAGE)
        page.click_element(element=Notifications.NOTIFI_CLOSE)

        return page

    @allure.feature('Regions page')
    @allure.title('Clean monitor')
    @DUsers.logout_all_users()
    def test_z_clean_monitor(self, browser, url):
        pass
