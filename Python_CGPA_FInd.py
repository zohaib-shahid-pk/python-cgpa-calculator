semester_no=""
grade=0
orignal_data=0
semester_list=[]



#it is completed with some changes may apply
def Chose_Grade(marks):
    global grade
    mark =marks
    if 85 <= mark <= 100:
        grade="A"
        return grade
    elif 80 <= mark <= 84:
        grade="A-"
        return grade
    elif 75 <= mark <= 79:
        grade="B+"
        return grade
    elif 71 <= mark <= 74:
        grade="B"
        return grade
    elif 68 <= mark <= 70:
        grade="B-"
        return grade
    elif 64 <= mark <= 67:
        grade="C+"
        return grade
    elif 61 <= mark <= 63:
        grade="C"
        return grade
    elif 58 <= mark <= 60:
        grade="C-"
        return grade
    elif 54 <= mark <= 57:
        grade="D+"
        return grade
    elif 50 < mark <= 53:
        grade="D"
        return grade
    elif mark ==50:
        grade="F"
        return grade
    elif mark <50:
        grade="Incomplete subject you need to resubmit your paper"
        return grade
    else:
        print("invalid Number")


def Marks_grade(mark):
    global semester_no
    semester_no=int(mark)
    #we use dictionary for mark and their grade point
    if semester_no>=50:
        grade_dictionary = {
            100: 4.00,
            99: 3.98,
            98: 3.96,
            97: 3.93,
            96: 3.91,
            95: 3.89,
            94: 3.87,
            93: 3.85,
            92: 3.83,
            91: 3.81,
            90: 3.78,
            89: 3.76,
            88: 3.74,
            87: 3.72,
            86: 3.70,
            85: 3.67,
            84: 3.64,
            83: 3.59,
            82: 3.51,
            81: 3.43,
            80: 3.34,
            79: 3.33,
            78: 3.26,
            77: 3.18,
            76: 3.1,
            75: 3.01,
            74: 3,
            73: 2.9,
            72: 2.89,
            71: 2.67,
            70: 2.66,
            69: 2.51,
            68: 2.34,
            67: 2.33,
            66: 2.24,
            65: 2.13,
            64: 2.1,
            63: 2,
            62: 1.84,
            61: 1.67,
            60: 1.66,
            59: 1.51,
            58: 1.31,
            57: 1.30,
            56: 1.21,
            55: 1.11,
            54: 1.00,
            53: 0.01,
            52: 0.77,
            51: 0.44,
            50: 0.10,

        }
        if semester_no in grade_dictionary:

           return  grade_dictionary[semester_no]
        else:
            print("your no is not present")
    elif semester_no < 50:
        print("your are fail ,You need to rearranged the paper ")
    else:
        print("Enter the number which is greater then 50")


def find_semester_gpa():
    global orignal_data
    total_gpa=0
    subject1=1
    subject_gpa_list=[]
    valid_subjects=0
    print("case1")

    while True:
        subject_count =input("Enter number of subjects you want to add: ")
        if subject_count.isdigit():
            subject_count=int(subject_count)
            break
        else:
            print("You need to Enter Number of Subject")

    for i in range(subject_count):
        while True:
            # subject_name = str(input("Enter Your subject name : "))
            subject_name = input("Enter Your subject name : ")
            if subject_name.isalpha():
                break
            else:
                print("Your need to add subject name not number")

        while True:
            subject1 = input(f"Enter marks for subject {i + 1}: ")
            if subject1.isdigit():
                if 100 >= int(subject1) >= 0:
                    break
                else:
                    print("Your need to enter number which is greater then 0 and less then 100 ")
            else:
                print("Your need to enter number not aphabit or word")



        # subject1 = input(f"Enter marks for subject {i + 1}: ")

        gpa = Marks_grade(subject1)
        grade_of_no=Chose_Grade(int(subject1))
        if gpa is not None:
            subject_gpa_list.append((subject_name,gpa ,grade_of_no))
            total_gpa+=gpa
            valid_subjects += 1
        else:
            print(f"Subject name : {subject_name} and Mark : {subject1} is Not added into Gpa calculation due to failing the paper ")
    if valid_subjects==0:
        print("all the subject is fail ")
    else:
        average=total_gpa / subject_count

        for subject_name,gpa,grade_of_no in subject_gpa_list:
            print(subject_name," : ",gpa," : ",grade_of_no)

        orignal_data=round(average,1)
        print( " Your combine subject Gpa is : ", round(average,2))
    return orignal_data




def add_multiple_semester():
    global  semester_list,orignal_data
    if orignal_data == 0:
        print(" Please enter GPA first by pressing 'Y'.")
        return
    else:
        semester_list.append(orignal_data)
        total_semester_result=sum(semester_list)
        total_semester_length=len(semester_list)

        try:
            cgpa = total_semester_result / total_semester_length
            print(semester_list)
            print("Sum of semester result : ", total_semester_result)
            print("your semester is : ", total_semester_length)
            print("your total  CGPA  : ", round(cgpa,3))
        except Exception:
            print("don't worries it well correct soon")


print("You Need to Find Gpa")
while True:
    select = input("Pres Y for yes/N for no result of cgpa R : ").strip().upper()
    if select=='Y':
        find_semester_gpa()
        add_multiple_semester()
    elif select== 'R':
        add_multiple_semester()
    elif select == 'N':
        break
    else:
        print("Your enter Invalid character")















