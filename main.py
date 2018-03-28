# Assignment 1
# ICS3U
# <Ahmed Abdulwahab>
# March 28, 2018

#celc to farh function.
def CtoF (tempC):
    tempF = (1.8 * tempC) + 32 
    return 'It would be: ~' + str(round(tempF)) + ' degrees Fahrenheit.'

#farh to calc function.
def FtoC (tempF):
    tempC = (0.55556) * (tempF - 32)
    return 'It would be: ~' + str(round(tempC)) + ' degrees Celsius.'


print("[]-------------------------------------------[]")
choice = str(input("Press C to convert from Fahrenheit to Celsius\nPress F to convert from Celsius to Fahrenheit\n"))
#lets user pick between the 2 functions.

if choice == str("F") or choice == str("f"): #added an or statement so it isn't case sensitive   
    temperature = int(input('Enter your temperature in Celsius: '))
    if temperature < -273.15:
        print("Not possible, absolute zero is -273 in Celsius.")
        quit()
    else:
        print(CtoF(temperature))

elif choice == str("C") or choice == str("c"):
    temperature = int(input('Enter your temperature in Fahrenheit: '))
    if temperature < -459.67:
        print("Not possible, absolute zero is -460 in Fahrenheit.")
        quit()
    else:
        print(FtoC(temperature))

else:
    print(":thinking emoji:")
    quit()
#passive aggresive comment if they don't pick an actual choice 
