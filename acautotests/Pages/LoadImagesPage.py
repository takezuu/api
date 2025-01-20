from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
import allure
from selenium.webdriver.support.select import Select

from Pages.BasePage import BasePage


class LoadImagesPage(BasePage):
    @allure.step('Select status')
    def select_status(self, element: WebElement, ind) -> None:
        """Выбирает дело 0: Не выбрано"""
        self.logger.info(f'Выбираю статус {ind}')
        Select(element).select_by_index(index=ind)

    @allure.step('Check badge')
    def compare_badge_in_while(self, element_text: str) -> None:
        """Проверка статуса загрузки образа"""
        try:
            self.logger.info(f'Проверяю статус загрузки')
            if element_text == 'Queued':
                self.logger.info(f'{element_text}')
                pass
            elif element_text == 'Indexing':
                self.logger.info(f'{element_text}')
                pass
            elif element_text == 'Upload':
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
