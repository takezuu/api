class HashesData:
    HASH_MD5 = 'test_md5'
    HASH_SHA1 = 'test_sha-1'
    HASH_SHA256 = 'test_sha-256'
    HASH_MD5_2 = 'test_md5_2'
    HASH_SHA1_2 = 'test_sha-1_2'
    HASH_SHA256_2 = 'test_sha-256_2'
    TYPE_MD5 = 'MD5'
    TYPE_SHA1 = 'SHA1'
    TYPE_SHA256 = 'SHA256'
    NOTE = 'New hash for test'

    all_hashes = {
        "page": 1,
        "limit": 25,
        "order": {
            "by": "created",
            "type": "desc"
        }
    }

    data_hash = {
        "name": "Test hash set",
        "type": "",
        "note": "",
        "hideThumbnail": False,
        "addHashAfterCreated": False
    }
