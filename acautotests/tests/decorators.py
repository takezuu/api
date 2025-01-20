import time
from functools import wraps

import API
import operation_system
from Pages.AdminPage import AdminPage
from Pages.CrimeTypesPage import CrimeTypesPage
from Pages.DepartmentsPage import DepartmentsPage
from Pages.DevicesPage import DevicesPage
from Pages.HashesPage import HashesPage
from Pages.KeywordsSetsPage import KeywordsSetsPage
from Pages.LoadImagesPage import LoadImagesPage
from Pages.LoginPage import LoginPage
from Pages.RegionsPage import RegionsPage
from Pages.TagsPage import TagsPage
from data import LoginData
from locators import LoginLocators, TopBars


class DLicense:

    @staticmethod
    def put_new_license(folder_name):
        """Заменяет license конфиг"""

        def setup(func):
            wraps(func)

            def inner(self, browser, url):
                try:

                    operation_system.delete_license()
                    operation_system.copy_paste_license(folder_name)
                    operation_system.reload_backend()

                finally:

                    return func(self, browser, url)

            return inner

        return setup

    @staticmethod
    def put_new_license_with_param(folder_name):
        """Заменяет license конфиг"""

        def setup(func):
            wraps(func)

            def inner(self, browser, url, param):
                try:

                    operation_system.delete_license()
                    operation_system.copy_paste_license(folder_name)
                    operation_system.reload_backend()

                finally:

                    return func(self, browser, url, param)

            return inner

        return setup


class DCases:

    @staticmethod
    def add_delete_case_with_param(case_name):
        """Декоратор для добавления и удаления дела"""

        def setup(func):
            wraps(func)

            def inner(self, browser, url, param):
                headers = None
                case_id = None
                try:
                    headers = API.api_user_login(url=url)

                    try:
                        case_id = API.api_add_entity(url=url, headers=headers, entity_type='case', case_name=case_name)
                        func(self, browser, url, param)
                    finally:
                        API.api_delete_entity(url=url, entity_type='case', entity_id=case_id, headers=headers)

                finally:
                    API.api_user_logout(url=url, headers=headers)
                    del headers

            return inner

        return setup

    @staticmethod
    def add_delete_case(case_name):
        """Декоратор для добавления и удаления дела"""

        def setup(func):
            wraps(func)

            def inner(self, browser, url):

                headers = None
                case_id = None
                try:
                    headers = API.api_user_login(url=url)

                    try:
                        case_id = API.api_add_entity(url=url, headers=headers, entity_type='case', case_name=case_name)
                        func(self, browser, url)
                    finally:
                        API.api_delete_entity(url=url, entity_type='case', entity_id=case_id, headers=headers)

                finally:
                    API.api_user_logout(url=url, headers=headers)
                    del headers

            return inner

        return setup

    @staticmethod
    def add_delete_cases(cases_name_list: list):
        """Декоратор для добавления и удаления нескольких дел"""

        def setup(func):
            wraps(func)

            def inner(self, browser, url):

                headers = None
                cases_id = None
                try:
                    headers = API.api_user_login(url=url)

                    try:
                        cases_id = [
                            API.api_add_entity(url=url, headers=headers, entity_type='case', case_name=case_name)
                            for case_name in cases_name_list]
                        func(self, browser, url)
                    finally:
                        [API.api_delete_entity(url=url, entity_type='case', entity_id=case_id, headers=headers)
                         for case_id in cases_id]

                finally:
                    API.api_user_logout(url=url, headers=headers)
                    del headers

            return inner

        return setup


class DDevices:

    @staticmethod
    def delete_several_devices():
        """Декоратор для удаления нескольких устройств"""

        def setup(func):
            wraps(func)

            def inner(self, browser, url):
                headers = None

                try:
                    try:
                        func(self, browser, url)
                    finally:
                        headers = API.api_user_login(url=url)
                        device_id_list = API.api_get_id_entity_list(url=url, headers=headers, entity_type='device')
                        for device_id in device_id_list:
                            API.api_delete_entity(url=url, entity_type='device', entity_id=device_id, headers=headers)

                finally:
                    API.api_user_logout(url=url, headers=headers)
                    del headers

            return inner

        return setup


