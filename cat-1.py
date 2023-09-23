#program for finding two digit number
for i in range (1,100):
    for j in range(1,i):
        if (i+j==8 and i-j==4):
            print (i,j)
