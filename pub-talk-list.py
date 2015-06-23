#To be able to read csv formated files, we will first have to import the
#csv module.

import csv

ifile  = open('dummy_list.csv', "rb")
reader = csv.reader(ifile)

rownum = 0
for row in reader:
    # Save header row.
    if rownum == 0:
        header = row
    else:
        colnum = 0
        for col in row:
            print '%-8s: %s' % (header[colnum], col)
            colnum += 1
            
    rownum += 1

ifile.close()
