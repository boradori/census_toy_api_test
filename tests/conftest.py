import pytest


def pytest_addoption(parser):
    # https://docs.python.org/2/library/argparse.html#action
    parser.addoption('--top_gender', action='store', default=0)
    parser.addoption('--top_country', action='store', default=0)
    parser.addoption('--top_pw_complex', action='store', default=0)


@pytest.fixture
def top_gender(request):
    return int(request.config.getoption('--top_gender'))


@pytest.fixture
def top_country(request):
    return int(request.config.getoption('--top_country'))


@pytest.fixture
def top_pw_complex(request):
    return int(request.config.getoption('--top_pw_complex'))
