# Python program to calculate the factorial of an integer

# Takes input from user

num = int(input("Enter a number: "))

# check to ensure no negative values are allowed
while num < 0:
    print(num, " is not a valid number")

    num = int(input("Please enter a positive value : "))
factorial = 1
for i in range(1, num + 1):
    factorial = factorial * i
print('The factorial of ', num, 'is', factorial)


## recursive way of finding the factorial 

def fact(num):
    if num == 0:
        return 1
    else:
        return num * fact(num-1)

print(fact(num))    
