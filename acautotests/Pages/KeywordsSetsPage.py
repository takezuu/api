import allure
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import Select
from Pages.BasePage import BasePage
from data import STAND_PATH_KEYWORDS_SETS, STAND_PATH_DOWNLOADS


class KeywordsSetsPage(BasePage):

    @allure.step('Select status')
    def select_status(self, element: WebElement, ind) -> None:
        """Выбирает тип словаря 0: Рабочее пространство, Карта и Контакты, 1: Файлы, 2: Все страницы"""
        type_list = ['Рабочее пространство, Карта и Контакты', 'Файлы', 'Все страницы']
        self.logger.info(f'Выбираю статус {type_list[ind]}')
        Select(element).select_by_index(index=ind)

    @allure.step('Check badge')
    def compare_badge_in_while(self, element_text: str) -> bool:
        """Проверка статуса загрузки словаря, возвращает True если статус Готов"""
        try:
            self.logger.info(f'Получаю статус загрузки')
            if element_text == 'Queued':
                self.logger.info(f'{element_text}')
                return False
            elif element_text == 'Indexing':
                self.logger.info(f'{element_text}')
                return False
            elif element_text == 'Waiting for indexing':
                self.logger.info(f'{element_text}')
                return False
            elif element_text == 'Ready':
                self.logger.info(f'{element_text}')
                return True
            else:
                assert element_text == 'Ошибка', 'Текст в элементе не совпадает'
        except AssertionError:
            self.logger.error(f'Статус загрузки: {element_text},')
            with allure.step('Screenshot'):
                allure.attach(body=self.browser.get_screenshot_as_png(),
                              name='compare_badge_in_while')
            raise AssertionError('Текст не совпадает')

    @allure.step('Check keyword set file')
    def check_len_keyword_set_file(self, file_name: str) -> int:
        """Проверяет, кол-во строк записей в файле"""
        file_path = f'{STAND_PATH_KEYWORDS_SETS}' + f'{file_name}'
        encoding = None
        if file_name == '1251.txt':
            encoding = 'windows-1251'
        elif file_name == 'utf_8.txt':
            encoding = 'utf-8'
        elif file_name == 'utf_16.txt':
            encoding = 'utf-16-le'

        with open(file_path, encoding=encoding) as file:
            self.logger.info(f'Проверяю содержимое файла {file_path}')
            try:
                return len(file.readlines())
            except AssertionError:
                self.logger.error(f'Файл пустой')
                with allure.step('Screenshot'):
                    allure.attach(body=self.browser.get_screenshot_as_png(), name='check_keyword_set_file')
                raise AssertionError('Файл пустой')

    @allure.step('Compare lists')
    def compare_text_list(self, element_text: str, message: str) -> None:
        """Проверка списков на совпадение"""
        try:
            self.logger.info(f'Проверяю корректный список: {message}, список элемента: {element_text}')
            assert element_text == message, 'Список в элементе не совпадает'
        except AssertionError:
            self.logger.error(f'Список не совпадает: {element_text}, должно быть: {message}')
            with allure.step('Screenshot'):
                allure.attach(body=self.browser.get_screenshot_as_png(),
                              name='compare_text_list')
            raise AssertionError('Список не совпадает')

    @allure.step('Check keyword set file')
    def check_keyword_set_file(self, file_name: str) -> None:
        """Проверяет, что в файле есть записи"""
        #
        file_path = f'{STAND_PATH_DOWNLOADS}' + f'{file_name}'
        with open(file_path) as file:
            self.logger.info(f'Проверяю содержимое файла {file_path}')
            try:
                assert len(file.read()) > 0, 'Файл пустой'
                #file.close()
                self.logger.info('Файл не пустой')
            except AssertionError:
                self.logger.error(f'Файл пустой')
                with allure.step('Screenshot'):
                    allure.attach(body=self.browser.get_screenshot_as_png(), name='check_keyword_set_file')
                raise AssertionError('Файл пустой')
            finally:
                import os
                os.remove(file_path)

    @allure.step('Return list of keyword set file')
    def return_list_keyword_set_file(self, file_name: str) -> list:
        """Возвращает список строк файла"""
        file_path = f'{STAND_PATH_KEYWORDS_SETS}' + f'{file_name}'
        encoding = None
        if file_name == '1251.txt':
            encoding = 'windows-1251'
        elif file_name == 'utf_8.txt':
            encoding = 'utf-8'
        elif file_name == 'utf_16.txt':
            encoding = 'utf-16-le'

        with open(file_path, encoding=encoding) as file:
            self.logger.info(f'Проверяю содержимое файла {file_path}')
            words_list = []
            try:
                words = file.readlines()
                if file_name == 'utf_16.txt':
                    words[0] = words[0][1:]
                for word in words[:-1]:
                    words_list.append(word[:-1])
                words_list.append(words[-1])
                return words_list
            except AssertionError:
                self.logger.error(f'Файл пустой')
                with allure.step('Screenshot'):
                    allure.attach(body=self.browser.get_screenshot_as_png(), name='return_list_keyword_set_file')
                raise AssertionError('Файл пустой')

    @allure.step('Select file status')
    def select_file_status(self, element: WebElement, ind: int) -> None:
        """Выбирает тип экспортируемого файла 0: JSON, 1: TXT"""
        type_list = ['JSON', 'TXT']
        self.logger.info(f'Выбираю статус {type_list[ind]}')
        Select(element).select_by_index(index=ind)
