# scores
student_scores= {
    "HARSH": 81,
    "HARSHU": 91,
    "HARSHIT": 69,
    "HARSHITA": 88,
    "HARSHIMA": 72,
}

student_grades={}

for key in student_scores:
    if student_scores[key]>90:
        student_grades[key] = "Outstading"
    elif student_scores[key]>80:
        student_grades[key] = "Exceeds Expectation"
    elif student_scores[key]>70:
        student_grades[key] = "Acceptable"
    else:
        student_grades[key]="Fail"

for key in student_grades:
    print(str(key) +" : " +str(student_grades[key]))