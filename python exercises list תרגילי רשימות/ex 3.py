list1=[]
list2=[]
list3=[]
list4=[]
list5=[]

for i in range(0,11):
    list5.append(i)
print(list5)

for i in range(0,11):
    list3.append(i)
print(list3)

print(list3[7:11])

print(list3[11:7:-1])
print(list3[7:11]+[11,12,13,14,15,16])

print(list3[::2])

print(list3[0:6])

print(list3[1::2])

#num=int(input('enter number:'))
#list1=list3
#(list3[7:10])=[num]
#print(list3)

#a=int(input('enter number:'))
list2=list3
(list3[4:5])=[a]
#print(list3)



list5=[]
for i in range(1,11):
    if i%3==0:
      list5.remove(i)
print(list5)


list6=[]
for i in range(1,11):
    if i % 3 == 0:
        list6.append(i)
print(list6)

