import csv

a = [['One call away', '2015'], ['All star', '1999'], ['Let me down slowly', '2018'],
     ['Somebody that i used to know', '2011'], ["My father's son", '1999'], ['Shape of my heart', '1993'],
     ['Way down we go', '2015']]

with open('BTS_ONE_LOVE.csv', 'w', newline='') as csvfile:
    fieldnames = ['Song', 'Year']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for i in a:
        writer.writerow({'Song': i[0],
                        'Year': i[1]})


with open('BTS_ONE_LOVE.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for heading in reader.fieldnames:
        print(heading, end=' ')
    print('\n------------------------------')
    for row in reader:
        print(row['Song'],',', row['Year'])
