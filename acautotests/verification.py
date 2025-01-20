class CasesVerif:
    ADMIN_STATUS = 'Case administrator'
    SUPER_STATUS = 'Administrator'
    EXPERT_STATUS = 'Reviewer'
    LOAD_STATUS = 'Uploader'
    NAME_OF_TAB = 'Cases'
    SAVE_CHANGES = 'Changes saved'
    CASES_LIST_UPDATED = 'Cases list updated'
    CASE = 'Auto_test_case'


class DevicesVerif:
    DEVICE_DELETED = 'Device Deleted'
    NAME_OF_TAB = 'Devices'
    ALIAS_SAVED = 'Device alias saved'
    DEVICE_NAME = 'Device_for_test'


class LoadImagesVerif:
    IMAGE_UPLOAD = 'Loading file:'
    IMAGE_PROCESS = 'Packages loaded'
    IMAGE_SUCCESS_UPLOAD = 'File loaded'
    NO_RESULTS = 'No results found.'
    GRID_NOTIFI = 'Datasource load failed!'
    RED_EMPTY_NOTIFI = 'File is empty'
    RED_INVALID_NOTIFI = 'Incorrect file format'
    OFBX_DEVICE = 'Apple iPhone 6 Chats'
    OFBR_DEVICE = 'Android zip (Telegram_Android_7.1.3(channel_msgs_inc).zip)'
    ODB_DEVICE = 'Desktop extraction (zl_ermis-f_000.rar)'
    UFED_DEVICE = 'Apple UFED backup (iPad 3 WiFi (A1416))'
    XRY_DEVICE = 'Android XRY file system (test.xry)'
    OST_DEVICE = 'Microsoft Outlook Data File (test.ost)'
    PST_DEVICE = 'Microsoft Outlook Data File (test.pst)'
    MAX_DEVICES = 'The maximum number of devices available for your license has been reached'
    NAME_OF_TAB = 'Load Data'


class RegionsVerif:
    ADDED_REGION = 'Region Created'
    ZERO_COUNT = 0
    NOCASES = 'No Data.'
    NAME_OF_TAB = 'Regions'
    HAVE_CASE = 1
    SAVE_CHANGES = 'Changes saved'
    FINAL_DELETE_MESSAGE = 'Region Deleted'
    REG1 = 'Moscow region'
    REG2 = 'Tokyo city'


class CrimeTypesVerif:
    NAME_OF_TAB = 'Incidents'
    ADDED_CRIME_TYPE = 'Incident Created'
    ZERO_COUNT = 0
    NOCASES = 'No Data.'
    HAVE_CASE = 1
    SAVE_CHANGES = 'Changes saved'
    FINAL_DELETE_MESSAGE = 'Incident Deleted'
    CRIME1 = 'Theft'
    CRIME2 = 'Robbery'


class TagsVerif:
    ADDED_TAG = 'Tag created'
    ZERO_COUNT = 0
    NOCASES = 'No Data.'
    NAME_OF_TAB = 'Tags'
    HAVE_CASE = 1
    SAVE_CHANGES = 'Changes saved'
    FINAL_DELETE_MESSAGE = 'Tag deleted'
    CARDS = 'Maps'
    TAG1 = 'New test tag'
    TAG2 = 'Second New test tag'


class HashesVerif:
    ADDED_HASH = 'Hash set created'
    HASHES_UPDATED = 'List of hash sets has been updated'
    HASH_UPDATED = 'Hash set has been updated'
    ZERO_COUNT = 0
    RECORDS = 13
    NAME_OF_TAB = 'Hash sets'
    SAVE_CHANGES = 'Changes saved'
    FINAL_DELETE_MESSAGE = 'Hash set deleted'
    HASH_READY = 'Hash set is ready'
    HASH_MD5 = 'test_md5'
    HASH_SHA1 = 'test_sha-1'
    HASH_SHA256 = 'test_sha-256'
    HASH_MD5_2 = 'test_md5_2'
    HASH_SHA1_2 = 'test_sha-1_2'
    HASH_SHA256_2 = 'test_sha-256_2'
    BADGE_EMPTY = 'Empty'
    TYPE_MD5 = 'MD5'
    TYPE_SHA1 = 'SHA-1'
    TYPE_SHA256 = 'SHA-256'
    IMAGE_UPLOAD = 'Loading file:'
    IMAGE_PROCESS = 'Packages loaded'
    IMAGE_SUCCESS_UPLOAD = 'File loaded'
    NOTE = 'New hash for test'
    NO_RESULTS = 'No results found.'


