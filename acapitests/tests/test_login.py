import allure
import pytest

from Funcs import TestCase
from Pages_verification.Verification import StatusCode
from data import Code
from Pages_data.API_login_data import LoginData
from tests.decorators import DEntities
from Factory import FUsers


class TestLogin:

    @allure.feature('Authorization page')
    @allure.title('Success login with case administrator/ correct login password')
    @DEntities.create_test()
    @DEntities.delete_all_entities()
    @DEntities.add_delete_entity(entity_type=Code.USER)
    def test_login_001(self, test: TestCase, user_id):
        result = test.login_user(json_data=LoginData.data_log_admin)
        test.check_status_code(result=result, entity_type=Code.USER, verif=StatusCode.STATUS_200)

    @allure.feature('Authorization page')
    @allure.title('Login with incorrect credentials')
    @pytest.mark.parametrize('param',
                             [LoginData.data_log_admin_invalid_password, LoginData.data_log_admin_invalid_login,
                              LoginData.data_log_admin_invalid])
    @DEntities.create_test_param()
    @DEntities.add_delete_entity(entity_type=Code.USER)
    def test_login_002(self, test: TestCase, user_id):
        param = test.param
        result = test.login_user(json_data=param)
        test.check_status_code(result=result, entity_type=Code.USER, verif=StatusCode.STATUS_401)

    @allure.feature('Authorization page')
    @allure.title('Login under dbadmin')
    @DEntities.create_test()
    def test_login_005(self, test: TestCase):
        test.check_already_login()

    @allure.feature('Authorization page')
    @allure.title('Login under expert')
    @DEntities.create_test()
    @DEntities.add_delete_entity(
        custom_data=FUsers().set_login('login12_ex').set_status(status=2).set_both_password('Vibnb47').build(),
        entity_type=Code.USER)
    def test_login_006(self, test: TestCase, user_id):
        result = test.login_user(json_data=LoginData.data_log_expert)
        test.check_status_code(result=result, entity_type=Code.USER, verif=StatusCode.STATUS_200)

    @allure.feature('Authorization page')
    @allure.title('Login under loader')
    @DEntities.create_test()
    @DEntities.add_delete_entity(
        custom_data=FUsers().set_login('login12_load').set_status(status=4).set_both_password('Vibnb47').build(),
        entity_type=Code.USER)
    def test_login_007(self, test: TestCase, user_id):
        result = test.login_user(json_data=LoginData.data_log_load)
        test.check_status_code(result=result, entity_type=Code.USER, verif=StatusCode.STATUS_200)

    @allure.feature('Authorization page')
    @allure.title('Delete users with different statuses')
    @pytest.mark.parametrize('param', [LoginData.data_log_admin, LoginData.data_log_expert, LoginData.data_log_load])
    @DEntities.create_test_param()
    @DEntities.add_delete_entity(entity_type=Code.USER)
    def test_login_008(self, test: TestCase, user_id: int):
        param = test.param
        result = test.delete_entity(entity_id=user_id, entity_type=Code.USER)
        test.check_status_code(result=result, entity_type=Code.USER, verif=StatusCode.STATUS_200)
        result = test.login_user(json_data=param)
        test.check_status_code(result=result, entity_type=Code.USER, verif=StatusCode.STATUS_401)
