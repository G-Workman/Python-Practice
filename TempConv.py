#!/usr/bin/python3

usertemptype = input("What unit of measurement is your temperature ('F' for Fahrenheit or 'C' Celsius)? ")
usertemptype = usertemptype.capitalize()

if (usertemptype == 'F'):
    usertemp = input("What is your degree of temperature in your standard? ")
    usertemp = int(usertemp)
    celsius = ((usertemp - 32) * (5/9))
    print("Your Fahrenheit temperature of {} is {} in Celsuis.".format(usertemp,celsius))
elif (usertemptype == 'C'):
    usertemp = input("What is the temperature in your standard?")
    usertemp = int(usertemp)
    fahrenheit = ((usertemp * 1.8) + 32) 
    print("Your Celsius temperature of {} is {} in Fahrenheit.".format(usertemp,fahrenheit))
else:
    print("Your unit of measurement is not recognized, please try again"                                                                             
