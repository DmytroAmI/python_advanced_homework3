from xml.etree import ElementTree as ET

tree = ET.parse('data.xml')
root = tree.getroot()

for user_data in root:
    print('PK:', user_data.attrib.get('pk'))
    print(user_data.find('first_name').text)
    print(user_data.find('last_name').text)
    print(user_data.find('age').text)
    print(user_data.find('mail').text)

print()

for user_data in root:
    print('PK:', user_data.attrib.get('pk'))
    for child in user_data:
        print('{}: {}'.format(child.tag, child.text))

print()

first_names = root.findall('./user/first_name')
last_names = root.findall('./user/last_name')
ages = root.findall('./user/age')
emails = root.findall('./user/mail')

for data_users in zip(first_names, last_names, ages, emails):
    data_dict = {data.tag: data.text for data in data_users}
    print(data_dict)

print()

first_name1 = root.find('./user/age/..[@pk][1]/first_name').text
print(first_name1)
first_name2 = root.find('./user/age/..[@pk][2]/first_name').text
print(first_name2)
first_name3 = root.find('./user/age/..[@pk][3]/first_name').text
print(first_name3)
