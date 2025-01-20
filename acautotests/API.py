import random
from bs4 import BeautifulSoup
import requests
from data import ApiData, STAND_PATH_HASHES, STAND_PATH_KEYWORDS_SETS, LoginData, CodeData
import allure
import logging
import copy

log = logging.getLogger('API')
file_handler = logging.FileHandler(f"C:\\Users\\User\\Develop\\acautotests\\tests\\logs\\API.log", encoding='utf-8')
file_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
log.addHandler(file_handler)
log.setLevel(level='DEBUG')


@allure.step('API user login')
def api_user_login(url, data_for_login=LoginData.SUPER_LOGIN):
    """Возвращает SSID и логинет суперпользователя"""
    log.info('Делаю post запрос: Возвращает SSID и логинет пользователя')

    json_data = None

    if data_for_login == LoginData.SUPER_LOGIN:
        json_data = copy.deepcopy(ApiData.data_log_super)
    elif data_for_login == LoginData.ADMIN_LOGIN:
        json_data = copy.deepcopy(ApiData.data_log_admin)
    elif data_for_login == LoginData.EXPERT_LOGIN:
        json_data = copy.deepcopy(ApiData.data_log_expert)
    elif data_for_login == LoginData.LOAD_LOGIN:
        json_data = copy.deepcopy(ApiData.data_log_load)

    api_url = url + CodeData.API_LOGIN
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
def api_user_logout(url, headers):
    """Выходит из системы"""
    log.info('Делаю post запрос: Выход из системы')

    api_url = url + CodeData.API_LOGOUT
    res = requests.get(api_url, headers=headers)

    log.info(f'api_user_logout status code: {res.status_code}, text: {res.text}')


@allure.step('API add entity')
def api_add_entity(url, headers, entity_type, user_status=CodeData.ADMIN, user_id=None, user_login=None, user_name=None,
                   user_lastname=None, position=None,
                   departments_id=None, department_name=None, department_note=None, case_name=None, case_id=None,
                   cases_list=None,
                   region_name=None, crime_type_name=None,
                   tag_name=None, hash_name=None, hash_type=None, hash_note=None, keyword_set_name=None,
                   keyword_set_note=None, keyword_class=None, watchlist_name=None, watchlist_class=None,
                   watchlist_note=None, watchlist_field=None):
    """Создает новую сущность по параметру entity"""
    log.info(f'Делаю post запрос: создаю сущность {entity_type}')

    json_data = None
    api_url = None

    if entity_type == CodeData.USER:
        if user_status == CodeData.ADMIN:
            json_data = copy.deepcopy(ApiData.data_admin)
        elif user_status == CodeData.EXPERT:
            json_data = copy.deepcopy(ApiData.data_expert)
        elif user_status == CodeData.LOAD:
            json_data = copy.deepcopy(ApiData.data_load)
        elif user_status == 0:
            json_data = copy.deepcopy(ApiData.super)

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
        api_url = url + CodeData.API_ADD_USER

    elif entity_type == CodeData.DEPARTMENT:
        json_data = copy.deepcopy(ApiData.data_test_dep)
        if department_name:
            json_data['name'] = department_name
        if department_note:
            json_data['note'] = department_note
        if case_id:
            json_data['casesId'] = [case_id]
        if user_id:
            json_data['usersId'] = [user_id]
        api_url = url + CodeData.API_ADD_DEPARTMENT

    elif entity_type == CodeData.CASE:
        json_data = copy.deepcopy(ApiData.data_test_case)
        if case_name:
            json_data['name'] = case_name
        json_data['number'] = str(random.randrange(1000, 5000) + random.randrange(10, 500))
        api_url = url + CodeData.API_ADD_CASE

    elif entity_type == CodeData.REGION:

        json_data = copy.deepcopy(ApiData.data_region)
        if region_name:
            json_data['name'] = region_name
        api_url = url + CodeData.API_ADD_REGION

    elif entity_type == CodeData.CRIMETYPE:
        json_data = copy.deepcopy(ApiData.data_crime_type)
        if crime_type_name:
            json_data['name'] = crime_type_name
        api_url = url + CodeData.API_ADD_CRIMETYPE

    elif entity_type == CodeData.TAG:
        json_data = copy.deepcopy(ApiData.data_tag)
        if tag_name:
            json_data['name'] = tag_name
        api_url = url + CodeData.API_ADD_TAG

    elif entity_type == CodeData.HASH:
        json_data = copy.deepcopy(ApiData.data_hash)
        if hash_name:
            json_data['name'] = hash_name
        if hash_type:
            json_data['type'] = hash_type
        if hash_note:
            json_data['note'] = hash_note
        api_url = url + CodeData.API_ADD_HASH

    elif entity_type == CodeData.KEYWORD_SET:
        json_data = copy.deepcopy(ApiData.data_keyword_set)
        if keyword_set_name:
            json_data['name'] = keyword_set_name
        if keyword_class or keyword_class == 0:
            json_data['dClass'] = keyword_class
        if keyword_set_note:
            json_data['note'] = keyword_set_note
        api_url = url + CodeData.API_ADD_KEYWORDS_SET

    elif entity_type == CodeData.WATCHLIST:
        json_data = copy.deepcopy(ApiData.data_watchlist)
        if watchlist_name:
            json_data['name'] = watchlist_name
        if watchlist_class or watchlist_class == 0:
            json_data['dClass'] = watchlist_class
        if watchlist_note:
            json_data['note'] = watchlist_note
        if watchlist_field:
            json_data['field'] = watchlist_field
        api_url = url + CodeData.API_ADD_WATCHLIST

    log.info(f'{json_data}')
    res = requests.post(api_url, json=json_data, headers=headers)
    log.info(f'api_add_entity: {entity_type}, status code: {res.status_code}, text: {res.text}')

    del json_data
    try:
        return res.json()['id']
    except KeyError as error:
        logging.error(f'res json: {res.json()}, error: {error}')


