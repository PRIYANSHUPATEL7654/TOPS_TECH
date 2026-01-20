# Menu driven program
# 1. Add data of student
# 2. search student
# 3. delete student
# 4. view all the student
# 5. exit

student_data = {"a@gmail.com" : ["A",20,1122334455,120],
                "b@gmail.com" : ["B",21,5544332211,150],
                "c@yahoo.com" : ["C",24,1234512345,180]}

while True:
    
    choice = int(input("1. Add data of student\n2. search student\n3. delete student\n4. view all the student\n5. exit\nEnter your choice from above options : "))
    match choice:
        case 1:
            key = input("Enter Email Address : ")
            value1 = input("Enter name : ")
            value2 = int(input("Enter age : "))
            value3 = int(input("Enter phone number : "))
            value4 = int(input("Enter marks : "))
            student_data[key] = [value1,value2,value3,value4]
        case 2:
            search_stud = input("Enter the email address of student you want to search for : ")
            for i,j in student_data.items():
                if search_stud == i:
                    for k in j:
                        print(k)
                    break
            else:
                print(f"{search_stud} not found")
        case 3:
            del_stud = input("Enter the email address of student you want to delete : ")
            del student_data[del_stud]
        case 4:
            print(student_data)
        case 5:
            break
        case _ :
            print("Invalid Choice")