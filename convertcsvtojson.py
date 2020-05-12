import os
import json
import csv

# Enter your data directory here
data_dir = "./fiona_data"

# Prepares data dictionary to include:
'''text, intent, entities
    entities is a list that includes dictionaries of:
        {start: int, end: int, value: str, entity: str}
    E.g:
        {
        "text": "i'm looking for a place in the north of town",
        "intent": "restaurant_search",
        "entities": [
          {
            "start": 31,
            "end": 36,
            "value": "north",
            "entity": "location"
          }
        ]
      },'''


def open_csv():
    # Open CSV file and create or add data into JSON file

    infile = input("Please enter your input file name (.csv): ")
    outfile = input("Please enter your output file name (.json): ")

    data_output = create_load_outfile(outfile)

    intents = []

    with open(os.path.join(data_dir, infile), "r+") as f:
        reader = csv.reader(f, delimiter=",", quotechar='"')
        for i, row in enumerate(reader):
            text, intent, *entities = row

            entity_list = []

            intents.append(intent)

            for entity in entities:
                start, end, value, entity_type = entity.split(",")
                entity_list.append(
                    {
                        "start": int(start),
                        "end": int(end),
                        "value": value,
                        "entity": entity_type
                    })

            data_output['rasa_nlu_data']['common_examples'].append(
                {'text': text, 'intent': intent, 'entities': entity_list})

    save_json_file(outfile, data_output)


def create_load_outfile(outfile):
    # type: () -> object

    if os.path.isfile(os.path.join(data_dir, outfile)):
        add_to_file = input("It looks like this file already exists. Would you like to add to it? (y/n)")

        if add_to_file == "y":
            with open(os.path.join(data_dir, outfile)) as json_data:
                return json.load(json_data)

    else:
        return {"rasa_nlu_data": {"common_examples": []}}


def save_json_file(outfile, data_output):
    # Save dictionary to rasa nlu JSON format
    with open(os.path.join(data_dir, outfile), 'w+') as f:
        json.dump(data_output, f, ensure_ascii=False, indent=4)


if __name__ == "__main__":
   # input_type = input("Would you like to import from a csv or enter text manually? (csv OR text) ")

    #if input_type == "csv":
        open_csv()
   # else:
       # enter_text()
