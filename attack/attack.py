import random
from classes.enemy import Enemey

enemy = Enemey(200,60)
print(enemy.get_hp()) #

'''
class enemy:
    hp = 200
    def __init__(self,atkl, atkh):
        self.atkl = atkl
        self.atkh = atkh

    def getAtk(self):
        print(self.atkl)
    def getHp(self):
        print("hp is", self.hp)

enemy1 = enemy(40, 49)
enemy1.getAtk()
enemy1.getHp()
enemy2 = enemy(75,90)
enemy2.getAtk()
enemy2.getHp()
'''
'''

playerhp =  260
enemyatkl = 60
enemyatkh = 80

while playerhp > 0:
    dmg = random.randrange(enemyatkl, enemyatkh)
    playerhp = playerhp - dmg

    if playerhp <=30:
        playerhp = 30

    print("Enemy Strikes for ", dmg, "points of damage. Curret HP is ", playerhp)

    if playerhp > 30:
       continue


    print("You have low health. You've been teleported to the neartes inn.")
    break

'''