class DTags:

    @staticmethod
    def delete_tag(tag_name):
        """Декоратор для удаления тега"""

        def setup(func):
            wraps(func)

            def inner(self, browser, url):
                headers = None

                try:

                    try:
                        func(self, browser, url)
                    finally:
                        headers = API.api_user_login(url=url)
                        tags_dict = API.api_get_entity_dict(url=url, headers=headers, entity_type='tag')
                        tag_id = API.api_get_added_entity_id(data=tags_dict, entity_name=tag_name)
                        API.api_delete_entity(url=url, entity_type='tag', entity_id=tag_id, headers=headers)

                finally:
                    API.api_user_logout(url=url, headers=headers)
                    del headers

            return inner

        return setup

    @staticmethod
    def add_delete_tag(tag_name):
        """Декоратор для добавления и удаления тега"""

        def setup(func):
            wraps(func)

            def inner(self, browser, url):
                headers = None

                try:
                    tag_id = None
                    headers = API.api_user_login(url=url)
                    try:
                        tag_id = API.api_add_entity(url=url, headers=headers, entity_type='tag', tag_name=tag_name)
                        func(self, browser, url)

                    finally:
                        API.api_delete_entity(url=url, entity_type='tag', entity_id=tag_id, headers=headers)
                finally:
                    API.api_user_logout(url=url, headers=headers)
                    del headers

            return inner

        return setup

    @staticmethod
    def add_delete_tags(tags_name_list: list):
        """Декоратор для добавления и удаления нескольких тегов"""

        def setup(func):
            wraps(func)

            def inner(self, browser, url):

                headers = None
                tags_id = None
                try:
                    headers = API.api_user_login(url=url)

                    try:
                        tags_id = [API.api_add_entity(url=url, headers=headers, entity_type='tag', tag_name=tag_name)
                                   for tag_name in tags_name_list]
                        func(self, browser, url)

                    finally:
                        [API.api_delete_entity(url=url, entity_type='tag', entity_id=tag_id, headers=headers)
                         for tag_id in tags_id]

                finally:
                    API.api_user_logout(url=url, headers=headers)
                    del headers

            return inner

        return setup


class DRegions:

    @staticmethod
    def delete_region(region_name):
        """Декоратор для удаления региона"""

        def setup(func):
            wraps(func)

            def inner(self, browser, url):
                headers = None
                try:

                    try:
                        func(self, browser, url)
                    finally:
                        headers = API.api_user_login(url=url)
                        regions_dict = API.api_get_entity_dict(url=url, headers=headers, entity_type='region')
                        region_id = API.api_get_added_entity_id(data=regions_dict, entity_name=region_name)
                        API.api_delete_entity(url=url, entity_type='region', entity_id=region_id, headers=headers)

                finally:
                    API.api_user_logout(url=url, headers=headers)
                    del headers

            return inner

        return setup

    @staticmethod
    def add_delete_region(region_name):
        """Декоратор для добавления и удаления региона"""

        def setup(func):
            wraps(func)

            def inner(self, browser, url):
                headers = None

                try:
                    region_id = None
                    headers = API.api_user_login(url=url)
                    try:
                        region_id = API.api_add_entity(url=url, headers=headers,
                                                       entity_type='region', region_name=region_name)
                        func(self, browser, url)
                    finally:
                        API.api_delete_entity(url=url, entity_type='region', entity_id=region_id, headers=headers)

                finally:
                    API.api_user_logout(url=url, headers=headers)
                    del headers

            return inner

        return setup


