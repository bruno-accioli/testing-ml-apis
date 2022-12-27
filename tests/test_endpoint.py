import requests
import pytest
from pytest import mark
from pytest_lazyfixture import lazy_fixture


@pytest.mark.endpoint
@mark.parametrize(
    "input_json, output_json_expected, status_code_expected",
    [
        (lazy_fixture('input_json_1'), lazy_fixture('output_json_1'), 200)
    ]
)
def test_endpoint_invocations(endpoint_address, input_json, output_json_expected, status_code_expected):
    if endpoint_address is None:
        raise Exception("Argument '--endpoint' was not defined")

    request = requests.post(f'{endpoint_address}/invocations', json=input_json)
    output_json = request.json()

    output = (request.status_code, output_json)
    output_expected = (status_code_expected, output_json_expected)
    assert (output == output_expected)
