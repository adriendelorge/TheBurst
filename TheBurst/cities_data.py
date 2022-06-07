import pandas as pd

def get_cities_data():
    df_cities=pd.read_csv('../raw_data/cities.csv')
    df_cities=df_cities[['code_commune_INSEE','code_postal','latitude','longitude','nom_commune_complet','code_departement','nom_departement','code_region','nom_region']]
    df_cities['coordinates'] = tuple(zip(df_cities.latitude,df_cities.longitude))
    df_cities=df_cities.drop_duplicates()
    df_cities.dropna(subset=['nom_departement'],inplace=True)
    df_cities.reset_index(inplace=True)
    return df_cities
