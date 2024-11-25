counter = 0
student_pass = 0
student_fail = 0
for counter in range(0, 15):
    score = int(input("Enter Student's score: "))
    if score > 15:
        student_pass += 1
        print("Pass")
    if score < 15:
        student_fail += 1
        print("Fail")
print("The students that passed: ", student_pass)
print("The students that failed: ", student_fail)
    
