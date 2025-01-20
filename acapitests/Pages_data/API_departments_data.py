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

    all_departments = {
        "page": 1,
        "limit": 25

    }

    data_test_dep = {
        "name": "test_departments",
        "note": "new department test",
        "id": 0,
        "casesId": [],
        "usersId": []
    }