@allure.step('API get full list')
def api_get_id_entity_list(url, headers, entity_type):
    """Возвращает список id всех запрошенных сущностей в параметре entity_type"""
    log.info(f'Делаю post запрос: Возвращает список {entity_type}')

    devices_stop_list = [1, 2, 3, 4, 5, 6, 7, 8]
    users_stop_list = [1]
    cases_stop_list = [1, 2, 3, 4]
    tags_stop_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]
    api_url = None

    if entity_type == CodeData.USER:
        api_url = url + CodeData.API_USERS
    elif entity_type == CodeData.DEPARTMENT:
        api_url = url + CodeData.API_DEPARTMENTS
    elif entity_type == CodeData.CASE:
        api_url = url + CodeData.API_CASES
    elif entity_type == CodeData.REGION:
        api_url = url + CodeData.API_REGIONS
    elif entity_type == CodeData.CRIMETYPE:
        api_url = url + CodeData.API_CRIMETYPES
    elif entity_type == CodeData.TAG:
        api_url = url + CodeData.API_TAGS
    elif entity_type == CodeData.HASH:
        api_url = url + CodeData.API_HASHES
    elif entity_type == CodeData.KEYWORD_SET:
        api_url = url + CodeData.API_KEYWORDS_SETS
    elif entity_type == CodeData.DEVICE:
        api_url = url + CodeData.API_DEVICES
    elif entity_type == CodeData.WATCHLIST:
        api_url = url + CodeData.API_WATCHLIST

    res = requests.post(api_url, json=ApiData.data_log_super, headers=headers)
    log.info(f'api_get_id__entity_list: {entity_type}, status code: {res.status_code}, text: {res.text}')
    del api_url

    if entity_type == CodeData.USER:
        return [user['id'] for user in res.json()['results'] if user['id'] not in users_stop_list]
    elif entity_type == CodeData.DEVICE:
        return [device['id'] for device in res.json()['results'] if device['id'] not in devices_stop_list]
    elif entity_type == CodeData.CASE:
        return [case['id'] for case in res.json()['results'] if case['id'] not in cases_stop_list]
    elif entity_type == CodeData.TAG:
        return [tag['id'] for tag in res.json()['results'] if tag['id'] not in tags_stop_list]
    else:
        return [entity['id'] for entity in res.json()['results'] if entity['id']]


@allure.step('API get dict of entity')
def api_get_entity_dict(url, headers, entity_type):
    """Возвращает список запрошенных сущностей в параметре entity_type"""
    log.info(f'Делаю post запрос: Возвращает список {entity_type}')

    api_url = None

    if entity_type == CodeData.USER:
        api_url = url + CodeData.API_USERS
    elif entity_type == CodeData.DEPARTMENT:
        api_url = url + CodeData.API_DEPARTMENTS
    elif entity_type == CodeData.CASE:
        api_url = url + CodeData.API_CASES
    elif entity_type == CodeData.REGION:
        api_url = url + CodeData.API_REGIONS
    elif entity_type == CodeData.CRIMETYPE:
        api_url = url + CodeData.API_CRIMETYPES
    elif entity_type == CodeData.TAG:
        api_url = url + CodeData.API_TAGS
    elif entity_type == CodeData.HASH:
        api_url = url + CodeData.API_HASHES
    elif entity_type == CodeData.KEYWORD_SET:
        api_url = url + CodeData.API_KEYWORDS_SETS
    elif entity_type == CodeData.DEVICE:
        api_url = url + CodeData.API_DEVICES

    res = requests.post(api_url, json=ApiData.data_log_super, headers=headers)
    log.info(f'api_get_entity_dict: {entity_type}, status code: {res.status_code}, text: {res.text}')
    del api_url

    return res.json()


