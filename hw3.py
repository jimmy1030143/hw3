s = input("Please type anything:\n")

d = {}
for c in s:
  if not c in d:
    d[c] = 1
  else:
   d[c]+=1

for key in d:
  print("'", key, "': ",d[key], sep='')


 