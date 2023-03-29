num1 = int(input("Ввечдите число: "))
num2 = int(input("Ввечдите число: "))
num3 = int(input("Ввечдите число: "))
array = list()
for i in range(num3):
    array.append(num1)
    num1 += num2
print(array)