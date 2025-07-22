list1=[1,2,3,4,5]
list2=[4,5,6,7]
for i in list2:
    if i in list1:
        continue
    else:
        list1.append(i)
        
print(list1)
        
