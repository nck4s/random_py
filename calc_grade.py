
test_1 = float(input("First test: "))
test_2 = float(input("Second test: "))
exam_grade = float(input('Exam grade: '))

def calculate_grade(test_1, test_2, exam_grade):
    lab_grade = (test_1 + test_2) / 2
    final_grade = 0.7 * lab_grade + 0.3 * exam_grade

    if lab_grade < 5 or exam_grade < 5:
        print('failed')
    else:
        print(f'Final grade: {final_grade:.2f}')

calculate_grade(test_1, test_2, exam_grade)