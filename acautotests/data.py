ENV_HOST = 'http://127.0.0.1/'
MY_PATH = '/home/nik/Downloads/'
STAND_PATH = 'C:\\Test_data\\'
STAND_PATH_EMPTY = 'C:\\Test_data\\empty\\'
STAND_PATH_INVALID = 'C:\\Test_data\\invalid\\'
STAND_PATH_HASHES = 'C:\\Test_data\\hashes\\'
STAND_PATH_KEYWORDS_SETS = 'C:\\Test_data\\keywords_sets\\'
STAND_PATH_DOWNLOADS = 'C:\\Users\\User\\Downloads\\'
STAND_PATH_LICENSE = 'C:\\Test_data\\license\\'
STAND_BACKEND = 'C:\\backend\\'


class DataBase:
    DATABASE = 'ocsViewDB'
    USER = 'postgres'
    PASSWORD = 'pgpassword'
    HOST = '127.0.0.1'
    PORT = '5432'


class CasesData:
    PAGE = 'lk/cases?noSSE=1'
    CASE = 'Auto_test_case'


class DevicesData:
    PAGE = 'lk/devices?noSSE=1'
    DEVICE = 'Apple iPhone 6 Chats'
    DEVICE_NAME = 'Device_for_test'


class LoadImagesData:
    PAGE = 'lk/queue-devices?stop=1&noSSE=1'


class RegionsData:
    PAGE = 'lk/regions?noSSE=1'
    REG1 = 'Moscow region'
    REG2 = 'Tokyo city'


class CrimeTypesData:
    PAGE = 'lk/crime-types?noSSE=1'
    CRIME1 = 'Theft'
    CRIME2 = 'Robbery'


class WorkspaceData:
    PAGE = 'lk/workspace/?noSSE=1'
    LOAD_TEXT = 'Loading... Please wait'
    GRID_NO_RESULTS = 'No results found.'


class TagsData:
    PAGE = 'lk/tags?noSSE=1'
    TAG1 = 'New test tag'
    TAG2 = 'Second New test tag'
    TAG_CARDS = 'Maps'


class HashesData:
    PAGE = 'lk/hashes?noSSE=1'
    HASH_MD5 = 'test_md5'
    HASH_SHA1 = 'test_sha-1'
    HASH_SHA256 = 'test_sha-256'
    HASH_MD5_2 = 'test_md5_2'
    HASH_SHA1_2 = 'test_sha-1_2'
    HASH_SHA256_2 = 'test_sha-256_2'
    TYPE_MD5 = 0
    TYPE_SHA1 = 1
    TYPE_SHA256 = 2
    API_MD5 = 'MD5'
    API_SHA1 = 'SHA1'
    API_SHA256 = 'SHA256'
    NOTE = 'New hash for test'


class KeywordsSetsData:
    PAGE = 'lk/dictionaries?noSSE=1'
    NOTE = 'New test keyword set'
    EMPTY = 'Empty keyword set'
    TEST = 'Test keyword'
    TEST_2 = 'Test keyword for test'
    TYPE_ALL_PAGES = 2
    TYPE_FILES = 1
    TYPE_WRKSPACE_CONTACTS_MAP = 0
    WEAPON = 'Weapon'
    PISTOLET = 'Guns'
    TYPE_1251 = 0
    TYPE_UTF8 = 1
    TYPE_UTF16 = 2
    API_ALL_PAGES = 0
    API_FILES = 2
    API_WRKSPACE_CONTACTS_MAP = 1


class WatchListsData:
    PAGE = 'lk/watchlist'


class DepartmentsData:
    PAGE = 'lk/departments?noSSE=1'
    DEPARTMENT_NAME_1 = 'new_test_department'
    DEPARTMENT_NAME_2 = 'new_test_department1'
    DEPARTMENT_NAME_3 = 'new_test_department2'
    DEPARTMENT_PART_NAME = 'new_part_department'
    DEPARTMENT_PART = 'part_dep'
    DEPARTMENT_NOTE = 'Note for test department\n       '
    CASE_NAME_1 = 'Auto_test_case'
    CASE_NAME_2 = 'Auto_test_case1'
    CASE_NAME_3 = 'Auto_test_case2'
    USER_LOGIN_1 = 'Sergey'
    USER_NAME_1 = 'Sergey'
    DEPARTMENT_NOTE_2 = 'Note for department'


class LoginData:
    PAGE = 'lk/admin?noSSE=1'
    SUPER_LOGIN = 'dbadmin'
    SUPER_PASSWORD = '1Qwerty'
    ADMIN_LOGIN = 'login12'
    EXPERT_LOGIN = 'login12_ex'
    EXPERT_LOGIN_2 = 'login12_ex_2'
    LOAD_LOGIN = 'login12_load'
    FIRST_NAME = 'Sergey'
    LAST_NAME = 'Ivanov'
    LAST_NAME_2 = 'Ivanov'
    NEW_FIRST_NAME = 'Andrew'
    NEW_LAST_NAME = 'Petrov'
    NEW_LAST_NAME_2 = 'Ivanov'
    PASSWORD = 'Vibnb47'
    NEW_PASSWORD = 'Newpassword12'
    INVALID_PASSWORD = 'Vi47bnb'
    INVALID_LOGIN = 'LOGin321'
    STATUS_ADMIN = 'admin'
    STATUS_EXPERT = 'expert'
    STATUS_LOAD = 'load'
    HALF_LOGIN = 'login'
    HALF_NAME = 'Ser'
    HALF_LAST_NAME = 'Iva'
    USER = 'mmmmm'
    USER_PW = '1Qwerty'


