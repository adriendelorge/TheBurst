from TheBurst.cities_data import get_cities_data
from TheBurst.transports import get_airport_data, get_train_data
from TheBurst.map import create_map
from TheBurst.price_sqmeter import sqmeterprice_data
from TheBurst.subsidies import subsidies

#Merge Dataframes
def final_dataframe():
    df=get_cities_data()
    df=df.merge(get_airport_data(),on='code_commune_INSEE',how='left')
    df=df.merge(get_train_data(),on='code_commune_INSEE',how='left')
    df=df.merge(sqmeterprice_data(),on='code_commune_INSEE',how='left')
    df=df.merge(subsidies(),on='code_commune_INSEE',how='left')
    return df

#Queries
def get_three_best_cities():
    pass