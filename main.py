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



while True:
    print()
    print("[]-------------------------------------------[]")
    choice = str(input("Press [C] to convert from Fahrenheit to Celsius\nPress [F] to convert from Celsius to Fahrenheit\n>>> "))
    #lets user pick between the 2 functions.

    if choice == str("F") or choice == str("f"): #added an or statement so it isn't case sensitive   
        temperature = int(input('Enter your temperature in Celsius:\n>>> '))
        
        if temperature < -273.15:
            print("Not possible, absolute zero is -273 in Celsius.")
            if int(input("Enter 1 to try another conversion\n>>> ")) == 1:
                continue
            else:
                break  
        else:
            print(CtoF(temperature))
            if int(input("Enter 1 to try another conversion\n>>> ")) == 1:
                continue
            else:
                break
              
    elif choice == str("C") or choice == str("c"):
           while True:   
                  temperature = int(input('Enter your temperature in Fahrenheit:\n>>> '))
                  if temperature < -459.67:
                         print("Not possible, absolute zero is -460 in Fahrenheit.")
                         continue
                  else:
                    print(FtoC(temperature))
                    print()
                    if int(input("Enter 1 to try another Fahrenheit conversion\nPress 2 to do a different conversion\n>>> ")) == 1:
                            continue
                    elif input() == 2:
                            break
                    
            
    else:
        print("why")
        continue
    #passive aggresive comment if they don't pick an actual choice 
