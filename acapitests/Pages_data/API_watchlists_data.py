class WatchlistsData:
    data_watchlist = {
        "name": "Test watch list",
        "dClass": 1,
        "note": "",
        "field": "phoneNumber",
        "words": []
    }

    create_watchlist = {
        "name": "",
        "dClass": 1,
        "note": "",
        "field": "phoneNumber",
        "words": []
    }

    all_watchlists = {
        "page": 1,
        "limit": 25,
        "order": {
            "by": "created",
            "type": "desc"
        }
    }

    content_watchlist = {
        "id": 0,
        "limit": 25,
        "page": 1,
        "search": ""
    }

    phone_number = "phoneNumber"
    display_name = "displayName"
    description = "description"
    email_address = "emailAddress"
    chat_id = "chatId"
    account_name = "accountName"

    type1 = 1
    type2 = 2

    words_list = ['weapon', 'evidence', 'drugs']
    new_words = ['laptop', 'airplane', 'hardware']
