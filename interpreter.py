expression = input("Expression: ")

x,y,z = expression.split()

num1 = int(x)
num2 = int(z)

if y == "+":
    sum = float(num1 + num2)
    print(sum)
elif y == "-":
    diff = float(num1 - num2)
    print(diff)
elif y == "*":
    product = float(num1*num2)
    print(product)
elif y == "/":
    quo = float(num1/num2)
    print(quo)
else:
    print("Invalid operation")


