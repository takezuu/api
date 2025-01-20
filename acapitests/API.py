import random
from bs4 import BeautifulSoup
import requests
from data import STAND_PATH_HASHES, STAND_PATH_KEYWORDS_SETS, Code
from Pages_data.API_cases_data import CasesData
from Pages_data.API_tags_data import TagsData
from Pages_data.API_keywords_sets_data import KeywordsSetsData
from Pages_data.API_hashes_data import HashesData
from Pages_data.API_crime_types_data import CrimeTypesData
from Pages_data.API_regions_data import RegionsData
from Pages_data.API_departments_data import DepartmentsData
from Pages_data.API_login_data import LoginData
from Pages_data.API_watchlists_data import WatchlistsData
import allure
import logging
import copy

my_log_path = 'C:\\Users\\User\\Develop\\acapitests\\tests\\logs\\API.log'
vm_log_path = 'C:\\ProgramData\\Jenkins\\.jenkins\\workspace\\Auto\\logs\\API.log'
log = logging.getLogger('API')
file_handler = logging.FileHandler(f"{my_log_path}", encoding='utf-8')
file_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
log.addHandler(file_handler)
log.setLevel(level='DEBUG')


@allure.step('API user login')
def api_user_login(url: str, data_for_login: str = LoginData.SUPER_LOGIN) -> dict:
    """Возвращает SID и логинет пользователя"""
    log.info('Делаю post запрос: Возвращает SID и логинет пользователя')

    json_data = None

    if data_for_login == LoginData.SUPER_LOGIN:
        json_data = copy.deepcopy(LoginData.data_log_super)
    elif data_for_login == LoginData.ADMIN_LOGIN:
        json_data = copy.deepcopy(LoginData.data_log_admin)
    elif data_for_login == LoginData.EXPERT_LOGIN:
        json_data = copy.deepcopy(LoginData.data_log_expert)
    elif data_for_login == LoginData.LOAD_LOGIN:
        json_data = copy.deepcopy(LoginData.data_log_load)

    api_url = url + Code.API_LOGIN
    log.info(f'{json_data}')
    try:
        ssid = requests.post(api_url, json=json_data).json()
        return {'x-session-id': ssid['SID']}

    except KeyError:
        log.info(f'Вылогиниваю monitor')
        api_logout_from_monitor(url)
        log.info(f'Делаю повторный вход')
        ssid = requests.post(api_url, json=json_data).json()
        return {'x-session-id': ssid['SID']}


@allure.step('API user logout')
def api_user_logout(url: str, headers: dict) -> None:
    """Вылогинивает пользователя из системы"""
    log.info('Делаю post запрос: Выход из системы')
    api_url = url + Code.API_LOGOUT
    res = requests.get(api_url, headers=headers)

    log.info(f'api_user_logout status code: {res.status_code}, text: {res.text}')


