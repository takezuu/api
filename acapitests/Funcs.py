import copy
import logging
import time
import re

import allure
import requests
from bs4 import BeautifulSoup
from requests import Response

from Pages_data.API_departments_data import DepartmentsData
from Pages_data.API_hashes_data import HashesData
from Pages_data.API_keywords_sets_data import KeywordsSetsData
from Pages_data.API_login_data import LoginData
from Pages_data.API_regions_data import RegionsData
from Pages_data.API_tags_data import TagsData
from Pages_data.API_watchlists_data import WatchlistsData
from data import Code, STAND_PATH_KEYWORDS_SETS, STAND_PATH_HASHES, STAND_LOGS_FOLDERS
from Pages_data.API_crime_types_data import CrimeTypesData


class TestLogger:

    def __init__(self, test_logger):
        self.test_logger = test_logger
        name_string = copy.deepcopy(self.test_logger.test_name)
        folder = re.findall(r'_.*_', name_string)[0][1:-1]
        self.logger = logging.getLogger(type(self).__name__)
        file_handler = logging.FileHandler(
            f"{STAND_LOGS_FOLDERS}\\{folder}\\{self.test_logger.test_name}.log",
            encoding='utf-8')
        file_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
        self.logger.addHandler(file_handler)
        self.logger.handlers[:] = [file_handler]
        self.logger.setLevel(level=self.test_logger.log_level)


