try:
    value=input("ENter a number")
    num=int(value)
    ok=num/0
    print("That number is square",num*num)
except ValueError:
    print("The value enterd is not anumber")
except ZeroDivisionError:
    print("The number is not divided by 0")