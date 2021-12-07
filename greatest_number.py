n = int(input("Enter the number of Values: "))
lst = []
for i in range(n):
    temp = int(input())
    lst.append(temp)

max = lst[0]

for i in range(n):
    if(max < lst[i]):
        max = lst[i]

print("Greatest number = ",max)