import copy
import datetime
import logging
import re
import pytest
from data import ENV_HOST, STAND_LOGS_FOLDERS


def pytest_addoption(parser):
    parser.addoption("--url", default=ENV_HOST)
    parser.addoption("--log_level", default="DEBUG")


@pytest.fixture
def url(request):
    return request.config.getoption("--url")


@pytest.fixture
def test_logger(request):
    log_level = request.config.getoption("--log_level")
    logger = logging.getLogger(request.node.name)
    name_string = copy.deepcopy(request.node.name)
    folder = re.findall(r'_.*_', name_string)[0][1:-1]
    file_handler = logging.FileHandler(
        f"{STAND_LOGS_FOLDERS}\\{folder}\\{request.node.name}.log",
        encoding='utf-8')
    file_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
    logger.addHandler(file_handler)
    logger.setLevel(level=log_level)
    logger.info("===> {} начался {}".format(request.node.name, datetime.datetime.now()))

    test_logger.log_level = log_level
    test_logger.logger = logger
    test_logger.test_name = request.node.name

    yield test_logger
    logger.info("===> {} закончился {}\n".format(request.node.name, datetime.datetime.now()))
