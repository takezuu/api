import allure
import pytest
from Funcs import TestCase
from Pages_verification.Verification import StatusCode
from Pages_verification.Verification_watchlists import VerifWatchLists
from data import Code
from Pages_data.API_watchlists_data import WatchlistsData
from tests.decorators import DEntities
from Factory import FWatchlists


class TestWatchLists:

    @allure.feature('Watchlists page')
    @allure.title('Create new empty watchlist with different types')
    @pytest.mark.parametrize('param', [(WatchlistsData.phone_number, VerifWatchLists.phone_number,
                                        WatchlistsData.type1, VerifWatchLists.type1),
                                       (WatchlistsData.display_name, VerifWatchLists.display_name,
                                        WatchlistsData.type1, VerifWatchLists.type1),
                                       (WatchlistsData.description, VerifWatchLists.description,
                                        WatchlistsData.type1, VerifWatchLists.type1),
                                       (WatchlistsData.email_address, VerifWatchLists.email_address,
                                        WatchlistsData.type1, VerifWatchLists.type1),
                                       (WatchlistsData.chat_id, VerifWatchLists.chat_id,
                                        WatchlistsData.type1, VerifWatchLists.type1),
                                       (WatchlistsData.account_name, VerifWatchLists.account_name,
                                        WatchlistsData.type1, VerifWatchLists.type1),
                                       (WatchlistsData.phone_number, VerifWatchLists.phone_number,
                                        WatchlistsData.type2, VerifWatchLists.type2),
                                       (WatchlistsData.display_name, VerifWatchLists.display_name,
                                        WatchlistsData.type2, VerifWatchLists.type2),
                                       (WatchlistsData.description, VerifWatchLists.description,
                                        WatchlistsData.type2, VerifWatchLists.type2),
                                       (WatchlistsData.email_address, VerifWatchLists.email_address,
                                        WatchlistsData.type2, VerifWatchLists.type2),
                                       (WatchlistsData.chat_id, VerifWatchLists.chat_id,
                                        WatchlistsData.type2, VerifWatchLists.type2),
                                       (WatchlistsData.account_name, VerifWatchLists.account_name,
                                        WatchlistsData.type2, VerifWatchLists.type2)])
    @DEntities.create_test_param()
    @DEntities.delete_all_entities()
    @DEntities.delete_entity_param(entity_type=Code.WATCHLIST, param_num=0)
    def test_watchlists_001(self, test: TestCase):
        param = test.param
        json_data = FWatchlists().set_name(name=param[0]).set_dclass(param[2]).set_field(param[0]).build()
        result = test.create_entity(entity_type=Code.WATCHLIST, custom_json=json_data)
        test.check_status_code(result=result, entity_type=Code.WATCHLIST, verif=StatusCode.STATUS_200)
        test.check_id_and_type(result=result)
        result = test.request_all_entities(entity_type=Code.WATCHLIST)
        test.check_dict_class(result=result, verif=param[3])
        test.check_entity_name(result=result, verif=param[1])

    @allure.feature('Watchlists page')
    @allure.title('Create new watchlist with words')
    @pytest.mark.parametrize('param', [(WatchlistsData.phone_number, VerifWatchLists.phone_number,
                                        WatchlistsData.type1, VerifWatchLists.type1, WatchlistsData.words_list),
                                       (WatchlistsData.display_name, VerifWatchLists.display_name,
                                        WatchlistsData.type1, VerifWatchLists.type1, WatchlistsData.words_list),
                                       (WatchlistsData.description, VerifWatchLists.description,
                                        WatchlistsData.type1, VerifWatchLists.type1, WatchlistsData.words_list),
                                       (WatchlistsData.email_address, VerifWatchLists.email_address,
                                        WatchlistsData.type1, VerifWatchLists.type1, WatchlistsData.words_list),
                                       (WatchlistsData.chat_id, VerifWatchLists.chat_id,
                                        WatchlistsData.type1, VerifWatchLists.type1, WatchlistsData.words_list),
                                       (WatchlistsData.account_name, VerifWatchLists.account_name,
                                        WatchlistsData.type1, VerifWatchLists.type1, WatchlistsData.words_list),
                                       (WatchlistsData.phone_number, VerifWatchLists.phone_number,
                                        WatchlistsData.type2, VerifWatchLists.type2, WatchlistsData.words_list),
                                       (WatchlistsData.display_name, VerifWatchLists.display_name,
                                        WatchlistsData.type2, VerifWatchLists.type2, WatchlistsData.words_list),
                                       (WatchlistsData.description, VerifWatchLists.description,
                                        WatchlistsData.type2, VerifWatchLists.type2, WatchlistsData.words_list),
                                       (WatchlistsData.email_address, VerifWatchLists.email_address,
                                        WatchlistsData.type2, VerifWatchLists.type2, WatchlistsData.words_list),
                                       (WatchlistsData.chat_id, VerifWatchLists.chat_id,
                                        WatchlistsData.type2, VerifWatchLists.type2, WatchlistsData.words_list),
                                       (WatchlistsData.account_name, VerifWatchLists.account_name,
                                        WatchlistsData.type2, VerifWatchLists.type2, WatchlistsData.words_list)])
    @DEntities.create_test_param()
    @DEntities.add_delete_entity_param_id(entity_type=Code.WATCHLIST)
    def test_watchlists_002(self, test: TestCase, watchlist_id: int):
        param = test.param
        result = test.request_all_entities(entity_type=Code.WATCHLIST)
        test.check_dict_class(result=result, verif=param[3])
        test.check_entity_name(result=result, verif=param[1])

        result = test.get_entity_content(entity_type=Code.WATCHLIST, entity_id=watchlist_id)
        test.check_total(result, verif_num=len(VerifWatchLists.words_list))

    @allure.feature('Watchlists page')
    @allure.title('Edit watchlist with words')
    @pytest.mark.parametrize('param', [(WatchlistsData.phone_number, VerifWatchLists.phone_number,
                                        WatchlistsData.type1, VerifWatchLists.type1, WatchlistsData.words_list),
                                       (WatchlistsData.display_name, VerifWatchLists.display_name,
                                        WatchlistsData.type1, VerifWatchLists.type1, WatchlistsData.words_list),
                                       (WatchlistsData.description, VerifWatchLists.description,
                                        WatchlistsData.type1, VerifWatchLists.type1, WatchlistsData.words_list),
                                       (WatchlistsData.email_address, VerifWatchLists.email_address,
                                        WatchlistsData.type1, VerifWatchLists.type1, WatchlistsData.words_list),
                                       (WatchlistsData.chat_id, VerifWatchLists.chat_id,
                                        WatchlistsData.type1, VerifWatchLists.type1, WatchlistsData.words_list),
                                       (WatchlistsData.account_name, VerifWatchLists.account_name,
                                        WatchlistsData.type1, VerifWatchLists.type1, WatchlistsData.words_list),
                                       (WatchlistsData.phone_number, VerifWatchLists.phone_number,
                                        WatchlistsData.type2, VerifWatchLists.type2, WatchlistsData.words_list),
                                       (WatchlistsData.display_name, VerifWatchLists.display_name,
                                        WatchlistsData.type2, VerifWatchLists.type2, WatchlistsData.words_list),
                                       (WatchlistsData.description, VerifWatchLists.description,
                                        WatchlistsData.type2, VerifWatchLists.type2, WatchlistsData.words_list),
                                       (WatchlistsData.email_address, VerifWatchLists.email_address,
                                        WatchlistsData.type2, VerifWatchLists.type2, WatchlistsData.words_list),
                                       (WatchlistsData.chat_id, VerifWatchLists.chat_id,
                                        WatchlistsData.type2, VerifWatchLists.type2, WatchlistsData.words_list),
                                       (WatchlistsData.account_name, VerifWatchLists.account_name,
                                        WatchlistsData.type2, VerifWatchLists.type2, WatchlistsData.words_list)])
    @DEntities.create_test_param()
    @DEntities.add_delete_entity_param_id(entity_type=Code.WATCHLIST)
    def test_watchlists_003(self, test: TestCase, watchlist_id: int):
        json_data = FWatchlists().set_id(watchlist_id).set_words(WatchlistsData.new_words).build()
        test.update_entity_content(entity_type=Code.WATCHLIST, json_data=json_data)
        result = test.get_entity_content(entity_type=Code.WATCHLIST, entity_id=watchlist_id)
        test.check_entity_content(result=result, verif=VerifWatchLists.words_list + VerifWatchLists.new_words)

    @allure.feature('Watchlists page')
    @allure.title('Create new watchlist with words and indexing')
    @pytest.mark.parametrize('param', [(WatchlistsData.phone_number, VerifWatchLists.phone_number,
                                        WatchlistsData.type1, VerifWatchLists.type1, WatchlistsData.words_list),
                                       (WatchlistsData.display_name, VerifWatchLists.display_name,
                                        WatchlistsData.type1, VerifWatchLists.type1, WatchlistsData.words_list),
                                       (WatchlistsData.description, VerifWatchLists.description,
                                        WatchlistsData.type1, VerifWatchLists.type1, WatchlistsData.words_list),
                                       (WatchlistsData.email_address, VerifWatchLists.email_address,
                                        WatchlistsData.type1, VerifWatchLists.type1, WatchlistsData.words_list),
                                       (WatchlistsData.chat_id, VerifWatchLists.chat_id,
                                        WatchlistsData.type1, VerifWatchLists.type1, WatchlistsData.words_list),
                                       (WatchlistsData.account_name, VerifWatchLists.account_name,
                                        WatchlistsData.type1, VerifWatchLists.type1, WatchlistsData.words_list),
                                       (WatchlistsData.phone_number, VerifWatchLists.phone_number,
                                        WatchlistsData.type2, VerifWatchLists.type2, WatchlistsData.words_list),
                                       (WatchlistsData.display_name, VerifWatchLists.display_name,
                                        WatchlistsData.type2, VerifWatchLists.type2, WatchlistsData.words_list),
                                       (WatchlistsData.description, VerifWatchLists.description,
                                        WatchlistsData.type2, VerifWatchLists.type2, WatchlistsData.words_list),
                                       (WatchlistsData.email_address, VerifWatchLists.email_address,
                                        WatchlistsData.type2, VerifWatchLists.type2, WatchlistsData.words_list),
                                       (WatchlistsData.chat_id, VerifWatchLists.chat_id,
                                        WatchlistsData.type2, VerifWatchLists.type2, WatchlistsData.words_list),
                                       (WatchlistsData.account_name, VerifWatchLists.account_name,
                                        WatchlistsData.type2, VerifWatchLists.type2, WatchlistsData.words_list)])
    @DEntities.create_test_param()
    @DEntities.add_delete_entity_param_id(entity_type=Code.WATCHLIST)
    def test_watchlists_004(self, test: TestCase, watchlist_id: int):
        result = test.indexing_entity(entity_type=Code.WATCHLIST, entity_id=watchlist_id)
        test.check_status_code(result=result, entity_type=Code.WATCHLIST, verif=StatusCode.STATUS_200)
        result = test.request_all_entities(entity_type=Code.WATCHLIST)
        test.check_entity_status(result=result, verif=1)

    @allure.feature('Watchlists page')
    @allure.title('Edit watchlist with words and indexing')
    @pytest.mark.parametrize('param', [(WatchlistsData.phone_number, VerifWatchLists.phone_number,
                                        WatchlistsData.type1, VerifWatchLists.type1, WatchlistsData.words_list),
                                       (WatchlistsData.display_name, VerifWatchLists.display_name,
                                        WatchlistsData.type1, VerifWatchLists.type1, WatchlistsData.words_list),
                                       (WatchlistsData.description, VerifWatchLists.description,
                                        WatchlistsData.type1, VerifWatchLists.type1, WatchlistsData.words_list),
                                       (WatchlistsData.email_address, VerifWatchLists.email_address,
                                        WatchlistsData.type1, VerifWatchLists.type1, WatchlistsData.words_list),
                                       (WatchlistsData.chat_id, VerifWatchLists.chat_id,
                                        WatchlistsData.type1, VerifWatchLists.type1, WatchlistsData.words_list),
                                       (WatchlistsData.account_name, VerifWatchLists.account_name,
                                        WatchlistsData.type1, VerifWatchLists.type1, WatchlistsData.words_list),
                                       (WatchlistsData.phone_number, VerifWatchLists.phone_number,
                                        WatchlistsData.type2, VerifWatchLists.type2, WatchlistsData.words_list),
                                       (WatchlistsData.display_name, VerifWatchLists.display_name,
                                        WatchlistsData.type2, VerifWatchLists.type2, WatchlistsData.words_list),
                                       (WatchlistsData.description, VerifWatchLists.description,
                                        WatchlistsData.type2, VerifWatchLists.type2, WatchlistsData.words_list),
                                       (WatchlistsData.email_address, VerifWatchLists.email_address,
                                        WatchlistsData.type2, VerifWatchLists.type2, WatchlistsData.words_list),
                                       (WatchlistsData.chat_id, VerifWatchLists.chat_id,
                                        WatchlistsData.type2, VerifWatchLists.type2, WatchlistsData.words_list),
                                       (WatchlistsData.account_name, VerifWatchLists.account_name,
                                        WatchlistsData.type2, VerifWatchLists.type2, WatchlistsData.words_list)])
    @DEntities.create_test_param()
    @DEntities.add_delete_entity_param_id(entity_type=Code.WATCHLIST)
    def test_watchlists_005(self, test: TestCase, watchlist_id: int):
        json_data = FWatchlists().set_words(WatchlistsData.new_words).set_id(watchlist_id).build()
        result = test.update_entity_content(entity_type=Code.WATCHLIST, json_data=json_data)
        test.check_status_code(result=result, entity_type=Code.WATCHLIST, verif=StatusCode.STATUS_200)
        result = test.indexing_entity(entity_type=Code.WATCHLIST, entity_id=watchlist_id)
        test.check_status_code(result=result, entity_type=Code.WATCHLIST, verif=StatusCode.STATUS_200)
        result = test.request_all_entities(entity_type=Code.WATCHLIST)
        test.check_entity_status(result=result, verif=1)

    @allure.feature('Watchlists page')
    @allure.title('Create new empty watchlist with different types and import words')
    @pytest.mark.parametrize('param', [('utf_8.txt', WatchlistsData.phone_number, VerifWatchLists.phone_number,
                                        WatchlistsData.type1, VerifWatchLists.type1),
                                       ('utf_8.txt', WatchlistsData.display_name, VerifWatchLists.display_name,
                                        WatchlistsData.type1, VerifWatchLists.type1),
                                       ('utf_8.txt', WatchlistsData.description, VerifWatchLists.description,
                                        WatchlistsData.type1, VerifWatchLists.type1),
                                       ('utf_8.txt', WatchlistsData.email_address, VerifWatchLists.email_address,
                                        WatchlistsData.type1, VerifWatchLists.type1),
                                       ('utf_8.txt', WatchlistsData.chat_id, VerifWatchLists.chat_id,
                                        WatchlistsData.type1, VerifWatchLists.type1),
                                       ('utf_8.txt', WatchlistsData.account_name, VerifWatchLists.account_name,
                                        WatchlistsData.type1, VerifWatchLists.type1),
                                       ('utf_8.txt', WatchlistsData.phone_number, VerifWatchLists.phone_number,
                                        WatchlistsData.type2, VerifWatchLists.type2),
                                       ('utf_8.txt', WatchlistsData.display_name, VerifWatchLists.display_name,
                                        WatchlistsData.type2, VerifWatchLists.type2),
                                       ('utf_8.txt', WatchlistsData.description, VerifWatchLists.description,
                                        WatchlistsData.type2, VerifWatchLists.type2),
                                       ('utf_8.txt', WatchlistsData.email_address, VerifWatchLists.email_address,
                                        WatchlistsData.type2, VerifWatchLists.type2),
                                       ('utf_8.txt', WatchlistsData.chat_id, VerifWatchLists.chat_id,
                                        WatchlistsData.type2, VerifWatchLists.type2),
                                       ('utf_8.txt', WatchlistsData.account_name, VerifWatchLists.account_name,
                                        WatchlistsData.type2, VerifWatchLists.type2)])
    @DEntities.create_test_param()
    @DEntities.add_import_delete_entity_param_id(entity_type=Code.WATCHLIST)
    def test_watchlists_006(self, test: TestCase, watchlist_id: int):
        result = test.get_entity_content(entity_type=Code.WATCHLIST, entity_id=watchlist_id)
        test.check_field(result=result, verif=5, field_name=Code.TOTAL, err_msg=Code.Err.ISNT_EQUAL)
