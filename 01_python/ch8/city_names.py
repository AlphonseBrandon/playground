'''
Author: Alphonse Brandon
Date Created: 09-07-2023
Subject: Ch6 - Working python functions
'''

def city_country(city: str, country: str) -> str:
    '''Print neatly formated pair of city, country'''
    pair = print(f'{city.title()}, {country.title()}')
    return pair

city_country('Buea', 'Cameroon')
city_country('madrid', 'spain')
city_country('texas', 'united states of america')