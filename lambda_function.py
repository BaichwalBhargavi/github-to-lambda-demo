import json
import pandas as pd
import requests


def lambda_handler(event, context):
    print("Event_data-> ", event)
    response = requests.get("https://www.google.com")
    print(response.text)

    d = {'Name': ['Bhargavi', 'Ankita'], 'Surname': ['Baichwal', 'Sonawane']}
    df= pd.DataFrame(data=d)
    print(df)
    print("Done with git to lambda testing !!!")