class DKeywordSets:
    @staticmethod
    def delete_keyword_set(keyword_set_name):
        """Декоратор для удаления словаря"""

        def setup(func):
            wraps(func)

            def inner(self, browser, url):
                headers = None

                try:
                    try:
                        func(self, browser, url)
                    finally:
                        headers = API.api_user_login(url=url)
                        keyword_set_dict = API.api_get_entity_dict(url=url, headers=headers, entity_type='keyword_set')
                        keyword_set_id = API.api_get_added_entity_id(data=keyword_set_dict,
                                                                     entity_name=keyword_set_name)
                        API.api_delete_entity(url=url, entity_id=keyword_set_id,
                                              entity_type='keyword_set', headers=headers)
                finally:
                    API.api_user_logout(url=url, headers=headers)
                    del headers

            return inner

        return setup

    @staticmethod
    def delete_keyword_set_param():
        """Декоратор для удаления словаря с параметром в тесте"""

        def setup(func):
            wraps(func)

            def inner(self, browser, url, param):
                headers = None
                try:

                    try:
                        return func(self, browser, url, param)

                    finally:
                        headers = API.api_user_login(url=url)
                        keyword_set_dict = API.api_get_entity_dict(url=url, headers=headers, entity_type='keyword_set')
                        keyword_set_id = API.api_get_added_entity_id(data=keyword_set_dict, entity_name=param[0])
                        API.api_delete_entity(url=url, entity_id=keyword_set_id, entity_type='keyword_set',
                                              headers=headers)
                finally:
                    API.api_user_logout(url=url, headers=headers)
                    del headers

            return inner

        return setup

    @staticmethod
    def delete_keyword_set_param_004():
        """Декоратор для удаления словаря с параметром в тесте"""

        def setup(func):
            wraps(func)

            def inner(self, browser, url, param):
                headers = None
                try:
                    try:
                        return func(self, browser, url, param)

                    finally:
                        headers = API.api_user_login(url=url)
                        keyword_set_dict = API.api_get_entity_dict(url=url, headers=headers, entity_type='keyword_set')
                        keyword_set_id = API.api_get_added_entity_id(data=keyword_set_dict, entity_name=param[4])
                        API.api_delete_entity(url=url, entity_id=keyword_set_id, entity_type='keyword_set',
                                              headers=headers)
                finally:
                    API.api_user_logout(url=url, headers=headers)
                    del headers

            return inner

        return setup

    @staticmethod
    def add_delete_keyword_set_with_param():
        """Декоратор для добавления и удаления словаря"""

        def setup(func):
            wraps(func)

            def inner(self, browser, url, param):
                headers = None
                try:
                    headers = API.api_user_login(url=url)
                    keyword_set_id = API.api_add_entity(url=url, headers=headers, entity_type='keyword_set',
                                                        keyword_set_name=param[0], keyword_set_type=param[1])
                    try:
                        func(self, browser, url, param)
                    finally:
                        API.api_delete_entity(url=url, entity_id=keyword_set_id, entity_type='keyword_set',
                                              headers=headers)
                finally:
                    API.api_user_logout(url=url, headers=headers)
                    del headers

            return inner

        return setup

    @staticmethod
    def add_delete_keywords_sets(keywords_sets_name_list: list):
        """Декоратор для добавления и удаления нескольких хешей"""

        def setup(func):
            wraps(func)

            def inner(self, browser, url):

                headers = None

                try:
                    headers = API.api_user_login(url=url)
                    keywords_sets_id = [
                        API.api_add_entity(url=url, headers=headers, entity_type='keyword_set',
                                           keyword_set_name=keyword_set_name)
                        for keyword_set_name in keywords_sets_name_list]
                    try:
                        func(self, browser, url)

                    finally:
                        [API.api_delete_entity(url=url, entity_type='keyword_set', entity_id=keyword_set_id,
                                               headers=headers)
                         for keyword_set_id in keywords_sets_id]

                finally:
                    API.api_user_logout(url=url, headers=headers)
                    del headers

            return inner

        return setup

    @staticmethod
    def add_import_delete_keyword_set():
        """Декоратор для импорта словаря"""

        def setup(func):
            wraps(func)

            def inner(self, browser, url, param):
                headers = None

                try:
                    headers = API.api_user_login(url=url)
                    keyword_set_id = API.api_add_entity(url=url, headers=headers, entity_type='keyword_set',
                                                        keyword_set_name=param[1])

                    API.api_import_entity(url=url, headers=headers, entity_type='keyword_set',
                                          keyword_set_id=keyword_set_id, encoding=param[2], file_name=param[0])
                    # indexind in db
                    time.sleep(300)
                    try:
                        func(self, browser, url, param)
                    finally:
                        API.api_delete_entity(url=url, entity_id=keyword_set_id, entity_type='keyword_set',
                                              headers=headers)
                finally:
                    API.api_user_logout(url=url, headers=headers)
                    del headers

            return inner

        return setup

    @staticmethod
    def add_import_delete_keyword_set_different_dict_class():
        """Декоратор для импорта словаря"""

        def setup(func):
            wraps(func)

            def inner(self, browser, url, param):
                headers = None

                try:
                    headers = API.api_user_login(url=url)
                    keyword_set_id = API.api_add_entity(url=url, headers=headers, entity_type='keyword_set',
                                                        keyword_set_name=param[1], keyword_class=param[3])
                    API.api_import_entity(url=url, headers=headers, entity_type='keyword_set',
                                          keyword_set_id=keyword_set_id, encoding=param[2], file_name=param[0])
                    # indexind in db
                    time.sleep(300)
                    try:
                        func(self, browser, url, param)
                    finally:
                        API.api_delete_entity(url=url, entity_id=keyword_set_id, entity_type='keyword_set',
                                              headers=headers)

                finally:
                    API.api_user_logout(url=url, headers=headers)
                    del headers

            return inner

        return setup

    @staticmethod
    def add_import_delete_2_keyword_set_different_dict_class():
        """Декоратор для импорта словаря"""

        def setup(func):
            wraps(func)

            def inner(self, browser, url, param):
                headers = None

                try:
                    headers = API.api_user_login(url=url)
                    keyword_set_id = API.api_add_entity(url=url, headers=headers, entity_type='keyword_set',
                                                        keyword_set_name=param[1], keyword_class=param[3])
                    keyword_set_id_2 = API.api_add_entity(url=url, headers=headers, entity_type='keyword_set',
                                                          keyword_set_name=param[8], keyword_class=param[3])

                    API.api_import_entity(url=url, headers=headers, keyword_set_id=keyword_set_id,
                                          entity_type='keyword_set', encoding=param[2], file_name=param[0])

                    API.api_import_entity(url=url, headers=headers, keyword_set_id=keyword_set_id_2,
                                          entity_type='keyword_set', encoding=param[9], file_name=param[7])
                    # indexind in db
                    time.sleep(300)
                    try:
                        func(self, browser, url, param)
                    finally:
                        API.api_delete_entity(url=url, entity_id=keyword_set_id, entity_type='keyword_set',
                                              headers=headers)
                        API.api_delete_entity(url=url, entity_id=keyword_set_id_2, entity_type='keyword_set',
                                              headers=headers)
                finally:
                    API.api_user_logout(url=url, headers=headers)
                    del headers

            return inner

        return setup