@allure.step('API add entity')
def api_add_entity(url: str, headers: dict, entity_type: str, user_status: str = Code.ADMIN, entity_name: str = None,
                   user_id: int = None, user_login: str = None,
                   user_name: str = None,
                   user_lastname: str = None, position: str = None,
                   departments_id: int = None, department_note: str = None, case_id: int = None,
                   cases_list: list = None,
                   hash_type: str = None, hash_note: str = None,
                   keyword_set_note: str = None, keyword_class: str = None, watchlist_class: str = None,
                   watchlist_note: str = None, watchlist_field: str = None, watchlist_words: list = None) -> int:
    """Создает новую сущность по параметру entity"""
    log.info(f'Делаю post запрос: создаю сущность {entity_type}')

    json_data = None
    api_url = None

    if entity_type == Code.USER:
        if user_status == Code.ADMIN:
            json_data = copy.deepcopy(LoginData.data_admin)
        elif user_status == Code.EXPERT:
            json_data = copy.deepcopy(LoginData.data_expert)
        elif user_status == Code.LOAD:
            json_data = copy.deepcopy(LoginData.data_load)
        elif user_status == 0:
            json_data = copy.deepcopy(LoginData.super)

        if user_login:
            json_data['login'] = user_login
        if user_name:
            json_data['firstName'] = user_name
        if user_lastname:
            json_data['lastName'] = user_lastname
        if position:
            json_data['position'] = position
        if cases_list is not None:
            json_data['casesId'] = cases_list
        if case_id:
            json_data['casesId'] = [case_id]
        if departments_id:
            json_data['departmentsId'] = [departments_id]
        api_url = url + Code.API_ADD_USER

    elif entity_type == Code.DEPARTMENT:
        json_data = copy.deepcopy(DepartmentsData.data_test_dep)
        if entity_name:
            json_data['name'] = entity_name
        if department_note:
            json_data['note'] = department_note
        if case_id:
            json_data['casesId'] = [case_id]
        if user_id:
            json_data['usersId'] = [user_id]
        api_url = url + Code.API_ADD_DEPARTMENT

    elif entity_type == Code.CASE:
        json_data = copy.deepcopy(CasesData.data_test_case)
        if entity_name:
            json_data['name'] = entity_name
        json_data['number'] = str(random.randrange(1000, 5000) + random.randrange(10, 500))
        api_url = url + Code.API_ADD_CASE

    elif entity_type == Code.REGION:

        json_data = copy.deepcopy(RegionsData.data_region)
        if entity_name:
            json_data['name'] = entity_name
        api_url = url + Code.API_ADD_REGION

    elif entity_type == Code.CRIMETYPE:
        json_data = copy.deepcopy(CrimeTypesData.data_crime_type)
        if entity_name:
            json_data['name'] = entity_name
        api_url = url + Code.API_ADD_CRIMETYPE

    elif entity_type == Code.TAG:
        json_data = copy.deepcopy(TagsData.data_tag)
        if entity_name:
            json_data['name'] = entity_name
        api_url = url + Code.API_ADD_TAG

    elif entity_type == Code.HASH:
        json_data = copy.deepcopy(HashesData.data_hash)
        if entity_name:
            json_data['name'] = entity_name
        if hash_type:
            json_data['type'] = hash_type
        if hash_note:
            json_data['note'] = hash_note
        api_url = url + Code.API_ADD_HASH

    elif entity_type == Code.KEYWORD_SET:
        json_data = copy.deepcopy(KeywordsSetsData.data_keyword_set)
        if entity_name:
            json_data['name'] = entity_name
        if keyword_class or keyword_class == 0:
            json_data['dClass'] = keyword_class
        if keyword_set_note:
            json_data['note'] = keyword_set_note
        api_url = url + Code.API_ADD_KEYWORDS_SET

    elif entity_type == Code.WATCHLIST:
        json_data = copy.deepcopy(WatchlistsData.create_watchlist)
        if entity_name:
            json_data['name'] = entity_name
        if watchlist_class or watchlist_class == 0:
            json_data['dClass'] = watchlist_class
        if watchlist_note:
            json_data['note'] = watchlist_note
        if watchlist_field:
            json_data['field'] = watchlist_field
        if watchlist_words:
            json_data['words'] = watchlist_words
        api_url = url + Code.API_ADD_WATCHLIST

    log.info(f'{json_data}')
    res = requests.post(api_url, json=json_data, headers=headers)
    log.info(f'api_add_entity: {entity_type}, status code: {res.status_code}, text: {res.text}')

    del json_data
    try:
        return res.json()['id']
    except KeyError as error:
        logging.error(f'res json: {res.json()}, error: {error}')


@allure.step('API add entity')
def api_add_entity1(url: str, headers: dict, entity_type: str, custom_data: dict, user_status: str = Code.ADMIN) -> int:
    """Создает новую сущность по параметру entity"""
    log.info(f'Делаю post запрос: создаю сущность {entity_type}')

    api_url = None
    json_data = None

    if entity_type == Code.USER:
        api_url = url + Code.API_ADD_USER
        if user_status == Code.ADMIN:
            json_data = copy.deepcopy(LoginData.data_admin)
        elif user_status == Code.EXPERT:
            json_data = copy.deepcopy(LoginData.data_expert)
        elif user_status == Code.LOAD:
            json_data = copy.deepcopy(LoginData.data_load)
        elif user_status == 0:
            json_data = copy.deepcopy(LoginData.super)

    elif entity_type == Code.DEPARTMENT:
        api_url = url + Code.API_ADD_DEPARTMENT
        json_data = copy.deepcopy(DepartmentsData.data_test_dep)

    elif entity_type == Code.CASE:
        api_url = url + Code.API_ADD_CASE
        json_data = copy.deepcopy(CasesData.data_test_case)

    elif entity_type == Code.REGION:
        api_url = url + Code.API_ADD_REGION
        json_data = copy.deepcopy(RegionsData.data_region)

    elif entity_type == Code.CRIMETYPE:
        api_url = url + Code.API_ADD_CRIMETYPE
        json_data = copy.deepcopy(CrimeTypesData.data_crime_type)

    elif entity_type == Code.TAG:
        api_url = url + Code.API_ADD_TAG
        json_data = copy.deepcopy(TagsData.data_tag)

    elif entity_type == Code.HASH:
        api_url = url + Code.API_ADD_HASH
        json_data = copy.deepcopy(HashesData.data_hash)

    elif entity_type == Code.KEYWORD_SET:
        api_url = url + Code.API_ADD_KEYWORDS_SET
        json_data = copy.deepcopy(KeywordsSetsData.data_keyword_set)

    elif entity_type == Code.WATCHLIST:
        api_url = url + Code.API_ADD_WATCHLIST
        json_data = copy.deepcopy(WatchlistsData.data_watchlist)

    if custom_data:
        log.info(f'{custom_data}')
        res = requests.post(api_url, json=custom_data, headers=headers)
    else:
        log.info(f'{json_data}')
        res = requests.post(api_url, json=json_data, headers=headers)
    log.info(f'api_add_entity: {entity_type}, status code: {res.status_code}, text: {res.text}')

    try:
        return res.json()['id']
    except KeyError as error:
        logging.error(f'res json: {res.json()}, error: {error}')


