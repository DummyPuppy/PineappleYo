import numpy as np
import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List



app = FastAPI()
day1 = {'Date': '12-19-2022',
'Day': 1,
'Company':[{'name':'Lily', 'id':'001','detail': 'xxx'},
{'name': 'mike', 'id': '003', 'detail': 'yyy'}],
'Schedule':[{'Time': '8-9am', 'event':  'shopping', 'location': '5000 Forbes ave',
'Detail':'wanna buy a watch'},
{'Time': '9 - 10am', 'event':  'shopping', 'location': '4342  Murray ave',
'Detail': 'none'},
{'Time': '3- 4pm', 'event':  'afternoon tea', 'location': '4050 Murray ave',
'Detail': 'www.google.com'}]}
day2 = {'Date': '12-20-2022'}
day3 = {'Date': '12-21-2022'}
plan1 = {
'plan_id': 123,
'Plan name': 'chicago',
'plan_detail': [day1, day2, day3],
'Plan type': 'self-created',
'Shared': False,
'Status': 'active'
}


@app.get("/plans/{plan_id}")
def get_plan_data():
    #get the plan data from database

    return plan1