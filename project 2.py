n= int(input("Enter the number: "))
start = int(input("Enter the number from which you want to start: "))
end=int(input ("Enter the end value "))

for i in range(start,end+1):
    print(n,"x",i,"=",n*i)
    