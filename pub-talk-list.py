#To be able to read csv formated files, we will first have to import the
#csv module.

import csv
with open('dummy_list.csv', 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
        print row
