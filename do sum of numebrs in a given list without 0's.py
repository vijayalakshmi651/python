numbers=[3, 4, 6, 2, 0, 0, 0, 0, 0, 0, 6, 7, 6, 9, 10, 0, 0, 0, 0, 0, 7, 4, 4, 0, 0, 0, 0, 0, 0, 5, 3, 2, 9, 7, 1, 0, 0, 0]
sum1=[]
sum2=0
for num in numbers:
    if num!=0:
        sum2+=num
    elif sum2!=0:
        sum1.append(sum2)
        sum2=0
if sum2!=0:
    sum1.append(sum2)
print(sum1)
        
