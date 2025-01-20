import allure

from Funcs import TestCase
from Pages_verification.Verification import StatusCode
from Pages_verification.Verification_regions import RegionsVerif
from data import Code
from Pages_data.API_regions_data import RegionsData
from tests.decorators import DEntities
from Factory import FRegions


class TestRegions:

    @allure.feature('Regions page')
    @allure.title('Create region')
    @DEntities.create_test()
    @DEntities.delete_all_entities()
    @DEntities.delete_entity(entity_name=RegionsData.create_region['name'], entity_type=Code.REGION)
    def test_regions_001(self, test: TestCase):
        result = test.create_entity(entity_type=Code.REGION)
        test.check_status_code(result=result, entity_type=Code.REGION, verif=StatusCode.STATUS_200)
        test.check_id_and_type(result=result)

    @allure.feature('Regions page')
    @allure.title('Edit region')
    @DEntities.create_test()
    @DEntities.add_delete_entity(entity_type=Code.REGION)
    def test_regions_002(self, test: TestCase, region_id: int):
        json_data = FRegions().set_id(region_id).set_name('Rostov').build()
        result = test.edit_entity(json_data=json_data, entity_type=Code.REGION, entity_id=region_id)
        test.check_status_code(result=result, entity_type=Code.REGION, verif=StatusCode.STATUS_200)
        result = test.request_all_entities(entity_type=Code.REGION)
        test.check_entity_name(result=result, verif=RegionsVerif.EDIT_NAME)

    @allure.feature('Regions page')
    @allure.title('Delete region')
    @DEntities.create_test()
    @DEntities.add_delete_entity(entity_type=Code.REGION)
    def test_regions_003(self, test: TestCase, region_id: int):
        result = test.delete_entity(entity_id=region_id, entity_type=Code.REGION)
        test.check_status_code(result=result, entity_type=Code.REGION, verif=StatusCode.STATUS_200)
        result = test.request_all_entities(entity_type=Code.REGION)
        test.check_entities_deleted(result=result)
