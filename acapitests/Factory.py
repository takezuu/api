class FCrimeTypes:

    def __init__(self):
        self.result = {'name': 'Digital',
                       'id': 0}

    def set_name(self, name):
        self.result['name'] = name
        return self

    def set_id(self, crime_type_id):
        self.result['id'] = crime_type_id
        return self

    def build(self):
        return self.result


class FTags:

    def __init__(self):
        self.result = {'name': 'Test tag',
                       'id': 0}

    def set_name(self, name):
        self.result['name'] = name
        return self

    def set_id(self, tag_id):
        self.result['id'] = tag_id
        return self

    def build(self):
        return self.result


class FRegions:

    def __init__(self):
        self.result = {'name': 'Moscow',
                       'id': 0}

    def set_name(self, name):
        self.result['name'] = name
        return self

    def set_id(self, region_id):
        self.result['id'] = region_id
        return self

    def build(self):
        return self.result


class FDepartments:

    def __init__(self):
        self.result = {
            "name": "New test name",
            "note": "Note for test",
            "id": 0,
            "casesId": [],
            "usersId": [],
            "imagesId": []
        }

    def set_name(self, name):
        self.result['name'] = name
        return self

    def set_id(self, department_id):
        self.result['id'] = department_id
        return self

    def set_note(self, note):
        self.result['note'] = note

    def build(self):
        return self.result


class FUsers:

    def __init__(self):
        self.result = {
            "login": "login12",
            "status": 1,
            "firstName": "Sergey",
            "middleName": "",
            "lastName": "Ivanov",
            "position": "",
            "phoneNo": "",
            "email": "",
            "disabled": False,
            "id": 0,
            "casesId": [],
            "departmentsId": [],
            "imagesId": [],
            "rightsId": [],
            "canReadReports": True
        }

    def set_login(self, login):
        self.result['login'] = login
        return self

    def set_status(self, status):
        self.result['status'] = status
        return self

    def set_fname(self, fname):
        self.result['firstName'] = fname
        return self

    def set_lname(self, lname):
        self.result['lastName'] = lname
        return self

    def set_position(self, position):
        self.result['position'] = position
        return self

    def set_password(self, password):
        self.result['password'] = password
        return self

    def set_password_copy(self, password_copy):
        self.result['password_copy'] = password_copy
        return self

    def set_both_password(self, password):
        self.result['password'] = password
        self.result['password_copy'] = password
        return self

    def set_id(self, user_id):
        self.result['id'] = user_id
        return self

    def build(self):
        return self.result


class FWatchlists:

    def __init__(self):
        self.result = {
            "name": "Test watch list",
            "dClass": 1,
            "note": "",
            "field": "phoneNumber",
            "words": []
        }

    def set_name(self, name):
        self.result['name'] = name
        return self

    def set_dclass(self, dclass):
        self.result['dclass'] = dclass
        return self

    def set_note(self, note):
        self.result['note'] = note
        return self

    def set_field(self, field):
        self.result['field'] = field
        return self

    def set_words(self, words):
        self.result['words'] = words
        return self

    def set_id(self, watchlist_id):
        self.result['id'] = watchlist_id
        return self

    def build(self):
        return self.result


class FHashes:

    def __init__(self):
        self.result = {
            "name": "test hash",
            "type": "MD5",
            "note": "",
            "hideThumbnail": False,
            "addHashAfterCreated": False
        }

    def set_name(self, name):
        self.result['name'] = name
        return self

    def set_note(self, note):
        self.result['note'] = note
        return self

    def set_type(self, hash_type):
        self.result['type'] = hash_type
        return self

    def set_id(self, hash_id):
        self.result['id'] = hash_id
        return self

    def build(self):
        return self.result


class FKeywordsSets:

    def __init__(self):
        self.result = {
            "name": "1",
            "type": 1,
            "dClass": 1,
            "authorName": "dbadmin",
            "note": "",
            "words": []
        }

    def set_name(self, name):
        self.result['name'] = name
        return self

    def set_type(self, hash_type):
        self.result['type'] = hash_type
        return self

    def set_id(self, hash_id):
        self.result['id'] = hash_id
        return self

    def set_note(self, note):
        self.result['note'] = note
        return self

    def set_dclass(self, dclass):
        self.result['dClass'] = dclass
        return self

    def set_words(self, words):
        self.result['words'] = words
        return self

    def set_words_update(self, keyword_set_id, words):
        self.result["dictid"] = keyword_set_id
        self.result["words"] = words
        del self.result["name"]
        del self.result["type"]
        del self.result["dClass"]
        del self.result["authorName"]
        del self.result["note"]
        return self

    def build(self):
        return self.result
