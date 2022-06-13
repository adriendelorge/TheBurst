from fastapi import FastAPI
import os
from google.oauth2 import service_account
from google.cloud import bigquery

app = FastAPI()

# define a root `/` endpoint
@app.get("/")


def get_three_cities(employees,budget,dist_airplane,dist_train,quality,subsidies):
    #connection to database
    pathjson="/Users/Tomas/Desktop/KEYS/the-burst-b6d61e428faa.json"
    CREDENTIAL_KEY = os.getenv('CREDENTIAL_KEY')
    credentials = service_account.Credentials.from_service_account_file(pathjson)
    client = bigquery.Client(credentials=credentials, project=credentials.project_id)
    query1=f"""SELECT * FROM `the-burst.database_cities.testfrenchcities` WHERE Distance_x < {dist_airplane}
    AND Distance_y < {dist_train}"""
    query_job = client.query(query1)
    results = query_job.result()
    df=results.to_dataframe()
    if subsidies == 'Yes':
        df=df[df['statut']==1]
    df['scorelifelevel']= df['lifelevelscore']
    if quality == 'high':
        df['weightedscorelifelevel']= df['scorelifelevel']
    if quality == 'medium':
        df['weightedscorelifelevel'] = df['scorelifelevel']*df['scorelifelevel']
    if quality == 'low' :
        df['weightedscorelifelevel'] = df['scorelifelevel']*df['scorelifelevel']*df['scorelifelevel']
    df=df[df['lifelevelscore']!=0]
    df=df.sort_values(by='weightedscorelifelevel',ascending=False)
    df=df.head(3)
    for i in range(len(df)):
        df['coordinates'].iloc[i]=tuple(str(df['coordinates'].iloc[i]).replace('(','').replace(')','').split(","))
    dit = df.to_dict(orient='list')
    return dit

get_three_cities(100,300000,100,40,'high','Yes')
# /predict?employees=100&budget=300000&dist_airplane=100&dist_train=40&quality=high&subsidies=Yes
