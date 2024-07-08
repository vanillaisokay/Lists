'''
Created on Nov 8, 2023

@author: jer21551
'''
import math
def createList():
    import random
    global listSize, list, i
    list = []
    listSize = int(input("\nHow large is your list? "))
    i = 0
    while (i != listSize):
        variable = random.randint(0,100)
        list.append(variable)
        i += 1

def calcStandDev():
    global listAvg, sortList, x, devList, var, standDev
    devList = []
    x = 0
    listAvg = (sum(list) / i)
    while (x != listSize):
        newVar = (list[x] - listAvg) ** 2
        devList.append(newVar)
        x += 1

def printList():
    print(list)
    global maxNum, minNum, array_sum, standDev
    maxNum = max(list)
    minNum = min(list)
    array_sum = sum(list)
    listAvg = (sum(list) / i)
    calcStandDev()
    standDev = (math.sqrt(sum(devList) / 5))
    print(f"The maximum number in the list is {maxNum}")
    print(f"The minimum number in the list is {minNum}")
    print(f"The sum of the array is {array_sum}")
    print(f"The average is {listAvg}")
    print(f"Standard deviation is {standDev}")

while True:
    createList()
    printList()
    while True:
        print(f"\nWould you like to create another list?")
        userInput = input(f"Enter [Y] for yes, [N] for no.\n")
        if userInput in ('y', 'n'):
            break
        print("Invalid input. Please enter [Y] or [N] and try again.")
    if userInput == 'y':
        continue
    else:
        print("\nThank you for playing. See you next time!")
        break
