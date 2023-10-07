import random 
from time import sleep
hp = 100 
speed = 0
dist = 400

yetti = 1
tree = 2
rock = 3

while True:
   
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