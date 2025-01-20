from functools import wraps

import pytest

from locators import TopBars, Notifications, LoadImagesLocators, CasesLocators
from data import LoginData, LoadImagesData, STAND_PATH, STAND_PATH_INVALID, STAND_PATH_EMPTY, CasesData
from verification import LoadImagesVerif
import allure
import time
import os
from tests.decorators import DLicense, DCases, DUsers, DEntities

working_directory = 'C:\\Test_data\\1'


@pytest.mark.load_images
class TestLoadImagesPage:
    @staticmethod
    def _change_working_directory():
        """Меняет папку с образами для тестов импорта"""

        def setup(func):
            wraps(func)

            def inner(self, browser, url):
                global working_directory

                directories = ['1\\', '2\\', '3\\']
                i = 0
                for directory in directories:
                    if os.path.exists(STAND_PATH + directory + 'stop.txt'):
                        i += 1
                    else:
                        working_directory = STAND_PATH + directory
                        with open(working_directory + 'stop.txt', 'w'):
                            pass
                if i == 3:
                    for directory in directories:
                        os.remove(STAND_PATH + directory + 'stop.txt')
                    working_directory = STAND_PATH + directories[0]
                    with open(working_directory + 'stop.txt', 'w'):
                        pass
                try:

                    func(self, browser, url)

                finally:
                    pass

            return inner

        return setup

    @allure.feature('Load image page')
    @allure.title('Clean monitor')
    @DUsers.logout_all_users()
    @_change_working_directory()
    @DLicense.put_new_license(folder_name='base')
    @DEntities.delete_all_entities()
    def test_0_clean_monitor(self, browser, url):
        pass

    @allure.feature('Load image page')
    @allure.title('Upload .OFBX/.OFBR/.ODB/.UFED/.XRY/.OST/.PST')
    @pytest.mark.parametrize('param', [('test.ofbx', LoadImagesLocators.INPUT_FILE_OFBX_OFBR, LoadImagesLocators.OFBX,
                                        None),
                                       ('test.ofbr', LoadImagesLocators.INPUT_FILE_OFBX_OFBR, LoadImagesLocators.OFBR,
                                        None),
                                       ('test.odb', LoadImagesLocators.INPUT_FILE_ODB, LoadImagesLocators.ODB,
                                        LoadImagesLocators.BUTTON_ODB),
                                       ('test.zip', LoadImagesLocators.INPUT_FILE_UFD, LoadImagesLocators.UFED,
                                        LoadImagesLocators.BUTTON_UFD),
                                       ('test.xry', LoadImagesLocators.INPUT_FILE_XRY, LoadImagesLocators.XRY,
                                        LoadImagesLocators.BUTTON_XRY),
                                       ('test.ost', LoadImagesLocators.INPUT_FILE_PST_OST, LoadImagesLocators.OST,
                                        LoadImagesLocators.BUTTON_PST_OST),
                                       ('test.pst', LoadImagesLocators.INPUT_FILE_PST_OST, LoadImagesLocators.PST,
                                        LoadImagesLocators.BUTTON_PST_OST)
                                       ])
    @DUsers.login_logout_user_param(user_login=LoginData.SUPER_LOGIN, user_password=LoginData.SUPER_PASSWORD,
                                    page_name='load_images')
    def test_load_images_001_005_009_014_018_022_026(self, page, url, param):
        """
        https://knoxygen.atlassian.net/wiki/spaces/WA/pages/3765075982/Auto+Load+images.001+.OFBX
        https://knoxygen.atlassian.net/wiki/spaces/WA/pages/3765075993/Auto+Load+images.005+.OFBR
        https://knoxygen.atlassian.net/wiki/spaces/WA/pages/3765076004/Auto+Load+images.009+.ODB
        https://knoxygen.atlassian.net/wiki/spaces/WA/pages/3765076158/Auto+Load+images.014+.UFD
        https://knoxygen.atlassian.net/wiki/spaces/WA/pages/3765076202/Auto+Load+images.018+.XRY
        https://knoxygen.atlassian.net/wiki/spaces/WA/pages/3765076246/Auto+Load+images.022+.PST
        https://knoxygen.atlassian.net/wiki/spaces/WA/pages/3765076290/Auto+Load+images.026+.OST
        """
        page.wait_visability_element(element=TopBars.DATA_BAR)

        page.open_url(url=url, api=LoadImagesData.PAGE)

        page.wait_not_visability_element(element=Notifications.PRELOADER)
        page.wait_visability_element(element=LoadImagesLocators.ADD_BUTTON)
        page.wait_element_is_clickable(element=LoadImagesLocators.ADD_BUTTON)

        page.wait_not_visability_element(element=Notifications.PRELOADER)
        page.click_element(element=LoadImagesLocators.ADD_BUTTON)

        page.wait_visability_element(element=LoadImagesLocators.ADD_SECTION)

        if param[0] != 'test.ofbx' and param[0] != 'test.ofbr':
            page.click_element(element=param[3])

        page.upload_file(file_dir=working_directory, file_name=param[0],
                         element=param[1])

        if param[0] == 'test.odb':
            page.upload_file(file_dir=working_directory, file_name='test.z01',
                             element=LoadImagesLocators.INPUT_FILE_Z)

        page.click_element(element=LoadImagesLocators.FINAL_ADD)

        while True:
            page.wait_visability_element(element=Notifications.IMAGE_UPLOAD)
            element_text = page.get_text_element(Notifications.IMAGE_UPLOAD)[:13]
            if len(element_text) > 0:
                page.compare_text(element_text=element_text, message=LoadImagesVerif.IMAGE_UPLOAD)
                if page.check_element_is_appeared(element=param[2]):
                    break

        element_text = page.get_text_element(Notifications.IMAGE_UPLOAD_PROCESS)
        page.compare_text(element_text=element_text, message=LoadImagesVerif.IMAGE_SUCCESS_UPLOAD)

        while True:
            page.refresh_page()
            page.wait_not_visability_element(element=Notifications.PRELOADER)
            time.sleep(60)
            if page.check_element_is_appeared(element=param[2]):
                element_text = page.get_upload_badge(element=LoadImagesLocators.UPLOAD_BADGE)
                page.compare_badge_in_while(element_text=element_text)
                element_text = page.get_text_element(LoadImagesLocators.GRID_NOTIFI)
                page.check_text_not_in(element_text=element_text, message=LoadImagesVerif.GRID_NOTIFI)
            else:
                break

        page.wait_not_visability_element(element=Notifications.PRELOADER)
        page.check_element_contains_text_disappeared(element=param[2])
        return page

    @allure.feature('Load image page')
    @allure.title('Upload files with case appointment .OFBX/.OFBR/.ODB/.UFED/.XRY/.OST/.PST')
    @pytest.mark.parametrize('param', [('test.ofbx', LoadImagesLocators.INPUT_FILE_OFBX_OFBR, LoadImagesLocators.OFBX,
                                        None, CasesData.CASE),
                                       ('test.ofbr', LoadImagesLocators.INPUT_FILE_OFBX_OFBR, LoadImagesLocators.OFBR,
                                        None, CasesData.CASE),
                                       ('test.odb', LoadImagesLocators.INPUT_FILE_ODB, LoadImagesLocators.ODB,
                                        LoadImagesLocators.BUTTON_ODB, CasesData.CASE),
                                       ('test.zip', LoadImagesLocators.INPUT_FILE_UFD, LoadImagesLocators.UFED,
                                        LoadImagesLocators.BUTTON_UFD, CasesData.CASE),
                                       ('test.xry', LoadImagesLocators.INPUT_FILE_XRY, LoadImagesLocators.XRY,
                                        LoadImagesLocators.BUTTON_XRY, CasesData.CASE),
                                       ('test.ost', LoadImagesLocators.INPUT_FILE_PST_OST, LoadImagesLocators.OST,
                                        LoadImagesLocators.BUTTON_PST_OST,
                                        CasesData.CASE),
                                       ('test.pst', LoadImagesLocators.INPUT_FILE_PST_OST, LoadImagesLocators.PST,
                                        LoadImagesLocators.BUTTON_PST_OST,
                                        CasesData.CASE)
                                       ])
    @DCases.add_delete_case_with_param(case_name=CasesData.CASE)
    @DUsers.login_logout_user_param(user_login=LoginData.SUPER_LOGIN, user_password=LoginData.SUPER_PASSWORD,
                                    page_name='load_images')
    def test_load_images_002_006_010_015_019_023_027(self, page, url, param):
        """
        https://knoxygen.atlassian.net/wiki/spaces/WA/pages/3765076015/Auto+Load+images.002+.OFBX
        https://knoxygen.atlassian.net/wiki/spaces/WA/pages/3765076026/Auto+Load+images.006+.OFBR
        https://knoxygen.atlassian.net/wiki/spaces/WA/pages/3765076037/Auto+Load+images.010+.ODB
        https://knoxygen.atlassian.net/wiki/spaces/WA/pages/3765076169/Auto+Load+images.015+.UFD
        https://knoxygen.atlassian.net/wiki/spaces/WA/pages/3765076213/Auto+Load+images.019+.XRY
        https://knoxygen.atlassian.net/wiki/spaces/WA/pages/3765076257/Auto+Load+images.023+.PST
        https://knoxygen.atlassian.net/wiki/spaces/WA/pages/3765076301/Auto+Load+images.027+.OST
        """
        page.wait_visability_element(element=TopBars.DATA_BAR)

        page.open_url(url=url, api=LoadImagesData.PAGE)

        page.wait_not_visability_element(element=Notifications.PRELOADER)
        page.wait_visability_element(element=LoadImagesLocators.ADD_BUTTON)
        page.wait_element_is_clickable(element=LoadImagesLocators.ADD_BUTTON)

        page.wait_not_visability_element(element=Notifications.PRELOADER)
        page.click_element(element=LoadImagesLocators.ADD_BUTTON)

        page.wait_visability_element(element=LoadImagesLocators.ADD_SECTION)

        if param[0] != 'test.ofbx' and param[0] != 'test.ofbr':
            page.click_element(element=param[3])

        page.upload_file(file_dir=working_directory, file_name=param[0],
                         element=param[1])

        if param[0] == 'test.odb':
            page.upload_file(file_dir=working_directory, file_name='test.z01',
                             element=LoadImagesLocators.INPUT_FILE_Z)

        element = page.find_element(element=LoadImagesLocators.CASES_LIST)
        page.select_status(element=element, ind=1)

        page.click_element(element=LoadImagesLocators.CHECKBOX_NOFILES)

        page.click_element(element=LoadImagesLocators.FINAL_ADD)

        while True:
            page.wait_visability_element(element=Notifications.IMAGE_UPLOAD)
            element_text = page.get_text_element(Notifications.IMAGE_UPLOAD)[:13]
            if len(element_text) > 0:
                page.compare_text(element_text=element_text, message=LoadImagesVerif.IMAGE_UPLOAD)
                if page.check_element_is_appeared(element=param[2]):
                    break

        element_text = page.get_text_element(Notifications.IMAGE_UPLOAD_PROCESS)
        page.compare_text(element_text=element_text, message=LoadImagesVerif.IMAGE_SUCCESS_UPLOAD)

        while True:
            page.refresh_page()
            page.wait_not_visability_element(element=Notifications.PRELOADER)
            time.sleep(60)
            if page.check_element_is_appeared(element=param[2]):
                element_text = page.get_upload_badge(element=LoadImagesLocators.UPLOAD_BADGE)
                page.compare_badge_in_while(element_text=element_text)
                element_text = page.get_text_element(LoadImagesLocators.GRID_NOTIFI)
                page.check_text_not_in(element_text=element_text, message=LoadImagesVerif.GRID_NOTIFI)
            else:
                break

        page.wait_not_visability_element(element=Notifications.PRELOADER)
        page.check_element_contains_text_disappeared(element=param[2])

        page.open_url(url=url, api=CasesData.PAGE)

        page.wait_not_visability_element(element=Notifications.PRELOADER)
        page.wait_visability_element(element=CasesLocators.ADD_CASE_BUTTON)
        page.wait_element_is_clickable(element=CasesLocators.ADD_CASE_BUTTON)

        page.write_in_element(element=CasesLocators.SEARCH, text=param[4])
        page.click_element(element=CasesLocators.BUTTON_SEARCH)

        page.wait_not_visability_element(element=Notifications.PRELOADER)
        page.wait_visability_element(element=CasesLocators.ADD_CASE_BUTTON)
        page.wait_element_is_clickable(element=CasesLocators.ADD_CASE_BUTTON)

        counter = page.find_element(element=CasesLocators.RIGHT_SIDEBAT_DEVICE_COUNTER)
        counter_num = page.get_counter(element=counter)
        page.check_counter_plus(first_counter=0, second_counter=counter_num)

        return page

    @allure.feature('Load image page')
    @allure.title('Upload empty files .OFBX/.OFBR/.ODB/.UFED/.XRY/.OST/.PST')
    @pytest.mark.parametrize('param', [('empty.ofbx', LoadImagesLocators.INPUT_FILE_OFBX_OFBR, LoadImagesLocators.OFBX,
                                        None, Notifications.RED_NOTIFI, Notifications.RED_NOTIFI_CLOSE),
                                       ('empty.ofbr', LoadImagesLocators.INPUT_FILE_OFBX_OFBR, LoadImagesLocators.OFBR,
                                        None, Notifications.RED_NOTIFI, Notifications.RED_NOTIFI_CLOSE),
                                       ('empty.odb', LoadImagesLocators.INPUT_FILE_ODB, LoadImagesLocators.ODB,
                                        LoadImagesLocators.BUTTON_ODB, Notifications.RED_NOTIFI,
                                        Notifications.RED_NOTIFI_CLOSE),
                                       ('empty.zip', LoadImagesLocators.INPUT_FILE_UFD, LoadImagesLocators.UFED,
                                        LoadImagesLocators.BUTTON_UFD, Notifications.RED_NOTIFI,
                                        Notifications.RED_NOTIFI_CLOSE),
                                       ('empty.xry', LoadImagesLocators.INPUT_FILE_XRY, LoadImagesLocators.XRY,
                                        LoadImagesLocators.BUTTON_XRY, Notifications.RED_NOTIFI,
                                        Notifications.RED_NOTIFI_CLOSE),
                                       ('empty.ost', LoadImagesLocators.INPUT_FILE_PST_OST, LoadImagesLocators.OST,
                                        LoadImagesLocators.BUTTON_PST_OST, Notifications.RED_NOTIFI,
                                        Notifications.RED_NOTIFI_CLOSE),
                                       ('empty.pst', LoadImagesLocators.INPUT_FILE_PST_OST, LoadImagesLocators.PST,
                                        LoadImagesLocators.BUTTON_PST_OST, Notifications.RED_NOTIFI,
                                        Notifications.RED_NOTIFI_CLOSE)
                                       ])
    @DUsers.login_logout_user_param(user_login=LoginData.SUPER_LOGIN, user_password=LoginData.SUPER_PASSWORD,
                                    page_name='load_images')
    def test_load_images_003_007_012_016_020_024_028(self, page, url, param):
        """
        https://knoxygen.atlassian.net/wiki/spaces/WA/pages/3765076048/Auto+Load+images.003+.OFBX
        https://knoxygen.atlassian.net/wiki/spaces/WA/pages/3765076059/Auto+Load+images.007+.OFBR
        https://knoxygen.atlassian.net/wiki/spaces/WA/pages/3765076114/Auto+Load+images.012+.ODB
        https://knoxygen.atlassian.net/wiki/spaces/WA/pages/3765076180/Auto+Load+images.016+.UFD
        https://knoxygen.atlassian.net/wiki/spaces/WA/pages/3765076224/Auto+Load+images.020+.XRY
        https://knoxygen.atlassian.net/wiki/spaces/WA/pages/3765076268/Auto+Load+images.024+.PST
        https://knoxygen.atlassian.net/wiki/spaces/WA/pages/3765076312/Auto+Load+images.028+.OST
        """
        page.wait_visability_element(element=TopBars.DATA_BAR)

        page.open_url(url=url, api=LoadImagesData.PAGE)

        page.wait_not_visability_element(element=Notifications.PRELOADER)
        page.wait_visability_element(element=LoadImagesLocators.ADD_BUTTON)
        page.wait_element_is_clickable(element=LoadImagesLocators.ADD_BUTTON)

        page.wait_not_visability_element(element=Notifications.PRELOADER)
        page.click_element(element=LoadImagesLocators.ADD_BUTTON)

        page.wait_visability_element(element=LoadImagesLocators.ADD_SECTION)

        if param[0] != 'empty.ofbx' and param[0] != 'empty.ofbr':
            page.click_element(element=param[3])

        page.upload_file(file_dir=STAND_PATH_EMPTY, file_name=param[0],
                         element=param[1])

        if param[0] == 'empty.odb':
            page.upload_file(file_dir=STAND_PATH_EMPTY, file_name='empty.z01',
                             element=LoadImagesLocators.INPUT_FILE_Z)

        page.wait_visability_element(element=param[4])
        element_text = page.get_text_element(element=param[4])
        page.click_element(element=param[5])
        page.compare_text(element_text=element_text, message=LoadImagesVerif.RED_EMPTY_NOTIFI)

        page.click_element(element=LoadImagesLocators.CLOSE_BUTTON)

        return page

    @allure.feature('Load image page')
    @allure.title('Upload without files .OFBX/.OFBR/.ODB/.UFED/.XRY/.OST/.PST')
    @pytest.mark.parametrize('param', [('test.ofbx', LoadImagesLocators.INPUT_FILE_OFBX_OFBR, LoadImagesLocators.OFBX,
                                        None),
                                       ('test.ofbr', LoadImagesLocators.INPUT_FILE_OFBX_OFBR, LoadImagesLocators.OFBR,
                                        None),
                                       ('test.odb', LoadImagesLocators.INPUT_FILE_ODB, LoadImagesLocators.ODB,
                                        LoadImagesLocators.BUTTON_ODB),
                                       ('test.zip', LoadImagesLocators.INPUT_FILE_UFD, LoadImagesLocators.UFED,
                                        LoadImagesLocators.BUTTON_UFD),
                                       ('test.xry', LoadImagesLocators.INPUT_FILE_XRY, LoadImagesLocators.XRY,
                                        LoadImagesLocators.BUTTON_XRY),
                                       ('test.ost', LoadImagesLocators.INPUT_FILE_PST_OST, LoadImagesLocators.OST,
                                        LoadImagesLocators.BUTTON_PST_OST),
                                       ('test.pst', LoadImagesLocators.INPUT_FILE_PST_OST, LoadImagesLocators.PST,
                                        LoadImagesLocators.BUTTON_PST_OST)
                                       ])
    @DUsers.login_logout_user_param(user_login=LoginData.SUPER_LOGIN, user_password=LoginData.SUPER_PASSWORD,
                                    page_name='load_images')
    def test_load_images_004_008_013_017_021_025_029(self, page, url, param):
        """
        https://knoxygen.atlassian.net/wiki/spaces/WA/pages/3765076125/Auto+Load+images.004+.OFBX
        https://knoxygen.atlassian.net/wiki/spaces/WA/pages/3765076136/Auto+Load+images.008+.OFBR
        https://knoxygen.atlassian.net/wiki/spaces/WA/pages/3765076147/Auto+Load+images.013+.ODB
        https://knoxygen.atlassian.net/wiki/spaces/WA/pages/3765076191/Auto+Load+images.017+.UFD
        https://knoxygen.atlassian.net/wiki/spaces/WA/pages/3765076235/Auto+Load+images.021+.XRY
        https://knoxygen.atlassian.net/wiki/spaces/WA/pages/3765076279/Auto+Load+images.025+.PST
        https://knoxygen.atlassian.net/wiki/spaces/WA/pages/3765076323/Auto+Load+images.029+.OST
        """
        page.wait_visability_element(element=TopBars.DATA_BAR)

        page.open_url(url=url, api=LoadImagesData.PAGE)

        page.wait_not_visability_element(element=Notifications.PRELOADER)
        page.wait_visability_element(element=LoadImagesLocators.ADD_BUTTON)
        page.wait_element_is_clickable(element=LoadImagesLocators.ADD_BUTTON)

        page.wait_not_visability_element(element=Notifications.PRELOADER)
        page.click_element(element=LoadImagesLocators.ADD_BUTTON)

        page.wait_visability_element(element=LoadImagesLocators.ADD_SECTION)

        if param[0] != 'test.ofbx' and param[0] != 'test.ofbr':
            page.click_element(element=param[3])

        page.upload_file(file_dir=working_directory, file_name=param[0],
                         element=param[1])

        if param[0] == 'test.odb':
            page.upload_file(file_dir=working_directory, file_name='test.z01',
                             element=LoadImagesLocators.INPUT_FILE_Z)

        page.click_element(element=LoadImagesLocators.CHECKBOX_NOFILES)

        page.click_element(element=LoadImagesLocators.FINAL_ADD)

        while True:
            page.wait_visability_element(element=Notifications.IMAGE_UPLOAD)
            element_text = page.get_text_element(Notifications.IMAGE_UPLOAD)[:13]
            if len(element_text) > 0:
                page.compare_text(element_text=element_text, message=LoadImagesVerif.IMAGE_UPLOAD)
                if page.check_element_is_appeared(element=param[2]):
                    break

        element_text = page.get_text_element(Notifications.IMAGE_UPLOAD_PROCESS)
        page.compare_text(element_text=element_text, message=LoadImagesVerif.IMAGE_SUCCESS_UPLOAD)

        while True:
            page.refresh_page()
            page.wait_not_visability_element(element=Notifications.PRELOADER)
            time.sleep(60)
            if page.check_element_is_appeared(element=param[2]):
                element_text = page.get_upload_badge(element=LoadImagesLocators.UPLOAD_BADGE)
                page.compare_badge_in_while(element_text=element_text)
                element_text = page.get_text_element(LoadImagesLocators.GRID_NOTIFI)
                page.check_text_not_in(element_text=element_text, message=LoadImagesVerif.GRID_NOTIFI)
            else:
                break

        page.wait_not_visability_element(element=Notifications.PRELOADER)
        page.check_element_contains_text_disappeared(element=param[2])
        return page

    @allure.feature('Load image page')
    @allure.title('Upload invalid files .OFBX/.OFBR/.ODB/.UFED/.XRY/.OST/.PST')
    @pytest.mark.parametrize('param', [('invalid.py', LoadImagesLocators.INPUT_FILE_OFBX_OFBR, LoadImagesLocators.OFBX,
                                        'pass', Notifications.RED_NOTIFI, Notifications.RED_NOTIFI_CLOSE),
                                       ('invalid.py', LoadImagesLocators.INPUT_FILE_OFBX_OFBR, LoadImagesLocators.OFBR,
                                        'pass', Notifications.RED_NOTIFI, Notifications.RED_NOTIFI_CLOSE),
                                       ('invalid.py', LoadImagesLocators.INPUT_FILE_ODB, LoadImagesLocators.ODB,
                                        LoadImagesLocators.BUTTON_ODB, Notifications.RED_NOTIFI,
                                        Notifications.RED_NOTIFI_CLOSE),
                                       ('invalid.py', LoadImagesLocators.INPUT_FILE_UFD, LoadImagesLocators.UFED,
                                        LoadImagesLocators.BUTTON_UFD, Notifications.RED_NOTIFI,
                                        Notifications.RED_NOTIFI_CLOSE),
                                       ('invalid.py', LoadImagesLocators.INPUT_FILE_XRY, LoadImagesLocators.XRY,
                                        LoadImagesLocators.BUTTON_XRY, Notifications.RED_NOTIFI,
                                        Notifications.RED_NOTIFI_CLOSE),
                                       ('invalid.py', LoadImagesLocators.INPUT_FILE_PST_OST, LoadImagesLocators.OST,
                                        LoadImagesLocators.BUTTON_PST_OST, Notifications.RED_NOTIFI,
                                        Notifications.RED_NOTIFI_CLOSE),
                                       ('invalid.py', LoadImagesLocators.INPUT_FILE_PST_OST, LoadImagesLocators.PST,
                                        LoadImagesLocators.BUTTON_PST_OST, Notifications.RED_NOTIFI,
                                        Notifications.RED_NOTIFI_CLOSE)
                                       ])
    @DUsers.login_logout_user_param(user_login=LoginData.SUPER_LOGIN, user_password=LoginData.SUPER_PASSWORD,
                                    page_name='load_images')
    def test_load_images_030(self, page, url, param):
        """
        https://knoxygen.atlassian.net/wiki/spaces/WA/pages/3765076103/Auto+Load+images.030+.OFBX+.OFBR+.ODB+.XRY.+.UDEF+.PST+.OST
        """
        page.wait_visability_element(element=TopBars.DATA_BAR)

        page.open_url(url=url, api=LoadImagesData.PAGE)

        page.wait_not_visability_element(element=Notifications.PRELOADER)
        page.wait_visability_element(element=LoadImagesLocators.ADD_BUTTON)
        page.wait_element_is_clickable(element=LoadImagesLocators.ADD_BUTTON)

        page.wait_not_visability_element(element=Notifications.PRELOADER)
        page.click_element(element=LoadImagesLocators.ADD_BUTTON)

        page.wait_visability_element(element=LoadImagesLocators.ADD_SECTION)

        if param[3] != 'pass':
            page.click_element(element=param[3])

        page.upload_file(file_dir=STAND_PATH_INVALID, file_name=param[0],
                         element=param[1])

        page.wait_visability_element(element=param[4])
        element_text = page.get_text_element(element=param[4])

        page.click_element(element=param[5])
        page.compare_text(element_text=element_text, message=LoadImagesVerif.RED_INVALID_NOTIFI)

        page.click_element(element=LoadImagesLocators.CLOSE_BUTTON)

        return page

    @allure.feature('Load image page')
    @allure.title('Clean monitor')
    @DUsers.logout_all_users()
    def test_z_clean_monitor(self, browser, url):
        pass
