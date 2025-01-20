import time
from functools import wraps
import API
import operation_system
from Funcs import TestCase
from Funcs import TestLogger
from Pages_data.API_login_data import LoginData
from data import Code


class DLicense:

    @staticmethod
    def put_new_license(folder_name: str):
        """Заменяет license конфиг"""

        def setup(func):
            wraps(func)

            def inner(self, url, test_logger):
                try:
                    if folder_name == Code.DONGLE:
                        operation_system.delete_license()
                        operation_system.reload_backend()
                    else:
                        operation_system.delete_license()
                        operation_system.copy_paste_license(folder_name)
                        operation_system.reload_backend()

                    TestCase.api_logout_from_monitor(url)

                    func(self, url, test_logger)
                finally:

                    func(self, url, test_logger)

            return inner

        return setup


class DCases:

    @staticmethod
    def add_delete_case_param_id_for_import(case_name: str):
        """Декоратор для создания
         и удаления дела +
        использование параметра + передача id созданного дела в тест"""

        def setup(func):
            wraps(func)

            def inner(self, test):

                case_id = None
                if test.param[3] == Code.YES:
                    try:

                        case_id = API.api_add_entity(url=test.url, headers=test.headers, entity_type=Code.CASE,
                                                     entity_name=case_name)

                        func(self, test, case_id)
                    finally:
                        API.api_delete_entity(url=test.url, entity_type=Code.CASE, entity_id=case_id,
                                              headers=test.headers)

                else:

                    func(self, test, case_id)

            return inner

        return setup


class DDevices:

    @staticmethod
    def delete_several_devices():
        """Декоратор для удаления нескольких устройств"""

        def setup(func):
            wraps(func)

            def inner(self, test):

                try:

                    func(self, test)
                finally:

                    device_id_list = API.api_get_id_entity_list(url=test.url, headers=test.headers,
                                                                entity_type=Code.DEVICE)
                    for device_id in device_id_list:
                        API.api_delete_entity(url=test.url, entity_type=Code.DEVICE, entity_id=device_id,
                                              headers=test.headers)

            return inner

        return setup

    @staticmethod
    def delete_several_devices_case_id():
        """Декоратор для удаления нескольких устройств
        передается case id для теста"""

        def setup(func):
            wraps(func)

            def inner(self, test, case_id):

                try:

                    func(self, test, case_id)
                finally:

                    device_id_list = API.api_get_id_entity_list(url=test.url, headers=test.headers,
                                                                entity_type=Code.DEVICE)
                    for device_id in device_id_list:
                        API.api_delete_entity(url=test.url, entity_type=Code.DEVICE, entity_id=device_id,
                                              headers=test.headers)

            return inner

        return setup


