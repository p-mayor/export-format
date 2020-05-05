import csv
import sys

with open(sys.argv[1]) as csv_in, open('output.csv','w', newline='') as csv_out :
    grades = csv.reader(csv_in)
    grades_writer = csv.writer(csv_out, delimiter=',')
    delete_names = ['Test Student','Stanford Rosenthal', 'Randy Cox', '    Points Possible']
    line_count = 0
    for row in grades:
        if line_count == 0:
            print(row)
        letter_grade_field = row[-2]
        student_name_field = row[0]
        if len(letter_grade_field) == 2:
            row[-2] = letter_grade_field[0]
        if student_name_field not in delete_names:
            grades_writer.writerow(row)
        line_count+=1