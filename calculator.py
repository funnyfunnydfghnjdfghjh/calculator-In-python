multiply = '*'
subtract = '-'
add = '+'
divide = '/'
x = input("Enter a number: ")
sign = input
y = input("Enter a number: ")
input = input("Enter a sign: ")
z = int(x), int(y)

if input == add:
  z = int(x) + int(y)
elif input == subtract:
  z = int(x) - int(y)
elif input == multiply:
  z = int(x) * int(y)
elif input == divide:
  z = int(x) / int(y)
else:
  print("No valid token seen")
print(z)
