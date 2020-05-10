list1 = [10, 20, 4, 45, 99,99,45,46]
new_list = set(list1) 
new_list.remove(max(new_list)) 
print(max(new_list)) 