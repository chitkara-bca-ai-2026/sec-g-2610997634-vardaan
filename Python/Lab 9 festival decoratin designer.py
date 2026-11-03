print("star triangle'(right angele')")

for i in range(1,6):
    for j in range(i):   
     print("*",end="")
    print() 


print("number triangle")
n=5
for row in range(1,n+1):
    for col in range(1,row+1):   
     print(col,end="")
    print() 

print("inverted star triangle")
for i in range(5,0,-1):
    for j in range(i):   
     print("*",end="")
    print() 



print("pyramid centered triangle")
n=5
for row in range(1,n+1):
    for col in range(n-row):
        print(" ",end="")
    for col in range(2*row-1):
        print("*",end="")
    print() 