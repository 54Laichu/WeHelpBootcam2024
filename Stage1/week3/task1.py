import csv
import urllib.request
import json

def fetch_data(url):
    with urllib.request.urlopen(url) as response:
        data = json.loads(response.read().decode())
        results = data["data"]["results"].__str__()
    return results


task1 = open('taipei-attractions-assignment-1.csv', 'w', newline='')
task1.write(fetch_data("https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment-1"))

