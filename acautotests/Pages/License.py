from datetime import datetime, date

from Pages.BasePage import BasePage


class License(BasePage):

    def transform_date(self, date_str: str) -> date:
        """Перевожу дату из строкового типа в дату"""
        self.logger.info(f'Дата строка {date_str}')
        date_str = date_str.split('.')[::-1]
        self.logger.info(f'Дата форматированная {date_str}')
        return datetime.date(*date_str)

    def compare_date(self, formatted_date: date) -> None:
        """Сравнение двух дат"""
        self.logger.info(f'Сравниваю дату с сегодняшней {formatted_date}')
        today = date.today()
        assert formatted_date > today, 'Неверная дата'