@allure.step('API get full list')
def api_get_id_entity_list(url: str, headers: dict, entity_type: str) -> list:
    """Возвращает список id всех запрошенных сущностей в параметре entity_type
    кроме перечисленных в стоп списках"""
    log.info(f'Делаю post запрос: Возвращает список {entity_type}')

    devices_stop_list = [1, 2, 3, 4, 5, 6, 7, 8]
    users_stop_list = [1]
    cases_stop_list = [1, 2, 3, 4]
    tags_stop_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]
    api_url = None

    if entity_type == Code.USER:
        api_url = url + Code.API_USERS
    elif entity_type == Code.DEPARTMENT:
        api_url = url + Code.API_DEPARTMENTS
    elif entity_type == Code.CASE:
        api_url = url + Code.API_CASES
    elif entity_type == Code.REGION:
        api_url = url + Code.API_REGIONS
    elif entity_type == Code.CRIMETYPE:
        api_url = url + Code.API_CRIMETYPES
    elif entity_type == Code.TAG:
        api_url = url + Code.API_TAGS
    elif entity_type == Code.HASH:
        api_url = url + Code.API_HASHES
    elif entity_type == Code.KEYWORD_SET:
        api_url = url + Code.API_KEYWORDS_SETS
    elif entity_type == Code.DEVICE:
        api_url = url + Code.API_DEVICES
    elif entity_type == Code.WATCHLIST:
        api_url = url + Code.API_WATCHLIST

    res = requests.post(api_url, json=LoginData.data_log_super, headers=headers)
    log.info(f'api_get_id__entity_list: {entity_type}, status code: {res.status_code}, text: {res.text}')
    del api_url
    res = res.json()

    if entity_type == Code.USER:
        return [user['id'] for user in res['results'] if user['id'] not in users_stop_list]
    elif entity_type == Code.DEVICE:
        return [device['id'] for device in res['results'] if device['id'] not in devices_stop_list]
    elif entity_type == Code.CASE:
        return [case['id'] for case in res['results'] if case['id'] not in cases_stop_list]
    elif entity_type == Code.TAG:
        return [tag['id'] for tag in res['results'] if tag['id'] not in tags_stop_list]
    else:
        return [entity['id'] for entity in res['results'] if entity['id']]


@allure.step('API get dict of entity')
def api_get_entity_dict(url: str, headers: dict, entity_type: str) -> dict:
    """Возвращает список запрошенных сущностей в параметре entity_type"""
    log.info(f'Делаю post запрос: Возвращает {entity_type}')

    api_url = None

    if entity_type == Code.USER:
        api_url = url + Code.API_USERS
    elif entity_type == Code.DEPARTMENT:
        api_url = url + Code.API_DEPARTMENTS
    elif entity_type == Code.CASE:
        api_url = url + Code.API_CASES
    elif entity_type == Code.REGION:
        api_url = url + Code.API_REGIONS
    elif entity_type == Code.CRIMETYPE:
        api_url = url + Code.API_CRIMETYPES
    elif entity_type == Code.TAG:
        api_url = url + Code.API_TAGS
    elif entity_type == Code.HASH:
        api_url = url + Code.API_HASHES
    elif entity_type == Code.KEYWORD_SET:
        api_url = url + Code.API_KEYWORDS_SETS
    elif entity_type == Code.WATCHLIST:
        api_url = url + Code.API_WATCHLIST
    elif entity_type == Code.DEVICE:
        api_url = url + Code.API_DEVICES

    res = requests.post(api_url, json=LoginData.data_log_super, headers=headers)
    log.info(f'api_get_entity_dict: {entity_type}, status code: {res.status_code}, text: {res.text}')
    del api_url

    return res.json()