class DEntities:

    @staticmethod
    def add_delete_entity(entity_type, custom_data=None):
        """Декоратор для создания
         и удаления сущности"""

        def setup(func):
            wraps(func)

            def inner(self, test):
                entity_id = None
                try:
                    entity_id = API.api_add_entity1(url=test.url, headers=test.headers,
                                                    entity_type=entity_type, custom_data=custom_data)

                    func(self, test, entity_id)
                finally:
                    API.api_delete_entity(url=test.url, entity_id=entity_id,
                                          headers=test.headers, entity_type=entity_type)

            return inner

        return setup

    @staticmethod
    def add_delete_entities(entity_type: str, users_data: list = None, entities_name_list: list = None):
        """Декоратор для создания
         и удаления нескольких сущностей"""

        def setup(func):
            wraps(func)

            def inner(self, test):

                entities_id = None

                try:
                    if entity_type == Code.USER:
                        entities_id = [API.api_add_entity(url=test.url, headers=test.headers, entity_type=Code.USER,
                                                          user_name=user_data[1], user_login=user_data[0]) for user_data
                                       in users_data]
                    else:
                        entities_id = [API.api_add_entity(url=test.url, headers=test.headers, entity_type=entity_type,
                                                          entity_name=entity_name) for entity_name in
                                       entities_name_list]

                    func(self, test)

                finally:
                    [API.api_delete_entity(url=test.url, entity_type=entity_type, entity_id=entity_id,
                                           headers=test.headers) for entity_id in entities_id]

            return inner

        return setup

    @staticmethod
    def add_delete_entity_param_id(entity_type: str):
        """Декоратор для создания
        и удаления сущности с параметром в тесте
        передается id сущности в тест"""

        def setup(func):
            wraps(func)

            def inner(self, test):
                entity_id = None
                try:
                    if entity_type == Code.KEYWORD_SET:
                        entity_id = API.api_add_entity(url=test.url, headers=test.headers, entity_type=entity_type,
                                                       entity_name=test.param[0], keyword_class=test.param[1])
                    elif entity_type == Code.HASH:
                        entity_id = API.api_add_entity(url=test.url, headers=test.headers, entity_type=entity_type,
                                                       entity_name=test.param[0], hash_type=test.param[1])

                    elif entity_type == Code.WATCHLIST:
                        entity_id = API.api_add_entity(url=test.url, headers=test.headers, entity_type=entity_type,
                                                       entity_name=test.param[0], watchlist_words=test.param[4],
                                                       watchlist_field=test.param[0],
                                                       watchlist_class=test.param[2])

                    func(self, test, entity_id)

                finally:
                    API.api_delete_entity(url=test.url, entity_id=entity_id, entity_type=entity_type,
                                          headers=test.headers)

            return inner

        return setup

    @staticmethod
    def add_import_delete_entity_param(entity_type: str):
        """Декоратор для создания, импорта и удаления сущностей
        с передачей параметра в тест"""

        def setup(func):
            wraps(func)

            def inner(self, test):

                entity_id = None
                try:
                    if entity_type == Code.HASH:
                        entity_id = API.api_add_entity(url=test.url, headers=test.headers, entity_type=entity_type,
                                                       entity_name=test.param[1], hash_type=test.param[2])
                        API.api_import_entity(url=test.url, headers=test.headers, entity_type=entity_type,
                                              hash_id=entity_id, hash_type=test.param[2], file_name=test.param[0])

                    elif entity_type == Code.KEYWORD_SET:
                        entity_id = API.api_add_entity(url=test.url, headers=test.headers, entity_type=entity_type,
                                                       entity_name=test.param[1], keyword_class=test.param[3])

                        API.api_import_entity(url=test.url, headers=test.headers, entity_type=entity_type,
                                              keyword_set_id=entity_id, encoding=test.param[2],
                                              file_name=test.param[0])
                    # indexind in db
                    time.sleep(60)

                    func(self, test)

                finally:
                    API.api_delete_entity(url=test.url, entity_id=entity_id, headers=test.headers,
                                          entity_type=entity_type)

            return inner

        return setup

    @staticmethod
    def add_import_delete_entity_param_id(entity_type: str):
        """Декоратор для создания, импорта и удаления сущностей
        с передачей парметра и id сущности в тест"""

        def setup(func):
            wraps(func)

            def inner(self, test):

                entity_id = None
                try:
                    if entity_type == Code.HASH:
                        entity_id = API.api_add_entity(url=test.url, headers=test.headers, entity_type=entity_type,
                                                       entity_name=test.param[1], hash_type=test.param[2])
                        API.api_import_entity(url=test.url, headers=test.headers, entity_type=entity_type,
                                              hash_id=entity_id, hash_type=test.param[2], file_name=test.param[0])

                    elif entity_type == Code.KEYWORD_SET:
                        entity_id = API.api_add_entity(url=test.url, headers=test.headers, entity_type=entity_type,
                                                       entity_name=test.param[1])
                        API.api_import_entity(url=test.url, headers=test.headers, entity_type=entity_type,
                                              keyword_set_id=entity_id, file_name=test.param[0], encoding=test.param[2])

                    elif entity_type == Code.WATCHLIST:
                        entity_id = API.api_add_entity(url=test.url, headers=test.headers, entity_type=entity_type,
                                                       entity_name=test.param[1], watchlist_field=test.param[1],
                                                       watchlist_class=test.param[3])

                        API.api_import_entity(url=test.url, headers=test.headers, entity_type=entity_type,
                                              watchlist_id=entity_id, file_name=test.param[0])

                    # indexind in db
                    time.sleep(60)

                    func(self, test, entity_id)

                finally:
                    API.api_delete_entity(url=test.url, entity_id=entity_id, headers=test.headers,
                                          entity_type=entity_type)

            return inner

        return setup

    @staticmethod
    def create_test():
        """Создает экземпляр теста"""

        def setup(func):
            wraps(func)

            def inner(self, url, test_logger):
                test = None
                try:
                    test_logger = TestLogger(test_logger)
                    headers = API.api_user_login(url=url, data_for_login=LoginData.SUPER_LOGIN)
                    test = TestCase(test_logger=test_logger.logger, url=url, headers=headers)

                    func(self, test)
                finally:
                    API.api_user_logout(url=test.url, headers=test.headers)
                    del test

            return inner

        return setup

    @staticmethod
    def create_test_param():
        """Создает экземпляр теста с параметром в тесте"""

        def setup(func):
            wraps(func)

            def inner(self, url, test_logger, param):
                test = None
                try:
                    test_logger = TestLogger(test_logger)
                    headers = API.api_user_login(url=url, data_for_login=LoginData.SUPER_LOGIN)
                    test = TestCase(test_logger=test_logger.logger, url=url, headers=headers, param=param)

                    func(self, test)
                finally:
                    API.api_user_logout(url=test.url, headers=test.headers)
                    del test

            return inner

        return setup

    @staticmethod
    def create_test_no_login():
        """Создает экземпляр теста без логина в систему"""

        def setup(func):
            wraps(func)

            def inner(self, url, test_logger):
                try:
                    test_logger = TestLogger(test_logger)
                    test = TestCase(test_logger=test_logger.logger, url=url)

                    func(self, test)
                finally:
                    del test

            return inner

        return setup

    @staticmethod
    def delete_entity(entity_type: str, entity_name: str = None, entity_fname: str = None):
        """Декоратор для удаления сущности"""

        def setup(func):
            wraps(func)

            def inner(self, test):

                try:

                    func(self, test)

                finally:

                    entity_dict = API.api_get_entity_dict(url=test.url, headers=test.headers,
                                                          entity_type=entity_type)
                    if entity_type == Code.USER:
                        entity_id = API.api_get_added_entity_id(data=entity_dict, entity_fname=entity_fname)
                    else:
                        entity_id = API.api_get_added_entity_id(data=entity_dict, entity_name=entity_name)
                    API.api_delete_entity(url=test.url, entity_id=entity_id,
                                          headers=test.headers, entity_type=entity_type)

            return inner

        return setup

    @staticmethod
    def delete_all_entities():
        """Очищают базу от всех сущностей"""

        def setup(func):
            wraps(func)

            def inner(self, test):

                type_of_entities = ['user', 'department', 'case', 'region', 'crime_type', 'tag', 'hashset',
                                    'device', 'keyword_set', 'watchlist']
                entities_dict = {type_of_entity: API.api_get_id_entity_list(url=test.url, headers=test.headers,
                                                                            entity_type=type_of_entity) for
                                 type_of_entity in type_of_entities}

                for entity_type, entity_id_list in entities_dict.items():
                    for entity_id in entity_id_list:
                        API.api_delete_entity(url=test.url, entity_type=entity_type,
                                              entity_id=entity_id, headers=test.headers)

                func(self, test)

            return inner

        return setup

    @staticmethod
    def delete_entity_param(entity_type: str, param_num: int = None):
        """Декоратор для удаления сущности с параметром в тесте"""

        def setup(func):
            wraps(func)

            def inner(self, test):

                try:

                    func(self, test)
                finally:
                    entity_dict = API.api_get_entity_dict(url=test.url, headers=test.headers,
                                                          entity_type=entity_type)
                    if entity_type == Code.USER:
                        entity_id = API.api_get_added_entity_id_of_login(data=entity_dict,
                                                                         entity_login=test.param['login'])
                    else:
                        entity_id = API.api_get_added_entity_id(data=entity_dict, entity_name=test.param[param_num])
                    API.api_delete_entity(url=test.url, entity_type=entity_type, entity_id=entity_id,
                                          headers=test.headers)

            return inner

        return setup
