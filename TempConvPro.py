#!/usr/bin/python3

usertemptype = input("What unit of measurement is your temperature ('F' for Fahrenheit or 'C' Celsius or 'K' for Kelvin) ")
usertemptype = usertemptype.capitalize()

if (usertemptype == 'F'):
    desiredtype = input("What unit do you want to convert to ('F' for Fahrenheit or 'C' Celsius or 'K' for Kelvin) ")
    desiredtype = desiredtype.capitalize()
    if (desiredtype == 'C'):
        usertemp = input("What is your degree of temperature in your standard? ")
        usertemp = float(usertemp)
        celsius = ((usertemp - 32) * (5/9))
        print("Your Fahrenheit temperature of {} is {} in Celsuis.".format(usertemp,celsius))
    elif (desiredtype == 'K'):
        usertemp = input("What is your degree of temperature in your standard? ")
        usertemp = float(usertemp)
        kelvin = ((usertemp - 32) * (5/9) + 273.15)
        print("Your Fahrenheit temperature of {} is {} in Kelvin.".format(usertemp,kelvin))
    elif (desiredtype == 'F'):
        print("Your temperature is already in Farhenheit")
    else:
        print("Your temperature has an error")

elif (usertemptype == 'C'):
    desiredtype = input("What unit do you want to convert to ('F' for Fahrenheit or 'C' Celsius or 'K' for Kelvin) ")
    desiredtype = desiredtype.capitalize()
    if (desiredtype == 'F'):
        usertemp = input("What is the temperature in your standard? ")
        usertemp = float(usertemp)
        fahrenheit = ((usertemp * 1.8) + 32) 
        print("Your Celsius temperature of {} is {} in Fahrenheit.".format(usertemp,fahrenheit))
    elif (desiredtype == 'K'):
        usertemp = input("What is your degree of temperature in your standard? ")
        usertemp = float(usertemp)
        kelvin = (usertemp + 273.15)
        print("Your Celsius temperature of {} is {} in Kelvin.".format(usertemp,kelvin))
    elif (desiredtype == 'C'):
        print("Your temperature is already in Celsius")

elif (usertemptype == 'K'):
    desiredtype = input("What unit do you want to convert to ('F' for Fahrenheit or 'C' Celsius or 'K' for Kelvin) ")
    desiredtype = desiredtype.capitalize()
    if (desiredtype == 'C'):
        usertemp = input("What is your degree of temperature in your standard? ")
        usertemp = float(usertemp)
        celsius = (usertemp - 273.15)
        print("Your Kelvin temperature of {} is {} in Celsius.".format(usertemp,celsius))
    elif (desiredtype == 'F'):
        usertemp = input("What is your degree of temperature in your standard? ")
        usertemp = float(usertemp)
        farhenheit = ((usertemp - 273.15) * (9/5) + 32) 
        print("Your Kelvin temperature of {} is {} in Farhenheit.".format(usertemp,farhenheit))
    elif (desiredtype == 'K'):
        print("Your temperature is already in Kelvin")
    else:
        print("Your temperature has an error")

else:
    print("Your unit of measurement is not recognized, please try again")
