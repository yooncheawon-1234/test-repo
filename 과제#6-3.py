김민수 = {'name':'김민수',
        'assignment':[80,50,40,20],
        'test':[75, 75],
        'lab':[78.20, 77.20]
        }

이민아 = {'name':'이민아',
        'assignment':[82, 56, 44, 30],
        'test':[83,95],
        'lab':[67.90, 78.72]
        } 

배철수 = {'name':'배철수',
        'assignment' : [77,82, 23,39],
        'test': [78,77],
        'lab' : [80, 80]
        } 

def get_average(marks):
    total_sum = sum(marks)
    total_sum = float(total_sum)
    return total_sum / len(marks)

def calculate_total_average(students):
    assignment = get_average(students['assignment'])
    test = get_average(students['test'])
    lab=get_average(students['lab'])
    return (0.1 * assignment + 0.7*test + 0.2 *lab)

def assign_letter_grade(score):
    if score >= 90: return 'A'
    elif score >= 80: return 'B'
    elif score >= 70: return 'C'
    elif score >= 60: return 'D'
    else : return 'F'

def class_average_is(student_list):
    print('students 리스트를 출력합니다 - 딕셔너리들의 리스트에 주목!')
    print(student_list)
    print()
    result_list = []
    for student in student_list:
        stud_avg = calculate_total_average(student)
        result_list.append(stud_avg)
    return get_average(result_list)

students=[김민수, 이민아, 배철수]

for i in students :
    print(i['name'])
    print('=+=+=+=+=+=+=+=+=+=+=+=+=+=+')
    print('%s의 총점 = %0.2f' %(i['name'], calculate_total_average(i))) 
    print('%s의 grade = %s' %(i['name'],
    assign_letter_grade(calculate_total_average(i))))

    print()

class_av = class_average_is(students)
print('반 전체 평균 점수 = %0.2f' %(class_av))
print('반 전체 평균 grade = %s' %(assign_letter_grade(class_av)))