class KeywordsSetsData:
    NOTE = 'New test keyword set'
    EMPTY = 'Empty keyword set'
    TEST = 'Test keyword'
    TEST_2 = 'Test keyword for test'
    TYPE_ALL_PAGES = 0
    TYPE_FILES = 2
    TYPE_WRKSPACE_CONTACTS = 1
    WEAPON = 'Weapon'
    PISTOLET = 'Guns'
    TYPE_1251 = 0
    TYPE_UTF8 = 1
    TYPE_UTF16 = 2
    API_ALL_PAGES = 0
    API_FILES = 2
    API_WRKSPACE_CONTACTS_MAP = 1

    all_keywords_sets = {
        "page": 1,
        "limit": 25,
        "order": {
            "by": "created",
            "type": "desc"
        }
    }

    content = {
        "id": 0,
        "search": ""
    }

    data_keyword_set = {
        "name": "Test keywords set",
        "type": 1,
        "dClass": 1,
        "authorName": "dbadmin",
        "note": "",
        "words": []
    }

    asc_sort = {
        "page": 1,
        "limit": 25,
        "order": {
            "by": "name",
            "type": "asc"
        }
    }
