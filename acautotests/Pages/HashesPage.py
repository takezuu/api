import allure
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import Select
from Pages.BasePage import BasePage
from data import STAND_PATH_DOWNLOADS


class HashesPage(BasePage):

    @allure.step('Select status')
    def select_status(self, element: WebElement, ind: int) -> None:
        """Выбирает тип хеша 0: MD5, 1: SHA1, 2: SHA256"""
        type_list = ['MD5', 'SHA1', 'SHA256']
        self.logger.info(f'Выбираю статус {type_list[ind]}')
        Select(element).select_by_index(index=ind)

    @allure.step('Select file status')
    def select_file_status(self, element: WebElement, ind: int) -> None:
        """Выбирает тип экспортируемого файла 0: JSON, 1: TXT"""
        type_list = ['JSON', 'TXT']
        self.logger.info(f'Выбираю статус {type_list[ind]}')
        Select(element).select_by_index(index=ind)

    @allure.step('Check badge')
    def compare_badge_in_while(self, element_text: str) -> bool:
        """Проверка статуса загрузки хеша, возвращает True если статус Готов"""
        try:
            self.logger.info(f'Получают статус загрузки')
            if element_text == 'Queued':
                self.logger.info(f'{element_text}')
                return False
            elif element_text == 'Indexing':
                self.logger.info(f'{element_text}')
                return False
            elif element_text == 'Ready':
                self.logger.info(f'{element_text}')
                return True
            else:
                assert element_text == 'Error', 'Текст в элементе не совпадает'
        except AssertionError:
            self.logger.error(f'Статус загрузки: {element_text},')
            with allure.step('Screenshot'):
                allure.attach(body=self.browser.get_screenshot_as_png(),
                              name='compare_badge_in_while')
            raise AssertionError('Текст не совпадает')

    @allure.step('Check hash file')
    def check_hash_file(self, file_name: str) -> None:
        """Проверяет, что в файле есть записи"""
        # STAND_PATH_DOWNLOADS
        file_path = f'{STAND_PATH_DOWNLOADS}' + f'{file_name}'
        with open(file_path) as file:
            self.logger.info(f'Проверяю содержимое файла {file_path}')
            try:
                assert len(file.read()) > 0, 'Файл пустой'
                file.close()
                self.logger.info('Файл не пустой')
            except AssertionError:
                self.logger.error(f'Файл пустой')
                with allure.step('Screenshot'):
                    allure.attach(body=self.browser.get_screenshot_as_png(), name='check_hash_file')
                raise AssertionError('Файл пустой')
            finally:
                import os
                os.remove(file_path)
