import allure
import pytest

from Funcs import TestCase
from Pages_verification.Verification import StatusCode
from Pages_verification.Verification_keywords_sets import KeywordsSetsVerif
from data import Code, keywords_sets_different_names
from Pages_data.API_keywords_sets_data import KeywordsSetsData
from tests.decorators import DEntities
from Factory import FKeywordsSets


class TestKeywordsSets:

    @allure.feature('Keywords sets page')
    @allure.title('Create new empty keyword set with different types')
    @pytest.mark.parametrize('param', [(KeywordsSetsData.EMPTY, KeywordsSetsVerif.EMPTY,
                                        KeywordsSetsData.TYPE_ALL_PAGES, KeywordsSetsVerif.TYPE_ALL_PAGES),
                                       (KeywordsSetsData.EMPTY, KeywordsSetsVerif.EMPTY,
                                        KeywordsSetsData.TYPE_FILES, KeywordsSetsVerif.TYPE_FILES),
                                       (KeywordsSetsData.EMPTY, KeywordsSetsVerif.EMPTY,
                                        KeywordsSetsData.TYPE_WRKSPACE_CONTACTS,
                                        KeywordsSetsVerif.TYPE_WRKSPACE_CONTACTS)
                                       ])
    @DEntities.create_test_param()
    @DEntities.delete_all_entities()
    @DEntities.delete_entity_param(entity_type=Code.KEYWORD_SET, param_num=0)
    def test_keywords_sets_001(self, test: TestCase):
        param = test.param
        json_data = FKeywordsSets().set_name(param[0]).set_dclass(param[2]).build()
        result = test.create_entity(entity_type=Code.KEYWORD_SET, custom_json=json_data)
        test.check_status_code(result=result, entity_type=Code.KEYWORD_SET, verif=StatusCode.STATUS_200)
        test.check_id_and_type(result=result)
        result = test.request_all_entities(entity_type=Code.KEYWORD_SET)
        test.check_dict_class(result=result, verif=param[3])
        test.check_entity_name(result=result, verif=param[1], entity_type=Code.KEYWORD_SET)

    @allure.feature('Keywords sets page')
    @allure.title('Create new keyword set with different types')
    @pytest.mark.parametrize('param', [('utf_8.txt', KeywordsSetsData.TEST, KeywordsSetsData.TYPE_UTF8,
                                        KeywordsSetsData.TYPE_ALL_PAGES, KeywordsSetsVerif.TYPE_ALL_PAGES),
                                       ('utf_16.txt', KeywordsSetsData.TEST, KeywordsSetsData.TYPE_UTF16,
                                        KeywordsSetsData.TYPE_ALL_PAGES, KeywordsSetsVerif.TYPE_ALL_PAGES),
                                       ('utf_8.txt', KeywordsSetsData.TEST, KeywordsSetsData.TYPE_UTF8,
                                        KeywordsSetsData.TYPE_FILES, KeywordsSetsVerif.TYPE_FILES),
                                       ('utf_16.txt', KeywordsSetsData.TEST, KeywordsSetsData.TYPE_UTF16,
                                        KeywordsSetsData.TYPE_FILES, KeywordsSetsVerif.TYPE_FILES),
                                       ('utf_8.txt', KeywordsSetsData.TEST, KeywordsSetsData.TYPE_UTF8,
                                        KeywordsSetsData.TYPE_WRKSPACE_CONTACTS,
                                        KeywordsSetsVerif.TYPE_WRKSPACE_CONTACTS),
                                       ('utf_16.txt', KeywordsSetsData.TEST, KeywordsSetsData.TYPE_UTF16,
                                        KeywordsSetsData.TYPE_WRKSPACE_CONTACTS,
                                        KeywordsSetsVerif.TYPE_WRKSPACE_CONTACTS)
                                       ])
    @DEntities.create_test_param()
    @DEntities.add_import_delete_entity_param(entity_type=Code.KEYWORD_SET)
    def test_keywords_sets_002(self, test: TestCase):
        param = test.param
        result = test.request_all_entities(entity_type=Code.KEYWORD_SET)
        test.check_dict_class(result=result, verif=param[4])
        test.check_entity_name(result=result, verif=param[1])

    @allure.feature('Keywords sets page')
    @allure.title('Edit new empty keyword set with different types')
    @pytest.mark.parametrize('param', [(KeywordsSetsData.EMPTY, KeywordsSetsData.TYPE_ALL_PAGES,
                                        2, 'New dict name', 'note for test',
                                        KeywordsSetsVerif.WORDS_LIST, KeywordsSetsVerif.PARAMETERS_1
                                        ),
                                       (KeywordsSetsData.EMPTY, KeywordsSetsData.TYPE_FILES,
                                        1, 'New dict name', 'note for test',
                                        KeywordsSetsVerif.WORDS_LIST, KeywordsSetsVerif.PARAMETERS_2),
                                       (KeywordsSetsData.EMPTY, KeywordsSetsData.TYPE_WRKSPACE_CONTACTS,
                                        0, 'New dict name', 'note for test',
                                        KeywordsSetsVerif.WORDS_LIST, KeywordsSetsVerif.PARAMETERS_3
                                        )
                                       ])
    @DEntities.create_test_param()
    @DEntities.add_delete_entity_param_id(entity_type=Code.KEYWORD_SET)
    def test_keywords_sets_003(self, test: TestCase, keyword_set_id: int):
        param = test.param
        json_data = FKeywordsSets().set_id(keyword_set_id).set_name(param[3]).set_note(param[4]).set_dclass(
            param[2]).build()

        test.edit_entity(entity_type=Code.KEYWORD_SET, json_data=json_data, entity_id=keyword_set_id)

        json_data = FKeywordsSets().set_words_update(words=['weapon', 'knife', 'scar'],
                                                     keyword_set_id=keyword_set_id).build()
        test.content_update(json_data=json_data, entity_type=Code.KEYWORD_SET)

        result = test.request_all_entities(entity_type=Code.KEYWORD_SET)
        test.check_dict_class(result=result, verif=param[2])
        test.check_entity_name(result=result, verif=param[3])
        test.check_entity_note(result=result, verif=param[4])

        result = test.get_entity_content(entity_type=Code.KEYWORD_SET, entity_id=keyword_set_id)
        test.check_total(result=result, verif_num=3)

    @allure.feature('Keywords sets page')
    @allure.title('Delete keywords set')
    @pytest.mark.parametrize('param', [('utf_8.txt', KeywordsSetsData.TEST, KeywordsSetsData.TYPE_UTF8),
                                       ('utf_8.txt', KeywordsSetsData.TEST, KeywordsSetsData.TYPE_UTF8),
                                       ('utf_8.txt', KeywordsSetsData.TEST, KeywordsSetsData.TYPE_UTF8)])
    @DEntities.create_test_param()
    @DEntities.add_import_delete_entity_param_id(entity_type=Code.KEYWORD_SET)
    def test_keywords_sets_004(self, test: TestCase, keyword_set_id: int):
        result = test.delete_entity(entity_id=keyword_set_id, entity_type=Code.KEYWORD_SET)
        test.check_status_code(result=result, entity_type=Code.KEYWORD_SET, verif=StatusCode.STATUS_200)
        result = test.request_all_entities(entity_type=Code.KEYWORD_SET)
        test.check_entities_deleted(result=result, entity_type=Code.KEYWORD_SET)

    @allure.feature('Keywords sets page')
    @allure.title('Sort keywords set')
    @DEntities.create_test()
    @DEntities.add_delete_entities(entity_type=Code.KEYWORD_SET, entities_name_list=keywords_sets_different_names)
    def test_keywords_sets_005(self, test: TestCase):
        result = test.request_all_entities(entity_type=Code.TAG)
        test.check_sort_entity(result=result, verif=KeywordsSetsVerif.DESC_SORT)
        result = test.request_all_entities(entity_type=Code.TAG, custom_data=KeywordsSetsData.asc_sort)
        test.check_sort_entity(result=result, verif=KeywordsSetsVerif.ASC_SORT)
