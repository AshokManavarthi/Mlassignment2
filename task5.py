def up_low(s): #Used def up_low function.
    u = sum(1 for i in s if i.isupper()) # used for uppercase letter
    l = sum(1 for i in s if i.islower()) #To check lower case we use islower
    print( "No. of Upper case characters : %s,No. of Lower case characters : %s" % (u,l))

up_low("The quick Brow Fox")
