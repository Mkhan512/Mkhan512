
# Operators in Python
#   Arithmatical Operators (+, -, *, /, **, %, //)

# + Adding two numbers, or joining two strings

student_result_Math: int=75
student_result_English: int=85
student_result_Urdu: int=89
Total_Marks: int= student_result_Math + student_result_English + student_result_Urdu
print("Total Markes= ", Total_Marks)

# out Put of addition marks = 249

# joining two strings
string_1: str= "Malik "
string_2: str= "Bilal "
string_3: str= "Ahmed "
print("My Name=",string_1 + string_2 + string_3)

# out Put of addition string = Malik Bilal Ahmed

# - Subtraction of numbers

num_1: int=34
num_2: int= 24
num_3=num_1 - num_2
print("Ans of Subration= ",num_3)

# out Put of subtraction = 10

# * Multiplication of numbers

value_1: int= 8
value_2: float= 3.2
value_3: float= value_1 * value_2
print("Ans of Multiplication= ", value_3)

# out Put of Multiplication = 25.6

# / Division of numbers

a: int= 18
b: int= 2
print("Ans of Division=", a / b)

# out Put of Division = 9

# * Multiplication of numbers

a: int= 3
b: int= 4
c: int= 5
print("Ans of Multiplication is=",a*b*c)

# ** Power of number

a: int= 2
b: int= 4
result= a**b
print("Result of Exponention=", result)

# out Put of ** = 16 

# // floor division

a: int= 15
b: int= 4
result= a // b
print("Result of //= ",result)

# out Put of floor division // = 3

# Example of modulus operator ( % )
a = 13
b = 4

# Using the modulus operator
remainder = a % b

# out Put of % modulus = 1

print(f"The remainder of {a} divided by {b} is=  {remainder}")  


##Create a Calculator that takes two numbers as input
a = int( input("Enter 1st No: "))
b = int( input("Enter 2nd No: "))
input = a , b
print("addition =", a + b)
print("Subtraction =", a - b)
print("multiplecation = ",a * b)
print("devision = ",a / b)
print("modulus = ",a % b)
print("round_val = ",a // b)
print("power of value = ", b ** a)

