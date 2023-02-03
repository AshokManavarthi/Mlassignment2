def unique_list(l):
  y = []
  for a in l:
    if a not in y:
      y.append(a)
  return y

print(unique_list([1,2,3,3,3,3,4,5]))
