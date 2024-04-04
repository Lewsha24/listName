from random import randrange



#уворот
# x = 10
#
# y = int((x / 2) / 2)
#
# ran = randrange(y,x)
#
# if (ran > y):
#     print(ran)
#     print("Вы попали")
# if(ran <= y):
#     print(ran)
#     print("ВЫ НЕ ПОПАЛИ")
#

def damageRand():
    x = 10

    y = int((x / 2) / 2)

    ran = randrange(y, x)

    if (ran > y):
        print(ran)
        print("Вы попали")
        return 10
    if (ran <= y):
        print(ran)
        print("ВЫ НЕ ПОПАЛИ")

damageRand()

if (damageRand()  == 10):
    print('okey')
elif damageRand() != 10:
    print('return')
    damageRand()