class DHashsets:
    @staticmethod
    def delete_hash(hash_name):
        """Декоратор для удаления хеша"""

        def setup(func):
            wraps(func)

            def inner(self, browser, url):
                headers = None

                try:
                    try:
                        func(self, browser, url)

                    finally:
                        headers = API.api_user_login(url=url)
                        hashes_dict = API.api_get_entity_dict(url=url, headers=headers, entity_type='hashset')
                        hash_id = API.api_get_added_entity_id(data=hashes_dict, entity_name=hash_name)
                        API.api_delete_entity(url=url, entity_id=hash_id, headers=headers, entity_type='hashset')

                finally:
                    API.api_user_logout(url=url, headers=headers)
                    del headers

            return inner

        return setup

    @staticmethod
    def delete_hash_param():
        """Декоратор для удаления хеша с параметром в тесте"""

        def setup(func):
            wraps(func)

            def inner(self, browser, url, param):
                headers = None
                try:
                    try:
                        return func(self, browser, url, param)
                    finally:
                        headers = API.api_user_login(url=url)
                        hashes_dict = API.api_get_entity_dict(url=url, headers=headers, entity_type='hashset')
                        hash_id = API.api_get_added_entity_id(data=hashes_dict, entity_name=param[0])
                        API.api_delete_entity(url=url, entity_id=hash_id, headers=headers, entity_type='hashset')

                finally:
                    API.api_user_logout(url=url, headers=headers)
                    del headers

            return inner

        return setup

    @staticmethod
    def add_delete_hash_with_param():
        """Декоратор для добавления и удаления хеша"""

        def setup(func):
            wraps(func)

            def inner(self, browser, url, param):
                headers = None

                try:
                    headers = API.api_user_login(url=url)
                    try:
                        API.api_add_entity(url=url, headers=headers, entity_type='hashset', hash_name=param[0],
                                           hash_type=param[8])
                        func(self, browser, url, param)

                    finally:
                        hashes_dict = API.api_get_entity_dict(url=url, headers=headers, entity_type='hashset')
                        hash_id = API.api_get_added_entity_id(data=hashes_dict, entity_name=param[1])
                        API.api_delete_entity(url=url, entity_id=hash_id, headers=headers, entity_type='hashset')

                finally:
                    API.api_user_logout(url=url, headers=headers)
                    del headers

            return inner

        return setup

    @staticmethod
    def add_delete_hashes(hashes_name_list: list):
        """Декоратор для добавления и удаления нескольких хешей"""

        def setup(func):
            wraps(func)

            def inner(self, browser, url):

                headers = None
                hashes_id = None
                try:
                    headers = API.api_user_login(url=url)
                    try:
                        hashes_id = [
                            API.api_add_entity(url=url, headers=headers, entity_type='hashset', hash_name=hash_name)
                            for hash_name in hashes_name_list]
                        func(self, browser, url)

                    finally:
                        [API.api_delete_entity(url=url, entity_type='hashset', entity_id=hash_id, headers=headers)
                         for hash_id in hashes_id]

                finally:
                    API.api_user_logout(url=url, headers=headers)
                    del headers

            return inner

        return setup

    @staticmethod
    def add_import_delete_hash():
        """Декоратор для импорта хеша"""

        def setup(func):
            wraps(func)

            def inner(self, browser, url, param):
                headers = None

                try:
                    hash_id = None
                    headers = API.api_user_login(url=url)
                    try:
                        API.api_add_entity(url=url, headers=headers, entity_type='hashset', hash_name=param[1],
                                           hash_type=param[2])
                        hashes_dict = API.api_get_entity_dict(url=url, headers=headers, entity_type='hashset')
                        hash_id = API.api_get_added_entity_id(data=hashes_dict, entity_name=param[1])
                        API.api_import_entity(url=url, headers=headers, entity_type='hashset',
                                              hash_id=hash_id, hash_type=param[2], file_name=param[0])
                        # indexind in db
                        time.sleep(300)
                        func(self, browser, url, param)

                    finally:
                        API.api_delete_entity(url=url, entity_id=hash_id, headers=headers, entity_type='hashset')

                finally:
                    API.api_user_logout(url=url, headers=headers)
                    del headers

            return inner

        return setup


