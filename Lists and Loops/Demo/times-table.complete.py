# Assign printTable the value True
printTable = True
# While printTable is True
while printTable:
    # Assign table NoneType value
    table = None
    # While table is not a number
    while not type(table) == int:    
        # Use try-except to ask what times table to print
        try:
            table = int(input("What number do you want a times table for? "))
            break
        except ValueError:
            print("Please enter a whole number.")

    # For num in range(0,13)
    for num in range(0,13):
        # print "num x table = x*table"
        print(num, "x", table, "=", num*table)

    # ask if they need another times table if not set printTable to False
    multiplyAgain = input("Do you want another times table? Enter n for no. ")

    if multiplyAgain.lower() == "n":
        printTable = False
# print "I hope this times table generator was helpful."
print("I hope this times table generator was helpful.")