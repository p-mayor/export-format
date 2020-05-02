import csv
import sys

with open(sys.argv[1]) as csv_in, open('output.csv','w', newline='') as csv_out :
    grades = csv.reader(csv_in)
    grades_writer = csv.writer(csv_out, delimiter=',')
    delete_names = ['Test Student','Stanford Rosenthal', 'Randy Cox', '    Points Possible']
    letter_grade = row[-2]
    student_name = row[0]
    for row in grades:
        if len(letter_grade) == 2:
            letter_grade = letter_grade[0]
        if student_name not in delete_names:
            grades_writer.writerow(row)
