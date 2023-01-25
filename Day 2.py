# venn diagrams
# union and intersection
s1 = {1, 2, 3, 4}
s2 = {5, 6, 7, 8}
print(s1.union(s2))
print(s1.intersection(s2))
print(s1-s2)
print(s2-s1)
print(s2.intersection(s1))


# Conditional Statements
# if, elif, else

# Sample code for "if"
if 7 > 5:
    print("True")
else:
    print("False")


# Code For Even or Odd

a = 20

if a % 2 == 0:
    print("The given number is even")
else:
    print("The given number is odd")

# Prime Number Checking

b = 9
b = b//10
if b % 2 == 0:
    print("Its a Prime number")
else:
    print("Its Not  Prime Number")


# Elif statements

# Syntax for elif

''' if condition 1:
 code 1
 elif condition 2:
 code 2
 elif condition 3:
 code 3
 else:
 code 4 '''

# Sample code for elif
day = int(input("Enter a Number between one and seven:   "))
if day == 1:
    print("It is Monday")
elif day == 2:
    print("It is Tuesday")
elif day == 3:
    print("It is Wednesday")
elif day == 4:
    print("It is Thursday")
elif day == 5:
    print("It is Friday")
elif day == 6:
    print("It is Saturday")
elif day == 7:
    print("It is Sunday")
else:
    print("Enter a valid number")

# Again Run The Code For Entering New Number

'''if 0-20 and its even print weird if not print normal number
   if >30 and its even print normal if not print weird number'''

check = int(input("Enter a number that needed to be checked:   "))
if check > 0 and check < 20:
    if check % 2 == 0:
        print("Weird number")
    else:
        print("Normal Number")
elif check >= 20 and check < 30:
    print("Normal Number")
else:
    if check >= 30 and check % 2 == 0:

        print("It is normal")
    else:
        print("Weird Number")

# sample code 1
capital_city = {"Nepal": "Kathmandu", "Italy": "Rome", "England": "London"}
print(capital_city)

# Sample code 2
capital_city = {"Nepal": "Kathmandu", "England": "London"}
print("Initial Dictionary: ", capital_city)

capital_city["Japan"] = "Tokyo"

print("Updated Dictionary: ", capital_city)

# to print squares
lst = [1,2,3,4]
for i in lst:
    print(i*i)
# Range function
print(list(range(1, 10)))
# range(start, end, stepcount) syntax for range

# example code 2

ele = int(input("Enter a Number: "))
lst = [8, 7, 10, 12, 20, 6, 29]
flag = False
temp = 0
for i in range(len(lst)):
    if ele == lst[i]:
        print(i)
        break
if temp == False:
    print("Element not found please enter a valid number")

# List comprehension
l = [x*x*x for x in range(0,100)]
print(l)

# even numbers
l = [num for num in range(0,100) if num%2 == 0]
print(l)


# Divisible by 7 and 11

a = [seven for seven in range(1, 1000) if seven%7 == 0 and seven%11 == 0]
print(a)
print(len(a))


# While Loops
















