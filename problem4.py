x = range(100,1000)

y= []
for z in x:
  for a in x:
    y.append(a*z)

a = [ i for i in y if str(i) == str(i)[-1::-1]]
print max(a)
