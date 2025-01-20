from functools import wraps
import pytest
import API
from tests.decorators import DUsers, DCases, DLicense, DDepartment, DEntities
from locators import LoginLocators, TopBars, AdminLocators, Notifications, CasesLocators, \
    DevicesLocators
from data import LoginData, DepartmentsData, CasesData, ENV_HOST
from verification import AdminVerif, CasesVerif, LoginVerif
import allure
import time



@pytest.mark.admin
@pytest.mark.noload
class TestAdminPage:
    @staticmethod
    def parametrize_test_26(func):
        wraps(func)

        def inner(self, browser, url, param):
            headers = None

            try:
                headers = API.api_user_login(url=url)
                case_id = API.api_add_entity(url=url, headers=headers, entity_type='case',
                                             case_name=AdminVerif.DEPARTMENT_CASE)
                department_id = API.api_add_entity(url=url, headers=headers, entity_type='department',
                                                   department_name=AdminVerif.DEPARTMENT_NAME, case_id=case_id)
                func(self, browser, url, param)
                users_dict = API.api_get_entity_dict(url=url, headers=headers, entity_type='user')
                user_id = API.api_get_added_entity_id_of_login(data=users_dict, entity_login=LoginData.ADMIN_LOGIN)

                API.api_delete_entity(url=url, entity_type='department', entity_id=department_id, headers=headers)
                API.api_delete_entity(url=url, entity_type='user', entity_id=user_id, headers=headers)
                API.api_delete_entity(url=url, entity_type='case', entity_id=case_id, headers=headers)

            finally:
                API.api_user_logout(url=url, headers=headers)
                del headers

        return inner

    @staticmethod
    def parametrize_test_29(func):
        wraps(func)

        def inner(self, browser, url, param):
            headers = None

            try:
                headers = API.api_user_login(url=url)
                case_id = API.api_add_entity(url=url, headers=headers, entity_type='case',
                                             case_name=AdminVerif.DEPARTMENT_CASE)
                department_id = API.api_add_entity(url=url, headers=headers, entity_type='department',
                                                   department_name=AdminVerif.DEPARTMENT_NAME, case_id=case_id)
                API.api_add_entity(url=url, headers=headers, entity_type='user',
                                   user_status=param[2], departments_id=department_id)
                func(self, browser, url, param)
                users_dict = API.api_get_entity_dict(url=url, headers=headers, entity_type='user')
                user_id = API.api_get_added_entity_id_of_login(data=users_dict, entity_login=param[0])

                API.api_delete_entity(url=url, entity_type='department', entity_id=department_id, headers=headers)
                API.api_delete_entity(url=url, entity_type='user', entity_id=user_id, headers=headers)
                API.api_delete_entity(url=url, entity_type='case', entity_id=case_id, headers=headers)

            finally:
                API.api_user_logout(url=url, headers=headers)
                del headers

        return inner

    @allure.feature('Admin page')
    @allure.title('Clean monitor')
    @DUsers.logout_all_users()
    @DLicense.put_new_license(folder_name='base')
    @DEntities.delete_all_entities()
    def test_0_clean_monitor(self, browser, url):
        pass

    @allure.feature('Admin page')
    @allure.title('Add new user with Administrator status')
    @DUsers.delete_user(user_login=LoginData.ADMIN_LOGIN)
    @DUsers.login_logout_user(user_login=LoginData.SUPER_LOGIN, user_password=LoginData.SUPER_PASSWORD,
                              page_name='admin')
    def test_admin_001(self, page, url):
        """https://knoxygen.atlassian.net/wiki/spaces/WA/pages/3588063244"""
        page.wait_visability_element(element=AdminLocators.ADD_BUTTON)
        page.wait_visability_element(element=AdminLocators.COUNTER)
        counter = page.find_element(element=AdminLocators.COUNTER)
        first_counter = page.get_counter(element=counter)
        page.wait_not_visability_element(element=Notifications.PRELOADER)
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
        page.wait_visability_element(element=AdminLocators.GRID_LOGIN)
        param_list = page.get_grid_user_parameters(arg1=AdminLocators.GRID_LOGIN,
                                                   arg2=AdminLocators.GRID_STATUS,
                                                   arg3=AdminLocators.GRID_FNAME,
                                                   arg4=AdminLocators.GRID_LNAME)
        page.check_grid_user_parameters(parameters=param_list, check_parameters=AdminVerif.ADMIN_PARAM)
        counter = page.find_element(element=AdminLocators.COUNTER)
        second_counter = page.get_counter(element=counter)
        page.check_counter_plus(first_counter=first_counter, second_counter=second_counter)

        return page

    @allure.feature('Admin page')
    @allure.title('Add new user without fill fields')
    @DUsers.login_logout_user(user_login=LoginData.SUPER_LOGIN, user_password=LoginData.SUPER_PASSWORD,
                              page_name='admin')
    def test_admin_002(self, page, url):
        """https://knoxygen.atlassian.net/wiki/spaces/WA/pages/3588063255"""
        page.wait_visability_element(element=AdminLocators.ADD_BUTTON)
        page.wait_not_visability_element(element=Notifications.PRELOADER)
        page.click_element(element=AdminLocators.ADD_BUTTON)

        page.wait_visability_element(element=AdminLocators.FINAL_ADD)
        page.click_element(element=AdminLocators.FINAL_ADD)

        page.wait_visability_element(element=AdminLocators.REG_NOTIFI)
        text = page.get_text_element(element=AdminLocators.REG_NOTIFI)
        page.compare_text(element_text=text, message=AdminVerif.REG_NOTIFI_1)
        page.click_element(element=AdminLocators.NOTIFI_OK)

        page.click_element(element=AdminLocators.CANCEL_BUTTON)

        return page

    @allure.feature('Admin page')
    @allure.title('Add new user without login')
    @DUsers.login_logout_user(user_login=LoginData.SUPER_LOGIN, user_password=LoginData.SUPER_PASSWORD,
                              page_name='admin')
    def test_admin_003(self, page, url):
        """https://knoxygen.atlassian.net/wiki/spaces/WA/pages/3588063266"""
        page.wait_visability_element(element=AdminLocators.ADD_BUTTON)
        page.wait_not_visability_element(element=Notifications.PRELOADER)
        page.click_element(element=AdminLocators.ADD_BUTTON)

        page.wait_visability_element(element=AdminLocators.ADD_SECTION)
        page.write_in_element(element=AdminLocators.FIRST_NAME, text=LoginData.FIRST_NAME)
        page.write_in_element(element=AdminLocators.LAST_NAME, text=LoginData.LAST_NAME)
        page.write_in_element(element=AdminLocators.PASSWORD_FIELD, text=LoginData.PASSWORD)
        page.write_in_element(element=AdminLocators.PASSWORD_COPY_FIELD, text=LoginData.PASSWORD)

        page.click_element(element=AdminLocators.FINAL_ADD)

        page.wait_visability_element(element=AdminLocators.REG_NOTIFI)
        text = page.get_text_element(element=AdminLocators.REG_NOTIFI)
        page.compare_text(element_text=text, message=AdminVerif.REG_NOTIFI_2)
        page.click_element(element=AdminLocators.NOTIFI_OK)

        page.click_element(element=AdminLocators.CANCEL_BUTTON)

        return page

    @allure.feature('Admin page')
    @allure.title('Add new user without firstname and lastname')
    @DUsers.login_logout_user(user_login=LoginData.SUPER_LOGIN, user_password=LoginData.SUPER_PASSWORD,
                              page_name='admin')
    def test_admin_004(self, page, url):
        """https://knoxygen.atlassian.net/wiki/spaces/WA/pages/3588063277"""
        page.wait_visability_element(element=AdminLocators.ADD_BUTTON)
        page.wait_not_visability_element(element=Notifications.PRELOADER)
        page.click_element(element=AdminLocators.ADD_BUTTON)

        page.wait_visability_element(element=AdminLocators.ADD_SECTION)
        page.write_in_element(element=AdminLocators.LOGIN_FIELD, text=LoginData.ADMIN_LOGIN)
        page.write_in_element(element=AdminLocators.PASSWORD_FIELD, text=LoginData.PASSWORD)
        page.write_in_element(element=AdminLocators.PASSWORD_COPY_FIELD, text=LoginData.PASSWORD)

        page.click_element(element=AdminLocators.FINAL_ADD)

        page.wait_visability_element(element=AdminLocators.REG_NOTIFI)
        text = page.get_text_element(element=AdminLocators.REG_NOTIFI)
        page.compare_text(element_text=text, message=AdminVerif.REG_NOTIFI_3)
        page.click_element(element=AdminLocators.NOTIFI_OK)

        page.click_element(element=AdminLocators.CANCEL_BUTTON)

        return page

    @allure.feature('Admin page')
    @allure.title('Add new user without password')
    @DEntities.delete_all_entities()
    @DUsers.login_logout_user(user_login=LoginData.SUPER_LOGIN, user_password=LoginData.SUPER_PASSWORD,
                              page_name='admin')
    def test_admin_005(self, page, url):
        """https://knoxygen.atlassian.net/wiki/spaces/WA/pages/3588063288"""
        page.wait_visability_element(element=AdminLocators.ADD_BUTTON)
        page.wait_not_visability_element(element=Notifications.PRELOADER)
        page.click_element(element=AdminLocators.ADD_BUTTON)

        page.wait_visability_element(element=AdminLocators.ADD_SECTION)
        page.write_in_element(element=AdminLocators.LOGIN_FIELD, text=LoginData.ADMIN_LOGIN)
        page.write_in_element(element=AdminLocators.FIRST_NAME, text=LoginData.FIRST_NAME)
        page.write_in_element(element=AdminLocators.LAST_NAME, text=LoginData.LAST_NAME)

        page.click_element(element=AdminLocators.FINAL_ADD)

        page.wait_visability_element(element=AdminLocators.REG_NOTIFI)
        text = page.get_text_element(element=AdminLocators.REG_NOTIFI)
        page.compare_text(element_text=text, message=AdminVerif.REG_NOTIFI_4)
        page.click_element(element=AdminLocators.NOTIFI_OK)

        page.click_element(element=AdminLocators.CANCEL_BUTTON)

        return page

    @allure.feature('Admin page')
    @allure.title('Add new user without password')
    @DUsers.login_logout_user(user_login=LoginData.SUPER_LOGIN, user_password=LoginData.SUPER_PASSWORD,
                              page_name='admin')
    def test_admin_006(self, page, url):
        """https://knoxygen.atlassian.net/wiki/spaces/WA/pages/3663560717"""
        page.wait_visability_element(element=AdminLocators.ADD_BUTTON)
        page.wait_not_visability_element(element=Notifications.PRELOADER)
        page.click_element(element=AdminLocators.ADD_BUTTON)

        page.wait_visability_element(element=AdminLocators.ADD_SECTION)
        page.write_in_element(element=AdminLocators.LOGIN_FIELD, text=LoginData.ADMIN_LOGIN)
        page.write_in_element(element=AdminLocators.FIRST_NAME, text=LoginData.FIRST_NAME)
        page.write_in_element(element=AdminLocators.LAST_NAME, text=LoginData.LAST_NAME)
        page.write_in_element(element=AdminLocators.PASSWORD_COPY_FIELD, text=LoginData.PASSWORD)

        page.click_element(element=AdminLocators.FINAL_ADD)

        page.wait_visability_element(element=AdminLocators.REG_NOTIFI)
        text = page.get_text_element(element=AdminLocators.REG_NOTIFI)
        page.compare_text(element_text=text, message=AdminVerif.REG_NOTIFI_5)
        page.click_element(element=AdminLocators.NOTIFI_OK)

        page.click_element(element=AdminLocators.CANCEL_BUTTON)

        return page

    @allure.feature('Admin page')
    @allure.title('Add new user without second password')
    @DUsers.login_logout_user(user_login=LoginData.SUPER_LOGIN, user_password=LoginData.SUPER_PASSWORD,
                              page_name='admin')
    def test_admin_006_2(self, page, url):
        """https://knoxygen.atlassian.net/wiki/spaces/WA/pages/3588063299"""
        page.wait_visability_element(element=AdminLocators.ADD_BUTTON)
        page.wait_not_visability_element(element=Notifications.PRELOADER)
        page.click_element(element=AdminLocators.ADD_BUTTON)

        page.wait_visability_element(element=AdminLocators.ADD_SECTION)
        page.write_in_element(element=AdminLocators.LOGIN_FIELD, text=LoginData.ADMIN_LOGIN)
        page.write_in_element(element=AdminLocators.FIRST_NAME, text=LoginData.FIRST_NAME)
        page.write_in_element(element=AdminLocators.LAST_NAME, text=LoginData.LAST_NAME)
        page.write_in_element(element=AdminLocators.PASSWORD_FIELD, text=LoginData.PASSWORD)

        page.click_element(element=AdminLocators.FINAL_ADD)

        page.wait_visability_element(element=AdminLocators.REG_NOTIFI)
        text = page.get_text_element(element=AdminLocators.REG_NOTIFI)
        page.compare_text(element_text=text, message=AdminVerif.REG_NOTIFI_6)
        page.click_element(element=AdminLocators.NOTIFI_OK)

        page.click_element(element=AdminLocators.CANCEL_BUTTON)

        return page

    @allure.feature('Admin page')
    @allure.title('Add new user with wrong passwords')
    @pytest.mark.parametrize('param', ['rus', 'Login12', 'ibnb', 'Vibnb', 'VibnbBBB1', 'Vibnb4'])
    @DUsers.login_logout_user_param(user_login=LoginData.SUPER_LOGIN, user_password=LoginData.SUPER_PASSWORD,
                                    page_name='admin')
    def test_admin_007(self, page, url, param):
        """https://knoxygen.atlassian.net/wiki/spaces/WA/pages/3588063310"""
        page.wait_visability_element(element=AdminLocators.ADD_BUTTON)
        page.wait_not_visability_element(element=Notifications.PRELOADER)
        page.click_element(element=AdminLocators.ADD_BUTTON)

        page.wait_visability_element(element=AdminLocators.ADD_SECTION)
        page.write_in_element(element=AdminLocators.LOGIN_FIELD, text=LoginData.ADMIN_LOGIN)
        page.write_in_element(element=AdminLocators.FIRST_NAME, text=LoginData.FIRST_NAME)
        page.write_in_element(element=AdminLocators.LAST_NAME, text=LoginData.LAST_NAME)
        if param == 'rus':
            page.write_in_element(element=AdminLocators.PASSWORD_FIELD, text='Пароль32')
            page.write_in_element(element=AdminLocators.PASSWORD_COPY_FIELD, text='Пароль32')
        else:
            page.write_in_element(element=AdminLocators.PASSWORD_FIELD, text=param)
            page.write_in_element(element=AdminLocators.PASSWORD_COPY_FIELD, text=param)

        page.click_element(element=AdminLocators.FINAL_ADD)

        page.wait_visability_element(element=AdminLocators.REG_NOTIFI)
        text = page.get_text_element(element=AdminLocators.REG_NOTIFI)
        page.compare_text(element_text=text, message=AdminVerif.REG_NOTIFI_7)
        page.click_element(element=AdminLocators.NOTIFI_OK)

        page.click_element(element=AdminLocators.CANCEL_BUTTON)

        return page

    @allure.feature('Admin page')
    @allure.title('Add new user with different passwords')
    @pytest.mark.parametrize('param', [('Vibnb47', 'Vibnb57'), ('Vibnb57', 'Vibnb47')])
    @DUsers.login_logout_user_param(user_login=LoginData.SUPER_LOGIN, user_password=LoginData.SUPER_PASSWORD,
                                    page_name='admin')
    def test_admin_008(self, page, url, param):
        """https://knoxygen.atlassian.net/wiki/spaces/WA/pages/3588063321"""
        page.wait_visability_element(element=AdminLocators.ADD_BUTTON)
        page.wait_not_visability_element(element=Notifications.PRELOADER)
        page.click_element(element=AdminLocators.ADD_BUTTON)

        page.wait_visability_element(element=AdminLocators.ADD_SECTION)
        page.write_in_element(element=AdminLocators.LOGIN_FIELD, text=LoginData.ADMIN_LOGIN)
        page.write_in_element(element=AdminLocators.FIRST_NAME, text=LoginData.FIRST_NAME)
        page.write_in_element(element=AdminLocators.LAST_NAME, text=LoginData.LAST_NAME)
        page.write_in_element(element=AdminLocators.PASSWORD_FIELD, text=param[0])
        page.write_in_element(element=AdminLocators.PASSWORD_COPY_FIELD, text=param[1])

        page.click_element(element=AdminLocators.FINAL_ADD)

        page.wait_visability_element(element=AdminLocators.REG_NOTIFI)
        text = page.get_text_element(element=AdminLocators.REG_NOTIFI)
        page.compare_text(element_text=text, message=AdminVerif.REG_NOTIFI_8)
        page.click_element(element=AdminLocators.NOTIFI_OK)

        page.click_element(element=AdminLocators.CANCEL_BUTTON)

        return page

    @allure.feature('Admin page')
    @allure.title('Add new user with Expert status')
    @DUsers.delete_user(user_login=LoginData.EXPERT_LOGIN)
    @DUsers.login_logout_user(user_login=LoginData.SUPER_LOGIN, user_password=LoginData.SUPER_PASSWORD,
                              page_name='admin')
    def test_admin_009(self, page, url):
        """https://knoxygen.atlassian.net/wiki/spaces/WA/pages/3588063332"""
        page.wait_visability_element(element=AdminLocators.ADD_BUTTON)
        page.wait_not_visability_element(element=Notifications.PRELOADER)

        page.wait_visability_element(element=AdminLocators.COUNTER)
        counter = page.find_element(element=AdminLocators.COUNTER)
        first_counter = page.get_counter(element=counter)

        page.click_element(element=AdminLocators.ADD_BUTTON)

        page.wait_visability_element(element=AdminLocators.ADD_SECTION)
        page.write_in_element(element=AdminLocators.LOGIN_FIELD, text=LoginData.EXPERT_LOGIN)
        element = page.find_element(element=AdminLocators.SELECT_STATUS)
        page.select_status(element=element, ind=2)
        page.write_in_element(element=AdminLocators.FIRST_NAME, text=LoginData.FIRST_NAME)
        page.write_in_element(element=AdminLocators.LAST_NAME, text=LoginData.LAST_NAME)
        page.write_in_element(element=AdminLocators.PASSWORD_FIELD, text=LoginData.PASSWORD)
        page.write_in_element(element=AdminLocators.PASSWORD_COPY_FIELD, text=LoginData.PASSWORD)

        page.click_element(element=AdminLocators.FINAL_ADD)

        page.wait_visability_element(element=Notifications.BLUE_NOTIFI)
        element_text = page.get_text_element(element=Notifications.BLUE_NOTIFI)
        page.compare_text(element_text=element_text, message=AdminVerif.ADDED_USER)
        page.click_element(element=Notifications.NOTIFI_CLOSE)
        page.write_in_element(element=AdminLocators.SEARCH, text=LoginData.EXPERT_LOGIN)
        page.press_enter()
        page.wait_visability_element(AdminLocators.GRID_LOGIN)
        param_list = page.get_grid_user_parameters(arg1=AdminLocators.GRID_LOGIN,
                                                   arg2=AdminLocators.GRID_STATUS,
                                                   arg3=AdminLocators.GRID_FNAME,
                                                   arg4=AdminLocators.GRID_LNAME)
        page.check_grid_user_parameters(parameters=param_list, check_parameters=AdminVerif.EXPERT_PARAM)
        counter = page.find_element(element=AdminLocators.COUNTER)
        second_counter = page.get_counter(element=counter)
        page.check_counter_plus(first_counter=first_counter, second_counter=second_counter)

        return page

    @allure.feature('Admin page')
    @allure.title('Add new user with Loader status')
    @DUsers.delete_user(user_login=LoginData.LOAD_LOGIN)
    @DUsers.login_logout_user(user_login=LoginData.SUPER_LOGIN, user_password=LoginData.SUPER_PASSWORD,
                              page_name='admin')
    def test_admin_010(self, page, url):
        """https://knoxygen.atlassian.net/wiki/spaces/WA/pages/3588063343"""
        page.wait_visability_element(element=AdminLocators.ADD_BUTTON)

        page.wait_visability_element(element=AdminLocators.COUNTER)
        counter = page.find_element(element=AdminLocators.COUNTER)
        first_counter = page.get_counter(element=counter)

        page.click_element(element=AdminLocators.ADD_BUTTON)

        page.wait_visability_element(element=AdminLocators.ADD_SECTION)
        page.write_in_element(element=AdminLocators.LOGIN_FIELD, text=LoginData.LOAD_LOGIN)
        element = page.find_element(element=AdminLocators.SELECT_STATUS)
        page.select_status(element=element, ind=4)
        page.write_in_element(element=AdminLocators.FIRST_NAME, text=LoginData.FIRST_NAME)
        page.write_in_element(element=AdminLocators.LAST_NAME, text=LoginData.LAST_NAME)
        page.write_in_element(element=AdminLocators.PASSWORD_FIELD, text=LoginData.PASSWORD)
        page.write_in_element(element=AdminLocators.PASSWORD_COPY_FIELD, text=LoginData.PASSWORD)

        page.click_element(element=AdminLocators.FINAL_ADD)

        page.wait_visability_element(element=Notifications.BLUE_NOTIFI)
        element_text = page.get_text_element(element=Notifications.BLUE_NOTIFI)
        page.compare_text(element_text=element_text, message=AdminVerif.ADDED_USER)
        page.click_element(element=Notifications.NOTIFI_CLOSE)

        page.write_in_element(element=AdminLocators.SEARCH, text=LoginData.LOAD_LOGIN)
        page.press_enter()
        page.wait_visability_element(AdminLocators.GRID_LOGIN)
        param_list = page.get_grid_user_parameters(arg1=AdminLocators.GRID_LOGIN,
                                                   arg2=AdminLocators.GRID_STATUS,
                                                   arg3=AdminLocators.GRID_FNAME,
                                                   arg4=AdminLocators.GRID_LNAME)
        page.check_grid_user_parameters(parameters=param_list, check_parameters=AdminVerif.LOAD_PARAM)
        counter = page.find_element(element=AdminLocators.COUNTER)
        second_counter = page.get_counter(element=counter)
        page.check_counter_plus(first_counter=first_counter, second_counter=second_counter)

        return page

    @allure.feature('Admin page')
    @allure.title('Add new users with different statuses in row')
    @DUsers.delete_several_users(user_logins_list=["login12", "login12_ex", "login12_load"])
    @DUsers.login_logout_user(user_login=LoginData.SUPER_LOGIN, user_password=LoginData.SUPER_PASSWORD,
                              page_name='admin')
    def test_admin_011(self, page, url):
        """https://knoxygen.atlassian.net/wiki/spaces/WA/pages/3588063354"""
        page.wait_not_visability_element(element=Notifications.PRELOADER)
        param = [(LoginData.ADMIN_LOGIN, 1, AdminVerif.ADMIN_PARAM),
                 (LoginData.EXPERT_LOGIN, 2, AdminVerif.EXPERT_PARAM),
                 (LoginData.LOAD_LOGIN, 4, AdminVerif.LOAD_PARAM)]
        page.wait_visability_element(element=AdminLocators.ADD_BUTTON)

        counter = page.find_element(element=AdminLocators.COUNTER)
        first_counter = page.get_counter(element=counter)
        page.click_element(element=AdminLocators.ADD_BUTTON)

        page.wait_visability_element(element=AdminLocators.ADD_SECTION)
        page.write_in_element(element=AdminLocators.LOGIN_FIELD, text=param[0][0])
        element = page.find_element(element=AdminLocators.SELECT_STATUS)
        page.select_status(element=element, ind=param[0][1])
        page.write_in_element(element=AdminLocators.FIRST_NAME, text=LoginData.FIRST_NAME)
        page.write_in_element(element=AdminLocators.LAST_NAME, text=LoginData.LAST_NAME)
        page.write_in_element(element=AdminLocators.PASSWORD_FIELD, text=LoginData.PASSWORD)
        page.write_in_element(element=AdminLocators.PASSWORD_COPY_FIELD, text=LoginData.PASSWORD)

        page.click_element(element=AdminLocators.FINAL_ADD)

        page.wait_visability_element(element=Notifications.BLUE_NOTIFI)
        element_text = page.get_text_element(element=Notifications.BLUE_NOTIFI)
        page.compare_text(element_text=element_text, message=AdminVerif.ADDED_USER)
        page.click_element(element=Notifications.NOTIFI_CLOSE)

        page.write_in_element(element=AdminLocators.SEARCH, text=param[0][0])
        page.press_enter()
        page.wait_visability_element(AdminLocators.GRID_LOGIN)
        param_list = page.get_grid_user_parameters(arg1=AdminLocators.GRID_LOGIN,
                                                   arg2=AdminLocators.GRID_STATUS,
                                                   arg3=AdminLocators.GRID_FNAME,
                                                   arg4=AdminLocators.GRID_LNAME)
        page.check_grid_user_parameters(parameters=param_list, check_parameters=param[0][2])
        counter = page.find_element(element=AdminLocators.COUNTER)
        second_counter = page.get_counter(element=counter)
        page.check_counter_plus(first_counter=first_counter, second_counter=second_counter)

        page.wait_visability_element(element=AdminLocators.ADD_BUTTON)
        counter = page.find_element(element=AdminLocators.COUNTER)
        first_counter = page.get_counter(element=counter)

        page.click_element(element=AdminLocators.ADD_BUTTON)

        page.wait_visability_element(element=AdminLocators.ADD_SECTION)
        page.write_in_element(element=AdminLocators.LOGIN_FIELD, text=param[1][0])
        element = page.find_element(element=AdminLocators.SELECT_STATUS)
        page.select_status(element=element, ind=param[1][1])
        page.write_in_element(element=AdminLocators.FIRST_NAME, text=LoginData.FIRST_NAME)
        page.write_in_element(element=AdminLocators.LAST_NAME, text=LoginData.LAST_NAME)
        page.write_in_element(element=AdminLocators.PASSWORD_FIELD, text=LoginData.PASSWORD)
        page.write_in_element(element=AdminLocators.PASSWORD_COPY_FIELD, text=LoginData.PASSWORD)

        page.click_element(element=AdminLocators.FINAL_ADD)

        page.wait_visability_element(element=Notifications.BLUE_NOTIFI_2)
        element_text = page.get_text_element(element=Notifications.BLUE_NOTIFI_2)
        page.compare_text(element_text=element_text, message=AdminVerif.ADDED_USER)
        page.click_element(element=Notifications.NOTIFI_CLOSE_2)

        page.write_in_element(element=AdminLocators.SEARCH, text=param[1][0])
        page.press_enter()
        page.wait_visability_element(AdminLocators.GRID_LOGIN)
        param_list = page.get_grid_user_parameters(arg1=AdminLocators.GRID_LOGIN,
                                                   arg2=AdminLocators.GRID_STATUS,
                                                   arg3=AdminLocators.GRID_FNAME,
                                                   arg4=AdminLocators.GRID_LNAME)
        page.check_grid_user_parameters(parameters=param_list, check_parameters=param[1][2])
        counter = page.find_element(element=AdminLocators.COUNTER)
        second_counter = page.get_counter(element=counter)
        page.check_counter_plus(first_counter=first_counter, second_counter=second_counter)

        page.wait_visability_element(element=AdminLocators.ADD_BUTTON)

        counter = page.find_element(element=AdminLocators.COUNTER)
        first_counter = page.get_counter(element=counter)
        page.click_element(element=AdminLocators.ADD_BUTTON)

        page.wait_visability_element(element=AdminLocators.ADD_SECTION)
        page.write_in_element(element=AdminLocators.LOGIN_FIELD, text=param[2][0])
        element = page.find_element(element=AdminLocators.SELECT_STATUS)
        page.select_status(element=element, ind=param[2][1])
        page.write_in_element(element=AdminLocators.FIRST_NAME, text=LoginData.FIRST_NAME)
        page.write_in_element(element=AdminLocators.LAST_NAME, text=LoginData.LAST_NAME)
        page.write_in_element(element=AdminLocators.PASSWORD_FIELD, text=LoginData.PASSWORD)
        page.write_in_element(element=AdminLocators.PASSWORD_COPY_FIELD, text=LoginData.PASSWORD)

        page.click_element(element=AdminLocators.FINAL_ADD)

        page.wait_visability_element(element=Notifications.BLUE_NOTIFI_3)
        element_text = page.get_text_element(element=Notifications.BLUE_NOTIFI_3)
        page.compare_text(element_text=element_text, message=AdminVerif.ADDED_USER)
        page.click_element(element=Notifications.NOTIFI_CLOSE_3)

        page.write_in_element(element=AdminLocators.SEARCH, text=param[2][0])
        page.press_enter()
        page.wait_visability_element(AdminLocators.GRID_LOGIN)
        param_list = page.get_grid_user_parameters(arg1=AdminLocators.GRID_LOGIN,
                                                   arg2=AdminLocators.GRID_STATUS,
                                                   arg3=AdminLocators.GRID_FNAME,
                                                   arg4=AdminLocators.GRID_LNAME)
        page.check_grid_user_parameters(parameters=param_list, check_parameters=param[2][2])
        counter = page.find_element(element=AdminLocators.COUNTER)
        second_counter = page.get_counter(element=counter)
        page.check_counter_plus(first_counter=first_counter, second_counter=second_counter)

        return page

    @allure.feature('Admin page')
    @allure.title('Add user and department appointment')
    @DDepartment.add_delete_department(department_name=DepartmentsData.DEPARTMENT_NAME_1)
    @DUsers.delete_user(user_login=LoginData.ADMIN_LOGIN)
    @DUsers.login_logout_user(user_login=LoginData.SUPER_LOGIN, user_password=LoginData.SUPER_PASSWORD,
                              page_name='admin')
    def test_admin_012(self, page, url):
        """https://knoxygen.atlassian.net/wiki/spaces/WA/pages/3588063365"""
        page.wait_visability_element(element=AdminLocators.ADD_BUTTON)
        page.wait_visability_element(element=AdminLocators.COUNTER)

        page.wait_not_visability_element(element=Notifications.PRELOADER)
        page.click_element(element=AdminLocators.ADD_BUTTON)

        page.wait_visability_element(element=AdminLocators.ADD_SECTION)
        page.write_in_element(element=AdminLocators.LOGIN_FIELD, text=LoginData.ADMIN_LOGIN)
        element = page.find_element(element=AdminLocators.SELECT_STATUS)
        page.select_status(element=element, ind=1)
        page.write_in_element(element=AdminLocators.FIRST_NAME, text=LoginData.FIRST_NAME)
        page.write_in_element(element=AdminLocators.LAST_NAME, text=LoginData.LAST_NAME)
        page.write_in_element(element=AdminLocators.PASSWORD_FIELD, text=LoginData.PASSWORD)
        page.write_in_element(element=AdminLocators.PASSWORD_COPY_FIELD, text=LoginData.PASSWORD)
        page.click_element(element=AdminLocators.DEPARTMENTS_1ST_DEP)

        page.click_element(element=AdminLocators.FINAL_ADD)
        page.wait_visability_element(element=Notifications.BLUE_NOTIFI)
        element_text = page.get_text_element(element=Notifications.BLUE_NOTIFI)
        page.compare_text(element_text=element_text, message=AdminVerif.ADDED_USER)
        page.click_element(element=Notifications.NOTIFI_CLOSE)

        page.write_in_element(element=AdminLocators.SEARCH, text=LoginData.ADMIN_LOGIN)
        page.press_enter()
        page.wait_visability_element(AdminLocators.GRID_LOGIN)
        page.click_element(element=AdminLocators.RIGHT_SIDEBAR_DEPARTMENT)
        page.wait_visability_element(element=AdminLocators.RIGHT_SIDEBAR_DEPARTMENT_NAME)
        element_text = page.get_text_element(element=AdminLocators.RIGHT_SIDEBAR_DEPARTMENT_NAME)
        page.compare_text(element_text=element_text, message=AdminVerif.DEPARTMENT_NAME)

        return page

    @allure.feature('Admin page')
    @allure.title('Add user and case appointment')
    @DCases.add_delete_case(case_name=CasesData.CASE)
    @DUsers.delete_user(user_login=LoginData.ADMIN_LOGIN)
    @DUsers.login_logout_user(user_login=LoginData.SUPER_LOGIN, user_password=LoginData.SUPER_PASSWORD,
                              page_name='admin')
    def test_admin_013(self, page, url):
        """https://knoxygen.atlassian.net/wiki/spaces/WA/pages/3588063376"""
        page.wait_not_visability_element(element=Notifications.PRELOADER)
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
        page.click_element(element=AdminLocators.CASE_RIGHTS)
        page.click_element(element=AdminLocators.SORT_CASES)
        page.click_element(element=AdminLocators.CASES_1ST_CASE)

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
        page.click_element(element=AdminLocators.RIGHT_SIDEBAR_CASE)
        page.wait_visability_element(element=AdminLocators.RIGHT_SIDEBAR_CASE_NAME)
        element_text = page.get_text_element(element=AdminLocators.RIGHT_SIDEBAR_CASE_NAME)
        page.compare_text(element_text=element_text, message=AdminVerif.DEPARTMENT_CASE)
        page.check_counter_plus(first_counter=first_counter, second_counter=second_counter)

        return page

    @allure.feature('Admin page')
    @allure.title('Add user, case and department appointment')
    @DDepartment.add_delete_department(department_name=DepartmentsData.DEPARTMENT_NAME_1)
    @DCases.add_delete_case(case_name=CasesData.CASE)
    @DUsers.delete_user(user_login=LoginData.ADMIN_LOGIN)
    @DUsers.login_logout_user(user_login=LoginData.SUPER_LOGIN, user_password=LoginData.SUPER_PASSWORD,
                              page_name='admin')
    def test_admin_014(self, page, url):
        """https://knoxygen.atlassian.net/wiki/spaces/WA/pages/3588063387"""
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
        page.click_element(element=AdminLocators.DEPARTMENTS_1ST_DEP)
        page.click_element(element=AdminLocators.CASE_RIGHTS)
        page.click_element(element=AdminLocators.SORT_CASES)
        page.click_element(element=AdminLocators.CASES_1ST_CASE)

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

        page.click_element(element=AdminLocators.RIGHT_SIDEBAR_DEPARTMENT)
        page.wait_not_visability_element(element=Notifications.PRELOADER)
        page.wait_visability_element(element=AdminLocators.RIGHT_SIDEBAR_DEPARTMENT_NAME)

        element_text = page.get_text_element(element=AdminLocators.RIGHT_SIDEBAR_DEPARTMENT_NAME)
        page.compare_text(element_text=element_text, message=AdminVerif.DEPARTMENT_NAME)

        page.click_element(element=AdminLocators.RIGHT_SIDEBAR_CASE)
        page.wait_visability_element(element=AdminLocators.RIGHT_SIDEBAR_CASE_NAME)

        element_text = page.get_text_element(element=AdminLocators.RIGHT_SIDEBAR_CASE_NAME)
        page.wait_not_visability_element(element=Notifications.PRELOADER)
        page.compare_text(element_text=element_text, message=AdminVerif.DEPARTMENT_CASE)

        page.check_counter_plus(first_counter=first_counter, second_counter=second_counter)

        return page

    @allure.feature('Admin page')
    @allure.title('Edit login')
    @DUsers.delete_user(user_login=LoginData.ADMIN_LOGIN)
    @DUsers.login_logout_user(user_login=LoginData.SUPER_LOGIN, user_password=LoginData.SUPER_PASSWORD,
                              page_name='admin')
    def test_admin_015(self, page, url):
        """https://knoxygen.atlassian.net/wiki/spaces/WA/pages/3588063398/Auto+Admin.015"""
        page.wait_visability_element(element=AdminLocators.ADD_BUTTON)
        page.wait_not_visability_element(element=Notifications.PRELOADER)
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
        page.click_element(element=AdminLocators.RIGHT_SIDEBAR_EDIT_BUTTON)
        element = page.find_element(element=AdminLocators.LOGIN_FIELD)
        page.check_disable_element(element=element)

        page.click_element(element=AdminLocators.CANCEL_BUTTON)

        return page

    @allure.feature('Admin page')
    @allure.title('Edit firstname and lastname')
    @DUsers.delete_user(user_login=LoginData.ADMIN_LOGIN)
    @DUsers.login_logout_user(user_login=LoginData.SUPER_LOGIN, user_password=LoginData.SUPER_PASSWORD,
                              page_name='admin')
    def test_admin_016(self, page, url):
        """https://knoxygen.atlassian.net/wiki/spaces/WA/pages/3588063409/Auto+Admin.016"""
        page.wait_visability_element(element=AdminLocators.ADD_BUTTON)
        page.wait_not_visability_element(element=Notifications.PRELOADER)
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
        page.click_element(element=AdminLocators.RIGHT_SIDEBAR_EDIT_BUTTON)
        page.clear_element(element=AdminLocators.FIRST_NAME)
        page.clear_element(element=AdminLocators.LAST_NAME)
        page.write_in_element(element=AdminLocators.FIRST_NAME, text=LoginData.NEW_FIRST_NAME)
        page.write_in_element(element=AdminLocators.LAST_NAME, text=LoginData.NEW_LAST_NAME)
        page.click_element(element=AdminLocators.FINAL_ADD)

        page.wait_visability_element(element=Notifications.BLUE_NOTIFI_2)
        element_text = page.get_text_element(element=Notifications.BLUE_NOTIFI_2)
        page.compare_text(element_text=element_text, message=AdminVerif.SAVE_CHANGES)
        page.click_element(element=Notifications.NOTIFI_CLOSE_2)

        page.write_in_element(element=AdminLocators.SEARCH, text=LoginData.ADMIN_LOGIN)
        page.press_enter()
        page.wait_visability_element(AdminLocators.GRID_LOGIN)
        param_list = page.get_grid_user_parameters(arg1=AdminLocators.GRID_LOGIN,
                                                   arg2=AdminLocators.GRID_STATUS,
                                                   arg3=AdminLocators.GRID_FNAME,
                                                   arg4=AdminLocators.GRID_LNAME)
        page.check_grid_user_parameters(parameters=param_list, check_parameters=AdminVerif.NEW_ADMIN_PARAM)
        first_name = page.get_text_element(element=AdminLocators.RIGHT_SIDEBAR_FIRST_NAME)
        page.compare_text(element_text=first_name, message=AdminVerif.NEW_FIRST_NAME)
        first_name = page.get_text_element(element=AdminLocators.RIGHT_SIDEBAR_LAST_NAME)
        page.compare_text(element_text=first_name, message=AdminVerif.NEW_LAST_NAME)

        return page

    @allure.feature('Admin page')
    @allure.title('Edit password')
    @DUsers.delete_user(user_login=LoginData.ADMIN_LOGIN)
    @DUsers.login_logout_user(user_login=LoginData.SUPER_LOGIN, user_password=LoginData.SUPER_PASSWORD,
                              page_name='admin')
    def test_admin_017(self, page, url):
        """https://knoxygen.atlassian.net/wiki/spaces/WA/pages/3588063420/Auto+Admin.017"""
        page.wait_visability_element(element=AdminLocators.ADD_BUTTON)
        page.wait_not_visability_element(element=Notifications.PRELOADER)
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
        page.click_element(element=AdminLocators.RIGHT_SIDEBAR_EDIT_BUTTON)
        page.click_element(element=AdminLocators.CHANGE_PASSWORD)
        page.write_in_element(element=AdminLocators.PASSWORD_FIELD, text=LoginData.NEW_PASSWORD)
        page.write_in_element(element=AdminLocators.PASSWORD_COPY_FIELD, text=LoginData.NEW_PASSWORD)
        page.click_element(element=AdminLocators.FINAL_ADD)

        page.wait_visability_element(element=Notifications.BLUE_NOTIFI_2)
        page.click_element(element=Notifications.NOTIFI_CLOSE_2)

        page.hover_on_element(element=TopBars.RIGHT_BAR)
        page.wait_element_is_clickable(element=TopBars.EXIT_BUTTON)
        page.click_element(element=TopBars.EXIT_BUTTON)

        page.wait_visability_element(element=LoginLocators.LOGIN_BUTTON)
        page.write_in_element(element=LoginLocators.LOGIN_FIELD, text=LoginData.ADMIN_LOGIN)
        page.write_in_element(element=LoginLocators.PASSWORD_FIELD, text=LoginData.NEW_PASSWORD)
        page.click_element(element=LoginLocators.LOGIN_BUTTON)

        page.wait_visability_element(element=CasesLocators.ADD_CASE_BUTTON)
        page.check_name_of_tab(name_of_tab=CasesVerif.NAME_OF_TAB)

    @allure.feature('Admin page')
    @allure.title('Edit firstname and lastname negative case')
    @DEntities.delete_all_entities()
    @DUsers.delete_user(user_login=LoginData.ADMIN_LOGIN)
    @DUsers.login_logout_user(user_login=LoginData.SUPER_LOGIN, user_password=LoginData.SUPER_PASSWORD,
                              page_name='admin')
    def test_admin_018(self, page, url):
        """https://knoxygen.atlassian.net/wiki/spaces/WA/pages/3588063431"""
        page.wait_visability_element(element=AdminLocators.ADD_BUTTON)
        page.wait_not_visability_element(element=Notifications.PRELOADER)
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
        page.click_element(element=AdminLocators.RIGHT_SIDEBAR_EDIT_BUTTON)
        page.clear_element(element=AdminLocators.FIRST_NAME)
        page.write_in_element(element=AdminLocators.FIRST_NAME, text=' ')
        page.clear_element(element=AdminLocators.LAST_NAME)
        page.write_in_element(element=AdminLocators.LAST_NAME, text=' ')

        page.click_element(element=AdminLocators.FINAL_ADD)

        page.wait_visability_element(element=AdminLocators.REG_NOTIFI)
        text = page.get_text_element(element=AdminLocators.REG_NOTIFI)
        page.compare_text(element_text=text, message=AdminVerif.REG_NOTIFI_3)
        page.click_element(element=AdminLocators.NOTIFI_OK)

        page.click_element(element=AdminLocators.CANCEL_BUTTON)

        return page

    @allure.feature('Admin page')
    @allure.title('Edit password negative cases')
    @pytest.mark.parametrize('param', ['rus', 'Login12', 'ibnb', 'Vibnb', 'VibnbBBB1', 'Vibnb4'])
    @DUsers.delete_user_param(user_login=LoginData.ADMIN_LOGIN)
    @DUsers.login_logout_user_param(user_login=LoginData.SUPER_LOGIN, user_password=LoginData.SUPER_PASSWORD,
                                    page_name='admin')
    def test_admin_019(self, page, url, param):
        """https://knoxygen.atlassian.net/wiki/spaces/WA/pages/3588063442"""
        page.wait_visability_element(element=AdminLocators.ADD_BUTTON)
        page.wait_not_visability_element(element=Notifications.PRELOADER)
        page.click_element(element=AdminLocators.ADD_BUTTON)

        page.wait_visability_element(element=AdminLocators.ADD_SECTION)
        page.write_in_element(element=AdminLocators.LOGIN_FIELD, text=LoginData.ADMIN_LOGIN)
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

        page.click_element(element=AdminLocators.RIGHT_SIDEBAR_EDIT_BUTTON)
        page.click_element(element=AdminLocators.CHANGE_PASSWORD)
        if param == 'rus':
            page.write_in_element(element=AdminLocators.PASSWORD_FIELD, text="Пароль32")
            page.write_in_element(element=AdminLocators.PASSWORD_COPY_FIELD, text="Пароль32")
        else:
            page.write_in_element(element=AdminLocators.PASSWORD_FIELD, text=param)
            page.write_in_element(element=AdminLocators.PASSWORD_COPY_FIELD, text=param)

        page.click_element(element=AdminLocators.FINAL_ADD)

        page.wait_visability_element(element=AdminLocators.REG_NOTIFI)
        text = page.get_text_element(element=AdminLocators.REG_NOTIFI)
        page.compare_text(element_text=text, message=AdminVerif.REG_NOTIFI_7)
        page.click_element(element=AdminLocators.NOTIFI_OK)

        page.click_element(element=AdminLocators.CANCEL_BUTTON)

        return page

    @allure.feature('Admin page')
    @allure.title('Edit user status cases')
    @pytest.mark.parametrize('param', [(1, 2, CasesVerif.EXPERT_STATUS), (1, 4, CasesVerif.LOAD_STATUS),
                                       (2, 4, CasesVerif.LOAD_STATUS), (2, 1, CasesVerif.ADMIN_STATUS),
                                       (4, 4, CasesVerif.LOAD_STATUS), (4, 4, CasesVerif.LOAD_STATUS)])
    @DUsers.delete_users_param(users_login_list=[LoginData.ADMIN_LOGIN, LoginData.EXPERT_LOGIN, LoginData.LOAD_LOGIN])
    @DUsers.login_logout_user_param(user_login=LoginData.SUPER_LOGIN, user_password=LoginData.SUPER_PASSWORD,
                                    page_name='admin')
    def test_admin_020_025(self, page, url, param: list):
        """https://knoxygen.atlassian.net/wiki/spaces/WA/pages/3588063453"""
        page.wait_visability_element(element=AdminLocators.ADD_BUTTON)
        page.wait_not_visability_element(element=Notifications.PRELOADER)
        page.click_element(element=AdminLocators.ADD_BUTTON)
        page.wait_visability_element(element=AdminLocators.ADD_SECTION)

        page.write_in_element(element=AdminLocators.LOGIN_FIELD, text=LoginData.ADMIN_LOGIN)
        element = page.find_element(element=AdminLocators.SELECT_STATUS)
        page.select_status(element=element, ind=param[0])
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

        page.click_element(element=AdminLocators.RIGHT_SIDEBAR_EDIT_BUTTON)
        element = page.find_element(element=AdminLocators.SELECT_STATUS)
        if param[0] == 4:
            page.check_disable_element(element=element)
        else:
            page.select_status(element=element, ind=param[1])
        page.click_element(element=AdminLocators.FINAL_ADD)

        page.hover_on_element(element=TopBars.RIGHT_BAR)
        page.wait_visability_element(element=TopBars.EXIT_BUTTON)
        page.click_element(element=TopBars.EXIT_BUTTON)
        page.wait_visability_element(element=LoginLocators.LOGIN_BUTTON)

        page.wait_visability_element(element=LoginLocators.LOGIN_FIELD)
        page.write_in_element(element=LoginLocators.LOGIN_FIELD, text=LoginData.ADMIN_LOGIN)
        page.write_in_element(element=LoginLocators.PASSWORD_FIELD, text=LoginData.PASSWORD)
        page.click_element(element=LoginLocators.LOGIN_BUTTON)

        page.wait_visability_element(element=TopBars.USER_STATUS)
        text_element = page.get_text_element(element=TopBars.USER_STATUS)
        page.check_logged_status(text_element=text_element, check_string=param[2])
        page.check_name_of_tab(name_of_tab=CasesVerif.NAME_OF_TAB)

        if param[2] == CasesVerif.LOAD_STATUS:
            page.hover_on_element(element=TopBars.RIGHT_BAR_LOAD)
            page.wait_visability_element(element=TopBars.EXIT_BUTTON)
            page.click_element(element=TopBars.EXIT_BUTTON)
            page.wait_visability_element(element=LoginLocators.LOGIN_BUTTON)
            return False

        return page

    @allure.feature('Admin page')
    @allure.title('Create user with different statuses, appointment department and authorization')
    @pytest.mark.parametrize('param', [(1, CasesVerif.ADMIN_STATUS), (2, CasesVerif.EXPERT_STATUS),
                                       (4, CasesVerif.LOAD_STATUS)])
    @parametrize_test_26
    @DUsers.login_logout_user_param(user_login=LoginData.SUPER_LOGIN, user_password=LoginData.SUPER_PASSWORD,
                                    page_name='admin')
    def test_admin_026_028(self, page, url, param: list):
        """https://knoxygen.atlassian.net/wiki/spaces/WA/pages/3588063519"""
        page.wait_visability_element(element=AdminLocators.ADD_BUTTON)
        page.wait_not_visability_element(element=Notifications.PRELOADER)
        page.click_element(element=AdminLocators.ADD_BUTTON)
        page.wait_visability_element(element=AdminLocators.ADD_SECTION)

        page.write_in_element(element=AdminLocators.LOGIN_FIELD, text=LoginData.ADMIN_LOGIN)
        element = page.find_element(element=AdminLocators.SELECT_STATUS)
        page.select_status(element=element, ind=param[0])
        page.write_in_element(element=AdminLocators.FIRST_NAME, text=LoginData.FIRST_NAME)
        page.write_in_element(element=AdminLocators.LAST_NAME, text=LoginData.LAST_NAME)
        page.write_in_element(element=AdminLocators.PASSWORD_FIELD, text=LoginData.PASSWORD)
        page.write_in_element(element=AdminLocators.PASSWORD_COPY_FIELD, text=LoginData.PASSWORD)

        page.click_element(element=AdminLocators.DEPARTMENTS_1ST_DEP)

        page.click_element(element=AdminLocators.FINAL_ADD)

        page.hover_on_element(element=TopBars.RIGHT_BAR)

        page.wait_visability_element(element=TopBars.EXIT_BUTTON)
        page.click_element(element=TopBars.EXIT_BUTTON)
        page.wait_visability_element(element=LoginLocators.LOGIN_BUTTON)

        page.wait_visability_element(element=LoginLocators.LOGIN_FIELD)
        page.write_in_element(element=LoginLocators.LOGIN_FIELD, text=LoginData.ADMIN_LOGIN)
        page.write_in_element(element=LoginLocators.PASSWORD_FIELD, text=LoginData.PASSWORD)
        page.click_element(element=LoginLocators.LOGIN_BUTTON)

        page.wait_visability_element(element=TopBars.USER_STATUS)
        text_element = page.get_text_element(element=TopBars.USER_STATUS)
        page.check_logged_status(text_element=text_element, check_string=param[1])
        page.check_name_of_tab(name_of_tab=CasesVerif.NAME_OF_TAB)

        page.check_element_contains_text(element=CasesLocators.TEST_CASE_1)

        if param[1] == CasesVerif.LOAD_STATUS:
            page.hover_on_element(element=TopBars.RIGHT_BAR_LOAD)
            page.wait_visability_element(element=TopBars.EXIT_BUTTON)
            page.click_element(element=TopBars.EXIT_BUTTON)
            page.wait_visability_element(element=LoginLocators.LOGIN_BUTTON)
            return False

        return page

    @allure.feature('Admin page')
    @allure.title('Delete users with different statuses from department and authorization')
    @pytest.mark.parametrize('param', [(LoginData.ADMIN_LOGIN, LoginData.PASSWORD,
                                        LoginData.STATUS_ADMIN),
                                       (LoginData.EXPERT_LOGIN, LoginData.PASSWORD,
                                        LoginData.STATUS_EXPERT),
                                       (LoginData.LOAD_LOGIN, LoginData.PASSWORD,
                                        LoginData.STATUS_LOAD)])
    @parametrize_test_29
    @DUsers.login_logout_user_param(user_login=LoginData.SUPER_LOGIN, user_password=LoginData.SUPER_PASSWORD,
                                    page_name='admin')
    def test_admin_029_031(self, page, url, param):
        """https://knoxygen.atlassian.net/wiki/spaces/WA/pages/3588063552/Auto+Admin.029"""
        page.wait_visability_element(element=AdminLocators.SEARCH)
        page.write_in_element(element=AdminLocators.SEARCH, text=param[0])
        page.press_enter()

        page.wait_visability_element(element=AdminLocators.RIGHT_SIDEBAR_EDIT_BUTTON)
        page.wait_not_visability_element(element=Notifications.PRELOADER)

        page.click_element(element=AdminLocators.RIGHT_SIDEBAR_EDIT_BUTTON)

        page.click_element(element=AdminLocators.DEPARTMENTS_1ST_DEP)

        page.click_element(element=AdminLocators.FINAL_ADD)

        page.hover_on_element(element=TopBars.RIGHT_BAR)
        page.wait_visability_element(element=TopBars.EXIT_BUTTON)
        page.click_element(element=TopBars.EXIT_BUTTON)
        page.wait_visability_element(element=LoginLocators.LOGIN_BUTTON)

        page.write_in_element(element=LoginLocators.LOGIN_FIELD, text=param[0])
        page.write_in_element(element=LoginLocators.PASSWORD_FIELD,
                              text=param[1])
        page.click_element(element=LoginLocators.LOGIN_BUTTON)

        if param[2] == LoginData.STATUS_LOAD:
            page.wait_visability_element(element=TopBars.RIGHT_BAR_LOAD)
        else:
            page.wait_visability_element(element=TopBars.RIGHT_BAR)

        page.check_name_of_tab(name_of_tab=CasesVerif.NAME_OF_TAB)
        if param[0] == LoginData.ADMIN_LOGIN:
            page.wait_visability_element(element=CasesLocators.TEST_CASE_1)
            page.check_element_contains_text(element=CasesLocators.TEST_CASE_1)
        else:
            page.check_element_contains_text_disappeared(element=CasesLocators.TEST_CASE_1)

        if param[2] == LoginData.STATUS_LOAD:
            page.hover_on_element(element=TopBars.RIGHT_BAR_LOAD)
            page.wait_visability_element(element=TopBars.EXIT_BUTTON)
            page.click_element(element=TopBars.EXIT_BUTTON)
            page.wait_visability_element(element=LoginLocators.LOGIN_BUTTON)
            return False

        return page

    @allure.feature('Admin page')
    @allure.title('Account suspension and login')
    @DUsers.add_delete_user()
    @DUsers.login_logout_user(user_login=LoginData.SUPER_LOGIN, user_password=LoginData.SUPER_PASSWORD,
                              page_name='admin')
    def test_admin_032(self, page, url):
        """https://knoxygen.atlassian.net/wiki/spaces/WA/pages/3588063585/Auto+Admin.032"""
        page.wait_visability_element(element=AdminLocators.SEARCH)
        page.write_in_element(element=AdminLocators.SEARCH, text=LoginData.ADMIN_LOGIN)
        page.press_enter()

        page.wait_visability_element(element=AdminLocators.RIGHT_SIDEBAR_EDIT_BUTTON)
        page.wait_not_visability_element(element=Notifications.PRELOADER)

        page.click_element(element=AdminLocators.RIGHT_SIDEBAR_EDIT_BUTTON)

        page.wait_visability_element(element=AdminLocators.DEACTIVATE_ACCOUNT)
        page.click_element(element=AdminLocators.DEACTIVATE_ACCOUNT)

        page.click_element(element=AdminLocators.FINAL_ADD)

        page.hover_on_element(element=TopBars.RIGHT_BAR)
        page.wait_visability_element(element=TopBars.EXIT_BUTTON)
        page.click_element(element=TopBars.EXIT_BUTTON)
        page.wait_visability_element(element=LoginLocators.LOGIN_BUTTON)

        page.wait_visability_element(element=LoginLocators.LOGIN_FIELD)
        page.write_in_element(element=LoginLocators.LOGIN_FIELD, text=LoginData.ADMIN_LOGIN)
        page.write_in_element(element=LoginLocators.PASSWORD_FIELD, text=LoginData.PASSWORD)
        page.click_element(element=LoginLocators.LOGIN_BUTTON)

        page.wait_visability_element(element=LoginLocators.NOTIFICATION)
        element_text = page.get_text_element(element=LoginLocators.NOTIFICATION)
        page.compare_text(element_text=element_text, message=LoginVerif.DEACTIVATE_ACCOUNT_NOTIFICATION)

    @allure.feature('Admin page')
    @allure.title('User search')
    @DUsers.add_delete_user()
    @DUsers.login_logout_user(user_login=LoginData.SUPER_LOGIN, user_password=LoginData.SUPER_PASSWORD,
                              page_name='admin')
    def test_admin_033(self, page, url):
        """https://knoxygen.atlassian.net/wiki/spaces/WA/pages/3588063596/Auto+Admin.033"""
        page.wait_visability_element(element=AdminLocators.SEARCH)
        page.write_in_element(element=AdminLocators.SEARCH, text=LoginData.HALF_LOGIN)
        page.press_enter()

        page.wait_visability_element(element=AdminLocators.GRID_LOGIN)
        element_text = page.get_text_element(AdminLocators.GRID_LOGIN)
        page.compare_text(element_text=element_text, message=LoginData.ADMIN_LOGIN)
        page.clear_element(element=AdminLocators.SEARCH)

        page.write_in_element(element=AdminLocators.SEARCH, text=LoginData.HALF_NAME)
        page.press_enter()

        page.wait_visability_element(element=AdminLocators.GRID_FNAME)
        element_text = page.get_text_element(AdminLocators.GRID_FNAME)
        page.compare_text(element_text=element_text, message=LoginData.FIRST_NAME)
        page.clear_element(element=AdminLocators.SEARCH)

        page.write_in_element(element=AdminLocators.SEARCH, text=LoginData.HALF_LAST_NAME)
        page.press_enter()

        page.wait_visability_element(element=AdminLocators.GRID_LNAME)
        element_text = page.get_text_element(AdminLocators.GRID_LNAME)
        page.compare_text(element_text=element_text, message=LoginData.LAST_NAME)
        return page

    @allure.feature('Admin page')
    @allure.title('Appointment case and authorization')
    @DUsers.delete_user(user_login=LoginData.ADMIN_LOGIN)
    @DCases.add_delete_cases(cases_name_list=[DepartmentsData.CASE_NAME_1, DepartmentsData.CASE_NAME_2,
                                              DepartmentsData.CASE_NAME_3])
    @DUsers.login_logout_user(user_login=LoginData.SUPER_LOGIN, user_password=LoginData.SUPER_PASSWORD,
                              page_name='admin')
    def test_admin_034(self, page, url):
        """https://knoxygen.atlassian.net/wiki/spaces/WA/pages/3588063607/Auto+Admin.034"""
        page.wait_visability_element(element=AdminLocators.ADD_BUTTON)
        page.wait_not_visability_element(element=Notifications.PRELOADER)

        page.click_element(element=AdminLocators.ADD_BUTTON)
        page.wait_visability_element(element=AdminLocators.ADD_SECTION)

        page.write_in_element(element=AdminLocators.LOGIN_FIELD, text=LoginData.ADMIN_LOGIN)
        element = page.find_element(element=AdminLocators.SELECT_STATUS)
        page.select_status(element=element, ind=1)
        page.write_in_element(element=AdminLocators.FIRST_NAME, text=LoginData.FIRST_NAME)
        page.write_in_element(element=AdminLocators.LAST_NAME, text=LoginData.LAST_NAME)
        page.write_in_element(element=AdminLocators.PASSWORD_FIELD, text=LoginData.PASSWORD)
        page.write_in_element(element=AdminLocators.PASSWORD_COPY_FIELD, text=LoginData.PASSWORD)

        page.click_element(element=AdminLocators.CASE_RIGHTS)
        page.click_element(element=AdminLocators.SORT_CASES)
        page.click_element(element=AdminLocators.CASES_1ST_CASE)
        page.click_element(element=AdminLocators.CASES_2ND_CASE)
        page.click_element(element=AdminLocators.CASES_3RD_CASE)
        page.click_element(element=AdminLocators.FINAL_ADD)
        page.wait_visability_element(element=Notifications.BLUE_NOTIFI)
        element_text = page.get_text_element(element=Notifications.BLUE_NOTIFI)
        page.compare_text(element_text=element_text, message=AdminVerif.ADDED_USER)
        page.click_element(element=Notifications.NOTIFI_CLOSE)

        page.hover_on_element(element=TopBars.RIGHT_BAR)
        page.wait_visability_element(element=TopBars.EXIT_BUTTON)
        page.click_element(element=TopBars.EXIT_BUTTON)
        page.wait_visability_element(element=LoginLocators.LOGIN_BUTTON)

        page.wait_visability_element(element=LoginLocators.LOGIN_FIELD)
        page.write_in_element(element=LoginLocators.LOGIN_FIELD, text=LoginData.ADMIN_LOGIN)
        page.write_in_element(element=LoginLocators.PASSWORD_FIELD, text=LoginData.PASSWORD)
        page.click_element(element=LoginLocators.LOGIN_BUTTON)

        page.wait_visability_element(element=CasesLocators.TEST_CASE_1)
        page.check_element_contains_text(element=CasesLocators.TEST_CASE_1)
        page.check_element_contains_text(element=CasesLocators.TEST_CASE_2)
        page.check_element_contains_text(element=CasesLocators.TEST_CASE_3)

        return page

    @allure.feature('Admin page')
    @allure.title('Disappointment cases and authorization')
    @DUsers.delete_user(user_login=LoginData.ADMIN_LOGIN)
    @DCases.add_delete_cases(cases_name_list=[DepartmentsData.CASE_NAME_1, DepartmentsData.CASE_NAME_2,
                                              DepartmentsData.CASE_NAME_3])
    @DUsers.add_delete_user_with_cases()
    @DUsers.login_logout_user(user_login=LoginData.SUPER_LOGIN, user_password=LoginData.SUPER_PASSWORD,
                              page_name='admin')
    def test_admin_035(self, page, url):
        """https://knoxygen.atlassian.net/wiki/spaces/WA/pages/3588063618/Auto+Admin.035"""
        page.wait_visability_element(element=AdminLocators.SEARCH)
        page.write_in_element(element=AdminLocators.SEARCH, text=LoginData.ADMIN_LOGIN)
        page.press_enter()

        page.wait_visability_element(element=AdminLocators.RIGHT_SIDEBAR_EDIT_BUTTON)
        page.wait_not_visability_element(element=Notifications.PRELOADER)
        page.click_element(element=AdminLocators.RIGHT_SIDEBAR_EDIT_BUTTON)

        page.click_element(element=AdminLocators.CASES_1ST_CASE)
        page.click_element(element=AdminLocators.CASES_2ND_CASE)
        page.click_element(element=AdminLocators.CASES_3RD_CASE)

        page.click_element(element=AdminLocators.CASE_RIGHTS)

        page.click_element(element=AdminLocators.FINAL_ADD)

        page.wait_visability_element(element=Notifications.BLUE_NOTIFI)
        element_text = page.get_text_element(element=Notifications.BLUE_NOTIFI)
        page.compare_text(element_text=element_text, message=AdminVerif.SAVE_CHANGES)
        page.click_element(element=Notifications.NOTIFI_CLOSE)

        page.hover_on_element(element=TopBars.RIGHT_BAR)
        page.wait_visability_element(element=TopBars.EXIT_BUTTON)
        page.click_element(element=TopBars.EXIT_BUTTON)
        page.wait_visability_element(element=LoginLocators.LOGIN_BUTTON)

        page.wait_visability_element(element=LoginLocators.LOGIN_FIELD)
        page.write_in_element(element=LoginLocators.LOGIN_FIELD, text=LoginData.ADMIN_LOGIN)
        page.write_in_element(element=LoginLocators.PASSWORD_FIELD,
                              text=LoginData.PASSWORD)
        page.click_element(element=LoginLocators.LOGIN_BUTTON)

        page.wait_visability_element(element=CasesLocators.DB_CASE)
        page.check_element_contains_text(element=CasesLocators.DB_CASE)

        return page

    @allure.feature('Admin page')
    @allure.title('Sort cases')
    @DEntities.delete_all_entities()
    @DCases.add_delete_cases(cases_name_list=['1', '10', 'A', 'G', 'Z', 'g', 'z', 'Я', 'й', 'А', 'я', 'a'])
    @DDepartment.add_delete_departments(departments_names_list=['3', '34', 'Н', 'Я', 'А', 'а', 'я', 'н', 'F', 'Z',
                                                                'A', 'a', 'z', 'f'])
    @DUsers.login_logout_user(user_login=LoginData.SUPER_LOGIN, user_password=LoginData.SUPER_PASSWORD,
                              page_name='admin')
    def test_admin_036(self, page, url):
        """https://knoxygen.atlassian.net/wiki/spaces/WA/pages/3588063629/Auto+Admin.036"""
        page.wait_visability_element(element=AdminLocators.ADD_BUTTON)
        page.wait_not_visability_element(element=Notifications.PRELOADER)
        page.click_element(element=AdminLocators.ADD_BUTTON)
        page.wait_visability_element(element=AdminLocators.ADD_SECTION)

        page.click_element(element=AdminLocators.CASE_RIGHTS)

        unsorted_list = page.get_item_list(element=AdminLocators.CASES_1ST_CASE)
        sorted_1 = unsorted_list.copy()
        sorted_1.sort()

        page.click_element(element=AdminLocators.SORT_CASES)
        sorted_2 = page.get_item_list(element=AdminLocators.CASES_1ST_CASE)

        page.compare_lists(list_1=sorted_1, list_2=sorted_2)

        page.click_element(element=AdminLocators.SORT_CASES)

        unsorted_2 = page.get_item_list(element=AdminLocators.CASES_1ST_CASE)

        page.compare_lists(list_1=unsorted_list, list_2=unsorted_2)

        page.click_element(element=AdminLocators.CANCEL_BUTTON)

        return page

    @allure.feature('Admin page')
    @allure.title('Check box working in case and department sections')
    @DCases.add_delete_cases(cases_name_list=[DepartmentsData.CASE_NAME_1, DepartmentsData.CASE_NAME_2,
                                              DepartmentsData.CASE_NAME_3])
    @DDepartment.add_delete_departments(
        departments_names_list=[DepartmentsData.DEPARTMENT_NAME_1, DepartmentsData.DEPARTMENT_NAME_2,
                                DepartmentsData.DEPARTMENT_NAME_3])
    @DUsers.add_delete_user()
    @DUsers.login_logout_user(user_login=LoginData.SUPER_LOGIN, user_password=LoginData.SUPER_PASSWORD,
                              page_name='admin')
    def test_admin_037(self, page, url):
        """https://knoxygen.atlassian.net/wiki/spaces/WA/pages/3588063640/Auto+Admin.037"""
        page.wait_visability_element(element=AdminLocators.SEARCH)
        page.write_in_element(element=AdminLocators.SEARCH, text=LoginData.ADMIN_LOGIN)
        page.press_enter()

        page.wait_visability_element(element=AdminLocators.RIGHT_SIDEBAR_EDIT_BUTTON)
        page.wait_not_visability_element(element=Notifications.PRELOADER)

        page.click_element(element=AdminLocators.RIGHT_SIDEBAR_EDIT_BUTTON)

        page.click_element(element=AdminLocators.DEPARTMENTS_CHECKBOX)

        page.click_element(element=AdminLocators.CASE_RIGHTS)
        page.click_element(element=AdminLocators.CASES_CHECKBOX)

        page.click_element(element=AdminLocators.FINAL_ADD)

        page.wait_visability_element(element=Notifications.BLUE_NOTIFI)
        element_text = page.get_text_element(element=Notifications.BLUE_NOTIFI)
        page.compare_text(element_text=element_text, message=AdminVerif.SAVE_CHANGES)
        page.click_element(element=Notifications.NOTIFI_CLOSE)

        page.wait_visability_element(element=AdminLocators.SEARCH)
        page.write_in_element(element=AdminLocators.SEARCH, text=LoginData.ADMIN_LOGIN)
        page.press_enter()

        page.wait_element_is_clickable(element=AdminLocators.RIGHT_SIDEBAR_DEPARTMENT)
        page.click_element(element=AdminLocators.RIGHT_SIDEBAR_DEPARTMENT)
        page.wait_visability_element(element=AdminLocators.RIGHT_SIDEBAR_DEPARTMENT_NAME)
        elements_list = page.get_item_list(element=AdminLocators.RIGHT_SIDEBAR_DEPARTMENT_NAME)
        page.check_length_of_list(elements_list=elements_list, greater=True)

        page.click_element(element=AdminLocators.RIGHT_SIDEBAR_CASE)
        page.wait_visability_element(element=AdminLocators.RIGHT_SIDEBAR_CASE_NAME)
        elements_list = page.get_item_list(element=AdminLocators.RIGHT_SIDEBAR_CASE_NAME)
        page.check_length_of_list(elements_list=elements_list, greater=True)

        page.wait_visability_element(element=AdminLocators.RIGHT_SIDEBAR_EDIT_BUTTON)
        page.wait_not_visability_element(element=Notifications.PRELOADER)

        page.click_element(element=AdminLocators.RIGHT_SIDEBAR_EDIT_BUTTON)

        page.click_element(element=AdminLocators.DEPARTMENTS_CHECKBOX)

        page.click_element(element=AdminLocators.CASES_CHECKBOX)
        page.click_element(element=AdminLocators.CASE_RIGHTS)

        page.click_element(element=AdminLocators.FINAL_ADD)

        page.wait_visability_element(element=Notifications.BLUE_NOTIFI_2)
        page.click_element(element=Notifications.NOTIFI_CLOSE_2)

        page.wait_visability_element(element=AdminLocators.SEARCH)
        page.write_in_element(element=AdminLocators.SEARCH, text=LoginData.ADMIN_LOGIN)
        page.press_enter()

        page.click_element(element=AdminLocators.RIGHT_SIDEBAR_DEPARTMENT)
        page.wait_visability_element(element=AdminLocators.RIGHT_SIDEBAR_NO_DEPARTMENTS)
        element_text = page.get_text_element(element=AdminLocators.RIGHT_SIDEBAR_NO_DEPARTMENTS)
        page.compare_text(element_text=element_text, message=AdminVerif.NO_DEPARTMENTS)

        page.wait_visability_element(element=AdminLocators.RIGHT_SIDEBAR_CASE)
        page.click_element(element=AdminLocators.RIGHT_SIDEBAR_CASE)
        page.wait_visability_element(element=AdminLocators.RIGHT_SIDEBAR_NO_CASES)
        element_text = page.get_text_element(element=AdminLocators.RIGHT_SIDEBAR_NO_CASES)
        page.compare_text(element_text=element_text, message=AdminVerif.NO_CASES)

        return page

    @allure.feature('Admin page')
    @allure.title('Quick seach of case and department')
    @DDepartment.add_delete_departments(departments_names_list=[DepartmentsData.DEPARTMENT_NAME_1,
                                                                'Дополнительный отдел', 'Another department', '123'])
    @DCases.add_delete_cases(cases_name_list=[DepartmentsData.CASE_NAME_1, 'Дело о краже', 'Новое дело', '567'])
    @DUsers.add_delete_user()
    @DUsers.login_logout_user(user_login=LoginData.SUPER_LOGIN, user_password=LoginData.SUPER_PASSWORD,
                              page_name='admin')
    def test_admin_038(self, page, url):
        """https://knoxygen.atlassian.net/wiki/spaces/WA/pages/3588063651/Auto+Admin.038"""
        page.wait_visability_element(element=AdminLocators.SEARCH)
        page.wait_not_visability_element(element=Notifications.PRELOADER)

        page.write_in_element(element=AdminLocators.SEARCH, text=LoginData.ADMIN_LOGIN)
        page.press_enter()

        page.click_element(element=AdminLocators.RIGHT_SIDEBAR_EDIT_BUTTON)

        page.write_in_element(element=AdminLocators.DEPARTMENTS_SEARCH,
                              text=DepartmentsData.DEPARTMENT_NAME_1)

        page.click_element(element=AdminLocators.DEPARTMENTS_1ST_DEP)

        page.click_element(element=AdminLocators.CASE_RIGHTS)

        page.write_in_element(element=AdminLocators.CASES_SEARCH,
                              text=DepartmentsData.CASE_NAME_1)

        page.click_element(element=AdminLocators.CASES_1ST_CASE)

        page.click_element(element=AdminLocators.FINAL_ADD)

        page.wait_visability_element(element=Notifications.BLUE_NOTIFI)
        page.click_element(element=Notifications.NOTIFI_CLOSE)

        page.write_in_element(element=AdminLocators.SEARCH, text=LoginData.ADMIN_LOGIN)
        page.press_enter()

        page.click_element(element=AdminLocators.RIGHT_SIDEBAR_DEPARTMENT)
        page.wait_visability_element(element=AdminLocators.RIGHT_SIDEBAR_DEPARTMENT_NAME)
        element_text = page.get_text_element(element=AdminLocators.RIGHT_SIDEBAR_DEPARTMENT_NAME)
        page.compare_text(element_text=element_text, message=AdminVerif.DEPARTMENT_NAME)

        page.click_element(element=AdminLocators.RIGHT_SIDEBAR_CASE)
        page.wait_visability_element(element=AdminLocators.RIGHT_SIDEBAR_CASE_NAME)
        element_text = page.get_text_element(element=AdminLocators.RIGHT_SIDEBAR_CASE_NAME)
        page.compare_text(element_text=element_text, message=AdminVerif.DEPARTMENT_CASE)

        return page

    @allure.feature('Admin page')
    @allure.title('Delete user during user uses system')
    @DUsers.add_delete_user_with_cases()
    @DUsers.login_logout_user(user_login=LoginData.SUPER_LOGIN, user_password=LoginData.SUPER_PASSWORD,
                              page_name='admin')
    def test_admin_039(self, page, url):
        """https://knoxygen.atlassian.net/wiki/spaces/WA/pages/3588063662/Auto+Admin.039"""
        page.wait_visability_element(element=CasesLocators.ADD_CASE_BUTTON)

        url = ENV_HOST
        headers = API.api_user_login(url=url)
        users_dict = API.api_get_entity_dict(url=url, headers=headers, entity_type='user')
        user_id = API.api_get_added_entity_id_of_login(data=users_dict, entity_login=LoginData.ADMIN_LOGIN)
        API.api_delete_entity(url=url, entity_id=user_id, headers=headers, entity_type='user')
        API.api_user_logout(url=url, headers=headers)

        page.wait_visability_element(element=TopBars.DATA_BAR)
        page.hover_on_element(element=TopBars.DATA_BAR)
        page.wait_visability_element(element=TopBars.DROP_BLOCK_DEVICES)
        page.click_element(element=TopBars.DROP_BLOCK_DEVICES)

        page.wait_visability_element(element=DevicesLocators.COUNTER_SECTION)

        page.hover_on_element(element=TopBars.RIGHT_BAR)
        page.wait_visability_element(element=TopBars.EXIT_BUTTON)
        page.click_element(element=TopBars.EXIT_BUTTON)
        page.wait_visability_element(element=LoginLocators.LOGIN_BUTTON)

        page.wait_visability_element(element=LoginLocators.LOGIN_FIELD)
        page.write_in_element(element=LoginLocators.LOGIN_FIELD, text=LoginData.ADMIN_LOGIN)
        page.write_in_element(element=LoginLocators.PASSWORD_FIELD,
                              text=LoginData.PASSWORD)
        page.click_element(element=LoginLocators.LOGIN_BUTTON)

        page.wait_visability_element(element=LoginLocators.NOTIFICATION)
        element_text = page.get_text_element(element=LoginLocators.NOTIFICATION)
        page.compare_text(element_text=element_text, message=LoginVerif.LOGIN_PAGE_NOTIFICATION)

    @allure.feature('Admin page')
    @allure.title('Grid sorts')
    @DUsers.add_delete_user(user_login='4561', user_name='Антон', user_lastname=None, position='QA')
    @DUsers.add_delete_user(user_login='0000', user_name=None, user_lastname='Давыдов', position='Developer',
                            user_status=LoginData.STATUS_EXPERT)
    @DUsers.add_delete_user(user_login='02313', user_name='Игорь', user_lastname='Лозынин', position=None)
    @DUsers.add_delete_user(user_login='Glogin', user_name=None, user_lastname='Petrov', position=None)
    @DUsers.add_delete_user(user_login='Zlogin', user_name='Олег', position=None, user_status=LoginData.STATUS_EXPERT)
    @DUsers.add_delete_user(user_login='Alogin', user_status=LoginData.STATUS_LOAD)
    @DUsers.add_delete_user(user_login='flogin', user_name=None, user_lastname='Zhirnov', position='Manager')
    @DUsers.add_delete_user(user_login='jlogin', user_name='Stanislav', position=None,
                            user_status=LoginData.STATUS_EXPERT)
    @DUsers.add_delete_user(user_login='ylogin', user_name=None, user_lastname='Петров', position=' ')
    @DUsers.add_delete_user(user_login='Глогин', user_name='Максим', position=None)
    @DUsers.add_delete_user(user_login='Алогин', user_status=LoginData.STATUS_EXPERT)
    @DUsers.add_delete_user(user_login='Влогин', user_lastname='Шнягин', position=' ')
    @DUsers.add_delete_user(user_login='ялогин', position='DevOps', user_status=LoginData.STATUS_LOAD)
    @DUsers.add_delete_user(user_login='блогин', user_name='Nik', position=None, user_status=LoginData.STATUS_EXPERT)
    @DUsers.add_delete_user(user_login='ллогин', user_name='Zak', user_lastname='Koval', position=' ')
    @DUsers.login_logout_user(user_login=LoginData.SUPER_LOGIN, user_password=LoginData.SUPER_PASSWORD,
                              page_name='admin')
    def test_admin_040(self, page, url):
        """https://knoxygen.atlassian.net/wiki/spaces/WA/pages/3588063673/Auto+Admin.040"""
        page.wait_visability_element(element=AdminLocators.GRID_LOGIN)

        sorted_list = page.get_item_grid_list(element=AdminLocators.GRID_1ST_ROW, extra_locator=' > td')
        sorted_reverse_1 = sorted_list.copy()
        sorted_reverse_1.reverse()

        page.click_element(element=AdminLocators.GRID_SORT_LOGIN)
        time.sleep(1)
        page.wait_visability_element(element=AdminLocators.GRID_1ST_ROW)
        sorted_reverse_2 = page.get_item_grid_list(element=AdminLocators.GRID_1ST_ROW, extra_locator=' > td')

        page.compare_lists(list_1=sorted_reverse_1, list_2=sorted_reverse_2)

        page.click_element(element=AdminLocators.GRID_SORT_LOGIN)
        time.sleep(1)
        page.wait_visability_element(element=AdminLocators.GRID_1ST_ROW)
        sorted_2 = page.get_item_grid_list(element=AdminLocators.GRID_1ST_ROW, extra_locator=' > td')

        page.compare_lists(list_1=sorted_list, list_2=sorted_2)
        # сортировка имен
        page.click_element(element=AdminLocators.GRID_SORT_NAME)
        time.sleep(1)
        page.wait_visability_element(element=AdminLocators.GRID_1ST_ROW)
        sorted_list = page.get_item_grid_list(element=AdminLocators.GRID_1ST_ROW,
                                              extra_locator=' > td:nth-child(3)')
        sorted_reverse_1 = sorted_list.copy()
        sorted_reverse_1.reverse()
        page.click_element(element=AdminLocators.GRID_SORT_NAME)
        time.sleep(1)
        page.wait_visability_element(element=AdminLocators.GRID_1ST_ROW)
        sorted_reverse_2 = page.get_item_grid_list(element=AdminLocators.GRID_1ST_ROW,
                                                   extra_locator=' > td:nth-child(3)')

        page.compare_lists(list_1=sorted_reverse_1, list_2=sorted_reverse_2)

        page.click_element(element=AdminLocators.GRID_SORT_NAME)
        time.sleep(1)
        page.wait_visability_element(element=AdminLocators.GRID_1ST_ROW)
        sorted_2 = page.get_item_grid_list(element=AdminLocators.GRID_1ST_ROW,
                                           extra_locator=' > td:nth-child(3)')

        page.compare_lists(list_1=sorted_list, list_2=sorted_2)
        # сортировка фамалий
        page.click_element(element=AdminLocators.GRID_SORT_LASTNAME)
        time.sleep(1)
        page.wait_visability_element(element=AdminLocators.GRID_1ST_ROW)
        sorted_list = page.get_item_grid_list(element=AdminLocators.GRID_1ST_ROW,
                                              extra_locator=' > td:nth-child(4)')
        sorted_reverse_1 = sorted_list.copy()
        sorted_reverse_1.reverse()
        page.click_element(element=AdminLocators.GRID_SORT_LASTNAME)
        time.sleep(1)
        page.wait_visability_element(element=AdminLocators.GRID_1ST_ROW)
        sorted_reverse_2 = page.get_item_grid_list(element=AdminLocators.GRID_1ST_ROW,
                                                   extra_locator=' > td:nth-child(4)')

        page.compare_lists(list_1=sorted_reverse_1, list_2=sorted_reverse_2)

        page.click_element(element=AdminLocators.GRID_SORT_LASTNAME)
        time.sleep(1)
        page.wait_visability_element(element=AdminLocators.GRID_1ST_ROW)
        sorted_2 = page.get_item_grid_list(element=AdminLocators.GRID_1ST_ROW,
                                           extra_locator=' > td:nth-child(4)')

        page.compare_lists(list_1=sorted_list, list_2=sorted_2)
        # сортировка должностей
        page.click_element(element=AdminLocators.GRID_SORT_POSITION)
        time.sleep(1)
        page.wait_visability_element(element=AdminLocators.GRID_1ST_ROW)
        sorted_list = page.get_item_grid_list(element=AdminLocators.GRID_1ST_ROW,
                                              extra_locator=' > td:nth-child(5)')
        sorted_reverse_1 = sorted_list.copy()
        sorted_reverse_1.reverse()
        page.click_element(element=AdminLocators.GRID_SORT_POSITION)
        time.sleep(1)
        page.wait_visability_element(element=AdminLocators.GRID_1ST_ROW)
        sorted_reverse_2 = page.get_item_grid_list(element=AdminLocators.GRID_1ST_ROW,
                                                   extra_locator=' > td:nth-child(5)')

        page.compare_lists(list_1=sorted_reverse_1, list_2=sorted_reverse_2)

        page.click_element(element=AdminLocators.GRID_SORT_POSITION)
        time.sleep(1)
        page.wait_visability_element(element=AdminLocators.GRID_1ST_ROW)
        sorted_2 = page.get_item_grid_list(element=AdminLocators.GRID_1ST_ROW,
                                           extra_locator=' > td:nth-child(5)')

        page.compare_lists(list_1=sorted_list, list_2=sorted_2)

        return page

    @allure.feature('Admin page')
    @allure.title('Clean monitor')
    @DUsers.logout_all_users()
    def test_z_clean_monitor(self, browser, url):
        pass
