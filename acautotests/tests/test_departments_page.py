import time
from functools import wraps

import pytest

import API

from Pages.DepartmentsPage import DepartmentsPage
from tests.decorators import DUsers, DDepartment, DEntities, DCases
from locators import AdminLocators, Notifications, DepartmentsLocators, TopBars, LoginLocators, \
    CasesLocators, LoadImagesLocators, DevicesLocators
from data import LoginData, DepartmentsData, LoadImagesData, DevicesData, CasesData
from verification import DepartmentsVerif, CasesVerif, LoadImagesVerif, DevicesVerif
import allure


@pytest.mark.department
@pytest.mark.noload
class TestDepartmentPage:
    @staticmethod
    def prepare_for_test_010(case_name, department_name):
        def setup(func):
            wraps(func)

            def inner(self, browser, url):
                headers = None

                try:
                    user_id = None
                    case_id = None
                    department_id = None

                    try:
                        headers = API.api_user_login(url=url)
                        user_id = API.api_add_entity(url=url, headers=headers, entity_type='user')
                        case_id = API.api_add_entity(url=url, headers=headers, entity_type='case', case_name=case_name)
                        department_id = API.api_add_entity(url=url, headers=headers,
                                                           entity_type='department', department_name=department_name,
                                                           case_id=case_id, user_id=user_id)
                        func(self, browser, url)

                    finally:
                        API.api_delete_entity(url=url, entity_type='user', entity_id=user_id, headers=headers)
                        API.api_delete_entity(url=url, entity_type='case', entity_id=case_id, headers=headers)
                        API.api_delete_entity(url=url, entity_type='department',
                                              entity_id=department_id, headers=headers)
                finally:
                    API.api_user_logout(url=url, headers=headers)
                    del headers

            return inner

        return setup

    @staticmethod
    def prepare_for_test_011(department_name):
        def setup(func):
            wraps(func)

            def inner(self, browser, url):
                headers = None

                try:
                    user_id = None
                    department_id = None

                    try:
                        headers = API.api_user_login(url=url)
                        user_id = API.api_add_entity(url=url, headers=headers, entity_type='user')
                        department_id = API.api_add_entity(url=url, headers=headers,
                                                           entity_type='department', department_name=department_name,
                                                           user_id=user_id)
                        func(self, browser, url)

                    finally:
                        API.api_delete_entity(url=url, entity_type='user', entity_id=user_id, headers=headers)
                        API.api_delete_entity(url=url, entity_type='department',
                                              entity_id=department_id, headers=headers)
                finally:
                    API.api_user_logout(url=url, headers=headers)
                    del headers

            return inner

        return setup

    @staticmethod
    def prepare_for_test_012(department_name):
        def setup(func):
            wraps(func)

            def inner(self, browser, url):
                headers = None

                try:
                    user_id = None
                    department_id = None

                    try:
                        headers = API.api_user_login(url=url)
                        user_id = API.api_add_entity(url=url, headers=headers, entity_type='user')
                        department_id = API.api_add_entity(url=url, headers=headers,
                                                           entity_type='department', department_name=department_name,
                                                           user_id=user_id)
                        func(self, browser, url)

                    finally:
                        API.api_delete_entity(url=url, entity_type='user', entity_id=user_id, headers=headers)
                        API.api_delete_entity(url=url, entity_type='department',
                                              entity_id=department_id, headers=headers)
                finally:
                    API.api_user_logout(url=url, headers=headers)
                    del headers

            return inner

        return setup

    @staticmethod
    def prepare_for_test_015(case_name, department_name):
        def setup(func):
            wraps(func)

            def inner(self, browser, url, param):
                headers = None

                try:
                    user_id = None
                    case_id = None
                    department_id = None

                    try:
                        headers = API.api_user_login(url=url)
                        user_id = API.api_add_entity(url=url, headers=headers, entity_type='user', user_status=param[1])
                        case_id = API.api_add_entity(url=url, headers=headers, entity_type='case', case_name=case_name)
                        department_id = API.api_add_entity(url=url, headers=headers,
                                                           entity_type='department', department_name=department_name,
                                                           case_id=case_id, user_id=user_id)
                        func(self, browser, url, param)

                    finally:
                        API.api_delete_entity(url=url, entity_type='user', entity_id=user_id, headers=headers)
                        API.api_delete_entity(url=url, entity_type='case', entity_id=case_id, headers=headers)
                        API.api_delete_entity(url=url, entity_type='department',
                                              entity_id=department_id, headers=headers)
                finally:
                    API.api_user_logout(url=url, headers=headers)
                    del headers

            return inner

        return setup

    @allure.feature('Departments page')
    @allure.title('Clean monitor')
    @DUsers.logout_all_users()
    @DEntities.delete_all_entities()
    def test_0_clean_monitor(self, browser, url):
        pass

    @allure.feature('Departments page')
    @allure.title('Add new department')
    @DUsers.logout_all_users()
    @DDepartment.delete_department(department_name=DepartmentsData.DEPARTMENT_NAME_1)
    @DUsers.login_logout_user(user_login=LoginData.SUPER_LOGIN, user_password=LoginData.SUPER_PASSWORD,
                              page_name='departments')
    def test_departments_001(self, page, url):
        """https://knoxygen.atlassian.net/wiki/spaces/WA/pages/3822157838/Auto+Departments.001"""
        page.wait_not_visability_element(element=Notifications.PRELOADER)
        page.open_url(url=url, api=DepartmentsData.PAGE)

        page.wait_visability_element(element=DepartmentsLocators.ADD_BUTTON)
        page.wait_visability_element(element=DepartmentsLocators.COUNTER)

        counter = page.find_element(element=DepartmentsLocators.COUNTER)
        first_counter = page.get_counter(element=counter)

        page.click_element(element=DepartmentsLocators.ADD_BUTTON)
        page.wait_visability_element(element=DepartmentsLocators.ADD_SECTION)

        page.write_in_element(element=DepartmentsLocators.DEPARTMENT_NAME, text=DepartmentsData.DEPARTMENT_NAME_1)
        page.write_in_element(element=DepartmentsLocators.DEPARTMENT_NOTE, text=DepartmentsData.DEPARTMENT_NOTE)

        page.click_element(element=DepartmentsLocators.FINAL_ADD)

        page.wait_visability_element(element=Notifications.BLUE_NOTIFI)
        element_text = page.get_text_element(element=Notifications.BLUE_NOTIFI)
        page.compare_text(element_text=element_text, message=DepartmentsVerif.ADDED_DEPARTMENT)
        page.click_element(element=Notifications.NOTIFI_CLOSE)

        page.write_in_element(element=DepartmentsLocators.SEARCH, text=DepartmentsData.DEPARTMENT_NAME_1)
        page.press_enter()
        page.wait_visability_element(element=DepartmentsLocators.GRID_DEPARTMENT_NAME)
        param_list = page.get_grid_department_parameters(arg1=DepartmentsLocators.GRID_DEPARTMENT_NAME,
                                                         arg2=DepartmentsLocators.GRID_DEPARTMENT_NOTE, )
        page.check_grid_department_parameters(parameters=param_list, check_parameters=DepartmentsVerif.DEPARTMENT_PARAM)

        counter = page.find_element(element=DepartmentsLocators.COUNTER)
        second_counter = page.get_counter(element=counter)
        page.check_counter_plus(first_counter=first_counter, second_counter=second_counter)

        return page

    @allure.feature('Departments page')
    @allure.title('Add new department + users')
    @DUsers.logout_all_users()
    @DDepartment.delete_department(department_name=DepartmentsData.DEPARTMENT_NAME_1)
    @DUsers.login_logout_user(user_login=LoginData.SUPER_LOGIN, user_password=LoginData.SUPER_PASSWORD,
                              page_name='departments')
    @DUsers.add_delete_user()
    @DUsers.add_delete_user(user_login=LoginData.EXPERT_LOGIN, user_name=LoginData.NEW_FIRST_NAME,
                            user_lastname=LoginData.NEW_LAST_NAME)
    def test_departments_002(self, page, url):
        """https://knoxygen.atlassian.net/wiki/spaces/WA/pages/3822157849/Auto+Departments.002"""
        page.open_url(url=url, api=DepartmentsData.PAGE)
        page.wait_not_visability_element(element=Notifications.PRELOADER)

        page.wait_visability_element(element=DepartmentsLocators.ADD_BUTTON)
        page.wait_visability_element(element=DepartmentsLocators.COUNTER)

        page.click_element(element=DepartmentsLocators.ADD_BUTTON)
        page.wait_visability_element(element=DepartmentsLocators.ADD_SECTION)

        page.write_in_element(element=DepartmentsLocators.DEPARTMENT_NAME, text=DepartmentsData.DEPARTMENT_NAME_1)

        page.click_element(element=DepartmentsLocators.USERS_1ST)
        page.click_element(element=DepartmentsLocators.USERS_2ND)

        page.click_element(element=DepartmentsLocators.FINAL_ADD)

        page.wait_visability_element(element=Notifications.BLUE_NOTIFI)
        element_text = page.get_text_element(element=Notifications.BLUE_NOTIFI)
        page.compare_text(element_text=element_text, message=DepartmentsVerif.ADDED_DEPARTMENT)
        page.click_element(element=Notifications.NOTIFI_CLOSE)

        page.write_in_element(element=DepartmentsLocators.SEARCH, text=DepartmentsData.DEPARTMENT_NAME_1)
        page.press_enter()
        page.wait_visability_element(element=DepartmentsLocators.GRID_DEPARTMENT_NAME)

        page.click_element(element=DepartmentsLocators.RIGHT_SIDEBAR_USERS)
        text = page.get_text_element(element=DepartmentsLocators.RIGHT_SIDEBAR_USER_NAME_1ST)
        text_2 = page.get_text_element(element=DepartmentsLocators.RIGHT_SIDEBAR_USER_NAME_2ND)

        page.compare_text(element_text=text_2, message=f'{LoginData.FIRST_NAME} {LoginData.LAST_NAME}')
        page.compare_text(element_text=text, message=f'{LoginData.NEW_FIRST_NAME} {LoginData.NEW_LAST_NAME}')

        counter = page.find_element(element=DepartmentsLocators.RIGHT_SIDEBAR_USERS_COUNTER)
        users_counter = page.get_counter(element=counter)
        page.compare_text(element_text=users_counter, message=DepartmentsVerif.USERS_COUNTER)

        return page

    @allure.feature('Departments page')
    @allure.title('Add new department + cases')
    @DUsers.logout_all_users()
    @DCases.add_delete_cases(cases_name_list=['Case1', 'Case2'])
    @DDepartment.delete_department(department_name=DepartmentsData.DEPARTMENT_NAME_1)
    @DUsers.login_logout_user(user_login=LoginData.SUPER_LOGIN, user_password=LoginData.SUPER_PASSWORD,
                              page_name='departments')
    @DUsers.add_delete_user()
    @DUsers.add_delete_user(user_login=LoginData.EXPERT_LOGIN, user_name=LoginData.NEW_FIRST_NAME,
                            user_lastname=LoginData.NEW_LAST_NAME)
    def test_departments_003(self, page, url):
        """https://knoxygen.atlassian.net/wiki/spaces/WA/pages/3822157860/Auto+Departments.003"""
        page.open_url(url=url, api=DepartmentsData.PAGE)
        page.wait_not_visability_element(element=Notifications.PRELOADER)

        page.wait_visability_element(element=DepartmentsLocators.ADD_BUTTON)
        page.wait_visability_element(element=DepartmentsLocators.COUNTER)

        page.click_element(element=DepartmentsLocators.ADD_BUTTON)
        page.wait_visability_element(element=DepartmentsLocators.ADD_SECTION)

        page.write_in_element(element=DepartmentsLocators.DEPARTMENT_NAME, text=DepartmentsData.DEPARTMENT_NAME_1)

        page.click_element(element=DepartmentsLocators.CASES_1ST)
        page.click_element(element=DepartmentsLocators.CASES_2ND)

        page.click_element(element=DepartmentsLocators.FINAL_ADD)

        page.wait_visability_element(element=Notifications.BLUE_NOTIFI)
        element_text = page.get_text_element(element=Notifications.BLUE_NOTIFI)
        page.compare_text(element_text=element_text, message=DepartmentsVerif.ADDED_DEPARTMENT)
        page.click_element(element=Notifications.NOTIFI_CLOSE)

        page.write_in_element(element=DepartmentsLocators.SEARCH, text=DepartmentsData.DEPARTMENT_NAME_1)
        page.press_enter()
        page.wait_visability_element(element=DepartmentsLocators.GRID_DEPARTMENT_NAME)

        page.click_element(element=DepartmentsLocators.RIGHT_SIDEBAR_CASES)
        text = page.get_text_element(element=DepartmentsLocators.RIGHT_SIDEBAR_CASE_NAME_1ST)
        text_2 = page.get_text_element(element=DepartmentsLocators.RIGHT_SIDEBAR_CASE_NAME_2ND)

        page.compare_text(element_text=text, message=DepartmentsVerif.CASE_NAME_1)
        page.compare_text(element_text=text_2, message=DepartmentsVerif.CASE_NAME_2)

        counter = page.find_element(element=DepartmentsLocators.RIGHT_SIDEBAR_CASES_COUNTER)
        cases_counter = page.get_counter(element=counter)
        page.compare_text(element_text=cases_counter, message=DepartmentsVerif.CASES_COUNTER)

        return page

    @allure.feature('Departments page')
    @allure.title('Add new department + users + cases')
    @DEntities.delete_all_entities()
    @DUsers.logout_all_users()
    @DUsers.add_delete_users(
        users_data=[(LoginData.ADMIN_LOGIN, LoginData.FIRST_NAME), (LoginData.EXPERT_LOGIN, LoginData.NEW_FIRST_NAME)])
    @DDepartment.delete_department(department_name=DepartmentsData.DEPARTMENT_NAME_1)
    @DUsers.login_logout_user(user_login=LoginData.SUPER_LOGIN, user_password=LoginData.SUPER_PASSWORD,
                              page_name='departments')
    def test_departments_004(self, page, url):
        """https://knoxygen.atlassian.net/wiki/spaces/WA/pages/3822157871/Auto+Departments.004"""
        page.open_url(url=url, api=DepartmentsData.PAGE)
        page.wait_not_visability_element(element=Notifications.PRELOADER)

        page.wait_visability_element(element=DepartmentsLocators.ADD_BUTTON)
        page.wait_visability_element(element=DepartmentsLocators.COUNTER)

        page.click_element(element=DepartmentsLocators.ADD_BUTTON)
        page.wait_visability_element(element=DepartmentsLocators.ADD_SECTION)

        page.write_in_element(element=DepartmentsLocators.DEPARTMENT_NAME, text=DepartmentsData.DEPARTMENT_NAME_1)

        page.click_element(element=DepartmentsLocators.USERS_1ST)
        page.click_element(element=DepartmentsLocators.USERS_2ND)

        page.click_element(element=DepartmentsLocators.CASES_1ST)
        page.click_element(element=DepartmentsLocators.CASES_2ND)

        page.click_element(element=DepartmentsLocators.FINAL_ADD)

        page.wait_visability_element(element=Notifications.BLUE_NOTIFI)
        element_text = page.get_text_element(element=Notifications.BLUE_NOTIFI)
        page.compare_text(element_text=element_text, message=DepartmentsVerif.ADDED_DEPARTMENT)
        page.click_element(element=Notifications.NOTIFI_CLOSE)

        page.write_in_element(element=DepartmentsLocators.SEARCH, text=DepartmentsData.DEPARTMENT_NAME_1)
        page.press_enter()
        page.wait_visability_element(element=DepartmentsLocators.GRID_DEPARTMENT_NAME)

        page.click_element(element=DepartmentsLocators.RIGHT_SIDEBAR_USERS)
        text = page.get_text_element(element=DepartmentsLocators.RIGHT_SIDEBAR_USER_NAME_1ST)
        text_2 = page.get_text_element(element=DepartmentsLocators.RIGHT_SIDEBAR_USER_NAME_2ND)

        page.compare_text(element_text=text, message=f'{LoginData.NEW_FIRST_NAME} {LoginData.NEW_LAST_NAME_2}')
        page.compare_text(element_text=text_2, message=f'{LoginData.FIRST_NAME} {LoginData.LAST_NAME_2}')

        counter = page.find_element(element=DepartmentsLocators.RIGHT_SIDEBAR_USERS_COUNTER)
        users_counter = page.get_counter(element=counter)
        page.compare_text(element_text=users_counter, message=DepartmentsVerif.USERS_COUNTER)

        page.click_element(element=DepartmentsLocators.RIGHT_SIDEBAR_CASES)
        text = page.get_text_element(element=DepartmentsLocators.RIGHT_SIDEBAR_CASE_NAME_1ST)
        text_2 = page.get_text_element(element=DepartmentsLocators.RIGHT_SIDEBAR_CASE_NAME_2ND)

        page.compare_text(element_text=text, message=DepartmentsVerif.CASE_NAME_1)
        page.compare_text(element_text=text_2, message=DepartmentsVerif.CASE_NAME_2)

        counter = page.find_element(element=DepartmentsLocators.RIGHT_SIDEBAR_CASES_COUNTER)
        cases_counter = page.get_counter(element=counter)
        page.compare_text(element_text=cases_counter, message=DepartmentsVerif.CASES_COUNTER)

        return page

    @allure.feature('Departments page')
    @allure.title('Sort cases and users')
    @DUsers.logout_all_users()
    @pytest.mark.skip(reason='sort')
    @DUsers.add_delete_users(
        users_data=[('Bobie', 'Bob'), ('Zoid', 'Zoid'), ('Ann08', 'Anna'), ('Yaroslav', 'Yar_08'), ('Janna', 'Goonie'),
                    ('Sergey', 'Serg_k'), ('Sergey', 'login12')])
    @DCases.add_delete_cases(
        cases_name_list=['Best_case', 'First_case', 'Z_case', 'Our_case', 'Case', 'My_case',
                         'Z_case'])
    @DUsers.login_logout_user(user_login=LoginData.SUPER_LOGIN, user_password=LoginData.SUPER_PASSWORD,
                              page_name='departments')
    def test_departments_005(self, page, url):
        """https://knoxygen.atlassian.net/wiki/spaces/WA/pages/3822157882/Auto+Departments.005"""
        page.open_url(url=url, api=DepartmentsData.PAGE)
        page.wait_not_visability_element(element=Notifications.PRELOADER)

        page.wait_visability_element(element=DepartmentsLocators.ADD_BUTTON)
        page.click_element(element=DepartmentsLocators.ADD_BUTTON)
        page.wait_visability_element(element=DepartmentsLocators.ADD_SECTION)

        unsorted_list = page.get_item_list(element=DepartmentsLocators.USERS_1ST)
        sorted_1 = unsorted_list.copy()
        sorted_1.sort()

        page.click_element(element=DepartmentsLocators.SORT_USERS)
        sorted_2 = page.get_item_list(element=DepartmentsLocators.USERS_1ST)

        page.compare_lists(list_1=sorted_1, list_2=sorted_2)

        page.click_element(element=DepartmentsLocators.SORT_USERS)
        unsorted_2 = page.get_item_list(element=DepartmentsLocators.USERS_1ST)

        page.compare_lists(list_1=unsorted_list, list_2=unsorted_2)

        unsorted_list = page.get_item_list_slice(element=DepartmentsLocators.CASES_1ST, slice_index=52)
        sorted_1 = unsorted_list.copy()
        sorted_1.sort()
        page.click_element(element=DepartmentsLocators.SORT_CASES)
        sorted_2 = page.get_item_list_slice(element=DepartmentsLocators.CASES_1ST, slice_index=52)
        page.compare_lists(list_1=sorted_1, list_2=sorted_2)
        page.click_element(element=DepartmentsLocators.SORT_CASES)

        unsorted_2 = page.get_item_list_slice(element=DepartmentsLocators.CASES_1ST, slice_index=52)

        page.compare_lists(list_1=unsorted_list, list_2=unsorted_2)

        page.click_element(element=DepartmentsLocators.CANCEL_BUTTON)

        return page

    @allure.feature('Departments page')
    @allure.title('General checkbox in sections cases and users')
    @pytest.mark.skip(reason='can\'t check login list and name+lname list')
    @DUsers.logout_all_users()
    @DUsers.add_delete_users(
        users_data=[('Bobie', 'Bob'), ('Zoid', 'Zoid'), ('Ann08', 'Anna'), ('Yaroslav', 'Yar_08'), ('Janna', 'Inna'),
                    ('Sasha', 'Sasha_k'), ('Sergey', 'login12')])
    @DCases.add_delete_cases(
        cases_name_list=['Best_case', 'First_case', 'Z_case', 'Our_case', 'Case', 'My_case',
                         'Q_case'])
    @DUsers.login_logout_user(user_login=LoginData.SUPER_LOGIN, user_password=LoginData.SUPER_PASSWORD,
                              page_name='departments')
    @DDepartment.delete_department(department_name=DepartmentsData.DEPARTMENT_NAME_1)
    def test_departments_006(self, page, url):
        """https://knoxygen.atlassian.net/wiki/spaces/WA/pages/3822157893/Auto+Departments.006"""
        page.wait_not_visability_element(element=Notifications.PRELOADER)
        page.wait_visability_element(element=TopBars.DATA_BAR)

        page.open_url(url=url, api=DepartmentsData.PAGE)
        page.wait_visability_element(element=DepartmentsLocators.ADD_BUTTON)
        page.wait_visability_element(element=DepartmentsLocators.COUNTER)

        page.click_element(element=DepartmentsLocators.ADD_BUTTON)
        page.wait_visability_element(element=DepartmentsLocators.ADD_SECTION)

        page.write_in_element(element=DepartmentsLocators.DEPARTMENT_NAME, text=DepartmentsData.DEPARTMENT_NAME_1)

        page.click_element(element=DepartmentsLocators.GENERAL_CHECKBOX_USERS)
        page.click_element(element=DepartmentsLocators.GENERAL_CHECKBOX_CASES)
        time.sleep(10)
        users_list = page.get_item_list(element=DepartmentsLocators.USERS_1ST)
        cases_list = page.get_item_list_slice(element=DepartmentsLocators.CASES_1ST, slice_index=52)

        page.click_element(element=DepartmentsLocators.FINAL_ADD)

        page.wait_visability_element(element=Notifications.BLUE_NOTIFI)
        element_text = page.get_text_element(element=Notifications.BLUE_NOTIFI)
        page.compare_text(element_text=element_text, message=DepartmentsVerif.ADDED_DEPARTMENT)
        page.click_element(element=Notifications.NOTIFI_CLOSE)

        page.wait_visability_element(element=DepartmentsLocators.SEARCH)
        page.write_in_element(element=DepartmentsLocators.SEARCH, text=DepartmentsData.DEPARTMENT_NAME_1)
        page.press_enter()

        page.wait_element_is_clickable(element=DepartmentsLocators.RIGHT_SIDEBAR_CASES)
        page.click_element(element=DepartmentsLocators.RIGHT_SIDEBAR_CASES)
        elements_list = page.get_item_list(element=DepartmentsLocators.RIGHT_SIDEBAR_CASES_NAME)
        page.compare_lists(list_1=cases_list, list_2=elements_list)

        page.click_element(element=DepartmentsLocators.RIGHT_SIDEBAR_USERS)
        time.sleep(10)
        elements_list = page.get_item_list_slice(element=DepartmentsLocators.RIGHT_SIDEBAR_USER_NAME_1ST,
                                                 slice_index=17, only_first='yes')
        page.compare_lists(list_1=users_list, list_2=elements_list)

        page.wait_visability_element(element=DepartmentsLocators.RIGHT_SIDEBAR_EDIT_BUTTON)
        page.click_element(element=DepartmentsLocators.RIGHT_SIDEBAR_EDIT_BUTTON)

        page.click_element(element=DepartmentsLocators.GENERAL_CHECKBOX_USERS)
        page.click_element(element=DepartmentsLocators.GENERAL_CHECKBOX_CASES)

        page.click_element(element=DepartmentsLocators.FINAL_ADD)

        page.wait_visability_element(element=DepartmentsLocators.SEARCH)
        page.write_in_element(element=DepartmentsLocators.SEARCH, text=DepartmentsData.DEPARTMENT_NAME_1)
        page.press_enter()

        page.wait_visability_element(element=Notifications.BLUE_NOTIFI_2)
        page.click_element(element=Notifications.NOTIFI_CLOSE_2)

        page.click_element(element=DepartmentsLocators.RIGHT_SIDEBAR_USERS)
        page.wait_visability_element(element=DepartmentsLocators.RIGHT_SIDEBAR_NOUSERS)
        element_text = page.get_text_element(element=DepartmentsLocators.RIGHT_SIDEBAR_NOUSERS)
        page.compare_text(element_text, message=DepartmentsVerif.NOUSERS)

        page.click_element(element=DepartmentsLocators.RIGHT_SIDEBAR_CASES)
        page.wait_visability_element(element=DepartmentsLocators.RIGHT_SIDEBAR_NOCASES)
        element_text = page.get_text_element(element=DepartmentsLocators.RIGHT_SIDEBAR_NOCASES)
        page.compare_text(element_text, message=DepartmentsVerif.NOCASES)

        return page

    @allure.feature('Departments page')
    @allure.title('Quicksearch in users and cases')
    @DUsers.logout_all_users()
    @DUsers.add_delete_users(
        users_data=[('Bobie', 'Bob'), ('Zoid', 'Zoid'), ('Ann08', 'Anna'), ('Yaroslav', 'Yar_08'), ('Anna', 'Anie'),
                    ('Sasha', 'Sasha_k'), ('login12', 'Sergey')])
    @DCases.add_delete_cases(
        cases_name_list=['Best_case', 'First_case', 'Z_case', 'Наше_дело', 'Первый_дело', 'Я_дело',
                         'А_дело', DepartmentsData.CASE_NAME_1])
    @DUsers.login_logout_user(user_login=LoginData.SUPER_LOGIN, user_password=LoginData.SUPER_PASSWORD,
                              page_name='departments')
    def test_departments_007(self, page, url):
        """https://knoxygen.atlassian.net/wiki/spaces/WA/pages/3822157904/Auto+Departments.007"""
        page.open_url(url=url, api=DepartmentsData.PAGE)
        page.wait_not_visability_element(element=Notifications.PRELOADER)

        page.wait_visability_element(element=DepartmentsLocators.ADD_BUTTON)
        page.wait_visability_element(element=DepartmentsLocators.COUNTER)

        page.click_element(element=DepartmentsLocators.ADD_BUTTON)
        page.wait_visability_element(element=DepartmentsLocators.ADD_SECTION)

        page.write_in_element(element=DepartmentsLocators.DEPARTMENT_NAME, text=DepartmentsData.DEPARTMENT_NAME_1)
        page.write_in_element(element=DepartmentsLocators.USERS_SEARCH,
                              text=DepartmentsData.USER_LOGIN_1)

        page.click_element(element=DepartmentsLocators.USERS_1ST)

        page.write_in_element(element=DepartmentsLocators.CASES_SEARCH,
                              text=DepartmentsData.CASE_NAME_1)

        page.click_element(element=DepartmentsLocators.CASES_1ST)

        page.click_element(element=DepartmentsLocators.FINAL_ADD)

        page.wait_visability_element(element=Notifications.BLUE_NOTIFI)
        page.click_element(element=Notifications.NOTIFI_CLOSE)

        page.hover_on_element(element=TopBars.RIGHT_BAR)
        page.wait_visability_element(element=TopBars.EXIT_BUTTON)
        page.click_element(element=TopBars.EXIT_BUTTON)
        page.wait_visability_element(element=LoginLocators.LOGIN_BUTTON)

        page.write_in_element(element=LoginLocators.LOGIN_FIELD, text=LoginData.ADMIN_LOGIN)
        page.write_in_element(element=LoginLocators.PASSWORD_FIELD,
                              text=LoginData.PASSWORD)
        page.click_element(element=LoginLocators.LOGIN_BUTTON)

        page.wait_visability_element(element=TopBars.DATA_BAR)
        page.wait_not_visability_element(element=Notifications.PRELOADER)

        page.check_name_of_tab(name_of_tab=CasesVerif.NAME_OF_TAB)

        element = page.find_element(element=CasesLocators.COUNTER)
        counter = page.get_counter(element=element)
        page.compare_text(element_text=counter, message=DepartmentsVerif.CASE_COUNTER)

        page.find_element(element=CasesLocators.TEST_CASE_1)

        return page

    @allure.feature('Departments page')
    @allure.title('Change department name and note')
    @DUsers.logout_all_users()
    @DDepartment.add_delete_department(department_name=DepartmentsData.DEPARTMENT_NAME_1,
                                       department_note=DepartmentsData.DEPARTMENT_NOTE_2)
    @DUsers.login_logout_user(user_login=LoginData.SUPER_LOGIN, user_password=LoginData.SUPER_PASSWORD,
                              page_name='departments')
    def test_departments_008(self, page, url):
        """https://knoxygen.atlassian.net/wiki/spaces/WA/pages/3822157915/Auto+Departments.008"""
        page.open_url(url=url, api=DepartmentsData.PAGE)
        page.wait_not_visability_element(element=Notifications.PRELOADER)

        page.wait_visability_element(element=DepartmentsLocators.ADD_BUTTON)
        page.wait_visability_element(element=DepartmentsLocators.COUNTER)

        page.write_in_element(element=DepartmentsLocators.SEARCH, text=DepartmentsData.DEPARTMENT_NAME_1)
        page.press_enter()
        page.wait_visability_element(element=DepartmentsLocators.GRID_DEPARTMENT_NAME)

        page.click_element(element=DepartmentsLocators.RIGHT_SIDEBAR_EDIT_BUTTON)

        page.wait_visability_element(element=DepartmentsLocators.ADD_SECTION)

        page.clear_element(element=DepartmentsLocators.DEPARTMENT_NAME)
        page.clear_element(element=DepartmentsLocators.DEPARTMENT_NOTE)
        page.write_in_element(element=DepartmentsLocators.DEPARTMENT_NAME, text=DepartmentsData.DEPARTMENT_NAME_3)
        page.write_in_element(element=DepartmentsLocators.DEPARTMENT_NOTE, text=DepartmentsData.DEPARTMENT_NOTE_2)

        page.click_element(element=DepartmentsLocators.FINAL_ADD)

        page.wait_visability_element(element=Notifications.BLUE_NOTIFI)
        element_text = page.get_text_element(element=Notifications.BLUE_NOTIFI)
        page.compare_text(element_text=element_text, message=DepartmentsVerif.SAVE_CHANGES)
        page.click_element(element=Notifications.NOTIFI_CLOSE)

        page.write_in_element(element=DepartmentsLocators.SEARCH, text=DepartmentsData.DEPARTMENT_NAME_3)
        page.press_enter()
        page.wait_visability_element(element=DepartmentsLocators.GRID_DEPARTMENT_NAME)
        param_list = page.get_grid_department_parameters(arg1=DepartmentsLocators.GRID_DEPARTMENT_NAME,
                                                         arg2=DepartmentsLocators.GRID_DEPARTMENT_NOTE, )
        page.check_grid_department_parameters(parameters=param_list,
                                              check_parameters=DepartmentsVerif.DEPARTMENT_PARAM_2)

        element_text = page.get_text_element(element=DepartmentsLocators.RIGHT_SIDEBAR_TOP_DEPARTMENT_NAME)
        page.compare_text(element_text=element_text, message=DepartmentsVerif.DEPARTMENT_NAME_3)

        return page

    @allure.feature('Departments page')
    @allure.title('Change department add user and case with authorization')
    @DUsers.logout_all_users()
    @DUsers.add_delete_user()
    @DDepartment.add_delete_department(department_name=DepartmentsData.DEPARTMENT_NAME_1)
    @DCases.add_delete_case(case_name=DepartmentsData.CASE_NAME_1)
    @DUsers.login_logout_user(user_login=LoginData.SUPER_LOGIN, user_password=LoginData.SUPER_PASSWORD,
                              page_name='departments')
    def test_departments_009(self, page, url):
        """https://knoxygen.atlassian.net/wiki/spaces/WA/pages/3822157926/Auto+Departments.009"""
        page.open_url(url=url, api=DepartmentsData.PAGE)
        page.wait_not_visability_element(element=Notifications.PRELOADER)

        page.wait_visability_element(element=DepartmentsLocators.ADD_BUTTON)
        page.wait_visability_element(element=DepartmentsLocators.COUNTER)

        page.write_in_element(element=DepartmentsLocators.SEARCH, text=DepartmentsData.DEPARTMENT_NAME_1)
        page.press_enter()
        page.wait_visability_element(element=DepartmentsLocators.GRID_DEPARTMENT_NAME)

        page.click_element(element=DepartmentsLocators.RIGHT_SIDEBAR_EDIT_BUTTON)

        page.wait_visability_element(element=DepartmentsLocators.ADD_SECTION)

        page.write_in_element(element=DepartmentsLocators.USERS_SEARCH,
                              text=DepartmentsData.USER_NAME_1)

        page.click_element(element=DepartmentsLocators.USERS_1ST)

        page.write_in_element(element=DepartmentsLocators.CASES_SEARCH,
                              text=DepartmentsData.CASE_NAME_1)

        page.click_element(element=DepartmentsLocators.CASES_1ST)

        page.click_element(element=DepartmentsLocators.FINAL_ADD)

        page.wait_visability_element(element=Notifications.BLUE_NOTIFI)
        page.click_element(element=Notifications.NOTIFI_CLOSE)

        page.click_element(element=DepartmentsLocators.RIGHT_SIDEBAR_USERS)
        element_text = page.get_text_element(element=DepartmentsLocators.RIGHT_SIDEBAR_USER_NAME_1ST)
        page.compare_text(element_text, message=DepartmentsVerif.USER_NAME_1)

        page.click_element(element=DepartmentsLocators.RIGHT_SIDEBAR_CASES)
        element_text = page.get_text_element(element=DepartmentsLocators.RIGHT_SIDEBAR_CASES_NAME)
        page.compare_text(element_text, message=DepartmentsVerif.CASE_NAME)

        page.hover_on_element(element=TopBars.RIGHT_BAR)
        page.wait_visability_element(element=TopBars.EXIT_BUTTON)
        page.click_element(element=TopBars.EXIT_BUTTON)
        page.wait_visability_element(element=LoginLocators.LOGIN_BUTTON)

        page.write_in_element(element=LoginLocators.LOGIN_FIELD, text=LoginData.ADMIN_LOGIN)
        page.write_in_element(element=LoginLocators.PASSWORD_FIELD,
                              text=LoginData.PASSWORD)
        page.click_element(element=LoginLocators.LOGIN_BUTTON)

        page.wait_visability_element(element=TopBars.DATA_BAR)
        page.wait_not_visability_element(element=Notifications.PRELOADER)

        page.check_name_of_tab(name_of_tab=CasesVerif.NAME_OF_TAB)

        element = page.find_element(element=CasesLocators.COUNTER)
        counter = page.get_counter(element=element)
        page.compare_text(element_text=counter, message=DepartmentsVerif.CASE_COUNTER)

        page.find_element(element=CasesLocators.TEST_CASE_1)

        return page

    @allure.feature('Departments page')
    @allure.title('Change department remove user and case with authorization')
    @DEntities.delete_all_entities()
    @DUsers.logout_all_users()
    @prepare_for_test_010(case_name=DepartmentsData.CASE_NAME_1, department_name=DepartmentsData.DEPARTMENT_NAME_1)
    @DUsers.login_logout_user(user_login=LoginData.SUPER_LOGIN, user_password=LoginData.SUPER_PASSWORD,
                              page_name='departments')
    def test_departments_010(self, page, url):
        """https://knoxygen.atlassian.net/wiki/spaces/WA/pages/3822157937/Auto+Departments.010"""
        page.open_url(url=url, api=DepartmentsData.PAGE)
        page.wait_not_visability_element(element=Notifications.PRELOADER)

        page.wait_visability_element(element=DepartmentsLocators.ADD_BUTTON)
        page.wait_visability_element(element=DepartmentsLocators.COUNTER)

        page.write_in_element(element=DepartmentsLocators.SEARCH, text=DepartmentsData.DEPARTMENT_NAME_1)
        page.press_enter()
        page.wait_visability_element(element=DepartmentsLocators.GRID_DEPARTMENT_NAME)

        page.click_element(element=DepartmentsLocators.RIGHT_SIDEBAR_EDIT_BUTTON)

        page.wait_visability_element(element=DepartmentsLocators.ADD_SECTION)

        page.write_in_element(element=DepartmentsLocators.USERS_SEARCH,
                              text=DepartmentsData.USER_NAME_1)

        page.click_element(element=DepartmentsLocators.USERS_1ST)

        page.write_in_element(element=DepartmentsLocators.CASES_SEARCH,
                              text=DepartmentsData.CASE_NAME_1)

        page.click_element(element=DepartmentsLocators.CASES_1ST)

        page.click_element(element=DepartmentsLocators.FINAL_ADD)

        page.wait_visability_element(element=Notifications.BLUE_NOTIFI)
        page.click_element(element=Notifications.NOTIFI_CLOSE)

        page.write_in_element(element=DepartmentsLocators.SEARCH, text=DepartmentsData.DEPARTMENT_NAME_1)
        page.press_enter()
        page.wait_visability_element(element=DepartmentsLocators.GRID_DEPARTMENT_NAME)

        page.click_element(element=DepartmentsLocators.RIGHT_SIDEBAR_USERS)
        page.wait_visability_element(element=DepartmentsLocators.RIGHT_SIDEBAR_NOUSERS)
        element_text = page.get_text_element(element=DepartmentsLocators.RIGHT_SIDEBAR_NOUSERS)
        page.compare_text(element_text, message=DepartmentsVerif.NOUSERS)

        page.click_element(element=DepartmentsLocators.RIGHT_SIDEBAR_CASES)
        page.wait_visability_element(element=DepartmentsLocators.RIGHT_SIDEBAR_NOCASES)
        element_text = page.get_text_element(element=DepartmentsLocators.RIGHT_SIDEBAR_NOCASES)
        page.compare_text(element_text, message=DepartmentsVerif.NOCASES)

        page.hover_on_element(element=TopBars.RIGHT_BAR)
        page.wait_visability_element(element=TopBars.EXIT_BUTTON)
        page.click_element(element=TopBars.EXIT_BUTTON)
        page.wait_visability_element(element=LoginLocators.LOGIN_BUTTON)

        page.write_in_element(element=LoginLocators.LOGIN_FIELD, text=LoginData.ADMIN_LOGIN)
        page.write_in_element(element=LoginLocators.PASSWORD_FIELD,
                              text=LoginData.PASSWORD)
        page.click_element(element=LoginLocators.LOGIN_BUTTON)

        page.wait_visability_element(element=TopBars.DATA_BAR)
        page.wait_not_visability_element(element=Notifications.PRELOADER)

        page.check_name_of_tab(name_of_tab=CasesVerif.NAME_OF_TAB)

        element = page.find_element(element=CasesLocators.COUNTER)
        counter = page.get_counter(element=element)
        page.compare_text(element_text=counter, message=DepartmentsVerif.CASE_COUNTER_5)

        return page

    @allure.feature('Departments page')
    @allure.title('Change department remove user')
    @DUsers.logout_all_users()
    @prepare_for_test_011(department_name=DepartmentsData.DEPARTMENT_NAME_1)
    @DUsers.login_logout_user(user_login=LoginData.SUPER_LOGIN, user_password=LoginData.SUPER_PASSWORD,
                              page_name='departments')
    def test_departments_011(self, page, url):
        page.open_url(url=url, api=DepartmentsData.PAGE)
        page.wait_not_visability_element(element=Notifications.PRELOADER)

        page.wait_visability_element(element=DepartmentsLocators.ADD_BUTTON)
        page.wait_visability_element(element=DepartmentsLocators.COUNTER)

        page.write_in_element(element=DepartmentsLocators.SEARCH, text=DepartmentsData.DEPARTMENT_NAME_1)
        page.press_enter()
        page.wait_visability_element(element=DepartmentsLocators.GRID_DEPARTMENT_NAME)

        page.click_element(element=DepartmentsLocators.RIGHT_SIDEBAR_USERS)
        element_text = page.get_text_element(element=DepartmentsLocators.RIGHT_SIDEBAR_USER_NAME_1ST)
        page.compare_text(element_text, message=DepartmentsVerif.USER_NAME_1)

        headers = API.api_user_login(url=url)
        users_dict = API.api_get_entity_dict(url=url, headers=headers, entity_type='user')
        user_id = API.api_get_added_entity_id_of_login(data=users_dict, entity_login=LoginData.ADMIN_LOGIN)
        API.api_delete_entity(url=url, entity_type='user', entity_id=user_id, headers=headers)

        page.refresh_page()

        page.wait_visability_element(element=DepartmentsLocators.SEARCH)
        page.write_in_element(element=DepartmentsLocators.SEARCH, text=DepartmentsData.DEPARTMENT_NAME_1)
        page.press_enter()
        page.wait_visability_element(element=DepartmentsLocators.GRID_DEPARTMENT_NAME)

        page.click_element(element=DepartmentsLocators.RIGHT_SIDEBAR_USERS)
        page.wait_visability_element(element=DepartmentsLocators.RIGHT_SIDEBAR_NOUSERS)
        element_text = page.get_text_element(element=DepartmentsLocators.RIGHT_SIDEBAR_NOUSERS)
        page.compare_text(element_text, message=DepartmentsVerif.NOUSERS)

        return page

    @allure.feature('Departments page')
    @allure.title('Change department remove user')
    @DUsers.logout_all_users()
    @prepare_for_test_012(department_name=DepartmentsData.DEPARTMENT_NAME_1)
    @DUsers.login_logout_user(user_login=LoginData.SUPER_LOGIN, user_password=LoginData.SUPER_PASSWORD,
                              page_name='departments')
    def test_departments_012(self, page, url):
        page.open_url(url=url, api=DepartmentsData.PAGE)
        page.wait_not_visability_element(element=Notifications.PRELOADER)

        page.wait_visability_element(element=DepartmentsLocators.ADD_BUTTON)
        page.wait_visability_element(element=DepartmentsLocators.COUNTER)

        page.write_in_element(element=DepartmentsLocators.SEARCH, text=DepartmentsData.DEPARTMENT_NAME_1)
        page.press_enter()
        page.wait_visability_element(element=DepartmentsLocators.GRID_DEPARTMENT_NAME)

        page.click_element(element=DepartmentsLocators.RIGHT_SIDEBAR_USERS)
        element_text = page.get_text_element(element=DepartmentsLocators.RIGHT_SIDEBAR_USER_NAME_1ST)
        page.compare_text(element_text, message=DepartmentsVerif.USER_NAME_1)

        headers = API.api_user_login(url=url)
        users_dict = API.api_get_entity_dict(url=url, headers=headers, entity_type='user')
        user_id = API.api_get_added_entity_id(data=users_dict, entity_fname=DepartmentsData.USER_NAME_1)
        API.api_delete_entity(url=url, entity_type='user', entity_id=user_id, headers=headers)

        page.refresh_page()

        page.wait_visability_element(element=DepartmentsLocators.SEARCH)
        page.write_in_element(element=DepartmentsLocators.SEARCH, text=DepartmentsData.DEPARTMENT_NAME_1)
        page.press_enter()
        page.wait_visability_element(element=DepartmentsLocators.GRID_DEPARTMENT_NAME)
        page.wait_not_visability_element(element=Notifications.PRELOADER)
        page.wait_visability_element(element=DepartmentsLocators.RIGHT_SIDEBAR_USERS)
        page.click_element(element=DepartmentsLocators.RIGHT_SIDEBAR_USERS)
        page.wait_visability_element(element=DepartmentsLocators.RIGHT_SIDEBAR_NOUSERS)
        element_text = page.get_text_element(element=DepartmentsLocators.RIGHT_SIDEBAR_NOUSERS)
        page.compare_text(element_text, message=DepartmentsVerif.NOUSERS)

        return page

    @allure.feature('Departments page')
    @allure.title('Search department')
    @DUsers.logout_all_users()
    @DUsers.login_logout_user(user_login=LoginData.SUPER_LOGIN, user_password=LoginData.SUPER_PASSWORD,
                              page_name='departments')
    @DDepartment.delete_department(department_name=DepartmentsData.DEPARTMENT_PART_NAME)
    def test_departments_013(self, page, url):
        page.open_url(url=url, api=DepartmentsData.PAGE)
        page.wait_not_visability_element(element=Notifications.PRELOADER)

        page.wait_visability_element(element=DepartmentsLocators.ADD_BUTTON)
        page.wait_visability_element(element=DepartmentsLocators.COUNTER)

        page.click_element(element=DepartmentsLocators.ADD_BUTTON)
        page.wait_visability_element(element=DepartmentsLocators.ADD_SECTION)

        page.write_in_element(element=DepartmentsLocators.DEPARTMENT_NAME, text=DepartmentsData.DEPARTMENT_PART_NAME)

        page.click_element(element=DepartmentsLocators.FINAL_ADD)

        page.wait_visability_element(element=Notifications.BLUE_NOTIFI)
        element_text = page.get_text_element(element=Notifications.BLUE_NOTIFI)
        page.compare_text(element_text=element_text, message=DepartmentsVerif.ADDED_DEPARTMENT)
        page.click_element(element=Notifications.NOTIFI_CLOSE)

        page.write_in_element(element=DepartmentsLocators.SEARCH, text=DepartmentsData.DEPARTMENT_PART)
        page.press_enter()
        page.wait_visability_element(element=DepartmentsLocators.GRID_DEPARTMENT_NAME)

        text_element = page.get_text_element(element=DepartmentsLocators.GRID_DEPARTMENT_NAME)
        page.compare_text(element_text=text_element, message=DepartmentsVerif.DEPARTMENT_PART_NAME)

        page.clear_element(element=DepartmentsLocators.SEARCH)
        page.press_enter()
        page.wait_visability_element(element=DepartmentsLocators.GRID_DEPARTMENT_NAME)

        return page

    @allure.feature('Departments page')
    @allure.title('Delete department')
    @DEntities.delete_all_entities()
    @DUsers.logout_all_users()
    @DDepartment.add_delete_department(department_name=DepartmentsData.DEPARTMENT_NAME_1)
    @DUsers.login_logout_user(user_login=LoginData.SUPER_LOGIN, user_password=LoginData.SUPER_PASSWORD,
                              page_name='departments')
    def test_departments_014(self, page, url):
        """https://knoxygen.atlassian.net/wiki/spaces/WA/pages/3822157981/Auto+Departmetns.014"""
        page.open_url(url=url, api=DepartmentsData.PAGE)
        page.wait_not_visability_element(element=Notifications.PRELOADER)

        page.wait_visability_element(element=DepartmentsLocators.ADD_BUTTON)
        page.wait_visability_element(element=AdminLocators.SEARCH)

        page.write_in_element(element=AdminLocators.SEARCH, text=DepartmentsData.DEPARTMENT_NAME_1)
        page.press_enter()

        page.hover_on_element(element=DepartmentsLocators.GRID_DEPARTMENT_NAME)
        page.click_element(element=DepartmentsLocators.GRID_DEPARTMENT_BUCKET)

        page.wait_visability_element(element=DepartmentsLocators.DELETE_CONFIRM)

        page.click_element(element=DepartmentsLocators.YES_BUCKET_BUTTON)

        page.wait_visability_element(element=Notifications.BLUE_NOTIFI)
        element_text = page.get_text_element(element=Notifications.BLUE_NOTIFI)
        page.compare_text(element_text=element_text, message=DepartmentsVerif.DELETED_DEPARTMENT)
        page.click_element(element=Notifications.NOTIFI_CLOSE)

        page.check_element_contains_text(element=DepartmentsLocators.GRID_NO_RESULTS)

        return page

    @allure.feature('Departments page')
    @allure.title('Delete department during log in')
    @pytest.mark.parametrize('param', [(LoginData.ADMIN_LOGIN, LoginData.STATUS_ADMIN),
                                       (LoginData.EXPERT_LOGIN, LoginData.STATUS_EXPERT),
                                       (LoginData.LOAD_LOGIN, LoginData.STATUS_LOAD)])
    @DUsers.logout_all_users_with_param()
    @prepare_for_test_015(case_name=DepartmentsData.CASE_NAME_1, department_name=DepartmentsData.DEPARTMENT_NAME_1)
    def test_departments_015_016_017(self, browser, url, param):
        """https://knoxygen.atlassian.net/wiki/spaces/WA/pages/3822158003/Auto+Departments.015
        https://knoxygen.atlassian.net/wiki/spaces/WA/pages/3822158014/Auto+Departments.016
        https://knoxygen.atlassian.net/wiki/spaces/WA/pages/3822158025/Auto+Departments.017"""
        page = DepartmentsPage(browser)
        page.open_url(url=url)
        page.wait_visability_element(element=LoginLocators.LOGIN_FIELD)
        page.write_in_element(element=LoginLocators.LOGIN_FIELD, text=param[0])
        page.write_in_element(element=LoginLocators.PASSWORD_FIELD,
                              text=LoginData.PASSWORD)
        page.click_element(element=LoginLocators.LOGIN_BUTTON)

        page.wait_not_visability_element(element=Notifications.PRELOADER)

        headers = API.api_user_login(url=url)
        departments_dict = API.api_get_entity_dict(url=url, headers=headers, entity_type='department')
        department_id = API.api_get_added_entity_id(data=departments_dict,
                                                    entity_name=DepartmentsData.DEPARTMENT_NAME_1)
        API.api_delete_entity(url=url, headers=headers, entity_type='department', entity_id=department_id)

        page.open_url(url=url, api=LoadImagesData.PAGE)

        page.wait_not_visability_element(element=Notifications.PRELOADER)
        page.wait_visability_element(element=LoadImagesLocators.ADD_BUTTON)
        page.wait_element_is_clickable(element=LoadImagesLocators.ADD_BUTTON)

        page.check_name_of_tab(name_of_tab=LoadImagesVerif.NAME_OF_TAB)

        page.open_url(url=url, api=DevicesData.PAGE)

        page.wait_not_visability_element(element=Notifications.PRELOADER)
        page.wait_visability_element(element=TopBars.DATA_BAR)
        page.wait_element_is_clickable(element=DevicesLocators.SEARCH)

        page.check_name_of_tab(name_of_tab=DevicesVerif.NAME_OF_TAB)

        page.open_url(url=url, api=CasesData.PAGE)

        page.wait_not_visability_element(element=Notifications.PRELOADER)
        page.wait_visability_element(element=TopBars.DATA_BAR)
        page.wait_element_is_clickable(element=CasesLocators.SEARCH)

        page.check_name_of_tab(name_of_tab=CasesVerif.NAME_OF_TAB)

        page.hover_on_element(element=TopBars.RIGHT_BAR)
        page.wait_visability_element(element=TopBars.EXIT_BUTTON)
        page.click_element(element=TopBars.EXIT_BUTTON)
        page.wait_visability_element(element=LoginLocators.LOGIN_BUTTON)

        page.write_in_element(element=LoginLocators.LOGIN_FIELD, text=param[0])
        page.write_in_element(element=LoginLocators.PASSWORD_FIELD, text=LoginData.PASSWORD)
        page.click_element(element=LoginLocators.LOGIN_BUTTON)

        page.wait_visability_element(element=TopBars.DATA_BAR)
        page.wait_not_visability_element(element=Notifications.PRELOADER)

        if param[0] == LoginData.ADMIN_LOGIN:
            page.wait_visability_element(element=CasesLocators.TEST_CASE_1)
            page.check_element_contains_text(element=CasesLocators.TEST_CASE_1)
            element = page.find_element(element=CasesLocators.COUNTER)
            cases_counter = page.get_counter(element=element)
            page.compare_text(element_text=str(cases_counter), message=str(DepartmentsVerif.CASE_COUNTER_5))
        else:
            page.check_element_contains_text_disappeared(element=CasesLocators.TEST_CASE_1)

        return page

    @allure.feature('Crime types page')
    @allure.title('Clean monitor')
    @DUsers.logout_all_users()
    def test_z_clean_monitor(self, browser, url):
        pass
