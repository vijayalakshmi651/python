list1=[1,1,2,3,2,4]
j=0
for i in range(len(list1)):
    j=i+1
    while (j<(len(list1))):
        
        if(list1[i]==list1[j]):
            list1.pop(j)
        else:
            j=j+1
    i+=1
print(list1)
