list1=['fruit','jelly','subji','horse']
list2=['buteerfly','ant','beetle']
list1.append('banana')
list1.extend(list2)
list1.insert(1,'parrot')
list1.remove('parrot')
list1.pop()
#list1.clear()
p=list1.index('fruit')
list1.append('fruit')
a=list1.count('fruit')
list1.reverse()
print(p)
print(a)
print(list1)
