import requests
import json

days = 7
limit = 1

url = f"https://eonet.gsfc.nasa.gov/api/v3/events/geojson?limit={limit}&days={days}"

d = requests.get(url).json()

titles = [each["properties"]["title"] for each in d["features"]]
filter(lambda x: not x.startswith("Iceberg"), titles)

for each in d["features"]:
    print()
