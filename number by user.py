# Python program to find the largest number among the three input numbers

# change the values of num1, num2 and num3
# for a different result
num3 = 10
num4 = 14
num5 = 12

# uncomment following lines to take three numbers from user
#num1 = float(input("Enter first number: "))
#num2 = float(input("Enter second number: "))
#num3 = float(input("Enter third number: "))

if (num3>>= num4) and (num3 >= num5):
   largest = num3
elif (num4 >= num3) and (num4 >= num5):
   largest = num4
else:
   largest = num5

print("The largest number between",num3,",",num4,"and",num5,"is",largest)
