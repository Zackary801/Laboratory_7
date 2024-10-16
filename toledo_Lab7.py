prelim= float(input("Enter prelim grade:"))
midterm= float(input("Enter mid-term grade:"))
finalterm=float(input("Enter final grade:"))



prelim_grade = prelim * (33.33 / 100) 
midterm_grade = midterm * (33.33 / 100) 
final_grade = finalterm * (33.33 / 100)

total = prelim_grade + midterm_grade + final_grade


fg = round(total)
    
if fg >= 99.0 and fg <= 100.0:
        print( "student" , fg)
        print("GPA: 1.00")
        print("Excellent")
elif fg>=96 and fg<=98:
        print("Student's grade:", fg)
        print("GPA: 1.25")
        print("Outstading")
elif fg>=93 and fg<=95:
        print("Student's grade" , fg)
        print("GPA: 1.50")
        print("Superior")
elif fg>=90 and fg<=92:
     print("Student's grade" , fg)
     print("GPA: 2.00")
     print("Very good")
elif fg>=87 and fg<=89:
     print("Student's grade" , fg)
     print("GPA: 2.00")
     print("good")
elif fg>=84 and fg<=86:
     print("Student's grade" , fg)
     print("GPA: 2.25")
     print("satisfactory")
elif fg>=81 and fg<=83:
     print("Student's grade" , fg)
     print("GPA:2.50 ")
     print("fairly satisfactory")
elif fg>=78 and fg<=80:
     print("Student's grade" , fg)
     print("GPA:2.75")
     print("fair")
elif fg>=75 and fg<=77:
     print("Student's grade" , fg)
     print("GPA: 3.00")
     print("passed")
elif fg>=75 and fg<=75:
     print("Student's grade" , fg)
     print("GPA: 5.00")
     print("failed")