import sys
import pathlib
import pytest
import pandas as pd

ROOT_PATH = pathlib.Path(__file__).parents[1]
code_directory = ROOT_PATH/'deployment'

if str(code_directory) not in sys.path:
    sys.path.append(str(code_directory))

from api import app


def pytest_addoption(parser):
    parser.addoption("--endpoint", type=str, default=None, help="Endereco do endpoint para realizar os testes.")

@pytest.fixture
def endpoint_address(request):
    endpoint_address = request.config.getoption("--endpoint")
    if endpoint_address is not None and not endpoint_address.startswith('http://'):
        endpoint_address = f"http://{endpoint_address}"
    return endpoint_address

@pytest.fixture
def input_json_1():
    input_json = {
        "native_country": "Peru",
        "marital_status": "Never-married",
        "sex": "Male",
        "capital_gain": 0,
        "capital_loss": 0,
        "hours_per_week": 43,
        "age": 25,
        "education_num": 13
    }
    return input_json

@pytest.fixture
def input_json_preprocessed_1():
    input_json_preprocessed = pd.DataFrame(
        [{
            "native_usa": 0,
            "native_latin_america": 1,
            "native_europe": 0,
            "native_asia": 0,
            "is_male": 1,
            "is_married": 0,
            "capital_gain": 0,
            "capital_loss": 0,
            "hours_per_week": 43,
            "age": 25,
            "education_num": 13
        }]
    )
    return input_json_preprocessed

@pytest.fixture
def output_json_1():
    output_json = {
        "income > 50k": 0
    }
    return output_json

@pytest.fixture
def input_country_cuba():
    return pd.DataFrame([{"native_country": "Cuba"}])

@pytest.fixture
def input_country_england():
    return pd.DataFrame([{"native_country": "England"}])

@pytest.fixture
def input_country_japan():
    return pd.DataFrame([{"native_country": "Japan"}])

@pytest.fixture
def input_country_usa():
    return pd.DataFrame([{"native_country": "United-States"}])

@pytest.fixture
def input_country_cuba_preprocessed():
    return pd.DataFrame([{"native_usa": 0, "native_latin_america": 1, "native_europe": 0, "native_asia":0}])

@pytest.fixture
def input_country_england_preprocessed():
    return pd.DataFrame([{"native_usa": 0, "native_latin_america": 0, "native_europe": 1, "native_asia":0}])

@pytest.fixture
def input_country_japan_preprocessed():
    return pd.DataFrame([{"native_usa": 0, "native_latin_america": 0, "native_europe": 0, "native_asia":1}])

@pytest.fixture
def input_country_usa_preprocessed():
    return pd.DataFrame([{"native_usa": 1, "native_latin_america": 0, "native_europe": 0, "native_asia":0}])

@pytest.fixture
def input_male():
    return pd.DataFrame([{"sex": "Male", "marital_status":""}])

@pytest.fixture
def input_female():
    return pd.DataFrame([{"sex": "Female", "marital_status":""}])

@pytest.fixture
def input_male_preprocessed():
    return pd.DataFrame([{"is_male": 1}])

@pytest.fixture
def input_female_preprocessed():
    return pd.DataFrame([{"is_male": 0}])

@pytest.fixture
def input_married():
    return pd.DataFrame([{"sex": "", "marital_status":"Married-civ-spouse"}])

@pytest.fixture
def input_not_married():
    return pd.DataFrame([{"sex": "", "marital_status":"Separated"}])

@pytest.fixture
def input_married_preprocessed():
    return pd.DataFrame([{"is_married": 1}])

@pytest.fixture
def input_not_married_preprocessed():
    return pd.DataFrame([{"is_married": 0}])

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client
