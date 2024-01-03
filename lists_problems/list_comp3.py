#adding two diffrent list elements using list comprehension

list1 = [2,4,6,8]
list2 = [5,8,9,1]
li = [list1[i]+list2[i] for i in range(0,len(list1))]
print(li)