@allure.step('API delete entity')
def api_delete_entity(url, headers, entity_type, entity_id=None):
    """Удаляет сущность по параметру entity_type"""
    log.info(f'Произвожу удаление type {entity_type} id {entity_id}')
    api_url = None

    if entity_type == CodeData.USER:
        api_url = url + f'api/users/{entity_id}'
    elif entity_type == CodeData.DEPARTMENT:
        api_url = url + f'api/account/group/{entity_id}'
    elif entity_type == CodeData.CASE:
        api_url = url + f'api/cases/{entity_id}'
    elif entity_type == CodeData.REGION:
        api_url = url + f'api/regions/{entity_id}'
    elif entity_type == CodeData.CRIMETYPE:
        api_url = url + f'api/crimetypes/{entity_id}'
    elif entity_type == CodeData.TAG:
        api_url = url + f'api/tags/{entity_id}'
    elif entity_type == CodeData.HASH:
        api_url = url + f'api/hashsets/{entity_id}'
    elif entity_type == CodeData.KEYWORD_SET:
        api_url = url + f'api/dictionaries/{entity_id}'
    elif entity_type == CodeData.DEVICE:
        api_url = url + f'api/devices/{entity_id}'
    elif entity_type == CodeData.WATCHLIST:
        api_url = url + f'api/watchlist/{entity_id}'
    log.info(f'{api_url} удаление')
    res = requests.delete(api_url, headers=headers)

    log.info(f'api_delete_entity: {entity_type}, status code: {res.status_code}, text: {res.text}')


@allure.step('API import entity')
def api_import_entity(url, headers, file_name, entity_type, encoding=None,
                      keyword_set_id=None, hash_id=None, hash_type=None):
    """Импорт сущности по параметру entity_type"""
    log.info(f'Произвожу импорт в систему {entity_type}, {file_name}')

    api_url = None
    path_to_file = None

    if entity_type == CodeData.KEYWORD_SET:
        path_to_file = STAND_PATH_KEYWORDS_SETS

        api_encoding = None
        if encoding == 0:
            api_encoding = "Windows-1251"
        elif encoding == 1:
            api_encoding = "UTF8"
        elif encoding == 2:
            api_encoding = "UTF16"

        api_url = url + f'api/dictionaries/import?id={keyword_set_id}&name={file_name}&encoding={api_encoding}'
        log.info(f'api/dictionaries/import?id={keyword_set_id}&name={file_name}&encoding={api_encoding}')

    elif entity_type == CodeData.HASH:
        path_to_file = STAND_PATH_HASHES

        api_url = url + f'api/hashsets/import?id={hash_id}&type={hash_type}&name={file_name}'
        log.info(f'api/hashsets/import?id={hash_id}&type={hash_type}&name={file_name}')

    entity_file_path = open(f'{path_to_file}' + f'{file_name}', 'rb')
    upload_file = {'file': entity_file_path}

    res = requests.post(url=api_url, headers=headers, files=upload_file)

    entity_file_path.close()

    log.info(f'api_import_entity: {entity_type}, status code: {res.status_code}, text: {res.text}')


@allure.step('API reload backend')
def api_reload_back(url):
    """Перезапускает бек-енд"""
    log.info('Делаю get запрос: Перезапускаю систему')

    api_url = url + '/api/quit'
    res = requests.get(api_url)

    log.info(f'api_reload_back status code: {res.status_code}, text: {res.text}')


@allure.step('API return entity id')
def api_get_added_entity_id(data, entity_name=None, entity_fname=None):
    """Возвращает id сущности по параметру entity_type"""
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


@allure.step('API return entity id')
def api_get_added_entity_id_of_login(data, entity_login=None):
    """Возвращает id сущности по параметру entity_type"""

    if entity_login:
        for entity in data['results']:
            if entity['login'] == entity_login:
                log.info(f'api_get_added_entity_id_of_login: Возвращает login {entity_login} id {entity["id"]}')
                return entity['id']


@allure.step('API logout from monitor')
def api_logout_from_monitor(url):
    """Вылогинивает всех пользователей из монитора"""
    log.info('Вылогиниваю из монитора')
    req_list = BeautifulSoup(requests.post(url=url + CodeData.API_MONITOR).text)
    for link in req_list.find_all('a')[:-1]:
        link = (link.get('href'))
        requests.post(url=url + f'{link[1:]}')
        log.info(f'Вылогинил: {link}')
