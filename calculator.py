def cal():
    print("enter number")
    num1 = list(input())
    print("enter operator:")
    op = input()
    print("enter number 2:")
    num2 = int(input())
    if op == "+":
        print("your sum is:", num1+num2)
    elif op == "-":
        print("your substraction is ", num1-num2)
    elif op == "*":
        print("your product is: ", num1*num2)
    elif op == "/":
        print("your division is: ",num1/num2)
    again()
def again():
    print("want again?")
    choic = input()
    if (choic == "1"):
        cal()
cal()
