import pytest
import logging
from utilities.test_utils import (
    get_sorted_users_by,
    generate_random_users,
    make_post_request,
    compare_results_or_values
)


@pytest.mark.count_by_country
class TestCountByCountry:
    @pytest.fixture(scope="session")
    def headers(self):
        return {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }

    @pytest.fixture(scope="session")
    def api_url(self):
        return "https://census-toy.nceng.net/prod/toy-census"

    @pytest.mark.parametrize("num_of_users", [-1, 0, 1, 5])
    def test_count_by_country_returns_correct_values(self, api_url, headers, top_country, num_of_users):
        test_users = generate_random_users(num_of_users)
        response = make_post_request(
            api_url, test_users, action_type="CountByCountry", top=top_country, headers=headers
        )

        expected_status_code = 200
        logging.info(f'Expected status code: {expected_status_code}. Actual status code: {response.status_code}')
        assert expected_status_code == response.status_code, \
            f'Error: expected status code was {expected_status_code}, but actual status code was {response.status_code}'

        result = response.json()

        if num_of_users <= 0:
            num_users = len(test_users)
            num_results = len(result)
            logging.info(
                f'Verifying that the number of occurrences (actual: {num_results})'
                f' is equal to 0 when there are 0 users (actual: {num_users}).'
            )
            assert num_users == num_results == 0, \
                f'Error: Expected zero users and results, but got {num_users} users and {num_results} results.'
        else:
            expected_length = len(test_users) if top_country <= 0 or top_country > len(test_users) else top_country

            if top_country <= 0 or top_country > len(test_users):
                log_message = 'Verifying that the number of occurrences is equal to the number of generated users.'
            else:
                log_message = 'Verifying that the number of occurrences is equal to the specified "top" value.'

            logging.info(log_message)
            logging.info(f'Expected length of result: {expected_length}')
            logging.info(f'Actual length of result:   {len(result)}')
            assert expected_length == len(result), 'The number of results does not match the expected value.'

        logging.info('Verifying that the return values are ordered from highest to lowest.')
        expected_result = get_sorted_users_by('nat', test_users, top_country)
        logging.info(f'Expected result: {expected_result}')
        logging.info(f'Actual result:   {result}')

        # Compare the results directly, or by their values if they're not equal.
        if expected_result != result:
            results_match = compare_results_or_values(expected_result, result)
            assert results_match, f'Error: The expected result by values does not match the actual result.'

    def test_count_by_country_with_invalid_users_list(self, api_url, headers, top_country):
        test_users = generate_random_users()
        test_users.append({'invalid_name': 'test', 'invalid_value': 'test'})
        response = make_post_request(
            api_url, test_users, action_type="CountByCountry", top=top_country, headers=headers
        )

        expected_response_codes = [400, 422]
        logging.info(f'Verifying that the response status code are in {expected_response_codes}.')
        logging.info(f'Expected responses: {expected_response_codes}')
        logging.info(f'Actual response:    {response.status_code}')
        assert response.status_code in expected_response_codes, \
            f'Error: Expected response code {expected_response_codes}, but received {response.status_code}'

    @pytest.mark.parametrize("action_type", ["", " ", "invalid_action_type"])
    def test_count_by_country_with_invalid_action_type(self, api_url, headers, top_country, action_type):
        test_users = generate_random_users()
        response = make_post_request(api_url, test_users, action_type=action_type, top=top_country, headers=headers)

        expected_response_codes = [400, 422]
        logging.info(f'Verifying that the response status code are in {expected_response_codes}.')
        logging.info(f'Expected responses: {expected_response_codes}')
        logging.info(f'Actual response:    {response.status_code}')
        assert response.status_code in expected_response_codes, \
            f'Error: Expected response code {expected_response_codes}, but received {response.status_code}'

    def test_count_by_country_without_action_type(self, api_url, headers, top_country):
        test_users = generate_random_users()
        response = make_post_request(api_url, test_users, action_type=None, top=top_country, headers=headers)

        expected_response_codes = [400, 422]
        logging.info(f'Verifying that the response status code are in {expected_response_codes}.')
        logging.info(f'Expected responses: {expected_response_codes}')
        logging.info(f'Actual response:    {response.status_code}')
        assert response.status_code in expected_response_codes, \
            f'Error: Expected response code {expected_response_codes}, but received {response.status_code}'
