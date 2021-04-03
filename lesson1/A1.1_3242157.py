import datetime

name = input('Ihr Name: ')
year = int(input('Ihr Geburtsjahr: '))
location = input('Ihr Wohnort: ')

age = datetime.date.today().year - year;

print("Hallo mein Name ist {}, ich bin {} Jahre alt und wohne in {}.".format(name, age, location))