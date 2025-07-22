a=[2,3,4,5,6,7,8,9,10,11,12,13,14,15]
for i in a:
    for j in range(2,i):
        if i%j==0:
            break
    else:
        print(i)
