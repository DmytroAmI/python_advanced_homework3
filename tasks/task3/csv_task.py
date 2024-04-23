import csv


class CustomDialect(csv.Dialect):
    """Create a custom dialect"""
    quoting = csv.QUOTE_ALL
    quotechar = "|"
    delimiter = "-"
    lineterminator = '\n'


csv.register_dialect('my_dialect', CustomDialect)

with open('data.csv', 'w') as f:
    writer = csv.DictWriter(
        f,
        fieldnames=['first_name', 'last_name', 'age', 'mail'],
        dialect='my_dialect'
    )

    writer.writeheader()
    writer.writerow({
        'first_name': 'Marie',
        'last_name': 'Smith',
        'age': 18,
        'mail': 'ms@gmail.com'
    })
    writer.writerow({
        'first_name': 'Alex',
        'last_name': 'Smith',
        'age': 22,
        'mail': 'as@gmail.com'
    })
    writer.writerow({
        'first_name': 'Max',
        'last_name': 'Smith',
        'age': 27,
        'mail': 'MS@gmail.com'
    })

with open('data.csv', 'r') as f:
    reader = csv.DictReader(f, dialect='my_dialect')
    for row in reader:
        print(row)
