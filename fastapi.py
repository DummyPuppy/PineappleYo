import numpy as np
import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

#defign a class to store plan data
class Plan(BaseModel):
    plan_id: int
    plan_name: str
    plan_detail: List
    plan_type: str
    shared: bool
    status: str
#define a class to store daily schedule data
class DailySchedule(BaseModel):
    date: str
    day: int
    company: List
    schedule: List

#defin a class to store user data
class User(BaseModel):
    user_id: int
    user_name: str
    user_email: str
    user_password: str
    user_vocation: str

app = FastAPI()
day1 = {'Date': '12-19-2022',
'Day': 1,
'Company':[user1,user2],
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
plan_list = {plan1,plan2, plan3}

@app.get("/plans/{plan_id}")
def get_plan_data():
    #get the plan data from database
    for plan in plan_list:
            if plan_id == plan['plan_id']:
                return plan1
                
    return 'plan not found'


@app.post("/plans/")
def create_plan_data():
    #create a new plan
    plan3 = {'plan_id': 124,
'Plan name': 'chicago',}