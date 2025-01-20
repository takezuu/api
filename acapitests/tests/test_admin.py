import allure
import pytest

from Funcs import TestCase
from Pages_verification.Verification import StatusCode
from data import Code
from Pages_data.API_login_data import LoginData
from tests.decorators import DEntities, DLicense
from Pages_verification.Verification_admin import VerifAdmin
from Factory import FUsers


class TestAdmin:

    @allure.feature('Admin page')
    @allure.title('Prepare system')
    @DLicense.put_new_license(folder_name='base')
    @DEntities.create_test()
    @DEntities.delete_all_entities()
    def test_admin_clean(self, test: TestCase):
        pass

    @allure.feature('Admin page')
    @allure.title('Create users with different statuses')
    @pytest.mark.parametrize('param', [LoginData.data_admin, LoginData.data_expert, LoginData.data_load])
    @DEntities.create_test_param()
    @DEntities.delete_entity_param(entity_type=Code.USER)
    def test_admin_001(self, test: TestCase):
        param = test.param
        result = test.create_entity(entity_type=Code.USER, custom_json=param)
        test.check_status_code(result=result, entity_type=Code.USER, verif=StatusCode.STATUS_200)
        test.check_id_and_type(result=result)

    @allure.feature('Admin page')
    @allure.title('Create users with wrong data')
    @pytest.mark.parametrize('param', [LoginData.data_empty, LoginData.data_no_login, LoginData.data_no_fname_lname,
                                       LoginData.data_no_fname, LoginData.data_no_lname, LoginData.data_no_password])
    @DEntities.create_test_param()
    @DEntities.delete_entity_param(entity_type=Code.USER)
    def test_admin_002(self, test: TestCase):
        param = test.param
        result = test.create_entity(entity_type=Code.USER, custom_json=param)
        test.check_status_code(result=result, entity_type=Code.USER, verif=StatusCode.STATUS_400)
        if param == LoginData.data_no_password:
            test.check_field(result=result, verif=VerifAdmin.password_short, field_name=Code.MESSAGE,
                             err_msg=Code.Err.MSG_WRONG)
        else:
            test.check_field(result=result, verif=VerifAdmin.general_invalid_fields, field_name=Code.MESSAGE,
                             err_msg=Code.Err.MSG_WRONG)

    @allure.feature('Admin page')
    @allure.title('Edit fname lname')
    @DEntities.create_test()
    @DEntities.add_delete_entity(entity_type=Code.USER)
    def test_admin_003(self, test: TestCase, user_id: int):
        json_data = FUsers().set_id(user_id).set_fname('Nikita').set_lname('Petrov').build()
        result = test.edit_entity(entity_type=Code.USER, entity_id=user_id, json_data=json_data)
        test.check_status_code(result=result, entity_type=Code.USER, verif=StatusCode.STATUS_200)
        test.check_entity_id(result=result, verif=user_id)

    @allure.feature('Admin page')
    @allure.title('Edit password')
    @DEntities.create_test()
    @DEntities.add_delete_entity(entity_type=Code.USER)
    def test_admin_004(self, test: TestCase, user_id: int):
        json_data = FUsers().set_id(user_id).set_password('Newpassword1').set_password_copy('Newpassword1').build()
        result = test.edit_entity(entity_type=Code.USER, entity_id=user_id, json_data=json_data)
        test.check_status_code(result=result, entity_type=Code.USER, verif=StatusCode.STATUS_200)
        test.check_entity_id(result=result, verif=user_id)

    @allure.feature('Admin page')
    @allure.title('Edit fname lname negative case')
    @DEntities.create_test()
    @DEntities.add_delete_entity(entity_type=Code.USER)
    def test_admin_005(self, test: TestCase, user_id: int):
        json_data = FUsers().set_id(user_id).set_fname('').set_lname('').build()
        result = test.edit_entity(entity_type=Code.USER, entity_id=user_id, json_data=json_data)
        test.check_status_code(result=result, entity_type=Code.USER, verif=StatusCode.STATUS_400)
        test.check_field(result=result, verif=VerifAdmin.general_invalid_fields, field_name=Code.MESSAGE,
                         err_msg=Code.Err.MSG_WRONG)

    @allure.feature('Admin page')
    @allure.title('Change user\'s status')
    @pytest.mark.parametrize('param', [('login12', 1, 2), ('login12', 1, 4),
                                       ('login12_ex', 2, 1), ('login12_ex', 2, 4),
                                       ('login12_load', 4, 1), ('login12_load', 4, 2)])
    @DEntities.create_test_param()
    @DEntities.delete_entity(entity_type=Code.USER, entity_fname='Sergey')
    def test_admin_006(self, test: TestCase):
        param = test.param
        custom_json = FUsers().set_login(param[0]).set_status(param[1]).set_both_password('Vibnb47').build()
        user_id = test.create_entity(entity_type=Code.USER, custom_json=custom_json).json()['id']

        json_data = FUsers().set_status(param[2]).set_id(user_id).build()
        result = test.edit_entity(entity_type=Code.USER, entity_id=user_id, json_data=json_data)
        test.check_status_code(result=result, entity_type=Code.USER, verif=StatusCode.STATUS_200)
        result = test.request_all_entities(entity_type=Code.USER)
        test.check_entity_status(result=result, verif=param[2], entity_type=Code.USER)

    @allure.feature('Admin page')
    @allure.title('Delete user')
    @pytest.mark.parametrize('param', [LoginData.data_admin, LoginData.data_expert, LoginData.data_load])
    @DEntities.create_test_param()
    @DEntities.add_delete_entity(entity_type=Code.USER)
    def test_admin_007(self, test: TestCase, user_id: int):
        result = test.delete_entity(entity_id=user_id, entity_type=Code.USER)
        test.check_status_code(result=result, entity_type=Code.USER, verif=StatusCode.STATUS_200)
        result = test.request_all_entities(entity_type=Code.USER)
        test.check_entities_deleted(result=result, entity_type=Code.USER)
