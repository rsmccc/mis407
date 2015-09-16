import csv

with open('myData.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        print(row)
        print(row[0])
        print(row[0],row[1],row[2],)

# output:
# ['1/2/2014', '15', '8', 'red', '11.99']
# 1/2/2014
# 1/2/2014 15 8
# ['1/3/2014', '5', '2', 'green', '10.99']
# 1/3/2014
# 1/3/2014 5 2
# ['1/4/2014', '9', '1', 'blue', '10.99']
# 1/4/2014
# 1/4/2014 9 1
# ['1/5/2014', '15', '10', 'yellow', '11.99']
# 1/5/2014
# 1/5/2014 15 10
