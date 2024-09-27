from pymongo.mongo_client import MongoClient
import pandas as pd
import json 

uri="mongodb+srv://suhas:50456@cluster0.dttdp.mongodb.net/?retryWrites=true&w=majority"

# create a new client and connect to database
client = MongoClient(uri)


# create database name and collection name
DATABASE_NAME='pwskills'
COLLECTION_NAME ='waferfault'

df=pd.read_csv(r"E:\sensorproject\notebooks\wafer.csv")

df=df.drop('Unnamed: 0',axis=1)

json_record = list(json.loads(df.T.to_json()).values())

client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)
