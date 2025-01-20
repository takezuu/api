class LoginData:
    SUPER_LOGIN = 'dbadmin'
    SUPER_PASSWORD = '1Qwerty'
    ADMIN_LOGIN = 'login12'
    EXPERT_LOGIN = 'login12_ex'
    EXPERT_LOGIN_2 = 'login12_ex_2'
    EXPERT_LOGIN_3 = 'login12_ex_3'
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

    data_log_super = {'login': SUPER_LOGIN, 'password': SUPER_PASSWORD}
    data_log_admin = {'login': ADMIN_LOGIN, 'password': PASSWORD}
    data_log_admin_invalid_password = {'login': ADMIN_LOGIN, 'password': '1234'}
    data_log_admin_invalid = {'login': 'invalid', 'password': '1234'}
    data_log_admin_invalid_login = {'login': 'invalid', 'password': PASSWORD}
    data_log_expert = {'login': EXPERT_LOGIN, 'password': PASSWORD}
    data_log_load = {'login': LOAD_LOGIN, 'password': PASSWORD}

    all_users = {
        "page": 1,
        "limit": 25,
        "order": {
            "by": "login",
            "type": "asc"
        }
    }
    data_empty = {"login": "",
                  "status": 1,
                  "firstName": "",
                  "middleName": "",
                  "lastName": "",
                  "position": "",
                  "phoneNo": "",
                  "email": "",
                  "disabled": False,
                  "password": "",
                  "passwordCopy": "",
                  "id": 0,
                  "casesId": [],
                  "departmentsId": [],
                  "imagesId": [],
                  "rightsId": [],
                  "canReadReports": True
                  }

    data_no_login = {
        "login": "",
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
        "imagesId": [],
        "rightsId": [],
        "canReadReports": True
    }

    data_no_lname = {
        "login": "login12",
        "status": 1,
        "firstName": "Sergey",
        "middleName": "",
        "lastName": "",
        "position": "",
        "phoneNo": "",
        "email": "",
        "disabled": False,
        "password": "Vibnb47",
        "passwordCopy": "Vibnb47",
        "id": 0,
        "casesId": [],
        "departmentsId": [],
        "imagesId": [],
        "rightsId": [],
        "canReadReports": True
    }

    data_no_fname = {
        "login": "login12",
        "status": 1,
        "firstName": "",
        "middleName": "",
        "lastName": "Petrov",
        "position": "",
        "phoneNo": "",
        "email": "",
        "disabled": False,
        "password": "Vibnb47",
        "passwordCopy": "Vibnb47",
        "id": 0,
        "casesId": [],
        "departmentsId": [],
        "imagesId": [],
        "rightsId": [],
        "canReadReports": True
    }

    data_no_fname_lname = {
        "login": "login12",
        "status": 1,
        "firstName": "",
        "middleName": "",
        "lastName": "",
        "position": "",
        "phoneNo": "",
        "email": "",
        "disabled": False,
        "password": "Vibnb47",
        "passwordCopy": "Vibnb47",
        "id": 0,
        "casesId": [],
        "departmentsId": [],
        "imagesId": [],
        "rightsId": [],
        "canReadReports": True
    }

    data_no_password = {
        "login": "login12",
        "status": 1,
        "firstName": "Sergey",
        "middleName": "",
        "lastName": "Ivanov",
        "position": "",
        "phoneNo": "",
        "email": "",
        "disabled": False,
        "password": "",
        "passwordCopy": "",
        "id": 0,
        "casesId": [],
        "departmentsId": [],
        "imagesId": [],
        "rightsId": [],
        "canReadReports": True
    }

    data_wrong_pw = {
        "login": "login12",
        "status": 1,
        "firstName": "Sergey",
        "middleName": "",
        "lastName": "Ivanov",
        "position": "",
        "phoneNo": "",
        "email": "",
        "disabled": False,
        "password": "ПАРОЛЬ32",
        "passwordCopy": "ПАРОЛЬ32",
        "id": 0,
        "casesId": [],
        "departmentsId": [],
        "imagesId": [],
        "rightsId": [],
        "canReadReports": True
    }

    data_different_pw = {
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
        "passwordCopy": "Vibnb57",
        "id": 0,
        "casesId": [],
        "departmentsId": [],
        "imagesId": [],
        "rightsId": [],
        "canReadReports": True
    }

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
        "imagesId": [],
        "rightsId": [],
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
        "imagesId": [],
        "rightsId": [],
        "canReadReports": True
    }

    data_expert_new = {
        "login": "login12_ex_new",
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
        "imagesId": [],
        "rightsId": [],
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
        "imagesId": [],
        "rightsId": [],
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
        "imagesId": [],
        "rightsId": [],
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
        "imagesId": [],
        "rightsId": [],
        "canReadReports": True
    }
