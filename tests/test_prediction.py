import json
from pytest import mark
from pytest_lazyfixture import lazy_fixture


@mark.parametrize(
    "input_json, output_json_expected, status_code_expected",
    [(lazy_fixture('input_json_1'), lazy_fixture('output_json_1'), 200)]
)
def test_invocations(client, input_json, output_json_expected, status_code_expected):
    request_answer = client.post('/invocations', data=json.dumps(input_json), content_type='application/json')
    output_json = request_answer.json
    assert output_json == output_json_expected

