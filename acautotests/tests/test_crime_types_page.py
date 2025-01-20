import pytest

from tests.decorators import DCrimetypes, DCases, DUsers, DEntities
from locators import TopBars, Notifications, CrimeTypesLocators, \
    CasesLocators
from data import LoginData, CasesData, CrimeTypesData
from verification import CasesVerif, CrimeTypesVerif
import allure


@pytest.mark.crime_types
@pytest.mark.noload
class TestCrimeTypesPage:

    @allure.feature('Crime types page')
    @allure.title('Clean monitor')
    @DUsers.logout_all_users()
    @DEntities.delete_all_entities()
    def test_0_clean_monitor(self, browser, url):
        pass

    @allure.feature('Crime types page')
    @allure.title('Create new crime type')
    @DCrimetypes.delete_crime_type(crime_type_name=CrimeTypesData.CRIME1)
    @DUsers.login_logout_user(user_login=LoginData.SUPER_LOGIN, user_password=LoginData.SUPER_PASSWORD,
                              page_name='crimetypes')
    def test_crime_types_001(self, page, url):
        """https://knoxygen.atlassian.net/wiki/spaces/WA/pages/3775955383/Auto+Incidents.001"""
        page.wait_visability_element(element=TopBars.DATA_BAR)

        page.open_url(url=url, api=CrimeTypesData.PAGE)
        page.wait_not_visability_element(element=Notifications.PRELOADER)

        page.wait_visability_element(element=CrimeTypesLocators.ADD_BUTTON)

        counter = page.find_element(element=CrimeTypesLocators.COUNTER)
        first_counter = page.get_counter(element=counter, n=1)

        page.click_element(element=CrimeTypesLocators.ADD_BUTTON)

        page.write_in_element(element=CrimeTypesLocators.CRIME_TYPE_NAME,
                              text=CrimeTypesData.CRIME1)

        page.click_element(element=CrimeTypesLocators.FINAL_ADD)

        page.wait_visability_element(element=Notifications.BLUE_NOTIFI)
        element_text = page.get_text_element(element=Notifications.BLUE_NOTIFI)
        page.compare_text(element_text=element_text, message=CrimeTypesVerif.ADDED_CRIME_TYPE)
        page.click_element(element=Notifications.NOTIFI_CLOSE)

        counter = page.find_element(element=CrimeTypesLocators.COUNTER)
        second_counter = page.get_counter(element=counter, n=1)
        page.check_counter_plus(first_counter=first_counter, second_counter=second_counter)

        page.write_in_element(element=CrimeTypesLocators.SEARCH, text=CrimeTypesData.CRIME1)
        page.press_enter()
        page.wait_visability_element(CrimeTypesLocators.GRID_CRIME_TYPE)

        element_text = page.get_text_element(element=CrimeTypesLocators.GRID_CRIME_TYPE)
        page.compare_text(element_text=element_text, message=CrimeTypesVerif.CRIME1)

        return page

    @allure.feature('Crime types page')
    @allure.title('Create new crime type and attach to case')
    @DCrimetypes.add_delete_crime_type(crime_type_name=CrimeTypesData.CRIME1)
    @DCases.add_delete_case(case_name=CasesData.CASE)
    @DUsers.login_logout_user(user_login=LoginData.SUPER_LOGIN, user_password=LoginData.SUPER_PASSWORD,
                              page_name='crimetypes')
    def test_crime_types_002(self, page, url):
        """https://knoxygen.atlassian.net/wiki/spaces/WA/pages/3775955394/Auto+Incidents.002"""
        page.wait_visability_element(element=TopBars.DATA_BAR)

        page.open_url(url=url, api=CrimeTypesData.PAGE)

        page.wait_visability_element(element=CrimeTypesLocators.ADD_BUTTON)
        page.wait_not_visability_element(element=Notifications.PRELOADER)

        element = page.find_element(element=CrimeTypesLocators.RIGHT_SIDEBAR_COUNTER)
        element_text = page.get_counter(element=element)
        page.compare_text(element_text=element_text, message=CrimeTypesVerif.ZERO_COUNT)

        element_text = page.get_text_element(element=CrimeTypesLocators.RIGHT_SIDEBAR_NOCASES)
        page.compare_text(element_text=element_text, message=CrimeTypesVerif.NOCASES)

        page.open_url(url=url, api=CasesData.PAGE)
        page.wait_not_visability_element(element=Notifications.PRELOADER)

        page.wait_visability_element(element=CasesLocators.RIGHT_SIDEBAR_EDIT_BUTTON)
        page.click_element(element=CasesLocators.RIGHT_SIDEBAR_EDIT_BUTTON)

        page.wait_visability_element(element=CasesLocators.ADD_SECTION)
        page.click_element(element=CasesLocators.CRIME_TYPES_DROPDOWN)

        page.wait_visability_element(element=CasesLocators.CRIME_1ST)
        page.click_element(element=CasesLocators.CRIME_1ST)

        page.click_element(element=CasesLocators.FINAL_ADD)

        page.wait_visability_element(element=Notifications.BLUE_NOTIFI)
        element_text = page.get_text_element(element=Notifications.BLUE_NOTIFI)
        page.compare_text(element_text=element_text, message=CasesVerif.SAVE_CHANGES)
        page.click_element(element=Notifications.NOTIFI_CLOSE)

        page.wait_visability_element(element=Notifications.BLUE_NOTIFI)
        page.click_element(element=Notifications.NOTIFI_CLOSE)

        page.wait_visability_element(element=Notifications.BLUE_NOTIFI)
        page.click_element(element=Notifications.NOTIFI_CLOSE)

        page.open_url(url=url, api=CrimeTypesData.PAGE)
        page.wait_not_visability_element(element=Notifications.PRELOADER)

        page.wait_visability_element(element=TopBars.DATA_BAR)

        page.check_name_of_tab(name_of_tab=CrimeTypesVerif.NAME_OF_TAB)

        page.wait_visability_element(element=CrimeTypesLocators.RIGHT_SIDEBAR_COUNTER)
        element = page.find_element(element=CrimeTypesLocators.RIGHT_SIDEBAR_COUNTER)
        element_text = page.get_counter(element=element)
        page.compare_text(element_text=element_text, message=CrimeTypesVerif.HAVE_CASE)

        element_text = page.get_text_element(element=CrimeTypesLocators.RIGHT_SIDEBAR_NOCASES)
        page.compare_text(element_text=element_text, message=CasesVerif.CASE)

        return page

    @allure.feature('Crime types page')
    @allure.title('Change crime type')
    @DCrimetypes.add_delete_crime_type(crime_type_name=CrimeTypesData.CRIME1)
    @DCases.add_delete_case(case_name=CasesData.CASE)
    @DUsers.login_logout_user(user_login=LoginData.SUPER_LOGIN, user_password=LoginData.SUPER_PASSWORD,
                              page_name='crimetypes')
    def test_crime_types_003(self, page, url):
        """https://knoxygen.atlassian.net/wiki/spaces/WA/pages/3775955405/Auto+Incidents.003"""
        page.wait_visability_element(element=TopBars.DATA_BAR)

        page.open_url(url=url, api=CasesData.PAGE)
        page.wait_not_visability_element(element=Notifications.PRELOADER)

        page.wait_visability_element(element=CasesLocators.RIGHT_SIDEBAR_EDIT_BUTTON)
        page.click_element(element=CasesLocators.RIGHT_SIDEBAR_EDIT_BUTTON)

        page.wait_visability_element(element=CasesLocators.ADD_SECTION)
        page.click_element(element=CasesLocators.CRIME_TYPES_DROPDOWN)
        page.wait_visability_element(element=CasesLocators.CRIME_1ST)
        page.click_element(element=CasesLocators.CRIME_1ST)
        page.click_element(element=CasesLocators.FINAL_ADD)

        page.open_url(url=url, api=CrimeTypesData.PAGE)
        page.wait_not_visability_element(element=Notifications.PRELOADER)

        page.wait_visability_element(element=CrimeTypesLocators.RIGHT_SIDEBAR_EDIT_BUTTON)
        page.click_element(element=CrimeTypesLocators.RIGHT_SIDEBAR_EDIT_BUTTON)

        page.clear_element(element=CrimeTypesLocators.CRIME_TYPE_NAME)
        page.write_in_element(element=CrimeTypesLocators.CRIME_TYPE_NAME,
                              text=CrimeTypesData.CRIME2)

        page.click_element(element=CrimeTypesLocators.FINAL_ADD)

        page.wait_visability_element(element=Notifications.BLUE_NOTIFI)
        element_text = page.get_text_element(element=Notifications.BLUE_NOTIFI)
        page.compare_text(element_text=element_text, message=CrimeTypesVerif.SAVE_CHANGES)
        page.click_element(element=Notifications.NOTIFI_CLOSE)

        element_text = page.get_text_element(element=CrimeTypesLocators.RIGHT_SIDEBAR_CRIME_TYPE_NAME)
        page.compare_text(element_text=element_text, message=CrimeTypesVerif.CRIME2)

        element_text = page.get_text_element(element=CrimeTypesLocators.GRID_CRIME_TYPE)
        page.compare_text(element_text=element_text, message=CrimeTypesVerif.CRIME2)

        page.open_url(url=url, api=CasesData.PAGE)
        page.wait_not_visability_element(element=Notifications.PRELOADER)

        page.wait_visability_element(element=CasesLocators.RIGHT_SIDEBAR_EDIT_BUTTON)
        page.click_element(element=CasesLocators.RIGHT_SIDEBAR_EDIT_BUTTON)

        page.wait_visability_element(element=CasesLocators.ADD_SECTION)
        page.click_element(element=CasesLocators.CRIME_TYPES_DROPDOWN)

        page.wait_visability_element(element=CasesLocators.CRIME_1ST)
        element_text = page.get_text_element(element=CasesLocators.CRIME_1ST)

        page.compare_text(element_text=element_text, message=CrimeTypesVerif.CRIME2)

        page.click_element(element=CasesLocators.CANCEL_BUTTON)

        return page

    @allure.feature('Crime types page')
    @allure.title('Delete crime type')
    @DCrimetypes.add_delete_crime_type(crime_type_name=CrimeTypesData.CRIME1)
    @DUsers.login_logout_user(user_login=LoginData.SUPER_LOGIN, user_password=LoginData.SUPER_PASSWORD,
                              page_name='crimetypes')
    def test_crime_types_004(self, page, url):
        """https://knoxygen.atlassian.net/wiki/spaces/WA/pages/3775955416/Auto+Incidents.004"""
        page.wait_visability_element(element=TopBars.DATA_BAR)

        page.open_url(url=url, api=CrimeTypesData.PAGE)
        page.wait_not_visability_element(element=Notifications.PRELOADER)

        page.wait_visability_element(element=CrimeTypesLocators.ADD_BUTTON)

        page.hover_on_element(element=CrimeTypesLocators.GRID_CRIME_TYPE)
        page.hover_on_element(element=CrimeTypesLocators.BASKET)
        page.click_element(element=CrimeTypesLocators.BASKET)

        page.wait_visability_element(element=CrimeTypesLocators.BASKET_MESSAGE)
        page.click_element(element=CrimeTypesLocators.BASKET_YES_BUTTON)

        page.wait_visability_element(element=Notifications.BLUE_NOTIFI)
        element_text = page.get_text_element(element=Notifications.BLUE_NOTIFI)
        page.compare_text(element_text=element_text, message=CrimeTypesVerif.FINAL_DELETE_MESSAGE)
        page.click_element(element=Notifications.NOTIFI_CLOSE)

        return page

    @allure.feature('Crime types page')
    @allure.title('Clean monitor')
    @DUsers.logout_all_users()
    def test_z_clean_monitor(self, browser, url):
        pass
