import requests
import pymongo

def collect():
    # These code snippets use an open-source library. http://unirest.io/python
    response = requests.get("https://newsrain-petrol-diesel-prices-india-v1.p.mashape.com/capitals/history",
                           headers={
                               "X-Mashape-Key": "6doJchD6BsmshvPoZEwpowzZ8Rtep1xQLFRjsnopSWmfSXAed8",
                               "Accept": "application/json"
                           }
                           )

    return response.json()


response_data_dict = collect()
response_date = response_data_dict["date"]

client = pymongo.MongoClient()

db = client.ml_fuel;
data = db['monthly_data']

cursor = data.find({'date':response_date})

if cursor.count()==0:
    #If data of response not already present
    data.insert_one(response_data_dict)
    print("Done...recorded raw data")

    proc_data_petrol = db['processed_data_petrol']
    proc_data_diesel = db['processed_data_diesel']

    labels_list = response_data_dict['history']['labels']
    dataset_petrol_list = response_data_dict['history']['datasets'][0]["data"]
    dataset_diesel_list = response_data_dict['history']['datasets'][1]["data"]

    dict_petrol = {'obtained_on':response_date}
    dict_diesel = {'obtained_on':response_date}

    for label,data in zip(labels_list,dataset_petrol_list):
        dict_petrol[label]=float(data)

    for label,data in zip(labels_list,dataset_diesel_list):
        dict_diesel[label]=float(data)

    proc_data_petrol.insert_one(dict_petrol)
    proc_data_diesel.insert_one(dict_diesel)

    #City wise extraction

    db_city_wise = db['city_wise_price']

    cities_list_of_objects = response_data_dict['cities']

    for object in cities_list_of_objects:
        db_city_wise.insert_one(object)

    print("Processed.....")

else:
    print("Data Up to Date........")