list1=[]
for i in range(1,11):
    list1.append(i)
print(list1)


list2=[i*5 for i in range(1,11)]
print(list2)



list2=[i for i in range(1,11)]
print(list2)



list2=['a' for i in range(1,11)]
print(list2)


list2=[i for i in range(10)]
print(list2)


from random import randint
list2=[randint(10,100)  for i in range(1,11)]
print(list2)

str1='abcdeabbchi'
list1=[]
for i in str1:
    if i not in list1:
        list1.append(i)
print(list1)