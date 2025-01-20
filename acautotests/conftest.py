import pytest
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chromium.options import ChromiumOptions
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from data import ENV_HOST, STAND_PATH_DOWNLOADS
import datetime
import logging
from API import log


def pytest_addoption(parser):
    parser.addoption("--url", default=ENV_HOST)
    parser.addoption("--log_level", default="DEBUG")
    parser.addoption("--executor", default="no")
    parser.addoption("--nohead", default="no")
    parser.addoption("--browser_log", default="no")


@pytest.fixture()
def browser(request):
    executor = request.config.getoption("--executor")
    browser_log = request.config.getoption("--browser_log")
    log_level = request.config.getoption("--log_level")
    no_head = request.config.getoption("--nohead")
    # настройка логгера
    logger = logging.getLogger(request.node.name)
    file_handler = logging.FileHandler(f"C:\\Users\\User\\Develop\\acautotests\\tests\\logs\\{request.node.name}.log",
                                       encoding='utf-8')
    file_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
    logger.addHandler(file_handler)
    logger.setLevel(level=log_level)
    logger.info("===> {} начался {}".format(request.node.name, datetime.datetime.now()))
    log.info("===> {} начался {}".format(request.node.name, datetime.datetime.now()))
    # запуск браузера
    logger.info(f"Открываю браузер")

    if no_head == 'yes':
        caps = webdriver.DesiredCapabilities.CHROME.copy()
        caps['goog:loggingPrefs'] = {'browser': 'ALL'}
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        options.add_argument("--window-size=1920,1080")
        options.add_experimental_option("prefs", {
            "download.default_directory": f"{STAND_PATH_DOWNLOADS}",
            "download.prompt_for_download": False,
        })

        if executor != 'no':
            browser = webdriver.Remote(command_executor=f"http://{executor}:4444/wd/hub",
                                       desired_capabilities={"browserName": 'chrome'}, options=ChromiumOptions())
        else:
            browser = webdriver.Chrome(desired_capabilities=caps, options=options,
                                       service=ChromeService(ChromeDriverManager().install()))
        browser.command_executor._commands["send_command"] = ("POST", '/session/$sessionId/chromium/send_command')
        params = {'cmd': 'Page.setDownloadBehavior',
                  'params': {'behavior': 'allow', 'downloadPath': f"{STAND_PATH_DOWNLOADS}"}}
        browser.execute("send_command", params)
    else:
        browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        browser.maximize_window()
    #

    browser.log_level = log_level
    browser.logger = logger
    browser.test_name = request.node.name

    yield browser

    if browser_log == 'yes':
        browser_log = browser.get_log('browser')
        for line in browser_log:
            line = str(line)
            logger.info("ЛОГ БРАУЗЕРА: {}".format(line))
    browser.quit()

    logger.info("===> {} закончился {}\n".format(request.node.name, datetime.datetime.now()))
    log.info("===> {} закончился {}\n".format(request.node.name, datetime.datetime.now()))


@pytest.fixture
def url(request):
    return request.config.getoption("--url")
