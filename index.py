import pandas as pd
import pathlib
import csv

# define col name
col_names = ['name',
             'gender',
             'city',
             'email',
             'family status']

# define people with all col atribute
people = [
    ['Jackie Chan', 'm', 'Netanya', 'd1@example.org', 'single'],
    ['Bruce Lee', 'm', 'Tel-Aviv', 'B2@example.org', 'single'],
    ['Silvester Stalone', 'm', 'Ariel', 'e3@example.org', 'married'],
    ['James Bond', 'm', 'Kefar Sava', 'e4@example.org', 'married'],
    ['Kill Bill', 'f', 'Raanana', 'e5@example.org', 'in relationships'],
    ['Jason Statam', 'm', 'Raanana', 'e6@example.org', 'in relationships'],
    ['Jean-claude Vandam', 'm', 'Raanana', 'e7@example.org', 'married'],
]
# define name of the file
filename = 'filename.csv'
# introduce pandas i say file are going to contain people data and the name of the col would be what we define
file = pd.DataFrame(people, columns=col_names)
# define file name and encoding type
file.to_csv(filename, encoding="utf-8")
# print to check
print('End of the csv file creation')
# ??
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
