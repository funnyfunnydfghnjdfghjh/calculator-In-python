#variables for the symbols
multiply = '*'
subtract = '-'
add = '+'
divide = '/'
#Inputs
x = input("Enter your first number: ")
sign = input
y = input("Enter your second number: ")
c = input("Enter your third number: ")
input = input("Enter a sign: ")
z = float(x), float(y), float(c)

#checking for the signs
if input == add:
  z = float(x) + float(y) + float(c)
elif input == subtract:
  z = float(x) - float(y) - float(c)
elif input == multiply:
  z = float(x) * float(y) * float(c)
elif input == divide:
  z = float(x) / float(y) / float(c)
else:
  print("No valid token seen")
print(z)
