import re
import csv
import datetime
from django.contrib.auth.models import User
from library.models import Plant


def run():
    path = '/usr/src/app/scripts/plants_export.txt'
    with open(path) as file:
        reader = csv.reader(file, delimiter='|')
        next(reader)  # Advance past the header

        owner = User.objects.get(id=2)  # dntx

        for row in reader:
            print(row)

            plant = Plant()
            plant.uid = row[0].strip()
            plant.owner = owner

            if row[14]:
                date_purchase = get_date(row[14])
                if date_purchase:
                    plant.date_purchase = date_purchase,

            if row[13]:
                deta_seeding = get_date(row[13])
                if deta_seeding:
                    plant.deta_seeding = deta_seeding

            if check_cell(row[2]):
                plant.genus = row[2].strip().lower()

            if check_cell(row[3]):
                plant.species = row[3].strip().lower()

            if check_cell(row[4]):
                plant.subspecies = row[4].strip().lower()

            if check_cell(row[5]):
                plant.variety = row[5].strip().lower()

            if check_cell(row[6]):
                plant.cultivar = row[6].strip().lower()

            if check_cell(row[1]):
                plant.field_number = row[1].strip()
            
            if check_cell(row[8]):
                plant.form = row[8].strip().lower()

            if check_cell(row[9]):
                plant.affinity = row[9].strip().lower()

            if check_cell(row[10]):
                plant.ex = row[10].strip()

            if check_cell(row[11]):
                plant.info = row[11].strip()

            if check_cell(row[12]):
                plant.source = row[12].strip()

            if check_cell(row[18]):
                plant.description = row[18].strip()

            plant.save()


def get_date(date_as_str):
    date_purchase = None
    match1 = re.match(r'\d{4}-\d{2}-\d{2}', date_as_str)
    match2 = re.match(r'\d{2}\.\d{2}\.\d{4}', date_as_str)
    if match1:
        date_purchase = datetime.datetime.strptime(date_as_str, '%Y-%m-%d')
    if match2:
        date_purchase = datetime.datetime.strptime(date_as_str, '%d.%m.%Y')
    return date_purchase


def check_cell(cell_content):
    if 'None' in cell_content:
        return False
    if cell_content.strip():
        return True
    else:
        return False


run()