class DWathlists:

    @staticmethod
    def add_delete_watchlists(watchlists_name_list: list):
        """Декоратор для добавления и удаления нескольких сторожевых списков"""

        def setup(func):
            wraps(func)

            def inner(self, browser, url):

                headers = None
                watchlists_id = None
                try:
                    headers = API.api_user_login(url=url)
                    try:
                        watchlists_id = [
                            API.api_add_entity(url=url, headers=headers, entity_type='watchlist',
                                               watchlist_name=watchlist_name)
                            for watchlist_name in watchlists_name_list]
                        func(self, browser, url)

                    finally:
                        [API.api_delete_entity(url=url, entity_type='watchlist', entity_id=watchlist_id,
                                               headers=headers)
                         for watchlist_id in watchlists_id]

                finally:
                    API.api_user_logout(url=url, headers=headers)
                    del headers

            return inner

        return setup


class DCrimetypes:

    @staticmethod
    def delete_crime_type(crime_type_name):
        """Декоратор для удаления категории преступления"""

        def setup(func):
            wraps(func)

            def inner(self, browser, url):
                headers = None

                try:
                    try:
                        func(self, browser, url)

                    finally:
                        headers = API.api_user_login(url=url)
                        crime_types_dict = API.api_get_entity_dict(url=url, headers=headers, entity_type='crime_type')
                        crime_type_id = API.api_get_added_entity_id(data=crime_types_dict, entity_name=crime_type_name)
                        API.api_delete_entity(url=url, entity_id=crime_type_id,
                                              headers=headers, entity_type='crime_type')

                finally:
                    API.api_user_logout(url=url, headers=headers)
                    del headers

            return inner

        return setup

    @staticmethod
    def add_delete_crime_type(crime_type_name):
        """Декоратор для добавления и удаления категории преступления"""

        def setup(func):
            wraps(func)

            def inner(self, browser, url):
                headers = None

                try:
                    crime_type_id = None

                    try:
                        headers = API.api_user_login(url=url)
                        crime_type_id = API.api_add_entity(url=url, headers=headers,
                                                           entity_type='crime_type', crime_type_name=crime_type_name)
                        func(self, browser, url)
                    finally:
                        API.api_delete_entity(url=url, entity_id=crime_type_id,
                                              headers=headers, entity_type='crime_type')

                finally:
                    API.api_user_logout(url=url, headers=headers)
                    del headers

            return inner

        return setup