class ApiData:
    data_log_super = {'login': LoginData.SUPER_LOGIN, 'password': LoginData.SUPER_PASSWORD}
    data_log_admin = {'login': LoginData.ADMIN_LOGIN, 'password': LoginData.PASSWORD}
    data_log_expert = {'login': LoginData.EXPERT_LOGIN, 'password': LoginData.PASSWORD}
    data_log_load = {'login': LoginData.LOAD_LOGIN, 'password': LoginData.PASSWORD}

    data_admin = {
        "login": "login12",
        "status": 1,
        "firstName": "Sergey",
        "middleName": "",
        "lastName": "Ivanov",
        "position": "",
        "phoneNo": "",
        "email": "",
        "disabled": False,
        "password": "Vibnb47",
        "passwordCopy": "Vibnb47",
        "id": 0,
        "casesId": [],
        "departmentsId": [],
        "canReadReports": True
    }

    data_expert = {
        "login": "login12_ex",
        "status": 2,
        "firstName": "Sergey",
        "middleName": "",
        "lastName": "Ivanov",
        "position": "",
        "phoneNo": "",
        "email": "",
        "disabled": False,
        "password": "Vibnb47",
        "passwordCopy": "Vibnb47",
        "id": 0,
        "casesId": [],
        "departmentsId": [],
        "canReadReports": True
    }

    data_load = {
        "login": "login12_load",
        "status": 4,
        "firstName": "Sergey",
        "middleName": "",
        "lastName": "Ivanov",
        "position": "",
        "phoneNo": "",
        "email": "",
        "disabled": False,
        "password": "Vibnb47",
        "passwordCopy": "Vibnb47",
        "id": 0,
        "casesId": [],
        "departmentsId": [],
        "canReadReports": True
    }

    super = {
        "login": "login12_super",
        "status": 0,
        "firstName": "Sergey",
        "middleName": "",
        "lastName": "Ivanov",
        "position": "",
        "phoneNo": "",
        "email": "",
        "disabled": False,
        "password": "1Qwerty",
        "passwordCopy": "1Qwerty",
        "id": 0,
        "casesId": [],
        "departmentsId": [],
        "canReadReports": True
    }

    data_admin_cases = {
        "login": "login12",
        "status": 1,
        "firstName": "Sergey",
        "middleName": "",
        "lastName": "Ivanov",
        "position": "",
        "phoneNo": "",
        "email": "",
        "disabled": False,
        "password": "Vibnb47",
        "passwordCopy": "Vibnb47",
        "id": 0,
        "casesId": [],
        "departmentsId": [],
        "canReadReports": True
    }

    data_test_dep = {
        "name": "test",
        "note": "new department test",
        "id": 0,
        "casesId": [],
        "usersId": []
    }

    data_test_case = {
        "number": "",
        "name": "auto_test_case",
        "department": "",
        "status": "1",
        "crimeDate": None,
        "note": "",
        "region": 0,
        "crimeType": 0,
        "id": 0,
        "devicesId": []
    }

    data_region = {"name": "",
                   "id": 0}

    data_crime_type = {"name": "",
                       "id": 0}

    data_tag = {"name": "",
                "id": 0}

    data_hash = {
        "name": "",
        "type": "",
        "note": "",
        "hideThumbnail": False,
        "addHashAfterCreated": False
    }

    data_keyword_set = {
        "name": "",
        "type": 1,
        "dClass": 1,
        "authorName": "dbadmin",
        "note": "",
        "words": []
    }

    data_watchlist = {
        "name": "",
        "dClass": 1,
        "note": "",
        "field": "phoneNumber",
        "words": []
    }


class CodeData:
    API_LOGIN = 'api/account/login'
    API_LOGOUT = 'api/account/logout'
    API_LOGOUT_LOGIN = 'api/logout?login='
    API_ADD_USER = 'api/users/0'
    API_ADD_DEPARTMENT = 'api/account/group/0'
    API_ADD_CASE = 'api/cases/0'
    API_ADD_REGION = 'api/regions/0'
    API_ADD_CRIMETYPE = 'api/crimetypes/0'
    API_ADD_TAG = 'api/tags/0'
    API_ADD_HASH = 'api/hashsets/0'
    API_ADD_KEYWORDS_SET = 'api/dictionaries/0'
    API_ADD_WATCHLIST = 'api/watchlist/0'
    API_USERS = 'api/users'
    API_DEPARTMENTS = 'api/account/groups'
    API_CASES = 'api/cases'
    API_REGIONS = 'api/regions'
    API_CRIMETYPES = 'api/crimetypes'
    API_TAGS = 'api/tags'
    API_HASHES = 'api/hashsets'
    API_KEYWORDS_SETS = 'api/dictionaries'
    API_DEVICES = 'api/devices'
    API_ACTIVITIES = 'api/activities'
    API_MONITOR = 'api/monitor'
    API_WATCHLIST = 'api/watchlist'
    USER = 'user'
    ADMIN = 'admin'
    EXPERT = 'expert'
    LOAD = 'load'
    DEPARTMENT = 'department'
    CASE = 'case'
    KEYWORD_SET = 'keyword_set'
    REGION = 'region'
    CRIMETYPE = 'crime_type'
    TAG = 'tag'
    DEVICE = 'device'
    HASH = 'hashset'
    WATCHLIST = 'watchlist'
