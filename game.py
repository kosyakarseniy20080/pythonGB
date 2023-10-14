



import random # Импортируем готовый код из библиотеки готовый код random для случайного числа
from time import sleep # Из библиотеки time добавляем команду sleep
# переменные, которые хранят данные о персонаже
hp = 100 
speed = 0
dist = 400
# переменные с порядковым номером врагов
rock = 1
tree = 2
yetti = 3

#
while True:
   print('')
   chanceEnemy = random.randint(0,10)   
   if chanceEnemy == rock:
        print('Вы столкнулись с камнем')
        hp -= 5
        print(f'У вас осталось {hp} жизней')
        sleep(1)
    elif chanceEnemy == yetti:
        print('Вас пожрали Йети')
        hp -= 10
        print(f'У вас осталось {hp} жизней')
    elif chanceEnemy == tree:
        print('Вы влетели в дерево')
        hp -= 8
        print(f'У вас осталось {hp} жизней')
        
    speed += 1 
    dist -= speed 
    print(f'Вы летите со скоростью {speed} км/c')
    print(f'Осталось проехать {dist} километров')
    print(f'У вас осталось {hp} жизней')
    if (dist <= 0):
        print('УРА! Победа!')
        break
    if (hp <= 0):
        print('Вас сожрали')
        break
    
    sleep(0.9)













1.} пишем "Перед вами камень" print
2.} предлагаем "Влево, Вправо, перепрыгнуть, подкат" 
3.} Игрок делает выбор int(input("1. Влево, 2. Вправо, 3. перепрыгнуть, 4. подкат"))

4.} Программа выбирает случайное число от 1 до 4       choose.randint















































































