import allure

from Funcs import TestCase
from Pages_verification.Verification import StatusCode
from Pages_verification.Verification_crime_types import CrimeTypesVerif
from data import Code
from Pages_data.API_crime_types_data import CrimeTypesData
from tests.decorators import DEntities
from Factory import FCrimeTypes


class TestCrimeTypes:

    @allure.feature('Crime types page')
    @allure.title('Create crime_types type')
    @DEntities.create_test()
    @DEntities.delete_all_entities()
    @DEntities.delete_entity(entity_name='Digital', entity_type=Code.CRIMETYPE)
    def test_crime_types_001(self, test: TestCase):
        result = test.create_entity(entity_type=Code.CRIMETYPE)
        test.check_status_code(result=result, entity_type=Code.CRIMETYPE, verif=StatusCode.STATUS_200)
        test.check_id_and_type(result=result)

    @allure.feature('Crime types page')
    @allure.title('Edit crime_types type')
    @DEntities.create_test()
    @DEntities.add_delete_entity(entity_type=Code.CRIMETYPE)
    def test_crime_types_002(self, test: TestCase, crime_type_id: int):
        json_data = FCrimeTypes().set_id(crime_type_id).set_name('Robbery').build()
        result = test.edit_entity(json_data=json_data, entity_type=Code.CRIMETYPE, entity_id=crime_type_id)
        test.check_status_code(result=result, entity_type=Code.CRIMETYPE, verif=StatusCode.STATUS_200)
        result = test.request_all_entities(entity_type=Code.CRIMETYPE)
        test.check_entity_name(result=result, verif=CrimeTypesVerif.EDIT_NAME)

    @allure.feature('Crime types page')
    @allure.title('Delete crime_types type')
    @DEntities.create_test()
    @DEntities.add_delete_entity(entity_type=Code.CRIMETYPE)
    def test_crime_types_003(self, test: TestCase, crime_type_id: int):
        result = test.delete_entity(entity_id=crime_type_id, entity_type=Code.CRIMETYPE)
        test.check_status_code(result=result, entity_type=Code.CRIMETYPE, verif=StatusCode.STATUS_200)
        result = test.request_all_entities(entity_type=Code.CRIMETYPE)
        test.check_entities_deleted(result=result)
