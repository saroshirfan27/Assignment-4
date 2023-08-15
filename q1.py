def calculator():
    choice = 0
    while choice < 1 or choice > 4:
        print("\n\nSelect any one ( 1 - 4 )")
        print("1. Addition\t\t\t\t2. Subtraction\n3. Multiplication\t\t4.Division")
        choice = int(input("\n\nEnter:"))
        
    operand1 = float(input("\nEnter operand 1 : "))
    operand2 = float(input("\nEnter operand 2 : "))
    if( choice == 1 ):
        res = add(operand1, operand2)
        print(str(operand1) + " + " + str(operand2) + " = " + str(res))
    elif( choice == 2 ):
        res = sub(operand1, operand2)
        print(str(operand1) + " - " + str(operand2) + " = " + str(res))
    elif( choice == 3 ):
        res = mul(operand1, operand2)
        print(str(operand1) + " * " + str(operand2) + " = " + str(res))
    else:
        res = div(operand1, operand2)
        print(str(operand1) + " / " + str(operand2) + " = " + str(res))
        
calculator()
