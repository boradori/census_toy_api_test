import pytest
import requests
import random


@pytest.fixture(scope="session")
def setup_test_users():
    api_url = "https://randomuser.me/api"
    response = requests.get(api_url)

    assert response.status_code == 200

    # repeat the request if the response is not 200 with a while loop and error handling
    while response.status_code != 200:
        response = requests.get(api_url)
        if response.status_code == 200:
            break
        elif response.status_code != 200:
            raise Exception("The API is not responding.")

    users = []

    for i in range(random.randint(1, 5)):
        response = requests.get(api_url)
        users.append(response.json()["results"])

    yield users

