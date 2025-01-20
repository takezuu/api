import time
import pytest

from tests.decorators import DKeywordSets, DUsers, DEntities
from locators import TopBars, Notifications, KeywordsSetsLocators, WorkspaceLocators, FilesLocators, ContactsLocators
from data import LoginData, KeywordsSetsData, STAND_PATH_KEYWORDS_SETS, WorkspaceData
from verification import KeywordsSetsVerif, WorkspaceVerif, FilesVerif, ContactsVerif
import allure


@pytest.mark.keywords_sets
@pytest.mark.noload
class TestKeywordsSetsPage:

    @allure.feature('Keywords sets page')
    @allure.title('Clean monitor')
    @DUsers.logout_all_users()
    @DEntities.delete_all_entities()
    def test_0_clean_monitor(self, browser, url):
        pass

    @allure.feature('Keywords sets page')
    @allure.title('Create new empty keyword set with different types')
    @pytest.mark.parametrize('param', [(KeywordsSetsData.EMPTY, KeywordsSetsVerif.EMPTY,
                                        KeywordsSetsData.TYPE_ALL_PAGES, KeywordsSetsVerif.STR_TYPE_ALL_PAGES),
                                       (KeywordsSetsData.EMPTY, KeywordsSetsVerif.EMPTY,
                                        KeywordsSetsData.TYPE_FILES, KeywordsSetsVerif.STR_TYPE_FILES),
                                       (KeywordsSetsData.EMPTY, KeywordsSetsVerif.EMPTY,
                                        KeywordsSetsData.TYPE_WRKSPACE_CONTACTS_MAP,
                                        KeywordsSetsVerif.STR_TYPE_WRKSPACE_CONTACTS)
                                       ])
    @DUsers.login_logout_user_param(user_login=LoginData.SUPER_LOGIN, user_password=LoginData.SUPER_PASSWORD,
                                    page_name='keywords_sets')
    @DKeywordSets.delete_keyword_set_param()
    def test_keywords_sets_001(self, page, url, param):
        """https://knoxygen.atlassian.net/wiki/spaces/WA/pages/3775955816/Auto+Keywords+Sets.001"""
        page.wait_visability_element(element=TopBars.DATA_BAR)

        page.open_url(url=url, api=KeywordsSetsData.PAGE)
        page.wait_not_visability_element(element=Notifications.PRELOADER)

        page.wait_visability_element(element=KeywordsSetsLocators.ADD_BUTTON)

        counter = page.find_element(element=KeywordsSetsLocators.COUNTER)
        first_counter = page.get_counter(element=counter, n=2)

        page.click_element(element=KeywordsSetsLocators.ADD_BUTTON)
        page.wait_visability_element(element=KeywordsSetsLocators.KEYWORDSET_NAME)
        page.write_in_element(element=KeywordsSetsLocators.KEYWORDSET_NAME,
                              text=param[0])

        if param[2] != KeywordsSetsVerif.TYPE_WRKSPACE_CONTACTS:
            element = page.find_element(element=KeywordsSetsLocators.KEYWORDSET_TYPE)
            page.select_status(element=element, ind=param[2])

        page.click_element(element=KeywordsSetsLocators.FINAL_ADD)

        page.wait_visability_element(element=Notifications.BLUE_NOTIFI)
        element_text = page.get_text_element(element=Notifications.BLUE_NOTIFI)
        page.click_element(element=Notifications.NOTIFI_CLOSE)
        page.compare_text(element_text=element_text, message=KeywordsSetsVerif.ADDED_KEYWORD_SET)

        counter = page.find_element(element=KeywordsSetsLocators.COUNTER)
        second_counter = page.get_counter(element=counter, n=2)
        page.check_counter_plus(first_counter=first_counter, second_counter=second_counter)

        page.write_in_element(element=KeywordsSetsLocators.SEARCH, text=param[0])
        page.press_enter()
        page.wait_visability_element(KeywordsSetsLocators.GRID_KEYWORDSET)

        element_text = page.get_text_element(element=KeywordsSetsLocators.GRID_KEYWORDSET)
        page.compare_text(element_text=element_text, message=param[1])

        element_text = page.get_text_element(element=KeywordsSetsLocators.GRID_KEYWORDSET_TYPE)
        page.compare_text(element_text=element_text, message=param[3])

        element_text = page.get_text_element(element=KeywordsSetsLocators.KEYWORDSET_BADGE)
        page.compare_text(element_text=element_text, message=KeywordsSetsVerif.BADGE_EMPTY)

        element_text = page.get_text_element(
            element=KeywordsSetsLocators.RIGHT_SIDEBAR_KEYWORDSET_NAME)
        page.compare_text(element_text=element_text, message=param[1])

        element = page.find_element(element=KeywordsSetsLocators.RIGHT_SIDEBAR_COUNTER)
        element_text = page.get_counter(element)
        page.compare_text(element_text=element_text, message=KeywordsSetsVerif.ZERO_COUNT)

        element = page.find_element(element=KeywordsSetsLocators.RIGHT_SIDEBAR_EXPORT_BUTTON)
        page.check_disable_element(element=element)

        page.click_element(element=KeywordsSetsLocators.RIGHT_SIDEBAR_CONTENT_TAB)

        page.wait_visability_element(element=KeywordsSetsLocators.RIGHT_SIDEBAR_CONTENT_TAB_NODATA)
        element_text = page.get_text_element(
            element=KeywordsSetsLocators.RIGHT_SIDEBAR_CONTENT_TAB_NODATA)
        page.compare_text(element_text=element_text, message=KeywordsSetsVerif.NO_DATA)

        return page

    @allure.feature('Keywords sets page')
    @allure.title('Create new keyword set with different types')
    @pytest.mark.parametrize('param', [(KeywordsSetsData.TEST, KeywordsSetsVerif.TEST,
                                        KeywordsSetsData.TYPE_ALL_PAGES, KeywordsSetsVerif.STR_TYPE_ALL_PAGES),
                                       (KeywordsSetsData.TEST, KeywordsSetsVerif.TEST,
                                        KeywordsSetsData.TYPE_FILES, KeywordsSetsVerif.STR_TYPE_FILES),
                                       (KeywordsSetsData.TEST, KeywordsSetsVerif.TEST,
                                        KeywordsSetsData.TYPE_WRKSPACE_CONTACTS_MAP,
                                        KeywordsSetsVerif.STR_TYPE_WRKSPACE_CONTACTS)
                                       ])
    @DUsers.login_logout_user_param(user_login=LoginData.SUPER_LOGIN, user_password=LoginData.SUPER_PASSWORD,
                                    page_name='keywords_sets')
    @DKeywordSets.delete_keyword_set_param()
    def test_keywords_sets_002(self, page, url, param):
        """https://knoxygen.atlassian.net/wiki/spaces/WA/pages/3775955805/Auto+Keywords+Sets.002"""
        page.wait_visability_element(element=TopBars.DATA_BAR)

        page.open_url(url=url, api=KeywordsSetsData.PAGE)
        page.wait_not_visability_element(element=Notifications.PRELOADER)

        page.wait_visability_element(element=KeywordsSetsLocators.ADD_BUTTON)

        counter = page.find_element(element=KeywordsSetsLocators.COUNTER)
        first_counter = page.get_counter(element=counter, n=2)

        page.click_element(element=KeywordsSetsLocators.ADD_BUTTON)
        page.wait_visability_element(element=KeywordsSetsLocators.KEYWORDSET_NAME)
        page.write_in_element(element=KeywordsSetsLocators.KEYWORDSET_NAME,
                              text=param[0])

        if param[2] != KeywordsSetsVerif.TYPE_WRKSPACE_CONTACTS:
            element = page.find_element(element=KeywordsSetsLocators.KEYWORDSET_TYPE)
            page.select_status(element=element, ind=param[2])

        page.write_in_element(element=KeywordsSetsLocators.KEYWORDSET_ADD_WORD,
                              text=KeywordsSetsData.WEAPON)
        page.click_element(element=KeywordsSetsLocators.KEYWORDSET_ADD)

        page.write_in_element(element=KeywordsSetsLocators.KEYWORDSET_ADD_WORD,
                              text=KeywordsSetsData.PISTOLET)
        page.click_element(element=KeywordsSetsLocators.KEYWORDSET_ADD)

        page.click_element(element=KeywordsSetsLocators.FINAL_ADD)

        page.wait_visability_element(element=Notifications.BLUE_NOTIFI)
        element_text = page.get_text_element(element=Notifications.BLUE_NOTIFI)
        page.click_element(element=Notifications.NOTIFI_CLOSE)
        page.compare_text(element_text=element_text, message=KeywordsSetsVerif.ADDED_KEYWORD_SET)

        counter = page.find_element(element=KeywordsSetsLocators.COUNTER)
        second_counter = page.get_counter(element=counter, n=2)
        page.check_counter_plus(first_counter=first_counter, second_counter=second_counter)

        page.write_in_element(element=KeywordsSetsLocators.SEARCH, text=param[0])
        page.press_enter()
        page.wait_visability_element(KeywordsSetsLocators.GRID_KEYWORDSET)

        element_text = page.get_text_element(element=KeywordsSetsLocators.GRID_KEYWORDSET)
        page.compare_text(element_text=element_text, message=param[1])

        element_text = page.get_text_element(element=KeywordsSetsLocators.GRID_KEYWORDSET_TYPE)
        page.compare_text(element_text=element_text, message=param[3])

        element_text = page.get_text_element(element=KeywordsSetsLocators.KEYWORDSET_BADGE)
        page.compare_text(element_text=element_text, message=KeywordsSetsVerif.BADGE_EXPECT)

        element_text = page.get_text_element(
            element=KeywordsSetsLocators.RIGHT_SIDEBAR_KEYWORDSET_NAME)
        page.compare_text(element_text=element_text, message=param[1])

        element = page.find_element(element=KeywordsSetsLocators.RIGHT_SIDEBAR_COUNTER)
        element_text = page.get_counter(element=element)
        page.compare_text(element_text=element_text, message=KeywordsSetsVerif.COUNT_2)

        element = page.find_element(element=KeywordsSetsLocators.RIGHT_SIDEBAR_EXPORT_BUTTON)
        page.check_able_element(element=element)

        element = page.find_element(element=KeywordsSetsLocators.RIGHT_SIDEBAR_INDEX_BUTTON)
        page.check_able_element(element=element)

        page.click_element(element=KeywordsSetsLocators.RIGHT_SIDEBAR_CONTENT_TAB)

        page.wait_visability_element(element=KeywordsSetsLocators.RIGHT_SIDEBAR_CONTENT_TAB_1ST_WORD)
        element_text = page.get_text_element(
            element=KeywordsSetsLocators.RIGHT_SIDEBAR_CONTENT_TAB_1ST_WORD)
        page.compare_text(element_text=element_text, message=KeywordsSetsVerif.PISTOLET)
        element_text = page.get_text_element(
            element=KeywordsSetsLocators.RIGHT_SIDEBAR_CONTENT_TAB_2ND_WORD)
        page.compare_text(element_text=element_text, message=KeywordsSetsVerif.WEAPON)

        return page

    @allure.feature('Keywords sets page')
    @allure.title('Create new keyword set, indexing with different types')
    @pytest.mark.parametrize('param', [(KeywordsSetsData.TEST, KeywordsSetsVerif.TEST,
                                        KeywordsSetsData.TYPE_ALL_PAGES, KeywordsSetsVerif.STR_TYPE_ALL_PAGES),
                                       (KeywordsSetsData.TEST, KeywordsSetsVerif.TEST,
                                        KeywordsSetsData.TYPE_FILES, KeywordsSetsVerif.STR_TYPE_FILES),
                                       (KeywordsSetsData.TEST, KeywordsSetsVerif.TEST,
                                        KeywordsSetsData.TYPE_WRKSPACE_CONTACTS_MAP,
                                        KeywordsSetsVerif.STR_TYPE_WRKSPACE_CONTACTS)
                                       ])
    @DUsers.login_logout_user_param(user_login=LoginData.SUPER_LOGIN, user_password=LoginData.SUPER_PASSWORD,
                                    page_name='keywords_sets')
    @DKeywordSets.delete_keyword_set_param()
    def test_keywords_sets_003(self, page, url, param):
        """https://knoxygen.atlassian.net/wiki/spaces/WA/pages/3775955827/Auto+Keywords+Sets.003"""
        page.wait_visability_element(element=TopBars.DATA_BAR)

        page.open_url(url=url, api=KeywordsSetsData.PAGE)
        page.wait_not_visability_element(element=Notifications.PRELOADER)

        page.wait_visability_element(element=KeywordsSetsLocators.ADD_BUTTON)

        counter = page.find_element(element=KeywordsSetsLocators.COUNTER)
        first_counter = page.get_counter(element=counter, n=2)

        page.click_element(element=KeywordsSetsLocators.ADD_BUTTON)
        page.wait_visability_element(element=KeywordsSetsLocators.KEYWORDSET_NAME)
        page.write_in_element(element=KeywordsSetsLocators.KEYWORDSET_NAME,
                              text=param[0])

        if param[2] != KeywordsSetsVerif.TYPE_WRKSPACE_CONTACTS:
            element = page.find_element(element=KeywordsSetsLocators.KEYWORDSET_TYPE)
            page.select_status(element=element, ind=param[2])

        page.write_in_element(element=KeywordsSetsLocators.KEYWORDSET_ADD_WORD,
                              text=KeywordsSetsData.WEAPON)
        page.click_element(element=KeywordsSetsLocators.KEYWORDSET_ADD)

        page.write_in_element(element=KeywordsSetsLocators.KEYWORDSET_ADD_WORD,
                              text=KeywordsSetsData.PISTOLET)
        page.click_element(element=KeywordsSetsLocators.KEYWORDSET_ADD)

        page.click_element(element=KeywordsSetsLocators.FINAL_ADD)

        page.wait_visability_element(element=Notifications.BLUE_NOTIFI)
        element_text = page.get_text_element(element=Notifications.BLUE_NOTIFI)
        page.click_element(element=Notifications.NOTIFI_CLOSE)
        page.compare_text(element_text=element_text, message=KeywordsSetsVerif.ADDED_KEYWORD_SET)

        counter = page.find_element(element=KeywordsSetsLocators.COUNTER)
        second_counter = page.get_counter(element=counter, n=2)
        page.check_counter_plus(first_counter=first_counter, second_counter=second_counter)

        page.write_in_element(element=KeywordsSetsLocators.SEARCH, text=param[0])
        page.press_enter()
        page.wait_visability_element(KeywordsSetsLocators.GRID_KEYWORDSET)

        element_text = page.get_text_element(element=KeywordsSetsLocators.GRID_KEYWORDSET)
        page.compare_text(element_text=element_text, message=param[1])

        element_text = page.get_text_element(element=KeywordsSetsLocators.GRID_KEYWORDSET_TYPE)
        page.compare_text(element_text=element_text, message=param[3])

        element_text = page.get_text_element(element=KeywordsSetsLocators.KEYWORDSET_BADGE)
        page.compare_text(element_text=element_text, message=KeywordsSetsVerif.BADGE_EXPECT)

        element_text = page.get_text_element(
            element=KeywordsSetsLocators.RIGHT_SIDEBAR_KEYWORDSET_NAME)
        page.compare_text(element_text=element_text, message=param[1])

        element = page.find_element(element=KeywordsSetsLocators.RIGHT_SIDEBAR_COUNTER)
        element_text = page.get_counter(element)
        page.compare_text(element_text=element_text, message=KeywordsSetsVerif.COUNT_2)

        element = page.find_element(element=KeywordsSetsLocators.RIGHT_SIDEBAR_EXPORT_BUTTON)
        page.check_able_element(element=element)

        element = page.find_element(element=KeywordsSetsLocators.RIGHT_SIDEBAR_INDEX_BUTTON)
        page.check_able_element(element=element)

        page.click_element(element=KeywordsSetsLocators.RIGHT_SIDEBAR_CONTENT_TAB)

        page.wait_visability_element(element=KeywordsSetsLocators.RIGHT_SIDEBAR_CONTENT_TAB_1ST_WORD)
        element_text = page.get_text_element(
            element=KeywordsSetsLocators.RIGHT_SIDEBAR_CONTENT_TAB_1ST_WORD)
        page.compare_text(element_text=element_text, message=KeywordsSetsVerif.PISTOLET)
        element_text = page.get_text_element(
            element=KeywordsSetsLocators.RIGHT_SIDEBAR_CONTENT_TAB_2ND_WORD)
        page.compare_text(element_text=element_text, message=KeywordsSetsVerif.WEAPON)

        page.click_element(element=KeywordsSetsLocators.RIGHT_SIDEBAR_INDEX_BUTTON)

        while True:
            element_text = page.get_text_element(element=KeywordsSetsLocators.KEYWORDSET_BADGE)
            if page.compare_badge_in_while(element_text=element_text):
                break
            page.refresh_page()
            page.wait_not_visability_element(element=Notifications.PRELOADER)
            page.wait_visability_element(element=KeywordsSetsLocators.KEYWORDSET_BADGE)

        return page

    @allure.feature('Keywords sets page')
    @allure.title('Change empty keyword set, indexing with different types')
    @pytest.mark.parametrize('param', [(KeywordsSetsData.TEST, KeywordsSetsVerif.TEST,
                                        KeywordsSetsData.TYPE_ALL_PAGES, KeywordsSetsVerif.STR_TYPE_ALL_PAGES,
                                        KeywordsSetsData.TEST_2, KeywordsSetsVerif.TEST_2,
                                        KeywordsSetsData.NOTE, KeywordsSetsVerif.NOTE,
                                        KeywordsSetsData.TYPE_FILES, KeywordsSetsVerif.STR_TYPE_FILES),
                                       (KeywordsSetsData.TEST, KeywordsSetsVerif.TEST,
                                        KeywordsSetsData.TYPE_FILES, KeywordsSetsVerif.STR_TYPE_FILES,
                                        KeywordsSetsData.TEST_2, KeywordsSetsVerif.TEST_2,
                                        KeywordsSetsData.NOTE, KeywordsSetsVerif.NOTE,
                                        KeywordsSetsData.TYPE_ALL_PAGES, KeywordsSetsVerif.STR_TYPE_ALL_PAGES),
                                       (KeywordsSetsData.TEST, KeywordsSetsVerif.TEST,
                                        KeywordsSetsData.TYPE_WRKSPACE_CONTACTS_MAP,
                                        KeywordsSetsVerif.STR_TYPE_WRKSPACE_CONTACTS, KeywordsSetsData.TEST_2,
                                        KeywordsSetsVerif.TEST_2, KeywordsSetsData.NOTE, KeywordsSetsVerif.NOTE,
                                        KeywordsSetsData.TYPE_FILES, KeywordsSetsVerif.STR_TYPE_FILES)
                                       ])
    @DUsers.login_logout_user_param(user_login=LoginData.SUPER_LOGIN, user_password=LoginData.SUPER_PASSWORD,
                                    page_name='keywords_sets')
    @DKeywordSets.delete_keyword_set_param_004()
    def test_keywords_sets_004(self, page, url, param):
        """https://knoxygen.atlassian.net/wiki/spaces/WA/pages/3775955838/Auto+Keywords+Sets.004"""
        page.wait_visability_element(element=TopBars.DATA_BAR)

        page.open_url(url=url, api=KeywordsSetsData.PAGE)
        page.wait_not_visability_element(element=Notifications.PRELOADER)

        page.wait_visability_element(element=KeywordsSetsLocators.ADD_BUTTON)

        counter = page.find_element(element=KeywordsSetsLocators.COUNTER)
        first_counter = page.get_counter(element=counter, n=2)

        page.click_element(element=KeywordsSetsLocators.ADD_BUTTON)
        page.wait_visability_element(element=KeywordsSetsLocators.KEYWORDSET_NAME)
        page.write_in_element(element=KeywordsSetsLocators.KEYWORDSET_NAME,
                              text=param[0])

        if param[2] != KeywordsSetsVerif.TYPE_WRKSPACE_CONTACTS:
            element = page.find_element(element=KeywordsSetsLocators.KEYWORDSET_TYPE)
            page.select_status(element=element, ind=param[2])

        page.click_element(element=KeywordsSetsLocators.FINAL_ADD)

        page.wait_visability_element(element=Notifications.BLUE_NOTIFI)
        element_text = page.get_text_element(element=Notifications.BLUE_NOTIFI)
        page.click_element(element=Notifications.NOTIFI_CLOSE)
        page.compare_text(element_text=element_text, message=KeywordsSetsVerif.ADDED_KEYWORD_SET)

        counter = page.find_element(element=KeywordsSetsLocators.COUNTER)
        second_counter = page.get_counter(element=counter, n=2)
        page.check_counter_plus(first_counter=first_counter, second_counter=second_counter)

        page.write_in_element(element=KeywordsSetsLocators.SEARCH, text=param[0])
        page.press_enter()
        page.wait_visability_element(KeywordsSetsLocators.GRID_KEYWORDSET)

        element_text = page.get_text_element(element=KeywordsSetsLocators.GRID_KEYWORDSET)
        page.compare_text(element_text=element_text, message=param[1])

        element_text = page.get_text_element(element=KeywordsSetsLocators.GRID_KEYWORDSET_TYPE)
        page.compare_text(element_text=element_text, message=param[3])

        element_text = page.get_text_element(element=KeywordsSetsLocators.KEYWORDSET_BADGE)
        page.compare_text(element_text=element_text, message=KeywordsSetsVerif.BADGE_EMPTY)

        element_text = page.get_text_element(
            element=KeywordsSetsLocators.RIGHT_SIDEBAR_KEYWORDSET_NAME)
        page.compare_text(element_text=element_text, message=param[1])

        element = page.find_element(element=KeywordsSetsLocators.RIGHT_SIDEBAR_COUNTER)
        element_text = page.get_counter(element)
        page.compare_text(element_text=element_text, message=KeywordsSetsVerif.ZERO_COUNT)

        element = page.find_element(element=KeywordsSetsLocators.RIGHT_SIDEBAR_EXPORT_BUTTON)
        page.check_disable_element(element=element)

        page.click_element(element=KeywordsSetsLocators.RIGHT_SIDEBAR_CONTENT_TAB)

        page.wait_visability_element(element=KeywordsSetsLocators.RIGHT_SIDEBAR_CONTENT_TAB_NODATA)
        element_text = page.get_text_element(
            element=KeywordsSetsLocators.RIGHT_SIDEBAR_CONTENT_TAB_NODATA)
        page.compare_text(element_text=element_text, message=KeywordsSetsVerif.NO_DATA)

        page.click_element(element=KeywordsSetsLocators.RIGHT_SIDEBAR_EDIT_BUTTON)

        page.clear_element(element=KeywordsSetsLocators.KEYWORDSET_NAME)
        page.write_in_element(element=KeywordsSetsLocators.KEYWORDSET_NAME, text=param[4])

        page.write_in_element(element=KeywordsSetsLocators.KEYWORDSET_NOTE, text=param[6])

        element = page.find_element(element=KeywordsSetsLocators.KEYWORDSET_TYPE)
        page.select_status(element=element, ind=param[8])

        page.write_in_element(element=KeywordsSetsLocators.KEYWORDSET_ADD_WORD,
                              text=KeywordsSetsData.WEAPON)
        page.click_element(element=KeywordsSetsLocators.KEYWORDSET_ADD)

        page.clear_element(element=KeywordsSetsLocators.KEYWORDSET_ADD_WORD)

        page.write_in_element(element=KeywordsSetsLocators.KEYWORDSET_ADD_WORD,
                              text=KeywordsSetsData.PISTOLET)
        page.click_element(element=KeywordsSetsLocators.KEYWORDSET_ADD)

        page.click_element(element=KeywordsSetsLocators.FINAL_ADD)

        page.write_in_element(element=KeywordsSetsLocators.SEARCH, text=param[4])
        page.press_enter()
        page.wait_visability_element(KeywordsSetsLocators.GRID_KEYWORDSET)

        element_text = page.get_text_element(element=KeywordsSetsLocators.GRID_KEYWORDSET)
        page.compare_text(element_text=element_text, message=param[5])

        element_text = page.get_text_element(element=KeywordsSetsLocators.GRID_KEYWORDSET_TYPE)
        page.compare_text(element_text=element_text, message=param[9])

        element_text = page.get_text_element(element=KeywordsSetsLocators.GRID_KEYWORDSET_NOTE)
        page.compare_text(element_text=element_text, message=param[7])

        element_text = page.get_text_element(element=KeywordsSetsLocators.KEYWORDSET_BADGE)
        page.compare_text(element_text=element_text, message=KeywordsSetsVerif.BADGE_EXPECT)

        element_text = page.get_text_element(
            element=KeywordsSetsLocators.RIGHT_SIDEBAR_KEYWORDSET_NAME)
        page.compare_text(element_text=element_text, message=param[5])

        element = page.find_element(element=KeywordsSetsLocators.RIGHT_SIDEBAR_COUNTER)
        element_text = page.get_counter(element)
        page.compare_text(element_text=element_text, message=KeywordsSetsVerif.COUNT_2)

        element = page.find_element(element=KeywordsSetsLocators.RIGHT_SIDEBAR_EXPORT_BUTTON)
        page.check_able_element(element=element)

        element = page.find_element(element=KeywordsSetsLocators.RIGHT_SIDEBAR_INDEX_BUTTON)
        page.check_able_element(element=element)

        page.wait_visability_element(element=Notifications.BLUE_NOTIFI_2)
        page.click_element(element=Notifications.NOTIFI_CLOSE_2)

        page.wait_visability_element(element=Notifications.BLUE_NOTIFI_3)
        page.click_element(element=Notifications.NOTIFI_CLOSE_3)

        page.wait_visability_element(element=Notifications.BLUE_NOTIFI_4)
        page.click_element(element=Notifications.NOTIFI_CLOSE_4)

        page.click_element(element=KeywordsSetsLocators.RIGHT_SIDEBAR_CONTENT_TAB)

        page.wait_visability_element(element=KeywordsSetsLocators.RIGHT_SIDEBAR_CONTENT_TAB_1ST_WORD)
        element_text = page.get_text_element(
            element=KeywordsSetsLocators.RIGHT_SIDEBAR_CONTENT_TAB_1ST_WORD)
        page.compare_text(element_text=element_text, message=KeywordsSetsVerif.WEAPON)
        element_text = page.get_text_element(
            element=KeywordsSetsLocators.RIGHT_SIDEBAR_CONTENT_TAB_2ND_WORD)
        page.compare_text(element_text=element_text, message=KeywordsSetsVerif.PISTOLET)

        page.click_element(element=KeywordsSetsLocators.RIGHT_SIDEBAR_INDEX_BUTTON)

        while True:
            element_text = page.get_text_element(element=KeywordsSetsLocators.KEYWORDSET_BADGE)
            if page.compare_badge_in_while(element_text=element_text):
                break
            page.refresh_page()
            page.wait_not_visability_element(element=Notifications.PRELOADER)
            page.wait_visability_element(element=KeywordsSetsLocators.KEYWORDSET_BADGE)

        return page

    @allure.feature('Keywords sets page')
    @allure.title('Import keyword set with different types')
    @pytest.mark.parametrize('param', [(KeywordsSetsData.TEST, KeywordsSetsVerif.TEST,
                                        KeywordsSetsData.TYPE_ALL_PAGES, KeywordsSetsVerif.STR_TYPE_ALL_PAGES,
                                        '1251.txt', KeywordsSetsData.TYPE_1251, '1251.verif.txt'),
                                       (KeywordsSetsData.TEST, KeywordsSetsVerif.TEST,
                                        KeywordsSetsData.TYPE_ALL_PAGES, KeywordsSetsVerif.STR_TYPE_ALL_PAGES,
                                        'utf_8.txt', KeywordsSetsData.TYPE_UTF8, 'utf_8.verif.txt'),
                                       (KeywordsSetsData.TEST, KeywordsSetsVerif.TEST,
                                        KeywordsSetsData.TYPE_ALL_PAGES, KeywordsSetsVerif.STR_TYPE_ALL_PAGES,
                                        'utf_16.txt', KeywordsSetsData.TYPE_UTF16, 'utf_16.verif.txt'),
                                       (KeywordsSetsData.TEST, KeywordsSetsVerif.TEST,
                                        KeywordsSetsData.TYPE_FILES, KeywordsSetsVerif.STR_TYPE_FILES, '1251.txt',
                                        KeywordsSetsData.TYPE_1251, '1251.verif.txt'),
                                       (KeywordsSetsData.TEST, KeywordsSetsVerif.TEST,
                                        KeywordsSetsData.TYPE_FILES, KeywordsSetsVerif.STR_TYPE_FILES, 'utf_8.txt',
                                        KeywordsSetsData.TYPE_UTF8, 'utf_8.verif.txt'),
                                       (KeywordsSetsData.TEST, KeywordsSetsVerif.TEST,
                                        KeywordsSetsData.TYPE_FILES, KeywordsSetsVerif.STR_TYPE_FILES,
                                        'utf_16.txt', KeywordsSetsData.TYPE_UTF16, 'utf_16.verif.txt'),
                                       (KeywordsSetsData.TEST, KeywordsSetsVerif.TEST,
                                        KeywordsSetsData.TYPE_WRKSPACE_CONTACTS_MAP,
                                        KeywordsSetsVerif.STR_TYPE_WRKSPACE_CONTACTS, '1251.txt',
                                        KeywordsSetsData.TYPE_1251, '1251.verif.txt'),
                                       (KeywordsSetsData.TEST, KeywordsSetsVerif.TEST,
                                        KeywordsSetsData.TYPE_WRKSPACE_CONTACTS_MAP,
                                        KeywordsSetsVerif.STR_TYPE_WRKSPACE_CONTACTS, 'utf_8.txt',
                                        KeywordsSetsData.TYPE_UTF8, 'utf_8.verif.txt'),
                                       (KeywordsSetsData.TEST, KeywordsSetsVerif.TEST,
                                        KeywordsSetsData.TYPE_WRKSPACE_CONTACTS_MAP,
                                        KeywordsSetsVerif.STR_TYPE_WRKSPACE_CONTACTS, 'utf_16.txt',
                                        KeywordsSetsData.TYPE_UTF16, 'utf_16.verif.txt')
                                       ])
    @DUsers.login_logout_user_param(user_login=LoginData.SUPER_LOGIN, user_password=LoginData.SUPER_PASSWORD,
                                    page_name='keywords_sets')
    @DKeywordSets.delete_keyword_set_param()
    def test_keywords_sets_005(self, page, url, param):
        """https://knoxygen.atlassian.net/wiki/spaces/WA/pages/3775955849/Auto+Keywords+Sets.005"""
        page.wait_visability_element(element=TopBars.DATA_BAR)

        page.open_url(url=url, api=KeywordsSetsData.PAGE)
        page.wait_not_visability_element(element=Notifications.PRELOADER)

        page.wait_visability_element(element=KeywordsSetsLocators.ADD_BUTTON)

        counter = page.find_element(element=KeywordsSetsLocators.COUNTER)
        first_counter = page.get_counter(element=counter, n=2)

        page.click_element(element=KeywordsSetsLocators.ADD_BUTTON)
        page.wait_visability_element(element=KeywordsSetsLocators.KEYWORDSET_NAME)
        page.write_in_element(element=KeywordsSetsLocators.KEYWORDSET_NAME,
                              text=param[0])

        if param[2] != KeywordsSetsVerif.TYPE_WRKSPACE_CONTACTS:
            element = page.find_element(element=KeywordsSetsLocators.KEYWORDSET_TYPE)
            page.select_status(element=element, ind=param[2])

        page.upload_file(file_dir=STAND_PATH_KEYWORDS_SETS, file_name=param[4],
                         element=KeywordsSetsLocators.KEYWORDSET_UPLOAD)

        element = page.find_element(element=KeywordsSetsLocators.KEYWORDSET_ENCODING)
        page.select_status(element=element, ind=param[5])

        page.click_element(element=KeywordsSetsLocators.FINAL_ADD)

        page.wait_visability_element(element=Notifications.BLUE_NOTIFI)
        element_text = page.get_text_element(element=Notifications.BLUE_NOTIFI)
        page.click_element(element=Notifications.NOTIFI_CLOSE)
        page.compare_text(element_text=element_text, message=KeywordsSetsVerif.ADDED_KEYWORD_SET)

        counter = page.find_element(element=KeywordsSetsLocators.COUNTER)
        second_counter = page.get_counter(element=counter, n=2)
        page.check_counter_plus(first_counter=first_counter, second_counter=second_counter)

        page.write_in_element(element=KeywordsSetsLocators.SEARCH, text=param[1])
        page.press_enter()
        page.wait_visability_element(KeywordsSetsLocators.GRID_KEYWORDSET)

        element_text = page.get_text_element(Notifications.IMAGE_UPLOAD_PROCESS)
        page.compare_text(element_text=element_text, message=KeywordsSetsVerif.IMAGE_SUCCESS_UPLOAD)

        element_text = page.get_text_element(
            element=KeywordsSetsLocators.RIGHT_SIDEBAR_KEYWORDSET_NAME)
        page.compare_text(element_text=element_text, message=param[1])

        element = page.find_element(element=KeywordsSetsLocators.RIGHT_SIDEBAR_EXPORT_BUTTON)
        page.check_able_element(element=element)

        while True:
            element_text = page.get_text_element(element=KeywordsSetsLocators.KEYWORDSET_BADGE)
            if page.compare_badge_in_while(element_text=element_text):
                break
            page.refresh_page()
            page.wait_not_visability_element(element=Notifications.PRELOADER)
            page.wait_visability_element(element=KeywordsSetsLocators.KEYWORDSET_BADGE)

        element = page.find_element(element=KeywordsSetsLocators.RIGHT_SIDEBAR_COUNTER)
        element_text = page.get_counter(element=element)
        num_strings = page.check_len_keyword_set_file(file_name=param[4])
        page.compare_text(element_text=element_text, message=num_strings)

        page.click_element(element=KeywordsSetsLocators.RIGHT_SIDEBAR_CONTENT_TAB)

        page.wait_visability_element(element=KeywordsSetsLocators.RIGHT_SIDEBAR_CONTENT_TAB_NODATA)
        elements_text = page.get_item_list(
            element=KeywordsSetsLocators.RIGHT_SIDEBAR_CONTENT_TAB_1ST_WORD)
        keyword_list = page.return_list_keyword_set_file(file_name=param[4])
        page.compare_text_list(element_text=elements_text, message=keyword_list)

        return page

    @allure.feature('Keywords sets page')
    @allure.title('Export keyword set with different encodings')
    @pytest.mark.parametrize('param', [('1251.txt', KeywordsSetsData.TEST, KeywordsSetsData.TYPE_1251),
                                       ('utf_8.txt', KeywordsSetsData.TEST, KeywordsSetsData.TYPE_UTF8),
                                       ('utf_16.txt', KeywordsSetsData.TEST, KeywordsSetsData.TYPE_UTF16)])
    @DUsers.login_logout_user_param(user_login=LoginData.SUPER_LOGIN, user_password=LoginData.SUPER_PASSWORD,
                                    page_name='keywords_sets')
    @DKeywordSets.add_import_delete_keyword_set()
    def test_keywords_sets_006(self, page, url, param):
        """https://knoxygen.atlassian.net/wiki/spaces/WA/pages/3775955860/Auto+Keywords+Sets.006"""
        page.wait_visability_element(element=TopBars.DATA_BAR)

        page.open_url(url=url, api=KeywordsSetsData.PAGE)
        page.wait_not_visability_element(element=Notifications.PRELOADER)

        page.wait_visability_element(element=KeywordsSetsLocators.ADD_BUTTON)

        page.write_in_element(element=KeywordsSetsLocators.SEARCH, text=param[1])
        page.press_enter()
        page.wait_visability_element(KeywordsSetsLocators.GRID_KEYWORDSET)

        page.click_element(element=KeywordsSetsLocators.RIGHT_SIDEBAR_EXPORT_BUTTON)

        page.wait_visability_element(KeywordsSetsLocators.EXPORT_FORM)

        page.clear_element(element=KeywordsSetsLocators.KEYWORDSET_NAME)
        page.write_in_element(element=KeywordsSetsLocators.KEYWORDSET_NAME, text='new' + param[1])

        element = page.find_element(element=KeywordsSetsLocators.KEYWORDSET_EXTENSION)
        page.select_file_status(element=element, ind=0)

        page.click_element(element=KeywordsSetsLocators.KEYWORDSET_EXPORT)

        page.wait_visability_element(element=KeywordsSetsLocators.RIGHT_SIDEBAR_EXPORT_BUTTON)
        page.click_element(element=KeywordsSetsLocators.RIGHT_SIDEBAR_EXPORT_BUTTON)

        page.wait_visability_element(KeywordsSetsLocators.EXPORT_FORM)

        page.clear_element(element=KeywordsSetsLocators.KEYWORDSET_NAME)
        page.write_in_element(element=KeywordsSetsLocators.KEYWORDSET_NAME, text='new' + param[1])

        element = page.find_element(element=KeywordsSetsLocators.KEYWORDSET_EXTENSION)
        page.select_file_status(element=element, ind=1)

        page.click_element(element=KeywordsSetsLocators.KEYWORDSET_EXPORT)
        time.sleep(5)
        page.check_keyword_set_file(file_name='new' + param[1] + ".json")
        time.sleep(1)
        page.check_keyword_set_file(file_name='new' + param[1] + ".txt")

        return page

    @allure.feature('Keywords sets page')
    @allure.title('Delete keyword set with different encodings')
    @pytest.mark.parametrize('param', [('1251.txt', KeywordsSetsData.TEST, KeywordsSetsData.TYPE_1251),
                                       ('utf_8.txt', KeywordsSetsData.TEST, KeywordsSetsData.TYPE_UTF8),
                                       ('utf_16.txt', KeywordsSetsData.TEST, KeywordsSetsData.TYPE_UTF16)])
    @DUsers.login_logout_user_param(user_login=LoginData.SUPER_LOGIN, user_password=LoginData.SUPER_PASSWORD,
                                    page_name='keywords_sets')
    @DKeywordSets.add_import_delete_keyword_set()
    def test_keywords_sets_007(self, page, url, param):
        """https://knoxygen.atlassian.net/wiki/spaces/WA/pages/3775955860/Auto+Keywords+Sets.006"""
        page.wait_visability_element(element=TopBars.DATA_BAR)

        page.open_url(url=url, api=KeywordsSetsData.PAGE)
        page.wait_not_visability_element(element=Notifications.PRELOADER)

        page.wait_visability_element(element=KeywordsSetsLocators.ADD_BUTTON)

        page.write_in_element(element=KeywordsSetsLocators.SEARCH, text=param[1])
        page.press_enter()
        page.wait_visability_element(KeywordsSetsLocators.GRID_KEYWORDSET)

        page.hover_on_element(element=KeywordsSetsLocators.GRID_KEYWORDSET)
        page.hover_on_element(element=KeywordsSetsLocators.BASKET)
        page.click_element(element=KeywordsSetsLocators.BASKET)

        page.wait_visability_element(element=KeywordsSetsLocators.BASKET_MESSAGE)
        page.click_element(element=KeywordsSetsLocators.BASKET_YES_BUTTON)

        page.wait_visability_element(element=Notifications.BLUE_NOTIFI)
        element_text = page.get_text_element(element=Notifications.BLUE_NOTIFI)

        page.compare_text(element_text=element_text, message=KeywordsSetsVerif.FINAL_DELETE_MESSAGE)
        page.click_element(element=Notifications.NOTIFI_CLOSE)

        page.write_in_element(element=KeywordsSetsLocators.SEARCH, text=param[0])
        page.press_enter()
        page.wait_visability_element(element=KeywordsSetsLocators.NO_RESULTS)

        element_text = page.get_text_element(element=KeywordsSetsLocators.NO_RESULTS)

        page.compare_text(element_text=element_text, message=KeywordsSetsVerif.NO_RESULTS)

        return page

    @allure.feature('Keywords sets page')
    @allure.title('Open on the all pages')
    @pytest.mark.parametrize('param', [
        ('utf_8.txt', KeywordsSetsData.TEST, KeywordsSetsData.TYPE_UTF8, KeywordsSetsData.API_ALL_PAGES,
         KeywordsSetsLocators.WORKSPACE, WorkspaceVerif.NAME_OF_TAB,
         WorkspaceLocators.COUNTER),
        ('utf_8.txt', KeywordsSetsData.TEST, KeywordsSetsData.TYPE_UTF8, KeywordsSetsData.API_ALL_PAGES,
         KeywordsSetsLocators.FILES, FilesVerif.NAME_OF_TAB, FilesLocators.COUNTER),
        ('utf_8.txt', KeywordsSetsData.TEST, KeywordsSetsData.TYPE_UTF8, KeywordsSetsData.API_ALL_PAGES,
         KeywordsSetsLocators.CONTACTS, ContactsVerif.NAME_OF_TAB,
         ContactsLocators.COUNTER)
    ])
    @DKeywordSets.add_import_delete_keyword_set_different_dict_class()
    @DUsers.login_logout_user_param(user_login=LoginData.SUPER_LOGIN, user_password=LoginData.SUPER_PASSWORD,
                                    page_name='keywords_sets')
    def test_keywords_sets_008_1(self, page, url, param):
        """https://knoxygen.atlassian.net/wiki/spaces/WA/pages/3775955871/Auto+Keywords+Sets.008"""
        page.wait_visability_element(element=TopBars.DATA_BAR)

        page.open_url(url=url, api=KeywordsSetsData.PAGE)
        page.wait_not_visability_element(element=Notifications.PRELOADER)

        page.wait_visability_element(element=KeywordsSetsLocators.ADD_BUTTON)

        while True:
            element_text = page.get_text_element(element=KeywordsSetsLocators.KEYWORDSET_BADGE)
            if page.compare_badge_in_while(element_text=element_text):
                break
            page.refresh_page()
            page.wait_not_visability_element(element=Notifications.PRELOADER)
            page.wait_visability_element(element=KeywordsSetsLocators.KEYWORDSET_BADGE)

        page.write_in_element(element=KeywordsSetsLocators.SEARCH, text=param[1])
        page.press_enter()
        page.wait_visability_element(KeywordsSetsLocators.GRID_KEYWORDSET)

        page.click_element(element=KeywordsSetsLocators.OPEN_BUTTON)

        page.wait_visability_element(element=param[4])
        page.click_element(element=param[4])

        page.wait_not_visability_element(element=Notifications.PRELOADER)

        page.wait_visability_element(element=TopBars.DATA_BAR)
        page.check_name_of_tab(name_of_tab=param[5])
        page.wait_not_visability_element(element=Notifications.PRELOADER)

        while True:
            element_text = page.get_text_element(element=WorkspaceLocators.LOAD_WAIT)
            if page.compare_text_in_while(element_text=element_text, message=WorkspaceData.LOAD_TEXT,
                                          error_message=WorkspaceData.GRID_NO_RESULTS):
                break

        counter = page.find_element(element=param[6])
        counter_num = page.get_counter(element=counter)
        page.check_counter_plus(first_counter=0, second_counter=counter_num)

        return page

    @allure.feature('Keywords sets page')
    @allure.title('Open on the Workspace, Contacts, Map')
    @pytest.mark.parametrize('param', [
        ('utf_8.txt', KeywordsSetsData.TEST, KeywordsSetsData.TYPE_UTF8, KeywordsSetsData.API_WRKSPACE_CONTACTS_MAP,
         KeywordsSetsLocators.WORKSPACE, WorkspaceVerif.NAME_OF_TAB,
         WorkspaceLocators.COUNTER),
        ('utf_8.txt', KeywordsSetsData.TEST, KeywordsSetsData.TYPE_UTF8, KeywordsSetsData.API_WRKSPACE_CONTACTS_MAP,
         KeywordsSetsLocators.CONTACTS, ContactsVerif.NAME_OF_TAB,
         ContactsLocators.COUNTER)
    ])
    @DKeywordSets.add_import_delete_keyword_set_different_dict_class()
    @DUsers.login_logout_user_param(user_login=LoginData.SUPER_LOGIN, user_password=LoginData.SUPER_PASSWORD,
                                    page_name='keywords_sets')
    def test_keywords_sets_008_2(self, page, url, param):
        """https://knoxygen.atlassian.net/wiki/spaces/WA/pages/3775955871/Auto+Keywords+Sets.008"""
        page.wait_visability_element(element=TopBars.DATA_BAR)

        page.open_url(url=url, api=KeywordsSetsData.PAGE)
        page.wait_not_visability_element(element=Notifications.PRELOADER)

        page.wait_not_visability_element(element=Notifications.PRELOADER)
        page.wait_visability_element(element=KeywordsSetsLocators.ADD_BUTTON)

        while True:
            element_text = page.get_text_element(element=KeywordsSetsLocators.KEYWORDSET_BADGE)
            if page.compare_badge_in_while(element_text=element_text):
                break
            page.refresh_page()
            page.wait_not_visability_element(element=Notifications.PRELOADER)
            page.wait_visability_element(element=KeywordsSetsLocators.KEYWORDSET_BADGE)

        page.write_in_element(element=KeywordsSetsLocators.SEARCH, text=param[1])
        page.press_enter()
        page.wait_visability_element(KeywordsSetsLocators.GRID_KEYWORDSET)

        page.click_element(element=KeywordsSetsLocators.OPEN_BUTTON)

        page.wait_visability_element(element=param[4])
        page.click_element(element=param[4])

        page.wait_not_visability_element(element=Notifications.PRELOADER)

        page.wait_visability_element(element=TopBars.DATA_BAR)
        page.check_name_of_tab(name_of_tab=param[5])
        page.wait_not_visability_element(element=Notifications.PRELOADER)

        while True:
            element_text = page.get_text_element(element=WorkspaceLocators.LOAD_WAIT)
            if page.compare_text_in_while(element_text=element_text, message=WorkspaceData.LOAD_TEXT,
                                          error_message=WorkspaceData.GRID_NO_RESULTS):
                break

        counter = page.find_element(element=param[6])
        counter_num = page.get_counter(element=counter)
        page.check_counter_plus(first_counter=0, second_counter=counter_num)

        return page

    @allure.feature('Keywords sets page')
    @allure.title('Open on the Workspace, Contacts, Map')
    @pytest.mark.parametrize('param', [
        ('utf_8.txt', KeywordsSetsData.TEST, KeywordsSetsData.TYPE_UTF8,
         KeywordsSetsData.API_FILES,
         KeywordsSetsLocators.FILES, FilesVerif.NAME_OF_TAB,
         ContactsLocators.COUNTER)
    ])
    @DKeywordSets.add_import_delete_keyword_set_different_dict_class()
    @DUsers.login_logout_user_param(user_login=LoginData.SUPER_LOGIN, user_password=LoginData.SUPER_PASSWORD,
                                    page_name='keywords_sets')
    def test_keywords_sets_008_3(self, page, url, param):
        """https://knoxygen.atlassian.net/wiki/spaces/WA/pages/3775955871/Auto+Keywords+Sets.008"""
        page.wait_visability_element(element=TopBars.DATA_BAR)

        page.open_url(url=url, api=KeywordsSetsData.PAGE)
        page.wait_not_visability_element(element=Notifications.PRELOADER)

        page.wait_not_visability_element(element=Notifications.PRELOADER)
        page.wait_visability_element(element=KeywordsSetsLocators.ADD_BUTTON)

        while True:
            element_text = page.get_text_element(element=KeywordsSetsLocators.KEYWORDSET_BADGE)
            if page.compare_badge_in_while(element_text=element_text):
                break
            page.refresh_page()
            page.wait_not_visability_element(element=Notifications.PRELOADER)
            page.wait_visability_element(element=KeywordsSetsLocators.KEYWORDSET_BADGE)

        page.write_in_element(element=KeywordsSetsLocators.SEARCH, text=param[1])
        page.press_enter()
        page.wait_visability_element(KeywordsSetsLocators.GRID_KEYWORDSET)

        page.click_element(element=KeywordsSetsLocators.OPEN_BUTTON)

        browser_tabs = page.get_all_tabs()
        page.select_tab_number(2, browser_tabs)

        page.wait_not_visability_element(element=Notifications.PRELOADER)

        page.wait_visability_element(element=TopBars.DATA_BAR)
        page.check_name_of_tab(name_of_tab=param[5])
        page.wait_not_visability_element(element=Notifications.PRELOADER)

        while True:
            element_text = page.get_text_element(element=WorkspaceLocators.LOAD_WAIT)
            if page.compare_text_in_while(element_text=element_text, message=WorkspaceData.LOAD_TEXT,
                                          error_message=WorkspaceData.GRID_NO_RESULTS):
                break

        counter = page.find_element(element=param[6])
        counter_num = page.get_counter(element=counter)
        page.check_counter_plus(first_counter=0, second_counter=counter_num)

        return page

    @allure.feature('Keywords sets page')
    @allure.title('Open on the all pages in new tab')
    @pytest.mark.parametrize('param', [
        ('utf_8.txt', KeywordsSetsData.TEST, KeywordsSetsData.TYPE_UTF8, KeywordsSetsData.API_ALL_PAGES,
         KeywordsSetsLocators.WORKSPACE_TAB, WorkspaceVerif.NAME_OF_TAB,
         WorkspaceLocators.COUNTER),
        ('utf_8.txt', KeywordsSetsData.TEST, KeywordsSetsData.TYPE_UTF8, KeywordsSetsData.API_ALL_PAGES,
         KeywordsSetsLocators.FILES_TAB, FilesVerif.NAME_OF_TAB, FilesLocators.COUNTER),
        ('utf_8.txt', KeywordsSetsData.TEST, KeywordsSetsData.TYPE_UTF8, KeywordsSetsData.API_ALL_PAGES,
         KeywordsSetsLocators.CONTACTS_TAB, ContactsVerif.NAME_OF_TAB,
         ContactsLocators.COUNTER)
    ])
    @DKeywordSets.add_import_delete_keyword_set_different_dict_class()
    @DUsers.login_logout_user_param(user_login=LoginData.SUPER_LOGIN, user_password=LoginData.SUPER_PASSWORD,
                                    page_name='keywords_sets')
    def test_keywords_sets_009_1(self, page, url, param):
        """https://knoxygen.atlassian.net/wiki/spaces/WA/pages/3775955871/Auto+Keywords+Sets.008"""
        page.wait_visability_element(element=TopBars.DATA_BAR)

        page.open_url(url=url, api=KeywordsSetsData.PAGE)
        page.wait_not_visability_element(element=Notifications.PRELOADER)

        page.wait_not_visability_element(element=Notifications.PRELOADER)
        page.wait_visability_element(element=KeywordsSetsLocators.ADD_BUTTON)

        while True:
            element_text = page.get_text_element(element=KeywordsSetsLocators.KEYWORDSET_BADGE)
            if page.compare_badge_in_while(element_text=element_text):
                break
            page.refresh_page()
            page.wait_not_visability_element(element=Notifications.PRELOADER)
            page.wait_visability_element(element=KeywordsSetsLocators.KEYWORDSET_BADGE)

        page.write_in_element(element=KeywordsSetsLocators.SEARCH, text=param[1])
        page.press_enter()
        page.wait_visability_element(KeywordsSetsLocators.GRID_KEYWORDSET)

        page.click_element(element=KeywordsSetsLocators.OPEN_BUTTON)

        page.wait_visability_element(element=param[4])
        page.click_element(element=param[4])

        browser_tabs = page.get_all_tabs()
        page.select_tab_number(2, browser_tabs)

        page.wait_not_visability_element(element=Notifications.PRELOADER)

        page.wait_visability_element(element=TopBars.DATA_BAR)
        page.check_name_of_tab(name_of_tab=param[5])
        page.wait_not_visability_element(element=Notifications.PRELOADER)

        while True:
            element_text = page.get_text_element(element=WorkspaceLocators.LOAD_WAIT)
            if page.compare_text_in_while(element_text=element_text, message=WorkspaceData.LOAD_TEXT,
                                          error_message=WorkspaceData.GRID_NO_RESULTS):
                break

        counter = page.find_element(element=param[6])
        counter_num = page.get_counter(element=counter)
        page.check_counter_plus(first_counter=0, second_counter=counter_num)

        return page

    @allure.feature('Keywords sets page')
    @allure.title('Open on the Workspace, Contacts, Map in new tab')
    @pytest.mark.parametrize('param', [
        ('utf_8.txt', KeywordsSetsData.TEST, KeywordsSetsData.TYPE_UTF8,
         KeywordsSetsData.API_WRKSPACE_CONTACTS_MAP,
         KeywordsSetsLocators.WORKSPACE_TAB, WorkspaceVerif.NAME_OF_TAB,
         WorkspaceLocators.COUNTER),
        ('utf_8.txt', KeywordsSetsData.TEST, KeywordsSetsData.TYPE_UTF8,
         KeywordsSetsData.API_WRKSPACE_CONTACTS_MAP,
         KeywordsSetsLocators.CONTACTS_TAB, ContactsVerif.NAME_OF_TAB,
         ContactsLocators.COUNTER)
    ])
    @DKeywordSets.add_import_delete_keyword_set_different_dict_class()
    @DUsers.login_logout_user_param(user_login=LoginData.SUPER_LOGIN, user_password=LoginData.SUPER_PASSWORD,
                                    page_name='keywords_sets')
    def test_keywords_sets_009_2(self, page, url, param):
        """https://knoxygen.atlassian.net/wiki/spaces/WA/pages/3775955871/Auto+Keywords+Sets.008"""
        page.wait_visability_element(element=TopBars.DATA_BAR)

        page.open_url(url=url, api=KeywordsSetsData.PAGE)
        page.wait_not_visability_element(element=Notifications.PRELOADER)

        page.wait_not_visability_element(element=Notifications.PRELOADER)
        page.wait_visability_element(element=KeywordsSetsLocators.ADD_BUTTON)

        while True:
            element_text = page.get_text_element(element=KeywordsSetsLocators.KEYWORDSET_BADGE)
            if page.compare_badge_in_while(element_text=element_text):
                break
            page.refresh_page()
            page.wait_not_visability_element(element=Notifications.PRELOADER)
            page.wait_visability_element(element=KeywordsSetsLocators.KEYWORDSET_BADGE)

        page.write_in_element(element=KeywordsSetsLocators.SEARCH, text=param[1])
        page.press_enter()
        page.wait_visability_element(KeywordsSetsLocators.GRID_KEYWORDSET)

        page.click_element(element=KeywordsSetsLocators.OPEN_BUTTON)

        page.wait_visability_element(element=param[4])
        page.click_element(element=param[4])

        browser_tabs = page.get_all_tabs()
        page.select_tab_number(2, browser_tabs)

        page.wait_not_visability_element(element=Notifications.PRELOADER)

        page.wait_visability_element(element=TopBars.DATA_BAR)
        page.check_name_of_tab(name_of_tab=param[5])
        page.wait_not_visability_element(element=Notifications.PRELOADER)

        while True:
            element_text = page.get_text_element(element=WorkspaceLocators.LOAD_WAIT)
            if page.compare_text_in_while(element_text=element_text, message=WorkspaceData.LOAD_TEXT,
                                          error_message=WorkspaceData.GRID_NO_RESULTS):
                break

        counter = page.find_element(element=param[6])
        counter_num = page.get_counter(element=counter)
        page.check_counter_plus(first_counter=0, second_counter=counter_num)

        return page

    @allure.feature('Keywords sets page')
    @allure.title('Open two keywords sets on the all pages')
    @pytest.mark.parametrize('param', [
        ('utf_8.txt', KeywordsSetsData.TEST, KeywordsSetsData.TYPE_UTF8, KeywordsSetsData.API_ALL_PAGES,
         KeywordsSetsLocators.WORKSPACE, WorkspaceVerif.NAME_OF_TAB,
         WorkspaceLocators.COUNTER, 'utf_16.txt', KeywordsSetsData.TEST_2, KeywordsSetsData.TYPE_UTF16),
        ('utf_8.txt', KeywordsSetsData.TEST, KeywordsSetsData.TYPE_UTF8, KeywordsSetsData.API_ALL_PAGES,
         KeywordsSetsLocators.FILES, FilesVerif.NAME_OF_TAB, FilesLocators.COUNTER, 'utf_16.txt',
         KeywordsSetsData.TEST_2, KeywordsSetsData.TYPE_UTF16),
        ('utf_8.txt', KeywordsSetsData.TEST, KeywordsSetsData.TYPE_UTF8, KeywordsSetsData.API_ALL_PAGES,
         KeywordsSetsLocators.CONTACTS, ContactsVerif.NAME_OF_TAB,
         ContactsLocators.COUNTER, 'utf_16.txt', KeywordsSetsData.TEST_2, KeywordsSetsData.TYPE_UTF16)
    ])
    @DKeywordSets.add_import_delete_2_keyword_set_different_dict_class()
    @DUsers.login_logout_user_param(user_login=LoginData.SUPER_LOGIN, user_password=LoginData.SUPER_PASSWORD,
                                    page_name='keywords_sets')
    def test_keywords_sets_010(self, page, url, param):
        """https://knoxygen.atlassian.net/wiki/spaces/WA/pages/3775955871/Auto+Keywords+Sets.008"""
        page.wait_visability_element(element=TopBars.DATA_BAR)

        page.open_url(url=url, api=KeywordsSetsData.PAGE)
        page.wait_not_visability_element(element=Notifications.PRELOADER)

        page.wait_visability_element(element=KeywordsSetsLocators.ADD_BUTTON)

        page.wait_visability_element(element=KeywordsSetsLocators.GRID_KEYWORDSET)

        while True:
            element_text = page.get_text_element(element=KeywordsSetsLocators.KEYWORDSET_BADGE)
            if page.compare_badge_in_while(element_text=element_text):
                break
            page.refresh_page()
            page.wait_not_visability_element(element=Notifications.PRELOADER)
            page.wait_visability_element(element=KeywordsSetsLocators.KEYWORDSET_BADGE)

        page.click_element(element=KeywordsSetsLocators.GRID_GENERAL_CHECKBOX)

        page.click_element(element=KeywordsSetsLocators.OPEN_BUTTON)

        page.wait_visability_element(element=param[4])
        page.click_element(element=param[4])

        page.wait_not_visability_element(element=Notifications.PRELOADER)

        page.wait_visability_element(element=TopBars.DATA_BAR)
        page.check_name_of_tab(name_of_tab=param[5])
        page.wait_not_visability_element(element=Notifications.PRELOADER)

        while True:
            element_text = page.get_text_element(element=WorkspaceLocators.LOAD_WAIT)
            if page.compare_text_in_while(element_text=element_text, message=WorkspaceData.LOAD_TEXT,
                                          error_message=WorkspaceData.GRID_NO_RESULTS):
                break

        counter = page.find_element(element=param[6])
        counter_num = page.get_counter(element=counter)
        page.check_counter_plus(first_counter=0, second_counter=counter_num)

        return page

    @allure.feature('Keywords sets page')
    @allure.title('Clean monitor')
    @DUsers.logout_all_users()
    def test_z_clean_monitor(self, browser, url):
        pass
