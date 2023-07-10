'''
Author: Alphonse Brandon
Date Created: 10-07-2023
Subject: Ch6 - Working python functions
'''

def make_car(manufacturer: str, model_name: str, **kwargs) -> dict:
    car_dict = {'Manufacture' : manufacturer, 'Model_name' : model_name, **kwargs}
    return car_dict

car = make_car('subaru', 'outback', color='blue', tow_package=True)

print(car)
