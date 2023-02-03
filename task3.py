x = [23, "Python", 23.98]  # x contains all datatypes
dtypes = []  # dtypes created to store data type elements

for item in x:
    dtypes.append(type(item))  # Here type function is used for to append dtypes list

print(x)
print(dtypes)