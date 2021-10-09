import json
import csv

with open('covid_cases.json', 'r') as json_file:
    covid = json.load(json_file)

with open('parse_covid.csv', 'w') as parse_covid:
    file = csv.writer(parse_covid)
    file.writerow(["dateRep", "countriesAndTerritories", "cases", "deaths"])

    for parse in covid['records']:
        file.writerow([parse['dateRep'], parse['countriesAndTerritories'], parse['cases'], parse['deaths']])