class TestCase:

    def __init__(self, url: str, test_logger, headers: dict = None, param: any = None):
        """Создает экземпляр тест кейса
        url - адрес аналитики
        headers - получены после логина в систему {'x-session-id': sid['SID']}
        param - из фикстуры передаются параметры для тестов"""
        self.url = url
        self.headers = headers
        self.param = param
        self.logger = test_logger

    @allure.step('Create entity')
    def create_entity(self, entity_type: str, custom_json: any = None) -> Response:
        """Создание сущности
        entity_type определяет какая сущность будет создана.
        По умолчанию у каждой сущности передаются данные для создания json_data,
        если необходимо создать сущность с другими параметрами передается custom_json"""
        json_data = None
        url = None

        if entity_type == Code.CRIMETYPE:
            url = self.url + Code.API_ADD_CRIMETYPE
            json_data = CrimeTypesData.data_crime_type
        elif entity_type == Code.REGION:
            url = self.url + Code.API_ADD_REGION
            json_data = RegionsData.data_region
        elif entity_type == Code.TAG:
            url = self.url + Code.API_ADD_TAG
            json_data = TagsData.data_tag
        elif entity_type == Code.DEPARTMENT:
            url = self.url + Code.API_ADD_DEPARTMENT
            json_data = DepartmentsData.data_test_dep
        elif entity_type == Code.HASH:
            url = self.url + Code.API_ADD_HASH
            json_data = HashesData.data_hash
        elif entity_type == Code.KEYWORD_SET:
            url = self.url + Code.API_ADD_KEYWORDS_SET
            json_data = KeywordsSetsData.data_keyword_set
        elif entity_type == Code.WATCHLIST:
            url = self.url + Code.API_ADD_WATCHLIST
            json_data = WatchlistsData.data_watchlist
        elif entity_type == Code.USER:
            url = self.url + Code.API_ADD_USER

        try:
            if custom_json:
                self.logger.info(f'Create entity custom json: {custom_json}')
                self.logger.info(f'Делаю post запрос {custom_json}')
                result = requests.post(url=url, headers=self.headers, json=custom_json)
            else:
                self.logger.info(f'Делаю post запрос {json_data}')
                result = requests.post(url=url, headers=self.headers, json=json_data)
        except Exception as error:
            raise AssertionError(f'Create entity: {error}, json {json_data}, custom json: {custom_json}')
        return result

    @allure.step('Edit entity')
    def edit_entity(self, json_data: dict, entity_type: str, entity_id: int) -> Response:
        """Изменение сущности
        entity_type определяет какая сущность будет изменена
        entity_id - id сущности
        json_data - данные, которые будут изменены
        """
        self.logger.info(f'Edit entity: {entity_type}')
        url = None

        if entity_type == Code.CRIMETYPE:
            url = self.url + Code.API_CRIMETYPES + f'/{entity_id}'
        elif entity_type == Code.REGION:
            url = self.url + Code.API_REGIONS + f'/{entity_id}'
        elif entity_type == Code.TAG:
            url = self.url + Code.API_TAGS + f'/{entity_id}'
        elif entity_type == Code.DEPARTMENT:
            url = self.url + Code.API_DEPARTMENTS[:-1] + f'/{entity_id}'
        elif entity_type == Code.KEYWORD_SET:
            url = self.url + Code.API_KEYWORDS_SETS + f'/{entity_id}'
        elif entity_type == Code.USER:
            url = self.url + Code.API_USERS + f'/{entity_id}'
        elif entity_type == Code.HASH:
            url = self.url + Code.API_HASHES + f'/{entity_id}'

        try:
            self.logger.info(f'Делаю POST запрос: json {json_data}')
            result = requests.post(url=url, headers=self.headers, json=json_data)
        except Exception as error:
            self.logger.error(f'Edit entity: {error}')
            raise AssertionError(f'Edit entity: {error}')

        return result

    @allure.step('Request all entities')
    def request_all_entities(self, entity_type: str, custom_data: any = None) -> Response:
        """Возвращает response всех сущностей определенного типа"""
        self.logger.info(f'Запрашиваю все сущности: type {entity_type}')
        json_data = None
        url = None

        if entity_type == Code.CRIMETYPE:
            url = self.url + Code.API_CRIMETYPES
            json_data = CrimeTypesData.all_crime_type
        elif entity_type == Code.REGION:
            url = self.url + Code.API_REGIONS
            json_data = RegionsData.all_regions
        elif entity_type == Code.TAG:
            url = self.url + Code.API_TAGS
            json_data = TagsData.all_tags
        elif entity_type == Code.DEPARTMENT:
            url = self.url + Code.API_DEPARTMENTS
            json_data = DepartmentsData.all_departments
        elif entity_type == Code.HASH:
            url = self.url + Code.API_HASHES
            json_data = HashesData.all_hashes
        elif entity_type == Code.KEYWORD_SET:
            url = self.url + Code.API_KEYWORDS_SETS
            json_data = KeywordsSetsData.all_keywords_sets
        elif entity_type == Code.WATCHLIST:
            url = self.url + Code.API_WATCHLIST
            json_data = WatchlistsData.all_watchlists
        elif entity_type == Code.USER:
            url = self.url + Code.API_USERS
            json_data = LoginData.all_users
        try:
            if custom_data:
                self.logger.info(f'Делаю POST запрос: json {custom_data}')
                result = requests.post(url=url, headers=self.headers, json=custom_data)
            else:
                self.logger.info(f'Делаю POST запрос: json {json_data}')
                result = requests.post(url=url, headers=self.headers, json=json_data)
        except Exception as error:
            self.logger.error(f'Request all entities type: {entity_type}, error: {error}')
            raise AssertionError(f'Request all entities type: {entity_type}, error: {error}')

        return result

    @allure.step('Delete entity')
    def delete_entity(self, entity_id: int, entity_type: str) -> Response:
        """Удаляет сущность определенного типа
        entity_type - тип сущности
        entity_id - id удаляемой сущности"""
        self.logger.info('Удаляю сущность')
        url = None

        if entity_type == Code.CRIMETYPE:
            url = self.url + Code.API_CRIMETYPES + f'/{entity_id}'
        elif entity_type == Code.REGION:
            url = self.url + Code.API_REGIONS + f'/{entity_id}'
        elif entity_type == Code.TAG:
            url = self.url + Code.API_TAGS + f'/{entity_id}'
        elif entity_type == Code.DEPARTMENT:
            url = self.url + Code.API_ADD_DEPARTMENT[:-1] + f'/{entity_id}'
        elif entity_type == Code.HASH:
            url = self.url + Code.API_HASHES + f'/{entity_id}'
        elif entity_type == Code.KEYWORD_SET:
            url = self.url + Code.API_KEYWORDS_SETS + f'/{entity_id}'
        elif entity_type == Code.USER:
            url = self.url + Code.API_USERS + f'/{entity_id}'

        try:
            self.logger.info(f'Делаю запрос DELETE: {url}')
            result = requests.delete(url=url, headers=self.headers)
        except Exception as error:
            self.logger.error(f'Delete entity: {entity_type}, error: {error}')
            raise AssertionError(f'Delete entity: {entity_type}, error: {error}')

        return result

    @allure.step('Content update')
    def content_update(self, json_data: dict, entity_type: str) -> Response:
        """Обновляет список слов сущности"""
        self.logger.info(f'Content update: {entity_type}')
        url = None

        if entity_type == Code.KEYWORD_SET:
            url = self.url + Code.API_KEYWORDS_SETS_WORDS

        try:
            self.logger.info(f'Делаю POST запрос: {json_data}')
            result = requests.post(url=url, headers=self.headers, json=json_data)
        except Exception as error:
            self.logger.error(f'Content update: {entity_type}, error: {error}')
            raise AssertionError(f'Content update: {entity_type}, error: {error}')

        return result

    @allure.step('Get entity content')
    def get_entity_content(self, entity_type: str, entity_id: int) -> Response:
        """Получает список слов у сущности"""
        self.logger.info(f'Получаю content у {entity_type}')
        json_data = None
        url = None

        if entity_type == Code.KEYWORD_SET:
            url = self.url + Code.API_KEYWORDS_SETS_CONTENT
            json_data = KeywordsSetsData.content
            json_data['id'] = entity_id
        elif entity_type == Code.WATCHLIST:
            url = self.url + Code.API_WATCHLIST_CONTENT
            json_data = WatchlistsData.content_watchlist
            json_data['id'] = entity_id

        try:
            self.logger.info(f'Делаю POST запрос: {json_data}')
            result = requests.post(url=url, headers=self.headers, json=json_data)
        except Exception as error:
            self.logger.error(f'Entity content: {entity_type}, error: {error}')
            raise AssertionError(f'Entity content: {entity_type}, error: {error}')

        return result

    @allure.step('Update entity content')
    def update_entity_content(self, entity_type: str, json_data: dict) -> Response:
        """Обновляет список слов у сущности"""
        self.logger.info(f'Обновляю content у {entity_type}')
        url = None

        if entity_type == Code.WATCHLIST:
            url = self.url + Code.API_WATCHLIST_UPDATE
        try:
            self.logger.info(f'Делаю POST запрос: {json_data}')
            result = requests.post(url=url, headers=self.headers, json=json_data)
        except Exception as error:
            self.logger.error(f'Entity update content: {entity_type}, error: {error}')
            raise AssertionError(f'Entity update content: {entity_type}, error: {error}')

        return result

    @allure.step('Indexing entity')
    def indexing_entity(self, entity_type: str, entity_id: int) -> Response:
        """Запускает индексацию сущности"""
        self.logger.info(f'Запускаю индексацию у {entity_type}')
        url = None

        if entity_type == Code.WATCHLIST:
            url = self.url + Code.API_WATCHLIST_INDEX

        try:
            json_data = {'id': entity_id}
            self.logger.info(f'Делаю POST запрос: {json_data}')
            result = requests.post(url=url, headers=self.headers, json=json_data)
            # indexing
            time.sleep(15)
        except Exception as error:
            self.logger.error(f'Entity indexing: {entity_type}, error: {error}')
            raise AssertionError(f'Entity indexing: {entity_type}, error: {error}')

        return result

    @allure.step('Import entity')
    def import_entity(self, file_name: str, entity_type: str, encoding: str = None,
                      keyword_set_id: int = None, hash_id: int = None, hash_type: str = None,
                      watchlist_id: int = None) -> Response:
        """Импорт сущности по параметру entity_type загрузка файла с хешами или словами
        entity_type - определяет тип сущности
        encoding - кодировка
        hash_type - MD5, SHA1, SHA256"""
        self.logger.info(f'Импортирую {entity_type}')
        api_url = None
        path_to_file = None
        api_encoding = None

        if encoding == 0:
            api_encoding = "Windows-1251"
        elif encoding == 1:
            api_encoding = "UTF8"
        elif encoding == 2:
            api_encoding = "UTF16"

        if entity_type == Code.KEYWORD_SET:
            path_to_file = STAND_PATH_KEYWORDS_SETS

            api_url = self.url + f'api/dictionaries/import?id={keyword_set_id}&name={file_name}&encoding={api_encoding}'

        elif entity_type == Code.WATCHLIST:
            path_to_file = STAND_PATH_KEYWORDS_SETS

            api_url = self.url + f'api/watchlist/import?id={watchlist_id}&name={file_name}&encoding={api_encoding}'

        elif entity_type == Code.HASH:
            path_to_file = STAND_PATH_HASHES

            api_url = self.url + f'api/hashsets/import?id={hash_id}&type={hash_type}&name={file_name}'

        entity_file_path = open(f'{path_to_file}' + f'{file_name}', 'rb')
        upload_file = {'file': entity_file_path}

        self.logger.info(f'Делаю POST запрос: {upload_file}')
        result = requests.post(url=api_url, headers=self.headers, files=upload_file)

        entity_file_path.close()

        return result

    @allure.step('Log user in')
    def login_user(self, json_data: dict) -> Response:
        """Логинет пользователя"""
        self.logger.info(f'Логиню пользователя {json_data}')
        result = None

        try:
            self.logger.info(f'Делаю POST запрос: {json_data}')
            result = requests.post(url=self.url + Code.API_LOGIN, json=json_data)
        except Exception as error:
            self.logger.error(f'Login: {error}, json: {json_data}')
            AssertionError(f'Login: {error}, json: {json_data}')

        return result

    @allure.step('Log out')
    def logout_user(self, sid: Response) -> None:
        """Вылогинивает пользователя"""
        self.logger.info(f'Вылогиниваю пользователя')
        sid = sid.json()
        try:
            self.logger.info(f'Делаю GET запрос logout')
            requests.get(self.url + Code.API_LOGOUT, headers={'x-session-id': sid['SID']})
        except Exception as error:
            self.logger.error(f'Logout error: {error}')
            AssertionError(f'Logout error: {error}')

    @allure.step('Get license parameters')
    def get_license(self) -> Response:
        """Возвращает response с данными лицензии"""
        self.logger.info(f'Запрашиваю данные лицензии')
        result = None
        try:
            self.logger.info(f'Делаю GET запрос')
            result = requests.get(url=self.url + Code.API_LICENSE)
        except Exception as error:
            self.logger.error(f'Get license: {error}')
            AssertionError(f'Get license: {error}')

        return result

    @allure.step('Can upload')
    def can_upload(self, sid: Response) -> Response:
        """Проверка возможности импорта устройства"""
        self.logger.info(f'Проверяю возможность импорта устройства')
        result = None
        sid = sid.json()
        try:
            self.logger.info(f'Делаю GET запрос')
            result = requests.get(url=self.url + Code.API_CAN_UPLOAD, headers={'x-session-id': sid['SID']})
        except Exception as error:
            self.logger.error(f'Can upload: {error}')
            AssertionError(f'Can upload: {error}')

        return result

    @allure.step('Check status code')
    def check_status_code(self, result: Response, entity_type: str, verif: str) -> None:
        """Проверка статус кода
        verif - результат, который должен быть"""
        try:
            self.logger.info(f'Проверяю статус код {result.status_code} == {verif}')
            assert result.status_code == verif, f'status != {verif}'
        except AssertionError:
            self.logger.error(
                f'Request type: {entity_type}: status code: {result.status_code} != {verif}, json: {result.text}')
            raise AssertionError(
                f'Request type: {entity_type}: status code: {result.status_code} != {verif}, json: {result.text}')

    @allure.step('Check id and id type')
    def check_id_and_type(self, result: Response) -> None:
        """Проверка, что id>0 и тип id int"""
        result = result.json()
        try:
            self.logger.info(f'Проверка, что {result["id"]}>0 и тип {result["id"]} int')
            assert type(result['id']) is int and result['id'] > 0, 'wrong type or id !> 0'
        except AssertionError:
            self.logger.error(f'{type(result["id"])} is not int OR  id: {result["id"]} < 0')
            raise AssertionError(f'{type(result["id"])} is not int OR  id: {result["id"]} < 0')

    @allure.step('Check entity name')
    def check_entity_name(self, result: Response, verif: str | dict, tag_id: int = None,
                          entity_type: str = None) -> None:
        """Проверяет совпадение имени сущности с verif
        для тегов отдельная логика т.к response тегов отличается
        необходимо перебрать все и найти по id подходящий"""
        result = result.json()
        if entity_type == Code.TAG:
            try:
                for tag in result['results']:
                    if tag['id'] == tag_id:
                        self.logger.info(f'Проверяю соответствие имени у {tag["name"]} с {verif}')
                        assert tag['name'] == verif
            except AssertionError:
                raise AssertionError(f'Tag name: != {verif["name"]}')
        else:
            try:
                self.logger.info(f'Проверяю соответствие имени у {result["results"][0]["name"]} с {verif}')
                assert result['results'][0]['name'] == verif, 'name != edit_name or None'
            except AssertionError:
                self.logger.error(f'Entity name: {result["results"][0]["name"]} != {verif}')
                raise AssertionError(f'Entity name: {result["results"][0]["name"]} != {verif}')

    @allure.step('Check entities deleted')
    def check_entities_deleted(self, result: Response, entity_type: str = None) -> None:
        """Проверка, что сущность удалена
        по умолчанию в системе 23 тега
        и один суперпользователь"""
        result = result.json()

        if entity_type == Code.TAG:
            verif_num = 23
        elif entity_type == Code.USER:
            verif_num = 1
        else:
            verif_num = 0

        try:
            self.logger.info(f'Проверяю удаление {result["results"]} == {verif_num}')
            assert len(result['results']) == verif_num, f'results != {verif_num}'
        except AssertionError:
            self.logger.error(f'Len is not equal {verif_num}, {len(result["results"])} != {verif_num}')
            raise AssertionError(f'Len is not equal {verif_num}, {len(result["results"])} != {verif_num}')

    @allure.step('Check entity note')
    def check_entity_note(self, result: Response, verif: str) -> None:
        """Проверка соответствия заметки у сущности с verif"""
        result = result.json()

        try:
            self.logger.info(f'Проверяю заметку {result["results"][0]["note"]} == {verif}')
            assert result['results'][0]['note'] == verif, 'note != edit_note'
        except AssertionError:
            self.logger.error(f'Entity note: {result["results"][0]["note"]} != {verif}')
            raise AssertionError(f'Entity note: {result["results"][0]["note"]} != {verif}')

    @allure.step('Check hash type')
    def check_hash_type(self, result: Response, verif: str) -> None:
        """Проверка типа у хеша с verif"""
        result = result.json()

        try:
            self.logger.info(f'Проверяю тих хеша {result["results"][0]["type"]} == {verif}')
            assert result['results'][0]['type'] == verif, 'type != param'
        except AssertionError:
            self.logger.error(f'Hash type: {result["results"][0]["type"]} != {verif}')
            raise AssertionError(f'Hash type: {result["results"][0]["type"]} != {verif}')

    @allure.step('Check dict class')
    def check_dict_class(self, result: Response, verif: str) -> None:
        """Проверка класса у словаря с verif"""
        result = result.json()
        try:
            self.logger.info(f'Проверяю класс {result["results"][0]["dClass"]} == {verif}')
            assert result['results'][0]['dClass'] == verif, 'dClass != param'
        except AssertionError:
            self.logger.error(f'Dict class: {result["results"][0]["dClass"]} != {verif}')
            raise AssertionError(f'Dict class: {result["results"][0]["dClass"]} != {verif}')

    @allure.step('Check total')
    def check_total(self, result: Response, verif_num: int) -> None:
        """Проверка общего кол-ва элементов с verif_num"""
        result = result.json()
        try:
            self.logger.info(f'Проверяю общее кол-во элементов {result["total"]} == {verif_num}')
            assert result['total'] == verif_num, f'total != {verif_num}'
        except AssertionError:
            self.logger.error(f'Words list: {result["total"]} != {verif_num}')
            raise AssertionError(f'Words list: {result["total"]} != {verif_num}')

    @allure.step('Check total items')
    def check_total_items(self, result: Response, verif_num: int) -> None:
        """Проверка общего кол-ва элементов с verif_num"""
        result = result.json()
        try:
            self.logger.info(result)
            self.logger.info(f'Проверяю общее кол-во элементов {result["results"][0]["totalItems"]} == {verif_num}')
            assert result["results"][0]["totalItems"] == verif_num, f'total != {verif_num}'
        except AssertionError:
            self.logger.error(f'Words list: {result["results"][0]["totalItems"]} != {verif_num}')
            raise AssertionError(f'Words list: {result["results"][0]["totalItems"]} != {verif_num}')

    @allure.step('Entity content')
    def check_entity_content(self, result: Response, verif: str) -> None:
        """Проверка содержимого у сущности список слов с verif"""
        result = result.json()
        try:
            for result in result['results']:
                self.logger.info(f'Проверяю имя {result["name"]} in {verif}')
                assert result['name'] in verif, f'{result["name"]} not in {verif}'
        except AssertionError:
            self.logger.error(f'Content: {result["name"]} not in {verif}')
            raise AssertionError(f'Content: {result["name"]} not in {verif}')

    @allure.step('Check entity status')
    def check_entity_status(self, result: Response, verif: int, entity_type: str = None) -> None:
        """Проверка статуса у сущности с verif"""
        result = result.json()
        num = 0
        if entity_type == Code.USER:
            num = 1

        try:
            self.logger.info(f'Проверяю статус {result["results"][num]["status"]} == {verif}')
            assert result['results'][num]['status'] == verif, f'status != {verif}'
        except AssertionError:
            self.logger.error(f'Status: {result["results"][num]["status"]} != {verif}')
            raise AssertionError(f'Status: {result["results"][num]["status"]} != {verif}')

    @allure.step('Check field')
    def check_field(self, result: Response, verif: str | int, field_name: str, err_msg: str) -> None:
        """Проверка совпадения определенного поля в Response с field_name
        например сообщение об ошибке"""
        result = result.json()
        try:
            self.logger.info(f'Проверяю поле {field_name}:{result[field_name]} == {verif}')
            assert result[field_name] == verif, err_msg
        except AssertionError:
            self.logger.error(f'{result[field_name]} != {verif}, result: {result}')
            raise AssertionError(f'{result[field_name]} != {verif}, result: {result}')

    @allure.step('Check user is login')
    def check_already_login(self) -> None:
        """Проверка, что пользователь залогинен SID не пусто"""
        try:
            self.logger.info(f'Проверяю SID {self.headers["x-session-id"]} is not None')
            assert self.headers['x-session-id'] is not None, 'SID is not None'
        except AssertionError:
            self.logger.error(f'Login under dbadmin status code {self.headers["x-session-id"]} is None')
            raise AssertionError(f'Login under dbadmin status code {self.headers["x-session-id"]} is None')

    @allure.step('Check entity id')
    def check_entity_id(self, result: Response, verif: int) -> None:
        """Проверка id сущности с verif"""
        result = result.json()
        try:
            self.logger.info(f'Проверяю id сущности {result["id"]} == {verif}')
            assert result['id'] == verif
        except AssertionError:
            self.logger.error(f'Entity id: {result["id"]} != {verif}')
            raise AssertionError(f'Entity id: {result["id"]} != {verif}')

    @allure.step('Check sid length')
    def check_sid(self, result: Response) -> None:
        """Проверка, что длина SID больше 0"""
        result = result.json()
        try:
            self.logger.info(f'Проверяю длину SID {len(result["SID"])} > 0')
            assert len(result['SID']) > 0, 'SID is empty'
        except AssertionError:
            self.logger.error(f'SID is empty {result}')
            raise AssertionError(f'SID is empty {result}')

    @allure.step('Check license parameters')
    def check_field_bool_value(self, result: Response, field_name: str, verif: bool) -> None:
        """Проверка поля на соответствие True или False с verif"""
        result = result.json()
        try:
            self.logger.info(f'Проверяю поле True/False {result[field_name]} is {verif}')
            assert result[field_name] is verif, 'License type is Educational'
        except AssertionError:
            self.logger.error(f'Field {result[field_name]} is not {verif}')
            raise AssertionError(f'Field {result[field_name]} is not {verif}')

    @allure.step('Check sort')
    def check_sort_entity(self, result: Response, verif: str) -> None:
        """Проверка сортировки сущности
        реализовано только для тегов на данный момент"""
        result = result.json()
        check = []
        try:
            for tag in result['results']:
                check.append(tag['name'][0])
        except KeyError and IndexError as error:
            self.logger.error(f'Sort entity: {error}')
            raise AssertionError(f'Sort entity: {error}')

        try:
            self.logger.info(f'Проверяю соритровки {check} == {verif}')
            assert check == verif, f'Sort: {check} != {verif}'
        except AssertionError:
            self.logger.error(f'Sort: {check} != {verif}')
            raise AssertionError(f'Sort: {check} != {verif}')

    @allure.step('Check response')
    def check_response(self, result: Response, verif: str) -> None:
        """Проверка ответа с verif"""
        result = result.json()
        try:
            self.logger.info(f'Проверяю ответ {result} == {verif}')
            assert result == verif, f'{result} != {verif}'
        except AssertionError:
            self.logger.error(f'{result} != {verif}')
            raise AssertionError(f'{result} != {verif}')

    @staticmethod
    @allure.step('API logout from monitor')
    def api_logout_from_monitor(url: str) -> None:
        """Вылогинивает всех пользователей из монитора"""
        req_list = BeautifulSoup(requests.post(url=url + Code.API_MONITOR).text)
        for link in req_list.find_all('a')[:-1]:
            link = (link.get('href'))
            requests.post(url=url + f'{link[1:]}')
