import pandas as pd
import pathlib
import csv

col_names = ['name',
             'gender',
             'city',
             'email',
             'family status']

people = [
    ['Jackie Chan', 'm', 'Netanya', 'd1@example.org', 'single'],
    ['Bruce Lee', 'f', 'Tel-Aviv', 'B2@example.org', 'single'],
    ['Jinnie Dillinger', 'f', 'Ariel', 'e3@example.org', 'married'],
    ['James Daw', 'm', 'Kefar Sava', 'e4@example.org', 'married'],
    ['Jane Dough', 'f', 'Raanana', 'e5@example.org', 'in relationships'],
    ['John Doe', 'm', 'Raanana', 'e6@example.org', 'in relationships'],
    ['Jonathan Doe', 'm', 'Raanana', 'e7@example.org', 'married']
]
filename = 'filename.csv'
file = pd.DataFrame(people, columns=col_names)
file.to_csv(filename, encoding="utf-8")
print('End of the csv file creation')
print(f'At {pathlib.Path(__file__).parent.absolute()} / {filename}.')
# =======
#
# read the file
#
# =============

# the most simple file read
print(' -- the most simple file read -- ')
for line in open(filename):
    csv_row = line.split()  # returns a list ["1","50","60"]
    print(csv_row)

print(' -- simple file read -- ')
# simple read
with open(filename) as file:
    lis = [line.split() for line in file]  # create a list of lists
    for i, x in enumerate(lis):  # print the list items
        print(f'line{i} = {x}')
    file.close()

print(' --- file read with csv module --- ')
with open(filename, "rt", encoding='ascii') as infile:
    read = csv.reader(infile)
    for row in read:
        print(f'{row}')

print(' --- file read with Panda module --- ')
# read with Panda
df = pd.read_csv(filename, encoding="utf-8")

print('end')
