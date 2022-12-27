import pandas as pd
import numpy as np



def preprocess_input_data(example: dict) -> pd.DataFrame:
    dataset = pd.DataFrame([example])
    dataset = create_native_location_features(dataset)
    dataset = encode_binary_features(dataset)

    input_colums = ['native_usa', 'native_latin_america', 'native_europe', 'native_asia',
                    'is_male', 'is_married', 'hours_per_week', 'age', 'education_num',
                    'capital_gain', 'capital_loss']
    dataset = dataset[input_colums]
    return dataset

def create_native_location_features(dataset: pd.DataFrame) -> pd.DataFrame:
    latin_american_countries = ['Cuba', 'Jamaica', 'Mexico',
       'Puerto-Rico', 'Honduras', 'Haiti', 
       'El-Salvador', 'Guatemala', 'Nicaragua',
       'Columbia', 'Ecuador', 'Peru', 'Dominican-Republic']

    european_countries = ['England', 'Canada',
        'Germany', 'Italy', 'Poland', 'Portugal', 
        'France', 'Yugoslavia', 'Scotland',
        'Greece', 'Ireland', 'Hungary', 'Holand-Netherlands']

    asian_countries = ['India', 'Iran', 'Philippines', 
        'Cambodia', 'Thailand', 'Laos',
        'Taiwan', 'China', 'Japan', 'Yugoslavia', 'Vietnam', 'Hong']
    
    dataset = (
        dataset.assign(native_usa=lambda _df: (_df['native_country']=='United-States').astype(int),
                        native_latin_america=lambda _df: (_df['native_country'].isin(latin_american_countries)).astype(int),
                        native_europe=lambda _df: (_df['native_country'].isin(european_countries)).astype(int),
                        native_asia=lambda _df: (_df['native_country'].isin(asian_countries)).astype(int))
    )
    return dataset


def encode_binary_features(dataset: pd.DataFrame) -> pd.DataFrame:
    dataset = (
        dataset.assign(is_male=lambda _df: (_df['sex'] == "Male").astype(int),
                        is_married=lambda _df: _df['marital_status'].str.startswith('Married').astype(int))
    )
    return dataset
