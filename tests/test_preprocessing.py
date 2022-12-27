import sys
import pathlib
from pandas.testing import assert_frame_equal
from pytest import mark
from pytest_lazyfixture import lazy_fixture

root_path = pathlib.Path(__file__).parents[1]
preprocessing_directory = root_path/'deployment'

if str(preprocessing_directory) not in sys.path:
    sys.path.append(str(preprocessing_directory))

from preprocessing import preprocess_input_data
from preprocessing import create_native_location_features
from preprocessing import encode_binary_features


@mark.parametrize(
    "input_json, input_json_preprocessed_expected",
    [(lazy_fixture('input_json_1'), lazy_fixture('input_json_preprocessed_1'))]
)
def test_preprocess_input_data(input_json, input_json_preprocessed_expected):
    input_json_preprocessed = preprocess_input_data(input_json)
    assert_frame_equal(input_json_preprocessed, input_json_preprocessed_expected, 
                        check_dtype=False, check_like=True)


@mark.parametrize(
    "input_country, input_country_preprocessed_expected",
    [(lazy_fixture('input_country_cuba'), lazy_fixture('input_country_cuba_preprocessed')),
     (lazy_fixture('input_country_england'), lazy_fixture('input_country_england_preprocessed')),
     (lazy_fixture('input_country_japan'), lazy_fixture('input_country_japan_preprocessed')),
     (lazy_fixture('input_country_usa'), lazy_fixture('input_country_usa_preprocessed'))]
)
def test_create_native_location_features(input_country, input_country_preprocessed_expected):
    columns = ["native_usa", "native_latin_america", "native_europe", "native_asia"]
    input_country_preprocessed = create_native_location_features(input_country)
    assert_frame_equal(input_country_preprocessed[columns], input_country_preprocessed_expected[columns], 
                        check_dtype=False, check_like=True)


@mark.parametrize(
    "input_sex, input_sex_preprocessed_expected",
    [(lazy_fixture('input_male'), lazy_fixture('input_male_preprocessed')),
     (lazy_fixture('input_female'), lazy_fixture('input_female_preprocessed'))]
)
def test_encode_binary_features_sex(input_sex, input_sex_preprocessed_expected):
    column = ['is_male']
    input_sex_preprocessed = encode_binary_features(input_sex)
    assert_frame_equal(input_sex_preprocessed[column], input_sex_preprocessed_expected[column], 
                        check_dtype=False, check_like=True)


@mark.parametrize(
    "input_marital_status, input_marital_status_preprocessed_expected",
    [(lazy_fixture('input_married'), lazy_fixture('input_married_preprocessed')),
     (lazy_fixture('input_not_married'), lazy_fixture('input_not_married_preprocessed'))]
)
def test_encode_binary_features_marital_status(input_marital_status, input_marital_status_preprocessed_expected):
    column = ['is_married']
    input_marital_status_preprocessed = encode_binary_features(input_marital_status)
    assert_frame_equal(input_marital_status_preprocessed[column], input_marital_status_preprocessed_expected[column], 
                        check_dtype=False, check_like=True)
