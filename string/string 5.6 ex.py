list=[]
list2=[]
list3=[]
for i in range(1,11):
    list.append(i)
print(list)

print(list[-3:])
print(list[::-1])
print(list[0::2])


list[3:5]=[input(),input()]
list.append(input())
print(list)

for i in range(1,11):
    list2.append(i*2)
print(list2)

for i in range(1,11):
    list3.append(i)
print(list3)
 

print(max(list3),min(list3))
