import allure
import requests

from Funcs import TestCase
from Pages_verification.Verification import StatusCode
from Pages_verification.Verification_departments import VerifDepartment
from data import Code
from tests.decorators import DEntities
from Factory import FDepartments


class TestDepartments:

    @allure.feature('Departments page')
    @allure.title('Create department')
    @DEntities.create_test()
    @DEntities.delete_all_entities()
    @DEntities.delete_entity(entity_type=Code.DEPARTMENT)
    def test_departments_001(self, test: TestCase):
        result = test.create_entity(entity_type=Code.DEPARTMENT)
        test.check_status_code(result=result, entity_type=Code.DEPARTMENT, verif=StatusCode.STATUS_200)
        test.check_id_and_type(result=result)

    @allure.feature('Departments page')
    @allure.title('Edit department')
    @DEntities.create_test()
    @DEntities.add_delete_entity(entity_type=Code.DEPARTMENT)
    def test_departments_002(self, test: TestCase, department_id: int):
        json_data = FDepartments().set_id(department_id).build()
        result = test.edit_entity(json_data=json_data, entity_type=Code.DEPARTMENT, entity_id=department_id)
        test.check_status_code(result=result, entity_type=Code.DEPARTMENT, verif=StatusCode.STATUS_200)
        result = test.request_all_entities(entity_type=Code.DEPARTMENT)
        test.check_entity_name(result=result, verif=VerifDepartment.EDIT_NAME, entity_type=Code.DEPARTMENT)
        test.check_entity_note(result=result, verif=VerifDepartment.EDIT_NOTE)

    @allure.feature('Departments page')
    @allure.title('Delete department')
    @DEntities.create_test()
    @DEntities.add_delete_entity(entity_type=Code.DEPARTMENT)
    def test_departments_003(self, test: TestCase, department_id: int):
        result = test.delete_entity(entity_id=department_id, entity_type=Code.DEPARTMENT)
        test.check_status_code(result=result, entity_type=Code.DEPARTMENT, verif=StatusCode.STATUS_200)
        result = test.request_all_entities(entity_type=Code.DEPARTMENT)
        test.check_entities_deleted(result=result, entity_type=Code.DEPARTMENT)
