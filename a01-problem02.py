a  = []
n = int(input("Enter the numbers of element: "))
for i in range(0,n):
     x = int(input())
     a.append(x)
print("Orginal list: " + str(a))
print("Revese List: " +str(a[::-1]))