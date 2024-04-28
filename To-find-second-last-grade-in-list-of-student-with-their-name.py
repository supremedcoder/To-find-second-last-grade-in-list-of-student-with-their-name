if __name__ == '__main__':
    num_students = int(input())
    students = []
    for _ in range(num_students):
        name = input()
        grade = float(input())
        students.append([name, grade])

    grades = [grade for name, grade in students]

    if len(grades) < 2:
        print("There are not enough grades to determine the second last grade.")
    else:
        grades.sort()
        for i in range(0,len(grades)-1):
            if grades[0]==grades[i+1]:
                continue
            else:
                lasgrade = grades[i+1]
                break
        

        second = [name for name, grade in students if grade == lasgrade]

        second.sort()

        for student_name in second:
            print(student_name)
