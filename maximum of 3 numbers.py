def max_of_three(a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c

num1 = int(input("enter first number"))
num2 = int(input("enter second number"))
num3 = int(input("enter third number"))
sum = max_of_three(num1, num2, num3)
print("the greatest number is",sum)