import time
import pytest

from tests.decorators import DHashsets, DUsers, DEntities
from locators import TopBars, Notifications, HashesLocators, WorkspaceLocators, \
    FilesLocators
from data import LoginData, HashesData, STAND_PATH_HASHES
from verification import HashesVerif, WorkspaceVerif, FilesVerif
import allure


@pytest.mark.hashes
@pytest.mark.noload
class TestHashesPage:

    @allure.feature('Hashes page')
    @allure.title('Clean monitor')
    @DUsers.logout_all_users()
    @DEntities.delete_all_entities()
    def test_0_clean_monitor(self, browser, url):
        pass

    @allure.feature('Hashes page')
    @allure.title('Create new empty hash with different types')
    @pytest.mark.parametrize('param', [(HashesData.HASH_MD5, HashesVerif.HASH_MD5,
                                        HashesData.TYPE_MD5, HashesVerif.TYPE_MD5),
                                       (HashesData.HASH_SHA1, HashesVerif.HASH_SHA1,
                                        HashesData.TYPE_SHA1, HashesVerif.TYPE_SHA1),
                                       (HashesData.HASH_SHA256, HashesVerif.HASH_SHA256,
                                        HashesData.TYPE_SHA256, HashesVerif.TYPE_SHA256)
                                       ])
    @DUsers.login_logout_user_param(user_login=LoginData.SUPER_LOGIN, user_password=LoginData.SUPER_PASSWORD,
                                    page_name='hashsets')
    @DHashsets.delete_hash_param()
    def test_hashes_001(self, page, url, param):
        """https://knoxygen.atlassian.net/wiki/spaces/WA/pages/3775955950/Auto+Hash+Sets.001+-"""
        page.wait_visability_element(element=TopBars.DATA_BAR)

        page.open_url(url=url, api=HashesData.PAGE)
        page.wait_not_visability_element(element=Notifications.PRELOADER)

        page.wait_visability_element(element=HashesLocators.ADD_BUTTON)

        counter = page.find_element(element=HashesLocators.COUNTER)
        first_counter = page.get_counter(element=counter, n=2)

        page.click_element(element=HashesLocators.ADD_BUTTON)

        page.wait_visability_element(element=HashesLocators.HASH_NAME)
        page.write_in_element(element=HashesLocators.HASH_NAME,
                              text=param[0])

        if param[0] != HashesVerif.HASH_MD5:
            element = page.find_element(element=HashesLocators.HASH_TYPE)
            page.select_status(element=element, ind=param[2])

        page.click_element(element=HashesLocators.FINAL_ADD)

        page.wait_visability_element(element=Notifications.BLUE_NOTIFI)
        element_text = page.get_text_element(element=Notifications.BLUE_NOTIFI)
        page.click_element(element=Notifications.NOTIFI_CLOSE)
        page.compare_text(element_text=element_text, message=HashesVerif.ADDED_HASH)

        counter = page.find_element(element=HashesLocators.COUNTER)
        second_counter = page.get_counter(element=counter, n=2)
        page.check_counter_plus(first_counter=first_counter, second_counter=second_counter)

        page.write_in_element(element=HashesLocators.SEARCH, text=param[0])
        page.press_enter()
        page.wait_visability_element(HashesLocators.GRID_HASH)

        element_text = page.get_text_element(element=HashesLocators.GRID_HASH)
        page.compare_text(element_text=element_text, message=param[1])

        element_text = page.get_text_element(element=HashesLocators.HASH_BADGE)
        page.compare_text(element_text=element_text, message=HashesVerif.BADGE_EMPTY)

        element_text = page.get_text_element(element=HashesLocators.GRID_HASH_TYPE)
        page.compare_text(element_text=element_text, message=param[3])

        element_text = page.get_text_element(element=HashesLocators.RIGHT_SIDEBAR_HASH_NAME)
        page.compare_text(element_text=element_text, message=param[1])

        element = page.find_element(element=HashesLocators.RIGHT_SIDEBAR_COUNTER)
        element_text = page.get_counter(element)
        page.compare_text(element_text=element_text, message=HashesVerif.ZERO_COUNT)

        return page

    @allure.feature('Hashes page')
    @allure.title('Create hashes with different types')
    @pytest.mark.parametrize('param', [(HashesData.HASH_MD5, HashesVerif.HASH_MD5, HashesData.TYPE_MD5,
                                        'test_md5.txt', HashesVerif.TYPE_MD5),
                                       (HashesData.HASH_SHA1, HashesVerif.HASH_SHA1, HashesData.TYPE_SHA1,
                                        'test_sha-1.txt', HashesVerif.TYPE_SHA1),
                                       (HashesData.HASH_SHA256, HashesVerif.HASH_SHA256, HashesData.TYPE_SHA256,
                                        'test_sha-256.txt', HashesVerif.TYPE_SHA256)
                                       ])
    @DUsers.login_logout_user_param(user_login=LoginData.SUPER_LOGIN, user_password=LoginData.SUPER_PASSWORD,
                                    page_name='hashsets')
    @DHashsets.delete_hash_param()
    def test_hashes_002(self, page, url, param):
        """https://knoxygen.atlassian.net/wiki/spaces/WA/pages/3775955961/Auto+Hash+Sets.002+-"""
        page.wait_visability_element(element=TopBars.DATA_BAR)

        page.open_url(url=url, api=HashesData.PAGE)
        page.wait_not_visability_element(element=Notifications.PRELOADER)

        page.wait_visability_element(element=HashesLocators.ADD_BUTTON)

        counter = page.find_element(element=HashesLocators.COUNTER)
        first_counter = page.get_counter(element=counter, n=2)

        page.click_element(element=HashesLocators.ADD_BUTTON)
        page.wait_visability_element(element=HashesLocators.HASH_NAME)
        page.write_in_element(element=HashesLocators.HASH_NAME,
                              text=param[0])

        if param[0] != HashesVerif.HASH_MD5:
            element = page.find_element(element=HashesLocators.HASH_TYPE)
            page.select_status(element=element, ind=param[2])

        page.upload_file(file_dir=STAND_PATH_HASHES, file_name=param[3],
                         element=HashesLocators.HASH_UPLOAD)

        page.click_element(element=HashesLocators.FINAL_ADD)

        page.wait_visability_element(element=Notifications.BLUE_NOTIFI)
        element_text = page.get_text_element(element=Notifications.BLUE_NOTIFI)
        page.click_element(element=Notifications.NOTIFI_CLOSE)
        page.compare_text(element_text=element_text, message=HashesVerif.ADDED_HASH)

        counter = page.find_element(element=HashesLocators.COUNTER)
        second_counter = page.get_counter(element=counter, n=2)
        page.check_counter_plus(first_counter=first_counter, second_counter=second_counter)

        page.write_in_element(element=HashesLocators.SEARCH, text=param[0])
        page.press_enter()
        page.wait_visability_element(HashesLocators.GRID_HASH)

        element_text = page.get_text_element(element=HashesLocators.GRID_HASH)
        page.compare_text(element_text=element_text, message=param[1])

        element_text = page.get_text_element(element=HashesLocators.GRID_HASH_TYPE)
        page.compare_text(element_text=element_text, message=param[4])

        element_text = page.get_text_element(Notifications.IMAGE_UPLOAD_PROCESS)
        page.compare_text(element_text=element_text, message=HashesVerif.IMAGE_SUCCESS_UPLOAD)

        element_text = page.get_text_element(element=HashesLocators.RIGHT_SIDEBAR_HASH_NAME)
        page.compare_text(element_text=element_text, message=param[1])

        element = page.find_element(element=HashesLocators.RIGHT_SIDEBAR_COUNTER)
        element_text = page.get_counter(element)
        page.compare_text(element_text=element_text, message=HashesVerif.RECORDS)

        while True:
            element_text = page.get_text_element(element=HashesLocators.HASH_BADGE)
            if page.compare_badge_in_while(element_text=element_text):
                break
            page.refresh_page()
            page.wait_not_visability_element(element=Notifications.PRELOADER)
            page.wait_visability_element(element=HashesLocators.HASH_BADGE)

        return page

    @allure.feature('Hashes page')
    @allure.title('Edit hashes with different types')
    @pytest.mark.parametrize('param', [(HashesData.HASH_MD5, HashesData.HASH_SHA1_2,
                                        HashesData.TYPE_SHA1, HashesData.NOTE, 'test_sha-1.txt',
                                        HashesVerif.NOTE, HashesVerif.HASH_SHA1_2, HashesVerif.TYPE_SHA1,
                                        HashesData.API_MD5),
                                       (HashesData.HASH_MD5, HashesData.HASH_SHA256_2,
                                        HashesData.TYPE_SHA256, HashesData.NOTE, 'test_sha-256.txt',
                                        HashesVerif.NOTE, HashesVerif.HASH_SHA256_2, HashesVerif.TYPE_SHA256,
                                        HashesData.API_MD5),
                                       (HashesData.HASH_SHA1, HashesData.HASH_MD5_2,
                                        HashesData.TYPE_MD5, HashesData.NOTE, 'test_md5.txt',
                                        HashesVerif.NOTE, HashesVerif.HASH_MD5_2, HashesVerif.TYPE_MD5,
                                        HashesData.API_SHA1),
                                       (HashesData.HASH_SHA1, HashesData.HASH_SHA256_2,
                                        HashesData.TYPE_SHA256,
                                        HashesData.NOTE, 'test_sha-256.txt',
                                        HashesVerif.NOTE, HashesVerif.HASH_SHA256_2, HashesVerif.TYPE_SHA256,
                                        HashesData.API_SHA1),
                                       (HashesData.HASH_SHA256, HashesData.HASH_SHA1_2,
                                        HashesData.TYPE_SHA1, HashesData.NOTE, 'test_sha-1.txt',
                                        HashesVerif.NOTE, HashesVerif.HASH_SHA1_2, HashesVerif.TYPE_SHA1,
                                        HashesData.API_SHA256),
                                       (HashesData.HASH_SHA256, HashesData.HASH_MD5_2, HashesData.TYPE_MD5,
                                        HashesData.NOTE, 'test_md5.txt', HashesVerif.NOTE, HashesVerif.HASH_MD5_2,
                                        HashesVerif.TYPE_MD5, HashesData.API_SHA256)
                                       ])
    @DUsers.login_logout_user_param(user_login=LoginData.SUPER_LOGIN, user_password=LoginData.SUPER_PASSWORD,
                                    page_name='hashsets')
    @DHashsets.add_delete_hash_with_param()
    def test_hashes_003(self, page, url, param):
        """https://knoxygen.atlassian.net/wiki/spaces/WA/pages/3775955972/Auto+Hash+Sets.003+-"""
        page.wait_visability_element(element=TopBars.DATA_BAR)

        page.open_url(url=url, api=HashesData.PAGE)
        page.wait_not_visability_element(element=Notifications.PRELOADER)

        page.wait_visability_element(element=HashesLocators.ADD_BUTTON)

        page.write_in_element(element=HashesLocators.SEARCH, text=param[0])
        page.press_enter()
        page.wait_visability_element(HashesLocators.GRID_HASH)

        page.click_element(element=HashesLocators.RIGHT_SIDEBAR_EDIT_BUTTON)
        page.wait_visability_element(element=HashesLocators.HASH_NAME)

        page.clear_element(element=HashesLocators.HASH_NAME)
        page.write_in_element(element=HashesLocators.HASH_NAME, text=param[1])

        element = page.find_element(element=HashesLocators.HASH_TYPE)
        page.select_status(element=element, ind=param[2])

        page.write_in_element(element=HashesLocators.HASH_NOTE, text=param[3])

        page.upload_file(file_dir=STAND_PATH_HASHES, file_name=param[4],
                         element=HashesLocators.HASH_UPLOAD)

        page.click_element(element=HashesLocators.FINAL_ADD)

        page.wait_visability_element(element=Notifications.BLUE_NOTIFI)
        element_text = page.get_text_element(element=Notifications.BLUE_NOTIFI)
        page.click_element(element=Notifications.NOTIFI_CLOSE)
        page.compare_text(element_text=element_text, message=HashesVerif.SAVE_CHANGES)

        page.write_in_element(element=HashesLocators.SEARCH, text=param[1])
        page.press_enter()
        page.wait_visability_element(HashesLocators.GRID_HASH)

        element_text = page.get_text_element(element=HashesLocators.GRID_HASH)
        page.compare_text(element_text=element_text, message=param[6])

        element_text = page.get_text_element(element=HashesLocators.GRID_HASH_TYPE)
        page.compare_text(element_text=element_text, message=param[7])

        element_text = page.get_text_element(Notifications.IMAGE_UPLOAD_PROCESS)
        page.compare_text(element_text=element_text, message=HashesVerif.IMAGE_SUCCESS_UPLOAD)

        element_text = page.get_text_element(element=HashesLocators.RIGHT_SIDEBAR_HASH_NAME)
        page.compare_text(element_text=element_text, message=param[6])

        element = page.find_element(element=HashesLocators.RIGHT_SIDEBAR_COUNTER)
        element_text = page.get_counter(element)
        page.compare_text(element_text=element_text, message=HashesVerif.RECORDS)

        while True:
            element_text = page.get_text_element(element=HashesLocators.HASH_BADGE)
            if page.compare_badge_in_while(element_text=element_text):
                break
            page.refresh_page()
            page.wait_not_visability_element(element=Notifications.PRELOADER)
            page.wait_visability_element(element=HashesLocators.HASH_BADGE)

        return page

    @allure.feature('Hashes page')
    @allure.title('Delete hashes with different types')
    @pytest.mark.parametrize('param', [('test_sha-1.txt', HashesData.HASH_SHA1,
                                        HashesData.API_SHA1),
                                       ('test_sha-256.txt', HashesData.HASH_SHA256,
                                        HashesData.API_SHA256),
                                       ('test_md5.txt', HashesData.HASH_MD5,
                                        HashesData.API_MD5),
                                       ])
    @DHashsets.add_import_delete_hash()
    @DUsers.login_logout_user_param(user_login=LoginData.SUPER_LOGIN, user_password=LoginData.SUPER_PASSWORD,
                                    page_name='hashsets')
    def test_hashes_004(self, page, url, param):
        """https://knoxygen.atlassian.net/wiki/spaces/WA/pages/3775955994/Auto+Hash+Sets.004+-"""
        page.wait_visability_element(element=TopBars.DATA_BAR)

        page.open_url(url=url, api=HashesData.PAGE)
        page.wait_not_visability_element(element=Notifications.PRELOADER)

        page.wait_visability_element(element=HashesLocators.ADD_BUTTON)

        page.write_in_element(element=HashesLocators.SEARCH, text=param[1])
        page.press_enter()
        page.wait_visability_element(HashesLocators.GRID_HASH)

        page.hover_on_element(element=HashesLocators.GRID_HASH)
        page.hover_on_element(element=HashesLocators.BASKET)
        page.click_element(element=HashesLocators.BASKET)

        page.wait_visability_element(element=HashesLocators.BASKET_MESSAGE)
        page.click_element(element=HashesLocators.BASKET_YES_BUTTON)

        page.wait_visability_element(element=Notifications.BLUE_NOTIFI)
        element_text = page.get_text_element(element=Notifications.BLUE_NOTIFI)

        page.compare_text(element_text=element_text, message=HashesVerif.FINAL_DELETE_MESSAGE)
        page.click_element(element=Notifications.NOTIFI_CLOSE)

        page.write_in_element(element=HashesLocators.SEARCH, text=param[1])
        page.press_enter()
        page.wait_visability_element(element=HashesLocators.NO_RESULTS)

        element_text = page.get_text_element(element=HashesLocators.NO_RESULTS)

        page.compare_text(element_text=element_text, message=HashesVerif.NO_RESULTS)

        return page

    @allure.feature('Hashes page')
    @allure.title('Export hashes with different types')
    @pytest.mark.parametrize('param', [('test_md5.txt', HashesData.HASH_MD5, HashesData.API_MD5),
                                       ('test_sha-1.txt', HashesData.HASH_SHA1, HashesData.API_SHA1),
                                       ('test_sha-256.txt', HashesData.HASH_SHA256, HashesData.API_SHA256)
                                       ])
    @DHashsets.add_import_delete_hash()
    @DUsers.login_logout_user_param(user_login=LoginData.SUPER_LOGIN, user_password=LoginData.SUPER_PASSWORD,
                                    page_name='hashsets')
    def test_hashes_005(self, page, url, param):
        """https://knoxygen.atlassian.net/wiki/spaces/WA/pages/3775956016/Auto+Hash+Sets.005+-"""
        page.wait_visability_element(element=TopBars.DATA_BAR)

        page.open_url(url=url, api=HashesData.PAGE)
        page.wait_not_visability_element(element=Notifications.PRELOADER)

        page.wait_visability_element(element=HashesLocators.ADD_BUTTON)

        page.write_in_element(element=HashesLocators.SEARCH, text=param[1])
        page.press_enter()
        page.wait_visability_element(HashesLocators.GRID_HASH)

        page.click_element(element=HashesLocators.RIGHT_SIDEBAR_EXPORT_BUTTON)

        page.wait_visability_element(HashesLocators.EXPORT_FORM)

        page.clear_element(element=HashesLocators.HASH_NAME)
        page.write_in_element(element=HashesLocators.HASH_NAME, text='new' + param[1])

        element = page.find_element(element=HashesLocators.HASH_TYPE)
        page.select_file_status(element=element, ind=0)

        page.click_element(element=HashesLocators.HASH_EXPORT)

        page.wait_visability_element(element=HashesLocators.RIGHT_SIDEBAR_EXPORT_BUTTON)
        page.click_element(element=HashesLocators.RIGHT_SIDEBAR_EXPORT_BUTTON)

        page.wait_visability_element(HashesLocators.EXPORT_FORM)

        page.clear_element(element=HashesLocators.HASH_NAME)
        page.write_in_element(element=HashesLocators.HASH_NAME, text='new' + param[1])

        element = page.find_element(element=HashesLocators.HASH_TYPE)
        page.select_file_status(element=element, ind=1)

        page.click_element(element=HashesLocators.HASH_EXPORT)
        time.sleep(1)
        page.check_hash_file(file_name='new' + param[1] + ".json")
        time.sleep(1)
        page.check_hash_file(file_name='new' + param[1] + ".txt")

        return page

    @allure.feature('Hashes page')
    @allure.title('Open on the page')
    @pytest.mark.parametrize('param', [('test_md5.txt', HashesData.HASH_MD5, HashesData.API_MD5,
                                        HashesLocators.WORKSPACE, WorkspaceVerif.NAME_OF_TAB,
                                        WorkspaceLocators.COUNTER),
                                       ('test_md5.txt', HashesData.HASH_MD5, HashesData.API_MD5,
                                        HashesLocators.FILES, FilesVerif.NAME_OF_TAB, FilesLocators.COUNTER)])
    # ('test_md5.txt', HashesData.HASH_MD5, HashesData.API_MD5,
    #  HashesLocators.MAP, MapVerif.NAME_OF_TAB, MapLocators.COUNTER)
    # ])
    @DHashsets.add_import_delete_hash()
    @DUsers.login_logout_user_param(user_login=LoginData.SUPER_LOGIN, user_password=LoginData.SUPER_PASSWORD,
                                    page_name='hashsets')
    def test_hashes_006(self, page, url, param):
        """https://knoxygen.atlassian.net/wiki/spaces/WA/pages/3775956005/Auto+Hash+Sets.006"""
        page.wait_visability_element(element=TopBars.DATA_BAR)

        page.open_url(url=url, api=HashesData.PAGE)
        page.wait_not_visability_element(element=Notifications.PRELOADER)

        page.wait_visability_element(element=HashesLocators.ADD_BUTTON)

        page.write_in_element(element=HashesLocators.SEARCH, text=param[2])
        page.press_enter()
        page.wait_visability_element(HashesLocators.GRID_HASH)

        page.click_element(element=HashesLocators.OPEN_BUTTON)

        page.wait_visability_element(element=param[3])
        page.click_element(element=param[3])

        page.wait_not_visability_element(element=Notifications.PRELOADER)

        page.wait_visability_element(element=TopBars.DATA_BAR)
        page.check_name_of_tab(name_of_tab=param[4])

        counter = page.find_element(element=param[5])
        counter_num = page.get_counter(element=counter)
        page.check_counter_plus(first_counter=0, second_counter=counter_num)

        return page

    @allure.feature('Hashes page')
    @allure.title('Open on the page in new tab')
    @pytest.mark.parametrize('param', [('test_md5.txt', HashesData.HASH_MD5, HashesData.API_MD5,
                                        HashesLocators.WORKSPACE_TAB, WorkspaceVerif.NAME_OF_TAB,
                                        WorkspaceLocators.COUNTER),
                                       ('test_md5.txt', HashesData.HASH_MD5, HashesData.API_MD5,
                                        HashesLocators.FILES_TAB, FilesVerif.NAME_OF_TAB,
                                        FilesLocators.COUNTER)])
    # ('test_md5.txt', HashesData.HASH_MD5, HashesData.API_MD5,
    # HashesLocators.MAP_TAB, MapVerif.NAME_OF_TAB, MapLocators.COUNTER)
    # ]) for this test need more time for index
    @DHashsets.add_import_delete_hash()
    @DUsers.login_logout_user_param(user_login=LoginData.SUPER_LOGIN, user_password=LoginData.SUPER_PASSWORD,
                                    page_name='hashsets')
    def test_hashes_007(self, page, url, param):
        """https://knoxygen.atlassian.net/wiki/spaces/WA/pages/3775956038/Auto+Hash+Sets.007"""
        page.wait_visability_element(element=TopBars.DATA_BAR)

        page.open_url(url=url, api=HashesData.PAGE)
        page.wait_not_visability_element(element=Notifications.PRELOADER)

        page.wait_visability_element(element=HashesLocators.ADD_BUTTON)

        page.write_in_element(element=HashesLocators.SEARCH, text=param[2])
        page.press_enter()
        page.wait_visability_element(HashesLocators.GRID_HASH)

        page.click_element(element=HashesLocators.OPEN_BUTTON)

        page.wait_visability_element(element=param[3])
        page.click_element(element=param[3])

        browser_tabs = page.get_all_tabs()
        page.select_tab_number(2, browser_tabs)

        page.wait_not_visability_element(element=Notifications.PRELOADER)

        page.wait_visability_element(element=TopBars.DATA_BAR)
        page.check_name_of_tab(name_of_tab=param[4])

        counter = page.find_element(element=param[5])
        counter_num = page.get_counter(element=counter)
        page.check_counter_plus(first_counter=0, second_counter=counter_num)

        return page

    @allure.feature('Crime types page')
    @allure.title('Clean monitor')
    @DUsers.logout_all_users()
    def test_z_clean_monitor(self, browser, url):
        pass
