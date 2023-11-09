'''
Created on Nov 9, 2023

@author: jer21551
'''
def intro():
    print("This program creates polynomials and evaluates them.\n")
    global x, z, sums, sumList, i, poly, coeff, coeffList

def polyCode():
    coeffList = []
    i = 0
    poly = int(input("Please enter the degree of the polynomial you would like: "))
    while (i != (poly + 1)):
        coeff = int(input(f"Enter coefficient for degree [{i}]: "))
        coeffList.append(coeff)
        i += 1
    print(coeffList)
    coeffList.reverse()
    z = 0
    sumList = []
    x = int(input("What value of x would you like to use to evaluate the polynomial? "))
    while (z != (poly + 1)):
        i -= 1
        sums = (coeffList[z] * (x ** i))
        sumList.append(sums)
        z += 1
    finalSum = format((sum(sumList)), ',')
    print(f"Sum of polynomial is {finalSum}")

intro()
while True:
    polyCode()
    while True:
        print(f"\nWould you like to evaluate another polynomial?")
        userInput = input(f"Enter [Y] for yes, [N] for no. ")
        if userInput in ('y', 'n'):
            break
        print("Invalid input. Please enter [Y] or [N] and try again.")
    if userInput == 'y':
        continue
    else:
        print("\nThank you for playing. See you next time!")
        break
