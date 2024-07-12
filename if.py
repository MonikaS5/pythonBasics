print(" **** Weight Conversion in kg/lb **** ")
weight = input("Enter  k  for kilogram(kg)  and enter  l  for pound(lb) :")

if weight == 'k' or weight == 'K':
    lb = float(input("Enter weight in pound :"))
    kg = lb / 2.2
    print("Weight in Kg : " + str(kg))
    print(str(lb)+"lb" + " = " + str(kg)+"kg")

elif weight == 'l' or weight == 'L':
    kg = float(input("Enter weight in kg:"))
    lb = kg * 2.2
    print("Weight in pound(lb) :" + str(lb))
    print(str(kg)+"kg" + " : " + str(lb)+"lb")

else:
    print("Invalid Input")
