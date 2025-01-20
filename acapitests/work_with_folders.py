import os

from data import STAND_LOGS_FOLDERS

folder_path = STAND_LOGS_FOLDERS


def make_folders():
    """Создает необходимые папки для логов"""
    folders = ['admin', 'crime_types', 'departments', 'hashes', 'keywords_sets', 'license', 'login', 'regions', 'tags',
               'watchlists']

    if os.path.exists(folder_path):
        for folder in folders:
            os.mkdir(folder_path + folder)
    else:
        os.mkdir(folder_path)
        for folder in folders:
            os.mkdir(folder_path + folder)


def clear_folders():
    """Очищает папки для логов и удаляет API.log"""
    os.remove(folder_path + 'API.log')
    all_log_folders = os.listdir(folder_path)
    for folder in all_log_folders:
        logs_in_folder = os.listdir(folder_path + folder)
        for log in logs_in_folder:
            os.remove(folder_path + folder + '\\' + log)


# make_folders()
# clear_folders()
