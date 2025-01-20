import pytest

from tests.decorators import DTags, DUsers, DEntities
from locators import TopBars, Notifications, TagsLocators, MapLocators
from data import LoginData, TagsData
from verification import TagsVerif, WorkspaceVerif, FilesVerif, ContactsVerif, MapVerif
import allure


@pytest.mark.tags
@pytest.mark.noload
class TestTagsPage:

    @allure.feature('Tags page')
    @allure.title('Clean monitor')
    @DUsers.logout_all_users()
    @DEntities.delete_all_entities()
    def test_0_clean_monitor(self, browser, url):
        pass

    @allure.feature('Tags page')
    @allure.title('Create new tag')
    @DTags.delete_tag(tag_name=TagsData.TAG1)
    @DUsers.login_logout_user(user_login=LoginData.SUPER_LOGIN, user_password=LoginData.SUPER_PASSWORD,
                              page_name='tags')
    def test_tags_001(self, page, url):
        """https://knoxygen.atlassian.net/wiki/spaces/WA/pages/3775956062/Auto+Tags.001"""
        page.wait_visability_element(element=TopBars.DATA_BAR)

        page.open_url(url=url, api=TagsData.PAGE)
        page.wait_not_visability_element(element=Notifications.PRELOADER)

        page.wait_visability_element(element=TagsLocators.ADD_BUTTON)

        counter = page.find_element(element=TagsLocators.COUNTER)
        first_counter = page.get_counter(element=counter)

        page.click_element(element=TagsLocators.ADD_BUTTON)

        page.write_in_element(element=TagsLocators.TAG_NAME,
                              text=TagsData.TAG1)

        page.click_element(element=TagsLocators.FINAL_ADD)

        page.wait_visability_element(element=Notifications.BLUE_NOTIFI)
        element_text = page.get_text_element(element=Notifications.BLUE_NOTIFI)

        page.compare_text(element_text=element_text, message=TagsVerif.ADDED_TAG)
        page.click_element(element=Notifications.NOTIFI_CLOSE)

        counter = page.find_element(element=TagsLocators.COUNTER)
        second_counter = page.get_counter(element=counter)
        page.check_counter_plus(first_counter=first_counter, second_counter=second_counter)

        page.write_in_element(element=TagsLocators.SEARCH, text=TagsData.TAG1)
        page.press_enter()
        page.wait_visability_element(TagsLocators.GRID_TAG)

        element_text = page.get_text_element(element=TagsLocators.GRID_TAG)
        page.compare_text(element_text=element_text, message=TagsVerif.TAG1)

        return page

    @allure.feature('Tags page')
    @allure.title('Change tag')
    @DTags.add_delete_tag(tag_name=TagsData.TAG1)
    @DUsers.login_logout_user(user_login=LoginData.SUPER_LOGIN, user_password=LoginData.SUPER_PASSWORD,
                              page_name='tags')
    def test_tags_002(self, page, url):
        """https://knoxygen.atlassian.net/wiki/spaces/WA/pages/3775956073/Auto+Tags.002"""
        page.wait_visability_element(element=TopBars.DATA_BAR)

        page.open_url(url=url, api=TagsData.PAGE)
        page.wait_not_visability_element(element=Notifications.PRELOADER)

        page.wait_visability_element(element=TagsLocators.SEARCH)
        page.write_in_element(element=TagsLocators.SEARCH, text=TagsData.TAG1)
        page.press_enter()
        page.wait_visability_element(TagsLocators.GRID_TAG)

        page.wait_visability_element(element=TagsLocators.RIGHT_SIDEBAR_EDIT_BUTTON)
        page.click_element(element=TagsLocators.RIGHT_SIDEBAR_EDIT_BUTTON)

        page.clear_element(element=TagsLocators.TAG_NAME)
        page.write_in_element(element=TagsLocators.TAG_NAME,
                              text=TagsData.TAG2)

        page.click_element(element=TagsLocators.FINAL_ADD)

        page.wait_visability_element(element=Notifications.BLUE_NOTIFI)
        element_text = page.get_text_element(element=Notifications.BLUE_NOTIFI)

        page.compare_text(element_text=element_text, message=TagsVerif.SAVE_CHANGES)
        page.click_element(element=Notifications.NOTIFI_CLOSE)

        page.wait_visability_element(element=TagsLocators.SEARCH)
        page.write_in_element(element=TagsLocators.SEARCH, text=TagsData.TAG2)
        page.press_enter()
        page.wait_visability_element(TagsLocators.GRID_TAG)

        element_text = page.get_text_element(element=TagsLocators.RIGHT_SIDEBAR_TAG_NAME)
        page.compare_text(element_text=element_text, message=TagsVerif.TAG2)

        element_text = page.get_text_element(element=TagsLocators.GRID_TAG)
        page.compare_text(element_text=element_text, message=TagsVerif.TAG2)

        return page

    @allure.feature('Tags page')
    @allure.title('Delete tag')
    @DTags.add_delete_tag(tag_name=TagsData.TAG1)
    @DUsers.login_logout_user(user_login=LoginData.SUPER_LOGIN, user_password=LoginData.SUPER_PASSWORD,
                              page_name='tags')
    def test_tags_003(self, page, url):
        """https://knoxygen.atlassian.net/wiki/spaces/WA/pages/3775956084/Auto+Tags.003"""
        page.wait_visability_element(element=TopBars.DATA_BAR)

        page.open_url(url=url, api=TagsData.PAGE)
        page.wait_not_visability_element(element=Notifications.PRELOADER)

        page.wait_visability_element(element=TagsLocators.ADD_BUTTON)
        page.write_in_element(element=TagsLocators.SEARCH, text=TagsData.TAG1)
        page.press_enter()
        page.wait_visability_element(TagsLocators.GRID_TAG)

        page.hover_on_element(element=TagsLocators.GRID_TAG)
        page.hover_on_element(element=TagsLocators.BASKET)
        page.click_element(element=TagsLocators.BASKET)

        page.wait_visability_element(element=TagsLocators.BASKET_MESSAGE)
        page.click_element(element=TagsLocators.BASKET_YES_BUTTON)

        page.wait_visability_element(element=Notifications.BLUE_NOTIFI)
        element_text = page.get_text_element(element=Notifications.BLUE_NOTIFI)

        page.compare_text(element_text=element_text, message=TagsVerif.FINAL_DELETE_MESSAGE)
        page.click_element(element=Notifications.NOTIFI_CLOSE)

        return page

    @allure.feature('Tags page')
    @allure.title('Open on the page')
    @pytest.mark.parametrize('param', [(TagsLocators.WORKSPACE, WorkspaceVerif.NAME_OF_TAB),
                                       (TagsLocators.FILES, FilesVerif.NAME_OF_TAB),
                                       (TagsLocators.CONTACTS, ContactsVerif.NAME_OF_TAB),
                                       (TagsLocators.MAP, MapVerif.NAME_OF_TAB)
                                       ])
    @DUsers.login_logout_user_param(user_login=LoginData.SUPER_LOGIN, user_password=LoginData.SUPER_PASSWORD,
                                    page_name='tags')
    def test_tags_004(self, page, url, param):
        """https://knoxygen.atlassian.net/wiki/spaces/WA/pages/3775956095/Auto+Tags.004"""
        page.wait_visability_element(element=TopBars.DATA_BAR)

        page.open_url(url=url, api=TagsData.PAGE)
        page.wait_not_visability_element(element=Notifications.PRELOADER)

        page.wait_visability_element(element=TagsLocators.ADD_BUTTON)

        page.write_in_element(element=TagsLocators.SEARCH, text=TagsData.TAG_CARDS)
        page.press_enter()
        page.wait_visability_element(TagsLocators.GRID_TAG)

        page.click_element(element=TagsLocators.OPEN_BUTTON)

        page.wait_visability_element(element=param[0])
        page.click_element(element=param[0])

        page.wait_not_visability_element(element=Notifications.PRELOADER)

        if param[0] == TagsLocators.MAP:
            page.wait_visability_element(element=MapLocators.COUNTER)

        page.wait_visability_element(element=TopBars.DATA_BAR)
        page.check_name_of_tab(name_of_tab=param[1])

        return page

    @allure.feature('Tags page')
    @allure.title('Open on the page in new tab')
    @pytest.mark.parametrize('param', [(TagsLocators.WORKSPACE_TAB, WorkspaceVerif.NAME_OF_TAB),
                                       (TagsLocators.FILES_TAB, FilesVerif.NAME_OF_TAB),
                                       (TagsLocators.CONTACTS_TAB, ContactsVerif.NAME_OF_TAB),
                                       (TagsLocators.MAP_TAB, MapVerif.NAME_OF_TAB)
                                       ])
    @DUsers.login_logout_user_param(user_login=LoginData.SUPER_LOGIN, user_password=LoginData.SUPER_PASSWORD,
                                    page_name='tags')
    def test_tags_005(self, page, url, param):
        """https://knoxygen.atlassian.net/wiki/spaces/WA/pages/3775956128/Auto+Tags.005"""
        page.wait_visability_element(element=TopBars.DATA_BAR)

        page.open_url(url=url, api=TagsData.PAGE)
        page.wait_not_visability_element(element=Notifications.PRELOADER)

        page.wait_visability_element(element=TagsLocators.ADD_BUTTON)

        page.write_in_element(element=TagsLocators.SEARCH, text=TagsData.TAG_CARDS)
        page.press_enter()
        page.wait_visability_element(TagsLocators.GRID_TAG)

        page.click_element(element=TagsLocators.OPEN_BUTTON)

        page.wait_visability_element(element=param[0])
        page.click_element(element=param[0])

        browser_tabs = page.get_all_tabs()
        page.select_tab_number(2, browser_tabs)

        page.wait_visability_element(element=TopBars.DATA_BAR)
        page.check_name_of_tab(name_of_tab=param[1])

        return page

    @allure.feature('Tags page')
    @allure.title('Clean monitor')
    @DUsers.logout_all_users()
    def test_z_clean_monitor(self, browser, url):
        pass
