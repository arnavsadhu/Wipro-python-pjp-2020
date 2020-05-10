list1 = ['physics', 'chemistry','maths','bio','physics']
print(list1)

x=input('enter item to be removed:')
for z in list1:
  if x in list1:
    list1.remove(x)
    break

print(list1)