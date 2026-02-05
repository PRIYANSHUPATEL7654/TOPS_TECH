file = open("User_data.txt","a")
while True:
    user_text = input("Enter your data and type END at last if you no further wish to enter data : ")
    if user_text == "END":
        break
    file.write(user_text + "\n")