from selenium.common.exceptions import NoSuchElementException
from Pages.BasePage import BasePage
import allure


class LoginPage(BasePage):

    @allure.step('Check log in status')
    def check_logged_status(self, text_element: str, check_string: str) -> None:
        """Проверяет статус пользователя после входа в систему"""
        try:
            self.logger.info(f'Сравниваю статус пользователя {text_element} с правильным {check_string}')
            assert text_element == check_string, 'Не совпадает текст проверки'
        except AssertionError:
            self.logger.error(f'Статус {text_element} не совпадает  с правильным {check_string}')
            with allure.step('Screenshot'):
                allure.attach(body=self.browser.get_screenshot_as_png(),
                              name='check log in status')
            raise AssertionError('Статус не совпадает')

    @allure.step('Check available bars')
    def check_available_bars(self, **kwargs: tuple) -> None:
        """Проверяет доступные разделы(бары) в системе"""
        for arg in kwargs.values():
            try:
                self.logger.info(f'Проверяю наличие бара {arg[1]}')
                self.browser.find_element(*arg)
                self.logger.info(f'Бар {arg[1]} присутствует')
            except NoSuchElementException:
                self.logger.error(f'Бар отсутствует {arg[1]}')
                with allure.step('Screenshot'):
                    allure.attach(body=self.browser.get_screenshot_as_png(),
                                  name='check available bars')
                raise AssertionError(f'Бар отсутсвует {arg[1]}')
