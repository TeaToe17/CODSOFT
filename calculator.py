input1 = int(input("input a number! "))
operation = str(input("What operation do you want to perform? e.g +,-,* or / "))
input2 = int(input("input a second number! "))
if operation == "+":
    result = input1 + input2
    print(f"answer: {result}")
elif operation == "-":
    result = input1 - input2
    print(f"answer: {result}")
elif operation == "*":
    result = input1 * input2
    print(f"answer: {result}")
elif operation == "/":
    result = input1 / input2
    print(f"answer: {result}")

    
