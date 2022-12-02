a = []
b = []
result = []
n = int(input("Enter Numbers of input: "))
print("Enter values for 1st list")
for x in range (0,n):
    i = int(input())
    a.append(i)
print("Enter values for 2nd list")
for y in range (0,n):
    i = int(input())
    b.append(i)

print("First list values: " +str(a))
print("Second list values: " +str(b))

for i in range (0,n):
    result.append(a[i]+b[i])

print("Result: "+str(result))