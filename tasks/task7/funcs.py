import csv
import json
from dicttoxml import dicttoxml
from xml.dom.minidom import parseString


def create_or_overwrite_csv(filename):
    """Create or overwrite a csv file, data entered by the user."""
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.DictWriter(
            csvfile,
            fieldnames=['first_name', 'last_name', 'birth_date', 'city'],
            quoting=csv.QUOTE_ALL
        )
        writer.writeheader()
        add_data(writer)


def update_csv(filename):
    """Update a csv file data"""
    with open(filename, 'a', newline='') as csvfile:
        writer = csv.DictWriter(
            csvfile,
            fieldnames=['first_name', 'last_name', 'birth_date', 'city'],
            quoting=csv.QUOTE_ALL
        )
        add_data(writer)


def read_csv(filename):
    """Return a csv file data"""
    with open(filename, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        result = []
        for row in reader:
            result.append(row)
        return result


def add_data(writer):
    """User entered the data"""
    while True:
        choice = input("enter data?(y/n): ").lower().strip()
        if choice == 'y':
            writer.writerow({
                'first_name': input("first name: ").strip().title(),
                'last_name': input("last name: ").strip().title(),
                'birth_date': input("birth date: ").strip(),
                'city': input("city: ").strip().title()
            })
        elif choice == 'n':
            break
        else:
            print("invalid input! try again!")


def convert_to_json(filename):
    """Convert a csv file data to json format"""
    return json.dumps(read_csv(filename))


def convert_to_xml(filename):
    """Convert a csv file data to xml format"""
    xml_data = dicttoxml(read_csv(filename), custom_root='people', attr_type=False)
    return parseString(xml_data).toprettyxml()
