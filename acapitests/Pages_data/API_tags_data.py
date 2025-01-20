class TagsData:
    TAG1 = 'New test tag'
    TAG2 = 'Second New test tag'
    TAG_CARDS = 'Maps'
    create_tag = {
        "name": "Test_tag",
        "id": 0
    }
    edit_tag = {
        "name": "My_new_tag",
        "id": 0
    }
    all_tags = {
        "page": 1,
        "limit": 25,
        "order": {
            "by": "name",
            "type": "desc"
        }
    }

    data_tag = {"name": "Test tag",
                "id": 0}

    asc_sort = {
        "page": 1,
        "limit": 25,
        "order": {
            "by": "name",
            "type": "asc"
        }
    }
