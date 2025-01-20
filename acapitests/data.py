ENV_HOST = 'http://127.0.0.1/'
STAND_PATH = 'C:\\Test_data\\'
STAND_PATH_EMPTY = 'C:\\Test_data\\empty\\'
STAND_PATH_INVALID = 'C:\\Test_data\\invalid\\'
STAND_PATH_HASHES = 'C:\\Test_data\\hashes\\'
STAND_PATH_KEYWORDS_SETS = 'C:\\Test_data\\keywords_sets\\'
STAND_PATH_DOWNLOADS = 'C:\\Users\\User\\Downloads\\'
STAND_PATH_LICENSE = 'C:\\Test_data\\license\\'
STAND_BACKEND = 'C:\\backend\\'
STAND_LOGS_FOLDERS = 'C:\\Users\\User\\Develop\\acapitests\\tests\\logs\\'

tags = ['tag1', 'tag2', 'tag3', 'tag4', 'tag5', 'tag6', 'tag7', 'tag8', 'tag9', 'tag10',
        'tag11', 'tag12', 'tag13', 'tag14', 'tag15', 'tag16', 'tag17', 'tag18', 'tag19', 'tag20']
keywords_sets = ['keyword_set1', 'keyword_set2', 'keyword_set3', 'keyword_set4',
                 'keyword_set5', 'keyword_set6', 'keyword_set7', 'keyword_set8', 'keyword_set9',
                 'keyword_set10', 'keyword_set11', 'keyword_set12', 'keyword_set13', 'keyword_set14',
                 'keyword_set15', 'keyword_set16', 'keyword_set17', 'keyword_set18', 'keyword_set19',
                 'keyword_set20']
keywords_sets_different_names = ['crime_set', 'work', 'weapons', 'private', 'Important_set', 'gambling_set', 'graphic',
                                 'chats']
hashes = ['hashset1', 'hashset2', 'hashset3', 'hashset4', 'hashset5', 'hashset6',
          'hashset7', 'hashset8', 'hashset9', 'hashset10', 'hashset11', 'hashset12', 'hashset13',
          'hashset14', 'hashset15', 'hashset16', 'hashset17', 'hashset18', 'hashset19', 'hashset20']
watchlists = ['watchlist1', 'watchlist2', 'watchlist3', 'watchlist4', 'watchlist5', 'watchlist6',
              'watchlist7', 'watchlist8', 'watchlist9', 'watchlist10', 'watchlist11', 'watchlist12',
              'watchlist13', 'watchlist14', 'watchlist15', 'watchlist16', 'watchlist17', 'watchlist18',
              'watchlist19', 'watchlist20']


class DataBase:
    DATABASE = 'ocsViewDB'
    USER = 'postgres'
    PASSWORD = 'pgpassword'
    HOST = '127.0.0.1'
    PORT = '5432'


class Code:
    API_CAN_UPLOAD = 'api/devices/upload/can'
    API_LICENSE = 'api/license'
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
    API_KEYWORDS_SETS_WORDS = 'api/dictionaryContentUpdate'
    API_KEYWORDS_SETS_CONTENT = 'api/dictionaryContent'
    API_DEVICES = 'api/devices'
    API_DEVICES_UPLOAD = 'api/devices/upload'
    API_DEVICES_UPLOAD_ASYNC = 'api/device/upload-async'
    API_QUEUE = 'api/devices/queue'
    API_ACTIVITIES = 'api/activities'
    API_MONITOR = 'api/monitor'
    API_WATCHLIST = 'api/watchlist'
    API_WATCHLIST_CONTENT = 'api/watchlistContent'
    API_WATCHLIST_UPDATE = 'api/watchlistContentUpdate'
    API_WATCHLIST_IMPORT = 'api/watchlist/import'
    API_WORKSPACE_GRID = 'api/workspace/grid'
    API_WATCHLIST_INDEX = 'api/watchlist_index'
    API_FILTERS_COMMON_TREE = 'api/filters/commonTree/'
    API_FILTERS_COMMON_TREE_CASES = 'api/filters/commonTree/1'
    API_FILTERS_COMMON_TREE_DEVICES = 'api/filters/commonTree/2'
    API_FILTERS_COMMON_TREE_CATEGORIES = 'api/filters/commonTree/3'
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
    MESSAGE = 'message'
    ITEM = 'Item'
    REASON = 'Reason'
    DONGLE = 'dongle'
    YES = 'yes'
    TOTAL = 'total'

    class Err:
        MSG_WRONG = 'message is wrong'
        ITEM_WRONG = 'item is wrong'
        ISNT_EQUAL = 'is not equal'
        REASON_1 = 'reason != 1'
