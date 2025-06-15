
mapping = {
    'A+': 4,
    'A' : 4,
    'A-':3.7,
    'B+':3.3,
    'B' :3.0,
    'B-':2.7,
    'C+':2.3,
    'C' :2.0,
    'C-':1.7,
    'D+':1.3,
    'D':1.0,
    'F':0
}


def calculate_GPA(credit_hours, grades, ranges, courses_names):
    ## ranges and courses names will be used in a later update
    def dot_product(v1, v2):
        rng = len(v1)
        sum = 0
        for i in range(rng):
            sum+= v1[i] * v2[i]
        return sum
    
    grades_after_mapping = [mapping[grade] for grade in grades]
    grades_times_hours = dot_product(credit_hours, grades_after_mapping)
    total_hours = sum(credit_hours)
    GPA =  grades_times_hours/total_hours
    print(grades_times_hours) # grades*hours
    print(total_hours)
    return GPA



def read_file(file_path='my_grades.txt'):
    file = open(file_path)
    semester = 1
    courses = 0
    ranges = []
    courseName = []
    creditHours = []
    earnedGrade = []
    lines = file.readlines()
    for line in lines:
        if line.startswith("_"):
            semester+=1
            ranges.append(courses)
            courses=0
            continue
        if line.startswith("#"):
            continue
        courses+=1
        line = line.rstrip('\n')
        stuff = line.split(',')
        courseName.append(stuff[0])
        creditHours.append(int(stuff[1]))
        earnedGrade.append(stuff[2])

    file.close()
    return courseName, creditHours, earnedGrade, ranges


courses_names, credit_hours, earned_grade, ranges = read_file()

GPA = calculate_GPA(credit_hours, earned_grade, ranges, courses_names)
# print(ranges)
# print(courses_names)
print(GPA)