class KeywordsSetsVerif:
    ADDED_KEYWORD_SET = 'Keyword set created'
    NAME_OF_TAB = 'Keyword sets'
    SAVE_CHANGES = 'Changes saved'
    FINAL_DELETE_MESSAGE = 'Keyword set deleted'
    HASH_READY = 'Keyword set is ready'
    BADGE_EMPTY = 'Empty'
    BADGE_EXPECT = 'Waiting for indexing'
    BADGE_READY = 'Ready'
    IMAGE_UPLOAD = 'Loading file:'
    IMAGE_PROCESS = 'Packages loaded'
    IMAGE_SUCCESS_UPLOAD = 'File loaded'
    NOTE = 'New test keyword set'
    NO_RESULTS = 'No results found.'
    NO_DATA = 'No Data.'
    EMPTY = 'Empty keyword set'
    TYPE_ALL_PAGES = 2
    TYPE_FILES = 1
    TYPE_WRKSPACE_CONTACTS = 0
    STR_TYPE_ALL_PAGES = 'All pages'
    STR_TYPE_FILES = 'Files'
    STR_TYPE_WRKSPACE_CONTACTS = 'Workspace and Contacts'
    ZERO_COUNT = 0
    COUNT_2 = 2
    WEAPON = 'Weapon'
    PISTOLET = 'Guns'
    TEST = 'Test keyword'
    TEST_2 = 'Test keyword for test'
    TYPE_1251 = 0
    TYPE_UTF8 = 1
    TYPE_UTF16 = 2


class WorkspaceVerif:
    NAME_OF_TAB = 'Workspace'


class ContactsVerif:
    NAME_OF_TAB = 'Contacts'


class MapVerif:
    NAME_OF_TAB = 'Map'


class FilesVerif:
    NAME_OF_TAB = 'Files'


class LoginVerif:
    LOGIN_PAGE_NOTIFICATION = 'Incorrect Login or Password'
    DEACTIVATE_ACCOUNT_NOTIFICATION = 'This account has been suspended. Please contact the administrator.'
    NAME_OF_TAB = 'Authorization'
    EYE = 'Show password'
    HIDE_EYE = 'Hide password'
    PASSWORD = 'password'
    PASSWORD_HIDE = 'text'
    LICENSE_NUM = '3343'
    LICENSE_DATE1 = '10-10-2024'
    LICENSE_DATE2 = '10-10-2023'
    IVALID_HID = 'Server Hardware ID specified in the license file is invalid'