@allure.step('API delete entity')
def api_delete_entity(url: str, headers: dict, entity_type: str, entity_id: int = None) -> None:
    """Удаляет сущность по параметру entity_type"""
    log.info(f'Произвожу удаление type {entity_type} id {entity_id}')
    api_url = None

    if entity_type == Code.USER:
        api_url = url + f'api/users/{entity_id}'
    elif entity_type == Code.DEPARTMENT:
        api_url = url + f'api/account/group/{entity_id}'
    elif entity_type == Code.CASE:
        api_url = url + f'api/cases/{entity_id}'
    elif entity_type == Code.REGION:
        api_url = url + f'api/regions/{entity_id}'
    elif entity_type == Code.CRIMETYPE:
        api_url = url + f'api/crimetypes/{entity_id}'
    elif entity_type == Code.TAG:
        api_url = url + f'api/tags/{entity_id}'
    elif entity_type == Code.HASH:
        api_url = url + f'api/hashsets/{entity_id}'
    elif entity_type == Code.KEYWORD_SET:
        api_url = url + f'api/dictionaries/{entity_id}'
    elif entity_type == Code.DEVICE:
        api_url = url + f'api/devices/{entity_id}'
    elif entity_type == Code.WATCHLIST:
        api_url = url + f'api/watchlist/{entity_id}'
    log.info(f'{api_url} удаление')
    res = requests.delete(api_url, headers=headers)

    log.info(f'api_delete_entity: {entity_type}, status code: {res.status_code}, text: {res.text}')


@allure.step('API import entity')
def api_import_entity(url: str, headers, file_name: str, entity_type: str, encoding: int = 1,
                      keyword_set_id: int = None, hash_id: int = None, hash_type: str = None,
                      watchlist_id: int = None) -> None:
    """Импорт сущности по параметру entity_type, хеши или словари"""
    log.info(f'Произвожу импорт в систему {entity_type}, {file_name}')
    api_encoding = None
    api_url = None
    path_to_file = None

    if encoding == 0:
        api_encoding = "Windows-1251"
    if encoding == 1:
        api_encoding = "UTF8"
    elif encoding == 2:
        api_encoding = "UTF16"

    if entity_type == Code.KEYWORD_SET:
        path_to_file = STAND_PATH_KEYWORDS_SETS

        api_url = url + f'api/dictionaries/import?id={keyword_set_id}&name={file_name}&encoding={api_encoding}'
        log.info(f'api/dictionaries/import?id={keyword_set_id}&name={file_name}&encoding={api_encoding}')

    elif entity_type == Code.WATCHLIST:
        path_to_file = STAND_PATH_KEYWORDS_SETS
        api_url = url + f'api/watchlist/import?id={watchlist_id}&name={file_name}&encoding={api_encoding}'
        log.info(f'api/watchlist/import?id={watchlist_id}&name={file_name}&encoding={api_encoding}')

    elif entity_type == Code.HASH:
        path_to_file = STAND_PATH_HASHES

        api_url = url + f'api/hashsets/import?id={hash_id}&type={hash_type}&name={file_name}'
        log.info(f'api/hashsets/import?id={hash_id}&type={hash_type}&name={file_name}')

    entity_file_path = open(f'{path_to_file}' + f'{file_name}', 'rb')
    upload_file = {'file': entity_file_path}

    res = requests.post(url=api_url, headers=headers, files=upload_file)

    entity_file_path.close()

    log.info(f'api_import_entity: {entity_type}, status code: {res.status_code}, text: {res.text}')


@allure.step('API return entity id')
def api_get_added_entity_id(data: dict, entity_name: str = None, entity_fname: str = None) -> int:
    """Возвращает id сущности по параметру entity_type"""
    try:
        if entity_name is not None:
            log.info(f'Запускаю поиск {entity_name} по data {data}')
            for entity in data['results']:
                if entity['name'] == entity_name:
                    log.info(f'api_get_added_entity_id: Возвращает name {entity_name} id {entity["id"]}')
                    return entity['id']
        if entity_fname is not None:
            log.info(f'Запускаю поиск {entity_fname} по data {data}')
            for entity in data['results']:
                if entity['firstName'] == entity_fname:
                    log.info(f'api_get_added_entity_id: Возвращает name {entity_fname} id {entity["id"]}')
                    return entity['id']
    except KeyError as error:
        raise AssertionError(f'KeyError: {error}')


@allure.step('API return entity id')
def api_get_added_entity_id_of_login(data: dict, entity_login: str = None) -> int:
    """Возвращает id сущности по параметру entity_type"""

    if entity_login:
        for entity in data['results']:
            if entity['login'] == entity_login:
                log.info(f'api_get_added_entity_id_of_login: Возвращает login {entity_login} id {entity["id"]}')
                return entity['id']


@allure.step('API logout from monitor')
def api_logout_from_monitor(url: str) -> None:
    """Вылогинивает всех пользователей из монитора"""
    log.info('Вылогиниваю из монитора')
    req_list = BeautifulSoup(requests.post(url=url + Code.API_MONITOR).text)
    for link in req_list.find_all('a')[:-1]:
        link = (link.get('href'))
        requests.post(url=url + f'{link[1:]}')
        log.info(f'Вылогинил: {link}')
