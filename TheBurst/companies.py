import csv
import requests
import pandas as pd
import numpy as np
import xlrd
from google.colab import drive

def sectors():

    drive.mount ('/content/drive') #import data
    df = pd.read_excel('/content/drive/My Drive/Colab Notebooks/raw_data/demo_ent_sect.xlsx', header = 4)

    array = df['codgeo'].unique() #extract the unique city codes
    codgeo = array.tolist() #tolist

    allsectors = []
    for x in codgeo: #create an array with code city + 5 first sectors per city
        example = df[df['codgeo']==x].sort_values(by='ent_tot', ascending = False).reset_index().drop(columns = 'index')
        sectors = example.iloc[1:6]['service']
        sectors = sectors.tolist()
        sectors.insert(0,x)
        allsectors.append(sectors)

    dff = pd.DataFrame(allsectors) #convert array to DF
    dff.columns = ['code_commune_INSEE','s1','s2','s3','s4','s5']

    return dff