class AdminVerif:
    NAME_OF_TAB = 'Administration Panel'
    DELETE_MESSAGE = 'Remove user Sergey Ivanov?'
    FINAL_DELETE_MESSAGE = 'User deleted'
    WRONG_LOGIN_PASSWORD = 'Incorrect Login or Password'
    ADDED_USER = 'User created'
    SAVE_CHANGES = 'Changes saved'
    ADMIN_PARAM = ['login12', 'Case administrator', 'Sergey', 'Ivanov']
    NEW_ADMIN_PARAM = ['login12', 'Case administrator', 'Andrew', 'Petrov']
    FIRST_NAME = 'Sergey'
    LAST_NAME = 'Ivanov'
    NEW_FIRST_NAME = 'Andrew'
    NEW_LAST_NAME = 'Petrov'
    EXPERT_PARAM = ['login12_ex', 'Reviewer', 'Sergey', 'Ivanov']
    LOAD_PARAM = ['login12_load', 'Uploader', 'Sergey', 'Ivanov']
    REG_NOTIFI_1 = ('Error:\nPlease fill the Login field\nPlease fill the field First Name\nPlease fill the field '
                    'Last Name\nPlease fill the Password field\nPlease fill the Confirm Password field\nThe password '
                    'must not contain 3 or more identical characters in a row; The password must contain at least one '
                    'capital letter; The password must contain at least one digit; Minimum password length is 7 '
                    'characters; Password must not contain the login; Your password must contain only Latin '
                    'characters.')
    REG_NOTIFI_2 = 'Error:\nPlease fill the Login field'
    REG_NOTIFI_3 = 'Error:\nPlease fill the field First Name\nPlease fill the field Last Name'
    REG_NOTIFI_4 = ('Error:\nPlease fill the Password field\nPlease fill the Confirm Password field\nThe password '
                    'must not contain 3 or more identical characters in a row; The password must contain at least one '
                    'capital letter; The password must contain at least one digit; Minimum password length is 7 '
                    'characters; Password must not contain the login; Your password must contain only Latin '
                    'characters.')
    REG_NOTIFI_5 = ('Error:\nPlease fill the Password field\nPasswords do not match\nThe password must not contain 3 '
                    'or more identical characters in a row; The password must contain at least one capital letter; '
                    'The password must contain at least one digit; Minimum password length is 7 characters; Password '
                    'must not contain the login; Your password must contain only Latin characters.')
    REG_NOTIFI_6 = 'Error:\nPlease fill the Confirm Password field\nPasswords do not match'
    REG_NOTIFI_7 = ('Error:\nThe password must not contain 3 or more identical characters in a row; The password must '
                    'contain at least one capital letter; The password must contain at least one digit; Minimum '
                    'password length is 7 characters; Password must not contain the login; Your password must contain '
                    'only Latin characters.')
    REG_NOTIFI_8 = 'Error:\nPasswords do not match'
    DEPARTMENT_NAME = 'new_test_department'
    DEPARTMENT_CASE = 'Auto_test_case'
    MAX_USERS = 'License warning: maximum allowed number of users exceeds the number specified in your license'
    MAX_CONNECTIONS = 'The maximum number of connections allowed by your license has been reached.'
    NO_CASES = 'No results found'
    NO_DEPARTMENTS = 'Departments not stated'


class DepartmentsVerif:
    ADDED_DEPARTMENT = 'Department created'
    SAVE_CHANGES = 'Changes saved'
    DEPARTMENT_PARAM = ['new_test_department', 'Note for test department']
    DEPARTMENT_PARAM_2 = ['new_test_department2', 'Note for department']
    USERS_COUNTER = 2
    CASES_COUNTER = 2
    DEPARTMENT_NAME_1 = 'new_test_department'
    DEPARTMENT_NAME_2 = 'new_test_department1'
    DEPARTMENT_NAME_3 = 'new_test_department2'
    NOUSERS = 'Users not found'
    NOCASES = 'No results found'
    CASE_COUNTER = 1
    CASE_COUNTER_5 = 5
    CASE_NAME_1 = 'OFBR'
    CASE_NAME_2 = 'Itunes'
    USER_NAME_1 = 'Sergey Ivanov'
    CASE_NAME = 'Auto_test_case'
    DEPARTMENT_PART_NAME = 'new_part_department'
    DELETED_DEPARTMENT = 'Department deleted'
    DEPARTMENT_NOTE_2 = 'Note for department'


class LicenseVerif:
    LICENSE_ERROR = 'License Error'
    LICENSE_EXPIRATION = 'The license has expired'
    LICENSE_LIMIT_TOOLS = 'The allowed number of tools has been exceeded. The maximum number is 20'
    LICENSE_LIMIT_HASHES = 'The maximum number of hash sets available for your license has been reached'
    LICENSE_LIMIT_TAGS = 'The maximum number of user tags available for your license has been reached'
    LICENSE_LIMIT_KEYWORDS_SETS = 'The maximum number of keyword sets available for your license has been reached'
    LICENSE_LIMIT_KEYWORDS_WACHLISTS = 'The maximum number of watchlists available for your license has been reached'
