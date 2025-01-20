from datetime import datetime
import os
import time
import psycopg2
import sys
import ctypes
from data import DataBase, STAND_BACKEND, STAND_PATH_LICENSE
import shutil
from API import log


def reload_backend():
    """Перезапускат монитор и очищается фильтры в базе данных"""
    log.info(f'Перезагружаю монитор')
    try:
        connection = psycopg2.connect(database=DataBase.DATABASE, user=DataBase.USER,
                                      password=DataBase.PASSWORD,
                                      host=DataBase.HOST, port=DataBase.PORT)
        cursor = connection.cursor()
        delete_query = """delete from "Configuration" where Parameter='Filters'"""
        cursor.execute(delete_query)
        connection.commit()
        connection.close()
        os.system("C:\\backend\\WAMonitor.exe stop")
        time.sleep(10)
        os.system("C:\\backend\\WAMonitor.exe start")
        time.sleep(25)
    except Exception as ex:
        log.error(f"{ex}")


def reload_backend_clear_time():
    """Перезапускат монитор и очищается время захода в систему в базе данных"""
    log.info(f'Перезагружаю монитор')
    try:
        connection = psycopg2.connect(database=DataBase.DATABASE, user=DataBase.USER,
                                      password=DataBase.PASSWORD,
                                      host=DataBase.HOST, port=DataBase.PORT)
        cursor = connection.cursor()
        update_query = """UPDATE "Configuration" SET "pvalue"='0' WHERE "parameter"='TSValue';"""
        cursor.execute(update_query)
        connection.commit()
        connection.close()
        os.system("C:\\backend\\WAMonitor.exe stop")
        time.sleep(10)
        os.system("C:\\backend\\WAMonitor.exe start")
        time.sleep(25)
    except Exception as ex:
        log.error(f"{ex}")


def delete_license():
    """Удаляет файл лицензии"""
    log.info(f'Удаляю {STAND_BACKEND}license.config"')
    try:
        os.remove(STAND_BACKEND + 'license.config')
    except Exception as ex:
        log.error(f"{ex}")


def copy_paste_license(copy_path):
    """Копирует файл лицензии и вставляет в папку backend"""
    log.info(f'Копирую {STAND_PATH_LICENSE}{copy_path}\\license.config, в {STAND_BACKEND}license.config')
    try:
        shutil.copy2(STAND_PATH_LICENSE + copy_path + '\\license.config', STAND_BACKEND + 'license.config')
    except Exception as ex:
        log.error(f"{ex}")


def execute_time_script_day_before():
    """Устанавливает дату за 1 день до окончания лецензии"""
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, 'C:\\Test_data\\time\\1.py', None, 1)


def execute_time_script_day_today():
    """Устанавливает дату  в день окончания лецензии до 02:00 по мск"""
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, 'C:\\Test_data\\time\\2.py', None, 1)


def execute_time_script_day_after():
    """Устанавливает дату  окончания лецензии после 02:00 по мск"""
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, 'C:\\Test_data\\time\\3.py', None, 1)


def execute_time_script_back():
    """Устанавливает дату окончания лецензии после 02:00 по мск"""
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, 'C:\\Test_data\\time\\back.py', None, 1)


def save_system_time():
    time_now = datetime.now()
    with open('C:\\Test_data\\time\\time_now.py', 'w') as file:
        file.write(str(time_now.year) + ' ' + str(time_now.month) + ' ' + '1' + ' ' + str(time_now.day) + ' ' + str(
            time_now.hour) + ' ' + str(time_now.minute) + ' ' + str(time_now.second) + ' ' + '0')
