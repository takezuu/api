import allure
import pytest
import data
from Funcs import TestCase
from Pages_verification.Verification import StatusCode
from data import Code
from Pages_data.API_login_data import LoginData
from tests.decorators import DEntities, DLicense
from Pages_verification.Verification_license import VerifLicense
from Pages_data.API_license import LicenseData
from Pages_verification.Verification import Bool


class TestLicense:

    @allure.feature('License')
    @allure.title('Clean monitor, set license file, clean db')
    @DLicense.put_new_license(folder_name='1')
    @DEntities.create_test()
    @DEntities.delete_all_entities()
    def test_license_clean(self, test: TestCase):
        pass

    @allure.feature('License')
    @allure.title('Activate system/log in/check full version')
    @DEntities.create_test()
    def test_license_001(self, test: TestCase):
        result = test.login_user(json_data=LoginData.data_log_super)
        test.check_status_code(result=result, entity_type=Code.USER, verif=StatusCode.STATUS_200)
        test.check_sid(result=result)
        result = test.get_license()
        test.check_field_bool_value(result=result, verif=Bool.false, field_name=LicenseData.educational)
        test.logout_user(sid=result)

    @allure.feature('License')
    @allure.title('Create max users')
    @DLicense.put_new_license(folder_name='10')
    @DEntities.create_test()
    @DEntities.add_delete_entities(entity_type=Code.USER, users_data=[('login12', 'Nikita'), ('login12_exp', 'Dima')])
    def test_license_002(self, test: TestCase):
        result = test.create_entity(entity_type=Code.USER, custom_json=LoginData.data_expert_new)
        test.check_status_code(result=result, entity_type=Code.USER, verif=StatusCode.STATUS_400)
        test.check_field(result=result, verif=VerifLicense.number_users_exceed, field_name=Code.MESSAGE,
                         err_msg=Code.Err.MSG_WRONG)

    @allure.feature('License')
    @allure.title('Connection with max users')
    @DLicense.put_new_license(folder_name='13')
    @DEntities.create_test()
    @DEntities.add_delete_entities(entity_type=Code.USER, users_data=[('login12', 'Nikita'), ('login12_exp', 'Dima')])
    def test_license_003(self, test: TestCase):
        sid = test.login_user(json_data=LoginData.data_log_admin)
        result = test.login_user(json_data=LoginData.data_log_expert)
        test.check_status_code(result=result, entity_type=Code.USER, verif=StatusCode.STATUS_406)
        test.check_response(result=result, verif=VerifLicense.number_connection_exceed)
        test.logout_user(sid=sid)

    @allure.feature('License')
    @allure.title('Check invalid hardware id')
    @DLicense.put_new_license(folder_name='4')
    @DEntities.create_test_no_login()
    def test_license_004(self, test: TestCase):
        result = test.login_user(json_data=LoginData.data_log_super)
        test.check_status_code(result=result, entity_type=Code.USER, verif=StatusCode.STATUS_406)
        test.check_response(result=result, verif=VerifLicense.wrong_copy)

    @pytest.mark.test
    @allure.feature('License')
    @allure.title('Check denied access after expiration license')
    @DLicense.put_new_license(folder_name='6')
    @DEntities.create_test_no_login()
    def test_license_005(self, test: TestCase):
        result = test.login_user(json_data=LoginData.data_log_super)
        test.check_status_code(result=result, entity_type=Code.USER, verif=StatusCode.STATUS_406)
        test.check_response(result=result, verif=VerifLicense.license_expired)

    @allure.feature('License')
    @allure.title('Exclude dbadmin from users list')
    @DLicense.put_new_license(folder_name='10')
    @DEntities.create_test()
    @DEntities.add_delete_entities(entity_type=Code.USER, users_data=[(LoginData.EXPERT_LOGIN_3, 'Nikita'),
                                                                      (LoginData.EXPERT_LOGIN_2, 'Artem')])
    def test_license_006(self, test: TestCase):
        result = test.create_entity(entity_type=Code.USER, custom_json=LoginData.data_expert)
        test.check_status_code(result=result, entity_type=Code.USER, verif=StatusCode.STATUS_400)
        test.check_field(result=result, verif=VerifLicense.number_users_exceed, field_name=Code.MESSAGE,
                         err_msg=Code.Err.MSG_WRONG)

    @allure.feature('License')
    @allure.title('Check access after expiration license and prohibited import')
    @DLicense.put_new_license(folder_name='5')
    @DEntities.create_test()
    def test_license_007(self, test: TestCase):
        result = test.login_user(json_data=LoginData.data_log_super)
        test.check_status_code(result=result, entity_type=Code.USER, verif=StatusCode.STATUS_200)
        result = test.can_upload(sid=result)
        test.check_response(result=result, verif=VerifLicense.reason_1)

    @allure.feature('License')
    @allure.title('Check access after expiration education license')
    @DLicense.put_new_license(folder_name='11')
    @DEntities.create_test()
    def test_license_008(self, test: TestCase):
        result = test.login_user(json_data=LoginData.data_log_super)
        test.check_status_code(result=result, entity_type=Code.USER, verif=StatusCode.STATUS_200)
        result = test.can_upload(sid=result)
        test.check_response(result=result, verif=VerifLicense.reason_1)

    @allure.feature('License')
    @allure.title('Check denied access after expiration education license')
    @DLicense.put_new_license(folder_name='12')
    @DEntities.create_test_no_login()
    def test_license_009(self, test: TestCase):
        result = test.login_user(json_data=LoginData.data_log_super)
        test.check_status_code(result=result, entity_type=Code.USER, verif=StatusCode.STATUS_406)
        test.check_response(result=result, verif=VerifLicense.license_expired)

    @allure.feature('License')
    @allure.title('Check education license')
    @DLicense.put_new_license(folder_name='8')
    @DEntities.create_test()
    @DEntities.add_delete_entities(entities_name_list=data.tags, entity_type=Code.TAG)
    @DEntities.add_delete_entities(entities_name_list=data.keywords_sets, entity_type=Code.KEYWORD_SET)
    @DEntities.add_delete_entities(entities_name_list=data.hashes, entity_type=Code.HASH)
    @DEntities.add_delete_entities(entities_name_list=data.watchlists, entity_type=Code.WATCHLIST)
    def test_license_010(self, test: TestCase):
        # HASH
        result = test.create_entity(entity_type=Code.HASH)
        test.check_status_code(result=result, entity_type=Code.HASH, verif=StatusCode.STATUS_500)
        test.check_field(result=result, verif=VerifLicense.hash_20, field_name=Code.MESSAGE,
                         err_msg=Code.Err.MSG_WRONG)

        # KEYWORD SET
        result = test.create_entity(entity_type=Code.KEYWORD_SET)
        test.check_status_code(result=result, entity_type=Code.HASH, verif=StatusCode.STATUS_400)
        test.check_field(result=result, verif=VerifLicense.dict_watchlist_20, field_name=Code.MESSAGE,
                         err_msg=Code.Err.MSG_WRONG)

        # WATCH LIST
        result = test.create_entity(entity_type=Code.WATCHLIST)
        test.check_status_code(result=result, entity_type=Code.HASH, verif=StatusCode.STATUS_400)
        test.check_field(result=result, verif=VerifLicense.dict_watchlist_20, field_name=Code.MESSAGE,
                         err_msg=Code.Err.MSG_WRONG)

        # TAG
        result = test.create_entity(entity_type=Code.TAG)
        test.check_status_code(result=result, entity_type=Code.HASH, verif=StatusCode.STATUS_400)
        test.check_field(result=result, verif=VerifLicense.tag_20, field_name=Code.MESSAGE, err_msg=Code.Err.MSG_WRONG)
