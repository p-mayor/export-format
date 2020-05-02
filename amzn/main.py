import csv
import sys

with open(sys.argv[1]) as csv_in, open('output.csv','w', newline='') as csv_out :
    grades = csv.reader(csv_in)
    grades_writer = csv.writer(csv_out, delimiter=',')
    delete_names = ['Test Student','Stanford Rosenthal', 'Randy Cox', '    Points Possible']
    line_count = 0
    for row in grades:
        line_count=line_count+1
        if len(row[-2]) == 2:
            print(row[-2])
            row[-2] = row[-2][0]
            print(row[-2])
        if row[0] not in delete_names:
            grades_writer.writerow(row)
