import csv
import sys

with open(sys.argv[1]) as csv_in, open('output.csv','w', newline='') as csv_out :
    grades = csv.reader(csv_in)
    grades_writer = csv.writer(csv_out, delimiter=',')
    delete_names = ['Test Student','    Points Possible']
    for row in grades:
        letter_grade_field = row[-2]
        student_name_field = row[0]
        if len(letter_grade_field) == 2:
            letter_grade_field = letter_grade_field[0]
        if student_name_field not in delete_names:
            grades_writer.writerow(row)
