numbers = (1, 2, 3, 3, 3, 4, 4)
li = ('python', 'java')
y = ('c++',)
li += y
print(li)
numbers.count(3)
print(type(numbers))
print(type(li))

# numbers.__add__(2, 2)
print(numbers + li)

mytup = ("hi")  #not a tuple
print(type(mytup))

tup = ('hi',) #tuple
print(type(tup))

n = 5
for i in range(int(n)):
    tup = (tup,)
    print(tup)

