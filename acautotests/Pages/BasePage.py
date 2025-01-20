import os
from typing import List

from selenium.common.exceptions import NoSuchElementException, InvalidArgumentException, TimeoutException, \
    WebDriverException
from selenium.webdriver import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import allure
import logging
from urllib3.exceptions import MaxRetryError
import re


class BasePage:

    def __init__(self, browser, wait=30):
        self.browser = browser
        self.wait = WebDriverWait(browser, wait)
        self.actions = ActionChains(browser)
        # logger
        self.logger = logging.getLogger(type(self).__name__)
        file_handler = logging.FileHandler(
            f"C:\\Users\\User\\Develop\\acautotests\\tests\\logs\\{self.browser.test_name}.log", encoding='utf-8')
        file_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
        self.logger.addHandler(file_handler)
        self.logger.handlers[:] = [file_handler]
        self.logger.setLevel(level=self.browser.log_level)

    @allure.step('Check name of tab')
    def check_name_of_tab(self, name_of_tab: str) -> None:
        """Проверяет корректное название вкладки"""
        try:
            self.logger.info(f'Проверяю название вкладки, корректное название {name_of_tab}')
            assert self.browser.title == name_of_tab, 'Не соответствует название вкладки'
        except AssertionError:
            self.logger.error(f'Название вкладки {name_of_tab} не совпадает c {self.browser.title} ')
            with allure.step('Screenshot'):
                allure.attach(body=self.browser.get_screenshot_as_png(),
                              name='check name of tab')
            raise AssertionError('Не совпадает название вкладки')

    @allure.step('Click on button')
    def click_element(self, element: tuple) -> None:
        """Клик по элементу"""
        try:
            self.logger.info(f'Кликаю по элементу {element[1]}')
            self.browser.find_element(*element).click()
        except NoSuchElementException:
            self.logger.error(f'Не кликнул по элементу {element[1]}')
            with allure.step('Screenshot'):
                allure.attach(body=self.browser.get_screenshot_as_png(),
                              name='click on button')
            raise AssertionError('Не удалось кликнуть по элементу')
        except Exception as ex:
            self.logger.error(f'Общее исключение {element[1]}, {ex}')
            with allure.step('Screenshot'):
                allure.attach(body=self.browser.get_screenshot_as_png(),
                              name='click on button')
            raise AssertionError(f'Общее исключение, {ex}')

    @allure.step('Element contains text')
    def check_element_contains_text(self, element: tuple) -> None:
        """Проверка, что элемент содержащий текст присутствует"""
        try:
            self.logger.info(f'Ищу элемент содержащий текст {element[1]}')
            assert self.browser.find_element(*element), 'Элемент отсутствует'
        except (AssertionError, NoSuchElementException):
            self.logger.error(f'Не нашел элемент содержащий текст {element[1]}')
            with allure.step('Screenshot'):
                allure.attach(body=self.browser.get_screenshot_as_png(),
                              name='element contains text')
            raise AssertionError('Элемент c текстом отсутствует на странице')

    @allure.step('Element absent')
    def check_element_absent(self, element: tuple) -> bool:
        """Проверка, что элемент отсутствует"""
        result = None
        try:
            self.logger.info(f'Проверяю отсутствие элемента {element[1]}')
            result = self.browser.find_element(*element).is_displayed()
        except NoSuchElementException:
            self.logger.info(f'Не нашел элемент {element[1]} {result}')
            return False
        else:
            try:
                assert not result, 'Элемент присутсвует'
            except AssertionError:
                self.logger.error(f'Нашел элемент {element[1]} {result}')
                with allure.step('Screenshot'):
                    allure.attach(body=self.browser.get_screenshot_as_png(),
                                  name='element is not absent')
                raise AssertionError('Элемент присутствует на странице')

    @allure.step('Clear monitor')
    def clear_monitor(self, element: tuple) -> bool:
        """Вылогинивает пользователя"""
        self.logger.info(f'Проверяю монитор')
        try:
            self.browser.find_element(*element)
            self.logger.info(f'Есть авторизованные пользователи')
            return True
        except NoSuchElementException:
            self.logger.info(f'Все пользователи вылогинены')
            return False

    @allure.step('Element contains text, but doesn\'t')
    def check_element_contains_text_disappeared(self, element: tuple) -> None or bool:
        """Проверка, что элемент содержащий текст пропал"""
        try:
            self.logger.info(f'Проверяю отсутствие элемента с текстом {element[1]}')
            self.browser.find_element(*element)
        except NoSuchElementException:
            return True
        else:
            self.logger.error(f'Найден элемент с текстом {element[1]}, хотя должен отсутствовать')
            with allure.step('Screenshot'):
                allure.attach(body=self.browser.get_screenshot_as_png(),
                              name='element contains text, but doesn\'t')
            raise AssertionError('Элемент с текстом присутствует на странице, хотя не должен')

    @allure.step('Check disable element')
    def check_disable_element(self, element: WebElement, name_of_attribute: str = 'disabled') -> None:
        """Проверяет, что элемент не активен"""
        try:
            self.logger.info(f'Проверяю неактивность элемента')
            assert element.get_attribute(name_of_attribute) == 'true', 'Элемент активен'
        except AssertionError:
            self.logger.error('Неактивный элемент активен')
            with allure.step('Screenshot'):
                allure.attach(body=self.browser.get_screenshot_as_png(),
                              name='check disable element')
            raise AssertionError('Неактивный элемент активен')

    @allure.step('Check able element')
    def check_able_element(self, element: WebElement, name_of_attribute: str = 'disabled') -> None:
        """Проверяет, что элемент активен"""
        try:
            self.logger.info(f'Проверяю активность элемента {element}')
            assert element.get_attribute(name_of_attribute) is None, 'Элемент не активен'
        except AssertionError:
            self.logger.error('Активный элемент не активен')
            with allure.step('Screenshot'):
                allure.attach(body=self.browser.get_screenshot_as_png(),
                              name='check able element')
            raise AssertionError('Активный элемент не активен')

    @allure.step('Check element attribute')
    def check_element_attribute(self, element: WebElement, name_of_attribute: str, state: str) -> None:
        """Проверяет корректный атрибут"""
        try:
            self.logger.info(f'Проверяю атрибут {name_of_attribute} у элемента, состояние {state}')
            assert element.get_attribute(name_of_attribute) == state, 'Атрибут не соответсвует'
        except AssertionError:
            self.logger.error(f'Атрибут {name_of_attribute}, не соответсвует: {state}')
            with allure.step('Screenshot'):
                allure.attach(body=self.browser.get_screenshot_as_png(),
                              name='check element attribute')
            raise AssertionError('Атрибут не соответсвует')

    @allure.step('Check warning message')
    def check_warning_message(self, element_text: str, message: str) -> None:
        """Проверяет текст предупреждения на корректность"""
        try:
            self.logger.info(f'Проверяю: {message}, у элемента')
            assert element_text == message, 'Текст в предупреждении не совпадает'
        except AssertionError:
            self.logger.error(f'Текст в предупреждении не совпадает: {element_text}, должно быть {message}')
            with allure.step('Screenshot'):
                allure.attach(body=self.browser.get_screenshot_as_png(),
                              name='check warning message')
            raise AssertionError('Текст в предупреждении не совпадает')

    @allure.step('Check text not equal')
    def check_text_not_in(self, element_text: str, message: str) -> None:
        """Проверка текста на не совпадение"""
        try:
            self.logger.info(f'Проверяю наличие текста: {message}, в элементе: {element_text}')
            assert message not in element_text, 'Текст в элементе содержится'
        except AssertionError:
            self.logger.error(f'Текст совпадает, текст элемента: {element_text}, не должно быть: {message}')
            with allure.step('Screenshot'):
                allure.attach(body=self.browser.get_screenshot_as_png(),
                              name='check_text_not_equal')
            raise AssertionError('Текст совпадает')

    @allure.step('Check notification')
    def compare_text(self, element_text: str, message: str) -> None:
        """Проверка текста на совпадение"""
        try:
            self.logger.info(f'Проверяю корректный текст элемента: {message}, текст элемента: {element_text}')
            assert element_text == message, 'Текст в элементе не совпадает'
        except AssertionError:
            self.logger.error(f'Текст не совпадает: {element_text}, должно быть: {message}')
            with allure.step('Screenshot'):
                allure.attach(body=self.browser.get_screenshot_as_png(),
                              name='compare_text')
            raise AssertionError('Текст не совпадает')

    @allure.step('Check sort/unsort lists')
    def compare_lists(self, list_1: list, list_2: list) -> None:
        """Проверка списков на совпадение"""
        try:
            self.logger.info(f'Проверяю совпадение двух списков: {list_1} и {list_2}')
            assert list_1 == list_2, 'Списки не совпадают'
            self.logger.info('Списки совпали')
        except AssertionError:
            self.logger.error(f'Списки не совпадают {list_1} и {list_2}')
            with allure.step('Screenshot'):
                allure.attach(body=self.browser.get_screenshot_as_png(),
                              name='compare_lists')
            raise AssertionError('Списки не совпадают')

    @allure.step('Check text in while')
    def compare_text_in_while(self, element_text: str, message: str, error_message: str) -> None:
        """Проверка статуса в цикле while"""
        try:
            self.logger.info(f'Проверяю текст в цикле while')
            if element_text == message:
                self.logger.info(f'{element_text}')
                pass
            else:
                assert element_text == error_message, 'Текст в элементе не совпадает'
        except AssertionError:
            self.logger.error(f'Статус загрузки: {element_text},')
            with allure.step('Screenshot'):
                allure.attach(body=self.browser.get_screenshot_as_png(),
                              name='compare_text_in_while')
            raise AssertionError('Текст не совпадает')

    @allure.step('Check counter after plus')
    def check_counter_plus(self, first_counter: int, second_counter: int) -> None:
        """Проверяет, что счетчик увеличился"""
        self.logger.info(f'Сравниваю два счетчика {first_counter} и {second_counter}')
        try:
            assert first_counter < second_counter, 'Первый счетчик меньше'
        except AssertionError:
            self.logger.error(f'Второй счетчик: {second_counter}, меньше первого: {first_counter}')
            with allure.step('Screenshot'):
                allure.attach(body=self.browser.get_screenshot_as_png(),
                              name='check counter plus')
            raise AssertionError('Второй счетчик меньше первого')

    @allure.step('Clear element of text')
    def clear_element(self, element: tuple) -> None:
        """Очищает элемент от текста"""
        self.logger.info(f'Очищаю элемент {element}')
        try:
            self.browser.find_element(*element).clear()
        except NoSuchElementException:
            self.logger.error(f'Элемент {element} не найден')
            with allure.step('Screenshot'):
                allure.attach(body=self.browser.get_screenshot_as_png(),
                              name='clear element')
            raise AssertionError('Элемент не очищен от текста')

    @allure.step('Close tab')
    def close_tab(self) -> None:
        """Закрывает активную вкладку"""
        self.logger.info('Закрываю вкладку')
        self.browser.close()

    @allure.step('Find element')
    def find_element(self, element: tuple) -> WebElement:
        """Находит элемент"""
        try:
            web_element = self.browser.find_element(*element)
        except NoSuchElementException:
            self.logger.error(f'Элемент {element[1]} не найден basepage')
            with allure.step('Screenshot'):
                allure.attach(body=self.browser.get_screenshot_as_png(),
                              name='get text element')
            raise AssertionError(f'Элемент {element[1]} не найден')
        except Exception as ex:
            self.logger.error(f'Общее исключение {element[1]} {ex}')
            with allure.step('Screenshot'):
                allure.attach(body=self.browser.get_screenshot_as_png(),
                              name='click on button')
            raise AssertionError(f'Общее исключение {ex}')
        else:
            return web_element

    @allure.step('Get counter')
    def get_counter(self, element: WebElement, n=1) -> int | float:
        """Возвращает число"""
        counter_split_string = None
        counter = None
        try:
            self.logger.info('Получаю строку счетчика')
            text_element = element.text.replace(',', "")
            self.logger.info(f'Cтрока счетчика {text_element}')
            counter_split_string = text_element.split()
            self.logger.info(f'Cтрока в split {counter_split_string}, n={n}')
            counter = int(counter_split_string[n])
            self.logger.info(f'Возвращаю счетчик {counter}')
            return counter
        except ValueError:
            self.logger.info(f'ValueError {counter_split_string} n={n}')
            return counter

    @allure.step('Get list of all tabs')
    def get_all_tabs(self) -> List[str]:
        """Возвращает список из id открытых вкладок"""
        self.logger.info('Получаю список закладок у браузера')
        return self.browser.window_handles

    @allure.step('Get text of element')
    def get_text_element(self, element: tuple) -> str:
        """Возвращает текст элемента"""
        try:
            self.logger.info(f'Получаю текст у элемента {element[1]}')
            element_text = self.browser.find_element(*element).text
            self.logger.info(f'Получил текст у элемента {element[1]}: {element_text}')
        except NoSuchElementException:
            self.logger.error(f'Элемент {element[1]} для получения текста не найден')
            with allure.step('Screenshot'):
                allure.attach(body=self.browser.get_screenshot_as_png(),
                              name='get text element')
            raise AssertionError(f'Элемент {element[1]} для получения текста не найден')
        else:
            return element_text

    @allure.step('Get text of element')
    def get_text_element_of_item(self, element: tuple) -> str or None:
        """Возвращает текст элемента"""
        try:
            self.logger.info(f'Получаю текст у элемента {element[1]}')
            element_text = self.browser.find_element(*element).text
            self.logger.info(f'Получил текст у элемента {element[1]}: {element_text}')
        except NoSuchElementException:
            return None
        else:
            return element_text

    @allure.step('Get any items list')
    def get_item_list(self, element: tuple) -> list:
        """Возвращает любой список элементов"""
        items_list = []
        n = 2
        try:
            while True:
                item = self.get_text_element_of_item(element=element)
                self.logger.info(f'IF {item}')
                if item is not None:
                    item = re.sub('\\n.*$', '', item)
                    items_list.append(item)
                    element = list(element)
                    if n == 2:
                        element[1] = element[1] + f':nth-child({n})'
                    elif n <= 10:
                        element[1] = element[1][0:-13] + f':nth-child({n})'
                    elif n >= 11:
                        element[1] = element[1][0:-14] + f':nth-child({n})'
                    element = tuple(element)
                    self.logger.info(f'Новое значение элемента {element[1]}')
                    n += 1
                else:
                    self.logger.info(f'Возвращаю список элементов {items_list}')
                    return items_list
        except Exception as ex:
            self.logger.error(f'Ошибка при получении не сортированного списка {element[1]}, {ex}')
            with allure.step('Screenshot'):
                allure.attach(body=self.browser.get_screenshot_as_png(),
                              name='get_item_list')
            raise AssertionError(f'Ошибка при получении не сортированного списка {element[1]}, {ex}')

    @allure.step('Get any items list')
    def get_item_list_slice(self, element: tuple, slice_index: int, only_first: str = None) -> list:
        """Возвращает любой список элементов"""
        items_list = []
        n = 2
        try:
            while True:
                item = self.get_text_element_of_item(element=element)
                self.logger.info(f'IF {item}')
                if item is not None:
                    if only_first == 'yes':
                        item = re.sub('\s.*$', '', item)
                    else:
                        item = re.sub('\\n.*$', '', item)
                    items_list.append(item)
                    element = list(element)
                    if n == 2:
                        element[1] = element[1][:slice_index] + f':nth-child({n})' + element[1][slice_index:]
                    elif n <= 10:
                        element[1] = element[1][:slice_index] + f':nth-child({n})' + element[1][slice_index + 13:]
                    elif n >= 11:
                        element[1] = element[1][:slice_index] + f':nth-child({n})' + element[1][slice_index + 14:]
                    element = tuple(element)
                    self.logger.info(f'Новое значение элемента {element[1]}')
                    n += 1
                else:
                    self.logger.info(f'Возвращаю список элементов {items_list}')
                    return items_list
        except Exception as ex:
            self.logger.error(f'Ошибка при получении не сортированного списка {element[1]}, {ex}')
            with allure.step('Screenshot'):
                allure.attach(body=self.browser.get_screenshot_as_png(),
                              name='get_item_list')
            raise AssertionError(f'Ошибка при получении не сортированного списка {element[1]}, {ex}')

    @allure.step('Get grid list')
    def get_item_grid_list(self, element: tuple, extra_locator) -> list:
        """Возвращает любой список элементов из грида"""
        items_list = []
        n = 2
        try:
            element = list(element)
            element[1] = element[1] + extra_locator
            element = tuple(element)
            while True:
                item = self.get_text_element_of_item(element=element)
                self.logger.info(f'Новое значение элемента {type(item)}')
                if item is not None and (len(item) > 1):
                    items_list.append(item.lower())
                    element = list(element)
                    if n == 3:
                        element[1] = element[1].replace(f'tr:nth-child({n - 1})', f'tr:nth-child({n})')
                    elif n <= 10:
                        element[1] = element[1].replace(f'tr:nth-child({n - 1})', f'tr:nth-child({n})')
                    elif n >= 11:
                        element[1] = element[1].replace(f'tr:nth-child({n - 1})', f'tr:nth-child({n})')
                    element = tuple(element)
                    self.logger.info(f'Новое значение элемента {element[1]}')
                    n += 1
                else:
                    self.logger.info(f'Возвращаю список элементов {items_list}')
                    return items_list
        except Exception as ex:
            self.logger.error(f'Ошибка при получении списка {element[1]}, {ex}')
            with allure.step('Screenshot'):
                allure.attach(body=self.browser.get_screenshot_as_png(),
                              name='get_item_list')
            raise AssertionError(f'Ошибка при получении списка {element[1]}. {ex}')

    @allure.step('Get screenshot')
    def get_browser_screenshot(self) -> None:
        self.logger.info(f'Делаю скриншот браузера')
        with allure.step('Screenshot'):
            allure.attach(body=self.browser.get_screenshot_as_png(),
                          name='screen for check')

    @allure.step('Hover on element')
    def hover_on_element(self, element: tuple) -> None:
        """Наводит мышь на элемент"""
        try:
            self.logger.info(f'Навожу курсор на элемент {element[1]}')
            hover = self.browser.find_element(*element)
            self.actions.move_to_element(hover).perform()
        except NoSuchElementException:
            self.logger.error(f'Отсутствует элемент {element[1]}')
            with allure.step('Screenshot'):
                allure.attach(body=self.browser.get_screenshot_as_png(),
                              name='hover on element')
            raise AssertionError('Элемент отсутствует на странице')

    @allure.step('Open new tab')
    def open_new_tab(self) -> None:
        """Открывает новую вкладку в браузере"""
        self.logger.info(f'Открываю новую вкладку')
        self.browser.switch_to.new_window('tab')

    @allure.step('Open url')
    def open_url(self, url: str, api: str = '') -> None:
        """Переходит по url"""
        try:
            self.logger.info(f"Открываю url {url}{api}")
            self.browser.get(f'{url}{api}')
        except InvalidArgumentException:
            self.logger.error(f"Браузер не смог открыть url: {url}{api}")
            with allure.step('Screenshot'):
                allure.attach(body=self.browser.get_screenshot_as_png(),
                              name='open url')
            raise AssertionError('Не правильный url')
        except MaxRetryError:
            self.logger.error(f"Не установил соединение url: {url}{api}")
            with allure.step('Screenshot'):
                allure.attach(body=self.browser.get_screenshot_as_png(),
                              name='Failed to establish a new connection')
            raise AssertionError('MaxRetryError: Failed to establish a new connection')
        except WebDriverException:
            self.logger.error(f"Не установил соединение url: {url}{api}")
            self.logger.info(f"Открываю url повторно {url}{api}")
            self.open_url(url=url, api=api)

    @allure.step('Open page in new tab')
    def open_page_in_new_tab(self, element: tuple) -> None:
        """Открывает страницу в новой вкладке горячие клавиши SHIFT+CTRL+LEFT_MOUSE"""
        try:
            self.logger.info(f'Открываю страницу в новой вкладке по нажатию на {element[1]}')
            web_element = self.browser.find_element(*element)
            self.actions.move_to_element(web_element).key_down(Keys.LEFT_SHIFT).key_down(
                Keys.LEFT_CONTROL).click(
                web_element).key_up(Keys.LEFT_SHIFT).key_up(Keys.LEFT_CONTROL).perform()
            self.logger.info(f'Клик сделан по {element[1]}')
        except NoSuchElementException:
            self.logger.error(f'Отсутствует элемент {element[1]}')
            with allure.step('Screenshot'):
                allure.attach(body=self.browser.get_screenshot_as_png(),
                              name='open page in new tab')
            raise AssertionError('Элемент отсутствует на странице')

    @allure.step('Refresh browser')
    def refresh_page(self) -> None:
        """Обновляет страницу в браузере"""
        try:
            self.logger.info('Обновляю страницу в браузере')
            self.browser.refresh()
        except TimeoutException:
            try:
                self.logger.info('Долгая загрузка страницы после обновления, повторяю')
                self.browser.refresh()
            except TimeoutException:
                self.logger.error('Долгая загрузка страницы после обновления, повторная ошибка')

    @allure.step('Select tab number')
    def select_tab_number(self, number: int, tabs: list) -> None:
        """Переключает на указанную вкладку"""
        try:
            self.logger.info(f'Переключаюсь на вкладку номер {number}')
            tab = tabs[number - 1]
            self.browser.switch_to.window(tab)
        except IndexError:
            self.logger.error(f'Не переключился на вкладку номер {number - 1}')
            with allure.step('Screenshot'):
                allure.attach(body=self.browser.get_screenshot_as_png(),
                              name='select tab number')
            raise AssertionError('Указан неверный номер вкладки')

    @allure.step('Press Enter')
    def press_enter(self) -> None:
        """Нажимает Enter"""
        self.logger.info(f'Нажимаю Enter')
        self.actions.key_down(Keys.ENTER).key_up(Keys.ENTER).perform()

    @allure.step('Write in element')
    def write_in_element(self, element: tuple, text: str) -> None:
        """Пишет в элементе"""
        try:
            self.logger.info(f'Пишу в элементе {element[1]}, текст {text}')
            self.browser.find_element(*element).send_keys(text)
        except NoSuchElementException:
            self.logger.error(f'Отсутствует элемент {element[1]}, написать в нем невозможно')
            with allure.step('Screenshot'):
                allure.attach(body=self.browser.get_screenshot_as_png(),
                              name='write in element')
            raise AssertionError('Элемент отсутствует на странице')
        except Exception as ex:
            self.logger.error(f'Общее исключение {element[1]}, {ex}')
            with allure.step('Screenshot'):
                allure.attach(body=self.browser.get_screenshot_as_png(),
                              name='click on button')
            raise AssertionError(f'Общее исключение {ex}')

    @allure.step('Wait element')
    def wait_visability_element(self, element: tuple) -> None:
        """Ожидает элемент"""
        try:
            self.logger.info(f'Ожидаю элемент {element[1]}')
            self.wait.until(EC.visibility_of_element_located(element))
        except TimeoutException:
            self.logger.error(f'Время ожидания элемента закончилось {element[1]}')
            with allure.step('Screenshot'):
                allure.attach(body=self.browser.get_screenshot_as_png(),
                              name='wait element')
            raise AssertionError('Не дождался элемента')

    @allure.step('Wait element')
    def wait_not_visability_element(self, element: tuple) -> None:
        """Ожидает отсутствие элемента"""
        try:
            self.logger.info(f'Ожидаю скрытие элемента {element[1]}')
            self.wait.until_not(EC.visibility_of_element_located(element))
        except TimeoutException:
            self.logger.error(f'Время ожидания элемента закончилось {element[1]}')
            with allure.step('Screenshot'):
                allure.attach(body=self.browser.get_screenshot_as_png(),
                              name='wait element')
            raise AssertionError('Не дождался скрытие элемента')

    @allure.step('Wait element is clickable')
    def wait_element_is_clickable(self, element: tuple) -> None:
        """Ожидает, что элемент кликабелен"""
        try:
            self.logger.info(f'Ожидаю пока элемент станет кликабельным {element[1]}')
            self.wait.until(EC.element_to_be_clickable(element))
        except TimeoutException:
            self.logger.error(f'Время ожидания кликабельности закончилось {element[1]}')
            with allure.step('Screenshot'):
                allure.attach(body=self.browser.get_screenshot_as_png(),
                              name='wait element is clickable')
            raise AssertionError('Не дождался элемента')

    @allure.step('Quit browser')
    def quit(self) -> None:
        """Закрывает браузер"""
        self.logger.info(f'Закрываю браузер принудительно')
        self.browser.quit()

    @allure.step('Upload file')
    def upload_file(self, file_dir: str, file_name: str, element: tuple) -> None:
        """Загружает файл"""
        self.logger.info(f'Загружаю файл в браузер')
        file_path = os.path.join(file_dir, file_name)
        element = self.browser.find_element(*element)
        element.send_keys(file_path)
