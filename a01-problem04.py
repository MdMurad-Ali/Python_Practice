a = []
n = int(input("The number of elements: "))
print("Enter the values: ")
for i in range (0,n):
    x = int(input())
    a.append(x)

x = int(input("Enter the elements you want to remove: "))
print (a)
for i in range(0,n):
    if x in a:
        a.remove(x)
print(a)