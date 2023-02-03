def unique_list(l): #used function uniquelist
  y = []
  for a in l: #using a for loop to traverse the given input list
    if a not in y: #not in used to find unique list
      y.append(a)
  return y

print(unique_list([1,2,3,3,3,3,4,5])) #function is called as given in task
