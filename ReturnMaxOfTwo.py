#define a function max() that takes two numbers as arguments and returns the largest of them.
#use the if-then-else construct available in python.
#(it is true that python has the max() function built in,
#but writing it yourself is nevertheless a good exercise.)


def maxOfTwo(numberA, numberB):
    if int(numberA)>int(numberB):
        result = print ((numberA) + " is greater than " + (numberB))
    elif int(numberA)==int(numberB):
        result = print ((numberA) + " equals " + (numberB))
    else:    
        result = print ((numberB) + " is greater than " + (numberA))
    return

numberA = input("Write the first number ")
numberB = input("Write the second number ")

maxOfTwo (numberA , numberB)