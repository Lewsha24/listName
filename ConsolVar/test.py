from random import randrange
# from player import goodPlay, badPlay
from color import bcolors
from character import charcater

testGoodPlayer = charcater("test_one", 10 , 10, 10)
testbadPlayer = charcater("test_two", 10 , 10, 10)


# goodPlay.hp >= 1, badPlay.hp >= 1
# def damageRand(piople):
#     x = pipole
#
#     y = int((x / 2) / 2)
#
#     random = randrange(y, x)
#
def startPlay():
    start = 1
    # Если start = 1, то игра началась
    if (start == 1):
        # Если у хорошего игрока полное хп, то он начинает бить
        if (testGoodPlayer.hp >= 1):
            # Тут храним нанесенный урон
            hit = int(input('Сколько ты урона хочешь нанести?'))
            print(type(hit))

            x =  testGoodPlayer.mobility
            y = int((x / 2) / 2)
            random = randrange(y, x)

            # Если числа совпали то проходит урон
            if (random > y):
                print(type(testGoodPlayer.hp))
                print(type(hit))
                testGoodPlayer.hp = testGoodPlayer.hp - hit
                print(f"Ты попал и отнял {hit}")
                print(f"{bcolors.WARNING}Теперь бьет противник{bcolors.ENDC}")
                if (testbadPlayer.hp >= 1):
                    hit: int = input('Сколько ты урона хочешь нанести?')
                    random = randrange(testbadPlayer.mobility)
                    average = random / 2
                    if (random == round(average)):
                        testbadPlayer.hp = testbadPlayer.hp - hit
                        print(f"Ты попал и отнял {hit}")
                        print(f"{bcolors.WARNING}Теперь бьет хороший{bcolors.ENDC}")
                        startPlay()
                    elif (random != round(average)):
                        print("Увы, вы промахнулись, бьет противник ")
                        startPlay()
            # Если не было поподания , то выводит это сообщение
            elif(random <= y):
                print("Увы, вы промахнулись, бьет противник ")
                print(f"Здоровье {testGoodPlayer.name} = {testGoodPlayer.hp}")
                if (testbadPlayer.hp >= 1):
                    hit= int(input('Сколько ты урона хочешь нанести?'))
                    x = testGoodPlayer.mobility
                    y = int((x / 2) / 2)
                    random = randrange(y, x)

                    if (random > y):
                        print(type(testbadPlayer))
                        print(type(hit))
                        testbadPlayer.hp = testbadPlayer.hp - hit
                        print(f"Ты попал и отнял {hit}")
                        print(f"Здоровье {testbadPlayer.name} = {testbadPlayer.hp}")
                        print(f"{bcolors.WARNING}Теперь бьет хороший{bcolors.ENDC}")
                        startPlay()
                    elif (random <= y):
                        print("Увы, вы промахнулись, бьет противник ")
                        print(f"Здоровье {testbadPlayer.name} = {testbadPlayer.hp}")
                        startPlay()
                elif (testbadPlayer.hp <= 0):
                    start == 0
                    print("К сожелению вы проиграли ")
        if (testGoodPlayer.hp <= 0):
            start == 0
            print("К сожелению вы проиграли ")

    else:
        print("Игра Закончилась, победил")


startPlay()