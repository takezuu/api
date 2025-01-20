import allure
import pytest

from Funcs import TestCase
from Pages_verification.Verification import StatusCode
from Pages_verification.Verification_hashes import HashesVerif
from data import Code
from Pages_data.API_hashes_data import HashesData
from tests.decorators import DEntities
from Factory import FHashes


class TestHashes:

    @allure.feature('Hashes page')
    @allure.title('Create new empty hash with different types')
    @pytest.mark.parametrize('param', [(HashesData.HASH_MD5, HashesData.TYPE_MD5, HashesVerif.TYPE_MD5),
                                       (HashesData.HASH_SHA1, HashesData.TYPE_SHA1, HashesVerif.TYPE_SHA1),
                                       (HashesData.HASH_SHA256, HashesData.TYPE_SHA256, HashesVerif.TYPE_SHA256)
                                       ])
    @DEntities.create_test_param()
    @DEntities.delete_all_entities()
    @DEntities.delete_entity_param(entity_type=Code.HASH, param_num=0)
    def test_hashes_001(self, test: TestCase):
        param = test.param
        json_data = FHashes().set_name(param[0]).set_type(param[1]).build()
        result = test.create_entity(entity_type=Code.HASH, custom_json=json_data)
        test.check_status_code(result=result, entity_type=Code.HASH, verif=StatusCode.STATUS_200)
        test.check_id_and_type(result=result)
        result = test.request_all_entities(entity_type=Code.HASH)
        test.check_hash_type(result=result, verif=param[2])

    @allure.feature('Hashes page')
    @allure.title('Create hashes with different types')
    @pytest.mark.parametrize('param', [('test_sha-1.txt', HashesData.HASH_SHA1,
                                        HashesData.TYPE_SHA1),
                                       ('test_sha-256.txt', HashesData.HASH_SHA256,
                                        HashesData.TYPE_SHA256),
                                       ('test_md5.txt', HashesData.HASH_MD5,
                                        HashesData.TYPE_MD5),
                                       ])
    @DEntities.create_test_param()
    @DEntities.add_import_delete_entity_param(entity_type=Code.HASH)
    def test_hashes_002(self, test: TestCase):
        param = test.param
        result = test.request_all_entities(entity_type=Code.HASH)
        test.check_hash_type(result=result, verif=param[2])

    @allure.feature('Hashes page')
    @allure.title('Edit hashes with different types')
    @pytest.mark.parametrize('param',
                             [(HashesData.HASH_MD5, HashesData.TYPE_MD5, "edited_hash_sha1", "SHA1", "for new hash",
                               HashesVerif.NEW_SHA1),
                              (HashesData.HASH_SHA1, HashesData.TYPE_SHA1, "edited_hash_sha256", "SHA256",
                               "for new hash", HashesVerif.NEW_SHA256),
                              (HashesData.HASH_SHA256, HashesData.TYPE_SHA256, "edited_hash_MD5", "MD5", "for new hash",
                               HashesVerif.NEW_MD5)
                              ])
    @DEntities.create_test_param()
    @DEntities.add_delete_entity_param_id(entity_type=Code.HASH)
    def test_hashes_003(self, test: TestCase, hash_id: int):
        param = test.param
        json_data = FHashes().set_id(hash_id).set_name(param[2]).set_type(param[3]).set_note(param[4]).build()
        result = test.edit_entity(entity_type=Code.HASH, entity_id=hash_id, json_data=json_data)
        test.check_status_code(result=result, entity_type=Code.HASH, verif=StatusCode.STATUS_200)
        result = test.request_all_entities(entity_type=Code.HASH)
        test.check_hash_type(result=result, verif=param[5]['type'])
        test.check_entity_note(result=result, verif=param[5]['note'])
        test.check_entity_name(result=result, verif=param[5]['name'])

    @allure.feature('Hashes page')
    @allure.title('Delete hashes with different types')
    @pytest.mark.parametrize('param', [('test_sha-1.txt', HashesData.HASH_SHA1,
                                        HashesData.TYPE_SHA1),
                                       ('test_sha-256.txt', HashesData.HASH_SHA256,
                                        HashesData.TYPE_SHA256),
                                       ('test_md5.txt', HashesData.HASH_MD5,
                                        HashesData.TYPE_MD5),
                                       ])
    @DEntities.create_test_param()
    @DEntities.add_import_delete_entity_param_id(entity_type=Code.HASH)
    def test_hashes_004(self, test: TestCase, hash_id: int):
        result = test.delete_entity(entity_id=hash_id, entity_type=Code.HASH)
        test.check_status_code(result=result, entity_type=Code.HASH, verif=StatusCode.STATUS_200)
        result = test.request_all_entities(entity_type=Code.HASH)
        test.check_entities_deleted(result=result, entity_type=Code.HASH)
