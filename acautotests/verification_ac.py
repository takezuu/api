class CasesVerif:
    ADMIN_STATUS = 'Администратор'
    SUPER_STATUS = 'Суперпользователь'
    EXPERT_STATUS = 'Эксперт'
    LOAD_STATUS = 'Загрузчик'
    NAME_OF_TAB = 'Дела'
    SAVE_CHANGES = 'Изменения сохранены'
    CASES_LIST_UPDATED = 'Список дел обновлен'
    CASE = 'Auto_test_case'


class DevicesVerif:
    DEVICE_DELETED = 'Устройство удалено'
    NAME_OF_TAB = 'Устройства'


class LoadImagesVerif:
    IMAGE_UPLOAD = 'Загрузка файла:'
    IMAGE_PROCESS = 'Загружено пакетов'
    IMAGE_SUCCESS_UPLOAD = 'Файл загружен'
    NO_RESULTS = 'Нет результатов.'
    GRID_NOTIFI = 'Datasource load failed!'
    RED_EMPTY_NOTIFI = 'Файл пуст'
    RED_INVALID_NOTIFI = 'Неверный формат файла'
    OFBX_DEVICE = 'Apple iPhone 6 Chats'
    OFBR_DEVICE = 'Android zip (Telegram_Android_7.1.3(channel_msgs_inc).zip)'
    ODB_DEVICE = 'Desktop extraction (zl_ermis-f_000.rar)'
    UFED_DEVICE = 'Apple UFED backup (iPad 3 WiFi (A1416))'
    XRY_DEVICE = 'Android XRY file system (test.xry)'
    OST_DEVICE = 'Microsoft Outlook Data File (test.ost)'
    PST_DEVICE = 'Microsoft Outlook Data File (test.pst)'
    MAX_DEVICES = 'Достигнуто максимальное количество устройств, установленное вашей лицензией'
    NAME_OF_TAB = 'Загрузка образов'


class RegionsVerif:
    ADDED_REGION = 'Регион создан'
    ZERO_COUNT = 0
    NOCASES = 'Нет данных.'
    NAME_OF_TAB = 'Регионы'
    HAVE_CASE = 1
    SAVE_CHANGES = 'Изменения сохранены'
    FINAL_DELETE_MESSAGE = 'Регион удален'
    REG1 = 'Ярославская обл.'
    REG2 = 'Приморский край'


class CrimeTypesVerif:
    NAME_OF_TAB = 'Категории преступлений'
    ADDED_CRIME_TYPE = 'Категория преступлений создана'
    ZERO_COUNT = 0
    NOCASES = 'Нет данных.'
    HAVE_CASE = 1
    SAVE_CHANGES = 'Изменения сохранены'
    FINAL_DELETE_MESSAGE = 'Категория преступлений удалена'
    CRIME1 = 'Воровство'
    CRIME2 = 'Ограбление'


class TagsVerif:
    ADDED_TAG = 'Тег создан'
    ZERO_COUNT = 0
    NOCASES = 'Нет данных.'
    NAME_OF_TAB = 'Теги'
    HAVE_CASE = 1
    SAVE_CHANGES = 'Изменения сохранены'
    FINAL_DELETE_MESSAGE = 'Тег удален'
    CARDS = 'Карты'
    TAG1 = 'Новый тестовый тег'
    TAG2 = 'New test tag'


class HashesVerif:
    ADDED_HASH = 'Хеш-сет создан'
    HASHES_UPDATED = 'Список хеш-сетов обновлен'
    HASH_UPDATED = 'Хеш-сет обновлен'
    ZERO_COUNT = 0
    RECORDS = 13
    NAME_OF_TAB = 'Хеш-сеты'
    SAVE_CHANGES = 'Изменения сохранены'
    FINAL_DELETE_MESSAGE = 'Хеш-сет удален'
    HASH_READY = 'Хеш-сет готов'
    HASH_MD5 = 'test_md5'
    HASH_SHA1 = 'test_sha-1'
    HASH_SHA256 = 'test_sha-256'
    HASH_MD5_2 = 'test_md5_2'
    HASH_SHA1_2 = 'test_sha-1_2'
    HASH_SHA256_2 = 'test_sha-256_2'
    BADGE_EMPTY = 'Пустой'
    TYPE_MD5 = 'MD5'
    TYPE_SHA1 = 'SHA-1'
    TYPE_SHA256 = 'SHA-256'
    IMAGE_UPLOAD = 'Загрузка файла:'
    IMAGE_PROCESS = 'Загружено пакетов'
    IMAGE_SUCCESS_UPLOAD = 'Файл загружен'
    NOTE = 'Новый хеш для теста'
    NO_RESULTS = 'Нет результатов.'


