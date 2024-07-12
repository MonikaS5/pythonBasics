i = 1
while i <= 5:
    print(i)
    i += 1

j = 1
while j <= 7:
    print(j * '*')
    j += 1


numbers = [1, 2, 3, 4, 5, 6]
for items in numbers:
    print(items)

mynum1 = range(5)
print(mynum1)
for number in mynum1:
    print(number)

mynum = range(5, 10, 2)
print(mynum)
for number in mynum:
    print(number)

print("another way")
for number in range(8, 11):
    print(number)
