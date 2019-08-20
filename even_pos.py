lis1=[]
while True:
    a = int(input("Enter the number to be added: "))
    if(a!=-1):
        lis1.append(a)
    else:
        break
x = int(len(lis1)/2)
for i in range(0,x):
    print(lis1[2*i+1]," ")

    