class KeywordsSetsVerif:
    ADDED_KEYWORD_SET = 'Словарь создан'
    KEYWORDS_SETS_UPDATED = 'Список словарей обновлен'
    KEYWORD_SET_UPDATED = 'Словарь обновлен'
    NAME_OF_TAB = 'Словари'
    SAVE_CHANGES = 'Изменения сохранены'
    FINAL_DELETE_MESSAGE = 'Словарь удален'
    HASH_READY = 'Словарь готов'
    BADGE_EMPTY = 'Пустой'
    BADGE_EXPECT = 'Ожидает индексации'
    BADGE_READY = 'Готов'
    IMAGE_UPLOAD = 'Загрузка файла:'
    IMAGE_PROCESS = 'Загружено пакетов'
    IMAGE_SUCCESS_UPLOAD = 'Файл загружен'
    NOTE = 'Новый тестовый словарь'
    NO_RESULTS = 'Нет результатов.'
    NO_DATA = 'Нет данных.'
    EMPTY = 'Пустой словарь'
    TYPE_ALL_PAGES = 2
    TYPE_FILES = 1
    TYPE_WRKSPACE_CONTACTS_MAP = 0
    STR_TYPE_ALL_PAGES = 'Все страницы'
    STR_TYPE_FILES = 'Файлы'
    STR_TYPE_WRKSPACE_CONTACTS_MAP = 'Рабочее пространство, Карта и Контакты'
    ZERO_COUNT = 0
    COUNT_2 = 2
    WEAPON = 'Оружие'
    PISTOLET = 'Пистолет'
    TEST = 'Тестовый словарь'
    TEST_2 = 'Словарь для тестирования'
    TYPE_1251 = 0
    TYPE_UTF8 = 1
    TYPE_UTF16 = 2


class WorkspaceVerif:
    NAME_OF_TAB = 'Рабочее пространство'


class ContactsVerif:
    NAME_OF_TAB = 'Контакты'


class MapVerif:
    NAME_OF_TAB = 'Карта'


class FilesVerif:
    NAME_OF_TAB = 'Файлы'


class LoginVerif:
    LOGIN_PAGE_NOTIFICATION = 'Неверное имя пользователя или пароль'
    DEACTIVATE_ACCOUNT_NOTIFICATION = 'Работа учетной записи была приостановлена. ' \
                                      'Пожалуйста, обратитесь к администратору.'
    NAME_OF_TAB = 'Авторизация'
    EYE = 'Показать пароль'
    HIDE_EYE = 'Скрыть пароль'
    PASSWORD = 'password'
    PASSWORD_HIDE = 'text'
    LICENSE_NUM = '3343'
    LICENSE_DATE1 = '10.10.2024'
    LICENSE_DATE2 = '10.10.2023'
    IVALID_HID = 'В лицензионном файле указан неверный Hardware ID сервера'


