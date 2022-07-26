#!/usr/bin/python3

emailPrompt = input("What is your email (Use 'first.middle.last@domian.com' format): ")

first = emailPrompt.split(".")[0]
first = first.capitalize()

domain = emailPrompt.split("@")[-1]

print("Good afternoon {}, welcome to {}".format (first,domain))

#!/usr/bin/python3

usernumber = input("Enter a Number: ")

usernumber = int(usernumber)

if usernumber < 50:
    print ("Number is less than fifty")

elif usernumber <= 100:
    print ("Number is greater than fifty and is less than 101")

else:
    print ("Number is greater than 100")
