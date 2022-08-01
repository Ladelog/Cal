def cgpa ():
    cummlative_score = 0
    candidate_grade =  0

    coursesNo = input("Enter number of courses offered:  ")
    print("-----------------------------")
   
   for x in range (coursesNo):
            course1 = input("Enter course code: ")
            score = int(input("Enter course score: "))
            unit = int(input("Enter course unit: "))
            print("-------------------------------")

            cummlative_score += unit *5

            '''grade range (70 -100 =  5points, 60 - 70 = 4points, 50 - 60 = 3points, 40 - 50 = 2points, 40-30= 1point, 30 or lesser = 0point)''' 
            if (score >= 70):
              print("Your grade is 5")
            elif (score < 70 and score >= 60):
                print("Your grade is 4")
            elif (score < 60 and score >= 50):
                print ("Your grade is  3")
            elif (score < 50 and score >= 40):
                print ("Your grade is  2")
            elif (score < 40 and score >= 30):
                print("Your grade is 1")
            else:
                print("Your grade is 0")
                cgpa = float(candidate_grade/cummlative_score*5 )
                print("Your cgpa is: " +str(cgpa))
                cgpa()