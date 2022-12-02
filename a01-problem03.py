a=[]
n = int(input("Enter the number of elements: "))
for i in range(0,n):
    x = input()
    a.append(x)
x = int(input("Enter the specified position number : "))
y = input("Enter the item name: ")
print("Orginal list: ", a)
a.insert(x,y)
print("Updated List: ", a)
