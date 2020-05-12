
import csv, json, sys

csvFilePath = sys.argv[1]
jsonFilePath = sys.argv[2]

data = {}
with open(csvFilePath) as csvFile:
    csvReader = csv.DictReader(csvFile)
    for rows in csvReader:
        id_ = rows['id']
        data[id_] = rows
with open(jsonFilePath, 'w') as jsonFile:
    jsonFile.write(json.dumps(data, indent=4))
