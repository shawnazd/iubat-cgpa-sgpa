# SGPA and CGPA calculator

class enhance_char:
    
    BOLD = '\033[1m'
    END_BOLD = '\033[0m'

def create_lists():
    
    sems = []
    credits = []
    sgpa_s = []
    
    return sems, credits, sgpa_s

def take_input():

    sem = int(input("\nEnter the Semester: - "))
    n = int(input("\nEnter number of subjects: - "))

    grade = {
        'S': 10,
        'A': 9,
        'B': 8,
        'C': 7,
        'D': 6,
        'E': 5,
        'F': 0
    }

    print("\nEnter grade and credit for", n, "subjects: - \n")
    print("\tGrade\tPoints\n")
    for i in grade:
        print("\t", i, "\t", grade[i])

    print("\n")

    print("Credits could be ", enhance_char.BOLD + "1/2/3/4" + enhance_char.END_BOLD)

    main = []

    credit = []

    points = []

    print("\n")

    for i in range(n):
        main.append(list(map(int,input("Subject {}: - ".format(i+1)).split(","))))

    print("\n")

    for i in range(len(main)):
        credit.append(main[i][0])

    for i in range(len(main)):
        points.append(main[i][1])
    
    tot_credits = 0

    for i in range(len(credit)):
        tot_credits = tot_credits + credit[i]

    sgpa = 0
    ans_1 = 0

    for i in range(len(credit)):
        ans_1 = ans_1 + (credit[i] * points[i])
    
    sgpa = ans_1 / tot_credits
    
    # print(main, "\n", credit, "\n", points, "\n")
    return sem, tot_credits, sgpa, main

sems, credits, sgpa_s = create_lists()

num = int(input("Enter number of semesters: - "))

main = []

for i in range(num):
    
    s, c, sgpa, m = take_input()

    sgpa = round(sgpa, 2)

    sems.append(s)
    credits.append(c)
    sgpa_s.append(sgpa)
    # main.append(m)
    for j in range(len(m)):
        main.append(m[j])

c_credits = []
c_points = []

for i in range(len(main)):
    c_credits.append(main[i][0])

for i in range(len(main)):
    c_points.append(main[i][1])

tot_credits = 0

for i in range(len(c_credits)):
    tot_credits = tot_credits + c_credits[i]

cgpa = 0
ans_2 = 0

for i in range(len(c_credits)):
    ans_2 = ans_2 + (c_credits[i] * c_points[i])

cgpa = ans_2 / tot_credits

semesters = {
    'sems': [],
    'credits': [],
    'sgpa_s': []
}

for i in range(len(sems)):
    semesters['sems'].append(sems[i])
    semesters['credits'].append(credits[i])
    semesters['sgpa_s'].append(sgpa_s[i])

print("\t", "_____________________________________\n")
print("\t", "Semester", "\t", "Credits", "\t", "SGPA")
print("\t", "_____________________________________")
for i in range(num):
    print("\n", "\t  ", semesters.get('sems')[i], "\t\t  ", semesters.get('credits')[i], "\t\t", semesters.get('sgpa_s')[i])
    print("\t", "_____________________________________")

print("\nFinal CGPA - ",cgpa)
print("\nFinal CGPA(rounded off) - ",round(cgpa,2))
