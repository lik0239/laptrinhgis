import csv
from mapapp.models import Hospital

def run():
    with open('mapapp/data/hospitals_hcm.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            Hospital.objects.create(
                name=row['name'],
                latitude=float(row['lat']),
                longitude=float(row['lng']),
                address=row['address'],
                image_url=row['image_url']
            )
