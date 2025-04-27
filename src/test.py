import csv
import random

archivo_csv = 'src/test.csv'

timpo = 0
temperatura = round(random.uniform(20.0, 30.0), 2)

with open(archivo_csv, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Tiempo', 'Temperatura'])
    writer.writerow([timpo, temperatura])
