# b = int(input("Введите число")) 
# c = int(input("Введите число")) 

#mid_num = (a + b + c)/3
#print(round(mid_num,2))

количество = 0

a = int(input("Введите число A "))
количество = количество + 1
sum = 0

while a != 0:
    print("Вы ввели", количество, "чисел")
    sum = sum + a
    print("Сумма чисел равна",sum) 
    print("Цикл продолжается")
    a = int(input("Введите число A ")) 
    количество = количество + 1

middle = sum/количество
print(middle)








