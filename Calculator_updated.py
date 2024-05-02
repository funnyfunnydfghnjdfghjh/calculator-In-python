#variables for the symbols
multiply = '*'
subtract = '-'
add = '+'
divide = '/'
x = input("Enter a number: ")
sign = input
y = input("Enter a number: ")
input = input("Enter a sign: ")
z = float(x), float(y)

if input == add:
  z = float(x) + float(y)
elif input == subtract:
  z = float(x) - float(y)
elif input == multiply:
  z = float(x) * float(y)
elif input == divide:
  z = float(x) / float(y)
else:
  print("No valid token seen")
print(z)
