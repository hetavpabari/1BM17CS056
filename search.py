def lin_search(lis):
    a = int(input("Enter the number to search: "))
    for i in lis:
        if a in lis:
            print("The element is present at: ",i+1)
            break;

        elif i==len(lis)-1 and a not in lis:
            print("The element is not present !!")
lis = [1,4,5,-1,9]
lin_search(lis)
