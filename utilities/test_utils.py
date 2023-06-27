import requests
import logging
import re
import operator
from functools import reduce
from collections import Counter


def generate_random_users(num_of_users=5):
    api_url = "https://randomuser.me/api"
    users = []

    while True:
        response = requests.get(api_url)
        if response.status_code == 200:
            for i in range(num_of_users):
                response = requests.get(api_url)
                user = response.json()["results"][0]
                users.append(user)

            return users


def make_post_request(api_url, users, action_type=None, top=None):
    payload = {
        "users": users,
    }

    if action_type is not None:
        payload["actionType"] = action_type

    if top is not None:
        payload["top"] = top

    response = requests.post(api_url, json=payload)
    return response


def get_nested_property(data, property_type):
    try:
        # Splits the property_type string into a list of keys
        return reduce(operator.getitem, property_type.split('.'), data)
    except (TypeError, KeyError):
        return None


def get_sorted_users_by(property_type, users, top):
    property_type_counter = Counter([get_nested_property(item, property_type) for item in users])
    sorted_counts = sorted(property_type_counter.items(), key=lambda x: x[1], reverse=True)

    # Create a list of JSON objects with 'name' and 'value' keys up to the specified 'top' value
    if top > 0:
        return [{'name': property_type, 'value': count} for property_type, count in sorted_counts][:top]
    else:
        return [{'name': property_type, 'value': count} for property_type, count in sorted_counts]


def get_length_of_non_alphanumeric(data):
    return len(re.findall('\W', data))  # '\W' regex that matches any non-alphanumeric character


def get_sorted_pw_complexity(users, top):
    password_info_list = []

    for user in users:
        password_chars = get_nested_property(user, 'login.password')
        non_alphanumeric_count = get_length_of_non_alphanumeric(password_chars)
        password_info_list.append({'name': password_chars, 'value': non_alphanumeric_count})

    if top > 0:
        return sorted(password_info_list, key=lambda x: x['value'], reverse=True)[:top]
    else:
        return sorted(password_info_list, key=lambda x: x['value'], reverse=True)


def compare_results_or_values(expected_result, result):
    if expected_result != result:
        expected_result_by_values = [item['value'] for item in expected_result]
        result_by_values = [item['value'] for item in result]

        logging.info(f'Expected result by values: {expected_result_by_values}')
        logging.info(f'Actual result by values:   {result_by_values}')

        assert expected_result_by_values == result_by_values, \
            f'Error: The expected result by values {expected_result_by_values}' \
            f' does not match the actual result {result_by_values}.'
