from typing import List

from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import Select
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
import allure

from Pages.LoginPage import LoginPage


class AdminPage(LoginPage):

    @allure.step('Check added user')
    def check_grid_user_parameters(self, parameters: list[str], check_parameters: list[str]) -> None:
        """Проверяет соответсвие двух списков с параметрами пользователя в гриде"""
        try:
            self.logger.info(f'Сравниваю два списка параметров из грида {parameters} и {check_parameters}')
            assert parameters == check_parameters, "Параметры пользователя в гриде не сходятся"
        except AssertionError:
            self.logger.error(f'Два списка параметров не сошлись из грида {parameters} и {check_parameters}')
            with allure.step('Screenshot'):
                allure.attach(body=self.browser.get_screenshot_as_png(),
                              name='check added user')
            raise AssertionError('Параметры пользователя в гриде не сходятся')

    @allure.step('Select status')
    def select_status(self, element: WebElement, ind: int) -> None:
        """Выбирает статус пользователя 0: Суперпользователь 1: Администратор 2: Эксперт 3: Менеджер 4: Загрузчик"""
        status_list = ['Суперпользователь', 'Администратор', 'Эксперт', 'Менеджер', 'Загрузчик']
        self.logger.info(f'Выбираю статус {status_list[ind]}')
        Select(element).select_by_index(index=ind)

    @allure.step('Get user parameters')
    def get_grid_user_parameters(self, **kwargs: tuple) -> List[str]:
        """Возвращает список с параметрами пользователя в гриде"""
        parameters = []
        for arg in kwargs.values():
            self.logger.info(f'Получаю параметр у {arg[1]}')
            try:
                parameter = self.browser.find_element(*arg).text
            except NoSuchElementException:
                self.logger.error(f'Не получил параметр у {arg[1]}')
                with allure.step('Screenshot'):
                    allure.attach(body=self.browser.get_screenshot_as_png(),
                                  name='get user parameters')
                raise AssertionError('Параметр пользователя в гриде не получен')

            self.logger.info(f'Добавляю параметр {parameter} у {arg[1]} в список')
            parameters.append(parameter)
        self.logger.info('Возвращаю список')
        return parameters

    @allure.step('Check length of list')
    def check_length_of_list(self, elements_list: list, greater: bool = None, equal: bool = None) -> None:
        """Проверяю длину списка"""
        try:
            self.logger.info(f'Проверяю длину списка {elements_list}')
            if greater is not None:
                if len(elements_list) > 1:
                    self.logger.info(f'Длина списка больше 1 {elements_list}')
                    pass
                else:
                    self.logger.error(f'Длина списка не больше 1 {elements_list}')
                    with allure.step('Screenshot'):
                        allure.attach(body=self.browser.get_screenshot_as_png(),
                                      name='check_length_of_list')
                    raise AssertionError('Длина списка не больше 1')
            elif equal is not None:
                if len(elements_list) == 1:
                    self.logger.info(f'Длина списка равна 1 {elements_list}')
                    pass
                elif len(elements_list) > 1:
                    self.logger.error(f'Длина списка не равна 1 {elements_list}')
                    with allure.step('Screenshot'):
                        allure.attach(body=self.browser.get_screenshot_as_png(),
                                      name='check_length_of_list')
                    raise AssertionError('Длина списка 1 или больше 1')
        except Exception as ex:
            self.logger.error(f'Общее исключение {ex}')
            with allure.step('Screenshot'):
                allure.attach(body=self.browser.get_screenshot_as_png(),
                              name='check_length_of_list')
            raise AssertionError(f'Общее исключение {ex}')

    @allure.step('Check badge')
    def compare_badge_in_while(self, element_text: str) -> None:
        """Проверка статуса загрузки образа"""
        try:
            self.logger.info(f'Проверяю статус загрузки')
            if element_text == 'Queued':
                self.logger.info(f'{element_text}')
                pass
            elif element_text == 'Waiting for indexing':
                self.logger.info(f'{element_text}')
                pass
            elif element_text == 'Indexing':
                self.logger.info(f'{element_text}')
                pass
            elif element_text == 'Load':
                self.logger.info(f'{element_text}')
                pass
            else:
                assert element_text == 'Error', 'Текст в элементе не совпадает'
        except AssertionError:
            self.logger.error(f'Статус загрузки: {element_text},')
            with allure.step('Screenshot'):
                allure.attach(body=self.browser.get_screenshot_as_png(),
                              name='compare_badge_in_while')
            raise AssertionError('Текст не совпадает')

    @allure.step('Element is appeared')
    def check_element_is_appeared(self, element: tuple) -> bool:
        """Проверка, что элемент присутствует"""
        try:
            self.logger.info(f'Ищу элемент {element[1]}')
            assert self.browser.find_element(*element), 'Элемент отсутствует'
            self.logger.info(f'Элемент {element[1]} присутствует')
            return True
        except (AssertionError, NoSuchElementException):
            self.logger.info(f'Элемент {element[1]} отсутствует')
            return False

    @allure.step('Get badge')
    def get_upload_badge(self, element: tuple) -> str:
        """Возвращает статус загрузки образа"""
        try:
            self.logger.info(f'Получаю текст у элемента {element[1]}')
            element_text = self.browser.find_element(*element).text
            self.logger.info(f'Получил текст у элемента {element[1]}: {element_text}')
        except NoSuchElementException:
            self.logger.info(f'Отсутствует элемент {element[1]}')
            pass
        except Exception:
            self.logger.error(f'Общее исключение')
            with allure.step('Screenshot'):
                allure.attach(body=self.browser.get_screenshot_as_png(),
                              name='get upload badge')
            raise AssertionError(f'Общее исключение')
        else:
            return element_text

    @allure.step('Wait element')
    def wait_visability_upload(self, element: tuple) -> bool:
        """Ожидает элемент"""
        try:
            self.logger.info(f'Ожидаю элемент {element[1]}')
            self.wait.until(EC.visibility_of_element_located(element))
            self.logger.info(f'Возвращаю True загрузка присутсвует')
            return True
        except TimeoutException:
            self.logger.info(f'Возвращаю False загрузка отсутствует')
            return False