class AdminVerif:
    NAME_OF_TAB = 'Пользователи'
    DELETE_MESSAGE = 'Удалить пользователя Сергей Иванов?'
    FINAL_DELETE_MESSAGE = 'Пользователь удален'
    WRONG_LOGIN_PASSWORD = 'Неверное имя пользователя или пароль'
    ADDED_USER = 'Пользователь создан'
    SAVE_CHANGES = 'Изменения сохранены'
    ADMIN_PARAM = ['login12', 'Администратор', 'Сергей', 'Иванов']
    NEW_ADMIN_PARAM = ['login12', 'Администратор', 'Андрей', 'Петров']
    FIRST_NAME = 'Сергей'
    LAST_NAME = 'Иванов'
    NEW_FIRST_NAME = 'Андрей'
    NEW_LAST_NAME = 'Петров'
    EXPERT_PARAM = ['login12_ex', 'Эксперт', 'Сергей', 'Иванов']
    LOAD_PARAM = ['login12_load', 'Загрузчик', 'Сергей', 'Иванов']
    REG_NOTIFI_1 = 'Ошибка:\nПоле Логин обязательно для заполнения\nПожалуйста, заполните поле Имя\nПожалуйста, ' \
                   'заполните поле Фамилия\nПоле Пароль обязательно для заполнения\nПоле Подтверждение пароля ' \
                   'обязательно для заполнения\nПароль не должен содержать 3 и более одинаковых символов подряд; ' \
                   'Пароль должен содержать хотя бы одну заглавную букву; ' \
                   'Пароль должен содержать хотя бы одну цифру; ' \
                   'Минимальная длина пароля 7 символов; Пароль не должен содержать в себе логин; Пароль должен ' \
                   'содержать только латинские буквы.'
    REG_NOTIFI_2 = 'Ошибка:\nПоле Логин обязательно для заполнения'
    REG_NOTIFI_3 = 'Ошибка:\nПожалуйста, заполните поле Имя\nПожалуйста, заполните поле Фамилия'
    REG_NOTIFI_4 = 'Ошибка:\nПоле Пароль обязательно для заполнения\nПоле Подтверждение пароля обязательно для ' \
                   'заполнения\nПароль не должен содержать 3 и более одинаковых символов подряд; Пароль должен ' \
                   'содержать хотя бы одну заглавную букву; Пароль должен содержать хотя бы одну цифру; Минимальная ' \
                   'длина пароля 7 символов; Пароль не должен содержать в себе логин; Пароль должен содержать только ' \
                   'латинские буквы.'
    REG_NOTIFI_5 = 'Ошибка:\nПоле Пароль обязательно для заполнения\nПароли не совпадают\nПароль не должен содержать ' \
                   '3 и более одинаковых символов подряд; Пароль должен содержать хотя бы одну заглавную букву; ' \
                   'Пароль должен содержать хотя бы одну цифру; Минимальная длина пароля 7 символов; ' \
                   'Пароль не должен ' \
                   'содержать в себе логин; Пароль должен содержать только латинские буквы.'
    REG_NOTIFI_6 = 'Ошибка:\nПоле Подтверждение пароля обязательно для заполнения\nПароли не совпадают'
    REG_NOTIFI_7 = 'Ошибка:\nПароль не должен содержать 3 и более одинаковых символов подряд; ' \
                   'Пароль должен содержать ' \
                   'хотя бы одну заглавную букву; Пароль должен содержать хотя бы одну цифру; Минимальная длина ' \
                   'пароля 7 символов; Пароль не должен содержать в себе логин; Пароль должен содержать ' \
                   'только латинские буквы.'
    REG_NOTIFI_8 = 'Ошибка:\nПароли не совпадают'
    DEPARTMENT_NAME = 'new_test_department'
    DEPARTMENT_CASE = 'Auto_test_case'
    MAX_USERS = 'Превышено число пользователей допустимое лицензией'
    MAX_CONNECTIONS = 'Достигнуто максимальное число подключений разрешенных в лицензии'
    NO_CASES = 'Дела не найдены'
    NO_DEPARTMENTS = 'Отделы не назначены'


class DepartmentsVerif:
    ADDED_DEPARTMENT = 'Отдел создан'
    SAVE_CHANGES = 'Изменения сохранены'
    DEPARTMENT_PARAM = ['new_test_department', 'Заметка для тестового отдела']
    DEPARTMENT_PARAM_2 = ['new_test_department2', 'Заметка для отдела']
    USERS_COUNTER = 2
    CASES_COUNTER = 2
    DEPARTMENT_NAME_1 = 'new_test_department'
    DEPARTMENT_NAME_2 = 'new_test_department1'
    DEPARTMENT_NAME_3 = 'new_test_department2'
    NOUSERS = 'Пользователи не найдены'
    NOCASES = 'Дела не найдены'
    CASE_COUNTER = 1
    CASE_COUNTER_4 = 4
    USER_NAME_1 = 'Сергей Иванов'
    CASE_NAME = 'Auto_test_case'
    DEPARTMENT_PART_NAME = 'new_part_department'
    DELETED_DEPARTMENT = 'Отдел удален'


class LicenseVerif:
    LICENSE_ERROR = 'Ошибка лицензии'
    LICENSE_EXPIRATION = 'Срок действия лицензии истек'
    LICENSE_LIMIT_TOOLS = 'Превышено допустимое число инструментов. Максимальное число 20 штук'