class DUsers:

    @staticmethod
    def login_logout_user(user_login, user_password, page_name):
        """Декоратор для входа и выхода пользователя"""

        def setup(func):
            wraps(func)

            def inner(self, browser, url):
                page = None

                if page_name == 'admin':
                    page = AdminPage(browser)
                elif page_name == 'departments':
                    page = DepartmentsPage(browser)
                elif page_name == 'load_images':
                    page = LoadImagesPage(browser)
                elif page_name == 'regions':
                    page = RegionsPage(browser)
                elif page_name == 'crimetypes':
                    page = CrimeTypesPage(browser)
                elif page_name == 'tags':
                    page = TagsPage(browser)
                elif page_name == 'hashsets':
                    page = HashesPage(browser)
                elif page_name == 'keywords_sets':
                    page = KeywordsSetsPage(browser)
                elif page_name == 'login':
                    page = LoginPage(browser)
                elif page_name == 'devices':
                    page = DevicesPage(browser)

                page.open_url(url=url)
                page.wait_visability_element(element=LoginLocators.LOGIN_FIELD)
                page.write_in_element(element=LoginLocators.LOGIN_FIELD, text=user_login)
                page.write_in_element(element=LoginLocators.PASSWORD_FIELD,
                                      text=user_password)
                page.click_element(element=LoginLocators.LOGIN_BUTTON)
                time.sleep(0.1)
                page = func(self, page, url)

                if page:
                    page.hover_on_element(element=TopBars.RIGHT_BAR)
                    page.wait_visability_element(element=TopBars.EXIT_BUTTON)
                    page.click_element(element=TopBars.EXIT_BUTTON)
                    page.wait_visability_element(element=LoginLocators.LOGIN_BUTTON)

            return inner

        return setup

    @staticmethod
    def login_logout_user_param(user_login, user_password, page_name):
        """Декоратор для входа и выхода пользователя с параметром в тесте"""

        def setup(func):
            wraps(func)

            def inner(self, browser, url, param):
                page = None

                if page_name == 'admin':
                    page = AdminPage(browser)
                elif page_name == 'departments':
                    page = DepartmentsPage(browser)
                elif page_name == 'load_images':
                    page = LoadImagesPage(browser)
                elif page_name == 'regions':
                    page = RegionsPage(browser)
                elif page_name == 'crimetypes':
                    page = CrimeTypesPage(browser)
                elif page_name == 'tags':
                    page = TagsPage(browser)
                elif page_name == 'hashsets':
                    page = HashesPage(browser)
                elif page_name == 'keywords_sets':
                    page = KeywordsSetsPage(browser)
                elif page_name == 'login':
                    page = LoginPage(browser)
                elif page_name == 'devices':
                    page = DevicesPage(browser)

                page.open_url(url=url)
                page.wait_visability_element(element=LoginLocators.LOGIN_FIELD)
                page.write_in_element(element=LoginLocators.LOGIN_FIELD, text=user_login)
                page.write_in_element(element=LoginLocators.PASSWORD_FIELD,
                                      text=user_password)
                page.click_element(element=LoginLocators.LOGIN_BUTTON)
                time.sleep(0.1)
                page = func(self, page, url, param)

                if page:
                    page.hover_on_element(element=TopBars.RIGHT_BAR)
                    page.wait_visability_element(element=TopBars.EXIT_BUTTON)
                    page.click_element(element=TopBars.EXIT_BUTTON)
                    page.wait_visability_element(element=LoginLocators.LOGIN_BUTTON)

            return inner

        return setup

    @staticmethod
    def api_login_logout(data_for_login):
        """Вход выход пользователя через апи"""

        def setup(func):
            wraps(func)

            def inner(self, browser, url):
                headers = None

                try:
                    headers = API.api_user_login(url=url, data_for_login=data_for_login)
                    func(self, browser, url)

                finally:

                    API.api_user_logout(url=url, headers=headers)
                    del headers

            return inner

        return setup

    @staticmethod
    def add_delete_user(user_status=LoginData.STATUS_ADMIN, user_login=None, user_name=None,
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
                        API.api_delete_entity(url=url, entity_type='user', entity_id=user_id, headers=headers)

                finally:
                    API.api_user_logout(url=url, headers=headers)

            return inner

        return setup

    @staticmethod
    def add_delete_users(users_data: list):
        """Декоратор для добавления и удаления нескольких пользователей"""

        def setup(func):
            wraps(func)

            def inner(self, browser, url):
                headers = None

                try:
                    users_id = None
                    headers = API.api_user_login(url=url)
                    try:
                        users_id = [API.api_add_entity(url=url, headers=headers, entity_type='user',
                                                       user_name=user_data[1], user_login=user_data[0])
                                    for user_data in users_data]
                        func(self, browser, url)

                    finally:
                        [API.api_delete_entity(url=url, entity_type='user', entity_id=user_id,
                                               headers=headers)
                         for user_id in users_id]

                finally:
                    API.api_user_logout(url=url, headers=headers)
                    del headers

            return inner

        return setup

    @staticmethod
    def add_delete_user_with_cases():
        """Декоратор для добавления пользователя с прикрепленными делами"""

        def setup(func):
            wraps(func)

            def inner(self, browser, url):
                headers = None
                user_id = None
                try:
                    headers = API.api_user_login(url=url)
                    cases_list = API.api_get_id_entity_list(url=url, headers=headers, entity_type='case')
                    user_id = API.api_add_entity(url=url, headers=headers, entity_type='user', cases_list=cases_list)
                    func(self, browser, url)

                finally:
                    API.api_delete_entity(url=url, entity_type='user', entity_id=user_id,
                                          headers=headers)
                    API.api_user_logout(url=url, headers=headers)
                    del headers

            return inner

        return setup

    @staticmethod
    def delete_user(user_login):
        """Декоратор для удаления пользователя"""

        def setup(func):
            wraps(func)

            def inner(self, browser, url):
                headers = None

                try:
                    try:
                        func(self, browser, url)
                    finally:
                        headers = API.api_user_login(url=url)
                        users_dict = API.api_get_entity_dict(url=url, headers=headers, entity_type='user')
                        user_id = API.api_get_added_entity_id_of_login(data=users_dict, entity_login=user_login)
                        API.api_delete_entity(url=url, entity_type='user', entity_id=user_id, headers=headers)

                finally:
                    API.api_user_logout(url=url, headers=headers)

            return inner

        return setup

    @staticmethod
    def delete_user_param(user_login):
        """Декоратор для удаления пользователя"""

        def setup(func):
            wraps(func)

            def inner(self, browser, url, param):
                headers = None

                try:
                    try:
                        func(self, browser, url, param)

                    finally:
                        headers = API.api_user_login(url=url)
                        users_dict = API.api_get_entity_dict(url=url, headers=headers, entity_type='user')
                        user_id = API.api_get_added_entity_id_of_login(data=users_dict, entity_login=user_login)
                        API.api_delete_entity(url=url, entity_type='user', entity_id=user_id, headers=headers)

                finally:
                    API.api_user_logout(url=url, headers=headers)

            return inner

        return setup

    @staticmethod
    def delete_users_param(users_login_list):
        """Декоратор для удаления пользователей"""

        def setup(func):
            wraps(func)

            def inner(self, browser, url, param):

                try:
                    func(self, browser, url, param)

                finally:
                    headers = API.api_user_login(url=url)
                    users_dict = API.api_get_entity_dict(url=url, headers=headers, entity_type='user')
                    users_id = [API.api_get_added_entity_id_of_login(data=users_dict, entity_login=user_login) for
                                user_login in users_login_list]
                    [API.api_delete_entity(url=url, entity_type='user', entity_id=user_id,
                                           headers=headers)
                     for user_id in users_id]
                    API.api_user_logout(url=url, headers=headers)

            return inner

        return setup

    @staticmethod
    def delete_several_users(user_logins_list):
        """Декоратор для удаления нескольких пользователей"""

        def setup(func):
            wraps(func)

            def inner(self, browser, url):
                headers = None

                try:
                    try:
                        func(self, browser, url)
                    finally:
                        headers = API.api_user_login(url=url)
                        for user_login in user_logins_list:
                            users_dict = API.api_get_entity_dict(url=url, headers=headers, entity_type='user')
                            user_id = API.api_get_added_entity_id_of_login(data=users_dict, entity_login=user_login)
                            API.api_delete_entity(url=url, entity_type='user', entity_id=user_id, headers=headers)

                finally:
                    API.api_user_logout(url=url, headers=headers)
                    del headers

            return inner

        return setup

    @staticmethod
    def logout_all_users():
        """Декоратор для вылогинивания всех пользователей"""

        def setup(func):
            wraps(func)

            def inner(self, browser, url):
                API.api_logout_from_monitor(url=url)
                func(self, browser, url)

            return inner

        return setup

    @staticmethod
    def logout_all_users_with_param():
        """Декоратор для вылогинивания всех пользователей"""

        def setup(func):
            wraps(func)

            def inner(self, browser, url, param):
                API.api_logout_from_monitor(url=url)
                func(self, browser, url, param)

            return inner

        return setup


class DDepartment:

    @staticmethod
    def add_delete_department(department_name, department_note=None):
        """Декоратор для добавления и удаления отдела"""

        def setup(func):
            wraps(func)

            def inner(self, browser, url):
                headers = None

                try:
                    department_id = None
                    headers = API.api_user_login(url=url)
                    try:
                        department_id = API.api_add_entity(url=url, headers=headers,
                                                           entity_type='department', department_name=department_name,
                                                           department_note=department_note)
                        func(self, browser, url)

                    finally:
                        API.api_delete_entity(url=url, entity_type='department',
                                              entity_id=department_id, headers=headers)

                finally:
                    API.api_user_logout(url=url, headers=headers)
                    del headers

            return inner

        return setup

    @staticmethod
    def delete_department(department_name):
        """Удаления отдела"""

        def setup(func):
            wraps(func)

            def inner(self, browser, url):
                headers = None

                try:
                    try:
                        func(self, browser, url)
                    finally:
                        headers = API.api_user_login(url=url)
                        department_dict = API.api_get_entity_dict(url=url, headers=headers, entity_type='department')
                        department_id = API.api_get_added_entity_id(data=department_dict, entity_name=department_name)
                        API.api_delete_entity(url=url, entity_type='department',
                                              entity_id=department_id, headers=headers)

                finally:
                    API.api_user_logout(url=url, headers=headers)
                    del headers

            return inner

        return setup

    @staticmethod
    def add_delete_departments(departments_names_list):
        """Декоратор для добавления и удаления нескольких отделов"""

        def setup(func):
            wraps(func)

            def inner(self, browser, url):
                headers = None

                try:
                    departments_id = None
                    headers = API.api_user_login(url=url)
                    try:
                        departments_id = [API.api_add_entity(url=url, headers=headers, entity_type='department',
                                                             department_name=department_name)
                                          for department_name in departments_names_list]
                        func(self, browser, url)

                    finally:
                        [API.api_delete_entity(url=url, entity_type='department', entity_id=department_id,
                                               headers=headers)
                         for department_id in departments_id]

                finally:
                    API.api_user_logout(url=url, headers=headers)
                    del headers

            return inner

        return setup


class DEntities:

    @staticmethod
    def delete_all_entities():
        """Очищают базу от всех сущнойстей"""

        def setup(func):
            wraps(func)

            def inner(self, browser, url):
                headers = None

                try:
                    try:
                        func(self, browser, url)
                    finally:
                        headers = API.api_user_login(url=url)
                        users_id = API.api_get_id_entity_list(url=url, headers=headers, entity_type='user')
                        departments_id = API.api_get_id_entity_list(url=url, headers=headers, entity_type='department')
                        cases_id = API.api_get_id_entity_list(url=url, headers=headers, entity_type='case')
                        regions_id = API.api_get_id_entity_list(url=url, headers=headers, entity_type='region')
                        crime_types_id = API.api_get_id_entity_list(url=url, headers=headers, entity_type='crime_type')
                        tags_id = API.api_get_id_entity_list(url=url, headers=headers, entity_type='tag')
                        hashsets_id = API.api_get_id_entity_list(url=url, headers=headers, entity_type='hashset')
                        devices_id = API.api_get_id_entity_list(url=url, headers=headers, entity_type='device')
                        keywords_sets_id = API.api_get_id_entity_list(url=url, headers=headers,
                                                                      entity_type='keyword_set')
                        watchlists_id = API.api_get_id_entity_list(url=url, headers=headers,
                                                                   entity_type='watchlist')

                        entities_dict = {'user': users_id, 'department': departments_id, 'case': cases_id,
                                         'region': regions_id,
                                         'crime_type': crime_types_id, 'tag': tags_id, 'hashset': hashsets_id,
                                         'device': devices_id, 'keyword_set': keywords_sets_id,
                                         'watchlist': watchlists_id}

                        for entity_type, entity_id_list in entities_dict.items():
                            for entity_id in entity_id_list:
                                API.api_delete_entity(url=url, entity_type=entity_type,
                                                      entity_id=entity_id, headers=headers)

                finally:
                    API.api_user_logout(url=url, headers=headers)
                    del headers

            return inner

        return setup

    @staticmethod
    def delete_all_entities_with_param():
        """Очищают базу от всех сущнойстей"""

        def setup(func):
            wraps(func)

            def inner(self, browser, url, param):
                headers = None

                try:
                    try:
                        func(self, browser, url, param)
                    finally:
                        headers = API.api_user_login(url=url)
                        users_id = API.api_get_id_entity_list(url=url, headers=headers, entity_type='user')
                        departments_id = API.api_get_id_entity_list(url=url, headers=headers, entity_type='department')
                        cases_id = API.api_get_id_entity_list(url=url, headers=headers, entity_type='case')
                        regions_id = API.api_get_id_entity_list(url=url, headers=headers, entity_type='region')
                        crime_types_id = API.api_get_id_entity_list(url=url, headers=headers, entity_type='crime_type')
                        tags_id = API.api_get_id_entity_list(url=url, headers=headers, entity_type='tag')
                        hashsets_id = API.api_get_id_entity_list(url=url, headers=headers, entity_type='hashset')
                        devices_id = API.api_get_id_entity_list(url=url, headers=headers, entity_type='device')
                        keywords_sets_id = API.api_get_id_entity_list(url=url, headers=headers,
                                                                      entity_type='keyword_set')
                        watchlists_id = API.api_get_id_entity_list(url=url, headers=headers,
                                                                   entity_type='watchlist')

                        entities_dict = {'user': users_id, 'department': departments_id, 'case': cases_id,
                                         'region': regions_id,
                                         'crime_type': crime_types_id, 'tag': tags_id, 'hashset': hashsets_id,
                                         'device': devices_id, 'keyword_set': keywords_sets_id,
                                         'watchlist': watchlists_id}

                        for entity_type, entity_id_list in entities_dict.items():
                            for entity_id in entity_id_list:
                                API.api_delete_entity(url=url, entity_type=entity_type,
                                                      entity_id=entity_id, headers=headers)

                finally:
                    API.api_user_logout(url=url, headers=headers)
                    del headers

            return inner

        return setup


class DTime:
    @staticmethod
    def change_time_before():
        """Сохраняет текущее время и переключает за 1 день до истечения лицензии"""

        def setup(func):
            wraps(func)

            def inner(self, browser, url):
                operation_system.save_system_time()
                operation_system.execute_time_script_day_before()

                func(self, browser, url)

            return inner

        return setup

    @staticmethod
    def change_time_today():
        """Переключает на день истечения лицензии до 02:00 по мск"""

        def setup(func):
            wraps(func)

            def inner(self, browser, url):
                operation_system.execute_time_script_day_today()

                func(self, browser, url)

            return inner

        return setup

    @staticmethod
    def change_time_back():
        """Возвращает обратно сохраненное время"""

        def setup(func):
            wraps(func)

            def inner(self, browser, url):
                operation_system.execute_time_script_back()
                operation_system.reload_backend_clear_time()

                func(self, browser, url)

            return inner

        return setup
