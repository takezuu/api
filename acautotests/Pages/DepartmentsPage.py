from typing import List

from selenium.common.exceptions import NoSuchElementException

import allure

from Pages.LoginPage import LoginPage


class DepartmentsPage(LoginPage):

    @allure.step('Check added department')
    def check_grid_department_parameters(self, parameters: list[str], check_parameters: list[str]) -> None:
        """Проверяет соответсвие двух списков с параметрами отдела в гриде"""
        try:
            self.logger.info(f'Сравниваю два списка параметров из грида {parameters} и {check_parameters}')
            assert parameters == check_parameters, "Параметры отдела в гриде не сходятся"
        except AssertionError:
            self.logger.error(f'Два списка параметров не сошлись из грида {parameters} и {check_parameters}')
            with allure.step('Screenshot'):
                allure.attach(body=self.browser.get_screenshot_as_png(),
                              name='check added department')
            raise AssertionError('Параметры отдела в гриде не сходятся')

    @allure.step('Get department parameters')
    def get_grid_department_parameters(self, **kwargs: tuple) -> List[str]:
        """Возвращает список с параметрами отдела в гриде"""
        parameters = []
        for arg in kwargs.values():
            self.logger.info(f'Получаю параметр у {arg[1]}')
            try:
                parameter = self.browser.find_element(*arg).text
            except NoSuchElementException:
                self.logger.error(f'Не получил параметр у {arg[1]}')
                with allure.step('Screenshot'):
                    allure.attach(body=self.browser.get_screenshot_as_png(),
                                  name='get department parameters')
                raise AssertionError('Параметр отдела в гриде не получен')

            self.logger.info(f'Добавляю параметр {parameter} у {arg[1]} в список')
            parameters.append(parameter)
        self.logger.info('Возвращаю список')
        return parameters
