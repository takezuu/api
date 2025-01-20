import allure

from Funcs import TestCase
from Pages_verification.Verification import StatusCode
from Pages_verification.Verification_tags import TagsVerif
from data import Code
from Pages_data.API_tags_data import TagsData
from tests.decorators import DEntities
from Factory import FTags


class TestTags:

    @allure.feature('Tags page')
    @allure.title('Create tag')
    @DEntities.create_test()
    @DEntities.delete_all_entities()
    @DEntities.delete_entity(entity_name=TagsData.create_tag['name'], entity_type=Code.TAG)
    def test_tags_001(self, test: TestCase):
        result = test.create_entity(entity_type=Code.TAG)
        test.check_status_code(result=result, entity_type=Code.TAG, verif=StatusCode.STATUS_200)
        test.check_id_and_type(result=result)

    @allure.feature('Tags page')
    @allure.title('Edit tag')
    @DEntities.create_test()
    @DEntities.add_delete_entity(entity_type=Code.TAG)
    def test_tags_002(self, test: TestCase, tag_id: int):
        json_data = FTags().set_id(tag_id).build()
        result = test.edit_entity(json_data=json_data, entity_type=Code.TAG, entity_id=tag_id)
        test.check_status_code(result=result, entity_type=Code.TAG, verif=StatusCode.STATUS_200)
        result = test.request_all_entities(entity_type=Code.TAG)
        test.check_entity_name(result=result, verif=TagsVerif.EDIT_NAME, entity_type=Code.TAG)

    @allure.feature('Tags page')
    @allure.title('Delete tag')
    @DEntities.create_test()
    @DEntities.add_delete_entity(entity_type=Code.TAG)
    def test_tags_003(self, test: TestCase, tag_id: int):
        result = test.delete_entity(entity_id=tag_id, entity_type=Code.TAG)
        test.check_status_code(result=result, entity_type=Code.TAG, verif=StatusCode.STATUS_200)
        result = test.request_all_entities(entity_type=Code.TAG)
        test.check_entities_deleted(result=result, entity_type=Code.TAG)

    @allure.feature('Tags page')
    @allure.title('Sort tags')
    @DEntities.create_test()
    def test_tags_004(self, test):
        result = test.request_all_entities(entity_type=Code.TAG)
        test.check_sort_entity(result=result, verif=TagsVerif.DESC_SORT)
        result = test.request_all_entities(entity_type=Code.TAG, custom_data=TagsData.asc_sort)
        test.check_sort_entity(result=result, verif=TagsVerif.ASC_SORT)
