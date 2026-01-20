dr_dict = {'Dr. Harmi' : {"10am" : 0,'11am' : 0},
           'Dr. Disha' : {"2pm" : 0,"3pm" : 0,'4pm' : 0}}

no_of_bookings = int(input("Enter how many bookings do you want to do : "))
if no_of_bookings <= 3:
    for i in range(no_of_bookings):
        name = input("Enter name : ")
        m_no = int(input("Enter mobile number : "))
        age = int(input("Enter age : "))

        print(dr_dict.keys())
        pref_dr = input("Enter your preferred doctor from above options : ")
        print("Timings available are : ",dr_dict[pref_dr])
        sel_slot = input("Enter slot : ")
        print(f"Your preferred doctor is {pref_dr}")

        dr_dict[pref_dr][sel_slot]+=1
        print(f"Your appointment is booked with {pref_dr} at {sel_slot}")
        print(dr_dict[pref_dr])

        cancel_app = input("Do you want to cancel any appointment : ")
        cancel_app.lower()
        if(cancel_app == "yes"):
            dr_name = input("Enter doctor name for which you want to cancel appointment : ")
            print(f"Your current appointments with {dr_name} are : ",dr_dict[dr_name])
            dr_time = input("Enter time for which you want to cancel appointment : ")
            if(dr_dict[dr_name][dr_time] != 0):
                dr_dict[dr_name][dr_time] -=1
                print("Appointment cancelled")
                print(dr_dict[dr_name])
            else:
                print(f"There is no booked appointment at {dr_time}")
        else:
            print("Thank you")

        see_app = input("Do you want to see any appointment : ")
        see_app.lower()
        if(see_app == "yes"):
            print(dr_dict[pref_dr])
        else:
            print("Thank you")