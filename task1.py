print("Program to print star pattern: \n");
for i in range (0, 5): #I loop is used for the number of columns
    for j in range(0, i + 1): #To determine the number of stars in a column, j loop is utilized
        print("* ", end='')
    print("\r")  # we use \r  carriage return instead of \n
for i in range (5, 0, -1):
    for j in range(0, i -1):
        print("* ", end='')
    print("\r")
