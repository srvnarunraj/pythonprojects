marks = {"Maths": 85, "English": 95, "Social": 10}
finalmarks = {}


def grading(x):
    if 91 < x < 100:
        return 'A'
    elif 81 < x < 91:
        return 'B'
    else:
        return 'F'


mylist = marks.values()


def marking(mylist):
    subjects = ['Maths', 'English', 'Social']
    grades = []
    mg = []
    for i in mylist:
        grade = grading(i)
        grades.append(grade)

    for sub, marks in zip(subjects, grades):
        finalmarks.update({sub: marks})

    print(finalmarks)
    print(type(finalmarks))

marking(mylist)
