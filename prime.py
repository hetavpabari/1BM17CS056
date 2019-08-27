def prime(a):
    if(a==1 or a==2):
        print("Prime")
    else :
        
        for i in range(2,a+1):
            
            if a%i==0:
                print(a," is not  prime" )
                break
            elif a%i!=0 and i==a//2:
                 print(a," is prime")
                 break
a = int(input("Enter the lower limit: "))
b = int(input("Enter the upper limit: "))
for j in range(a,b+1):
    prime(j)
