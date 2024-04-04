class animals:


    def __init__(self, name, age):
        self.name = name,
        self.age = age

    def print_i(self,):
        print(self.name)

list = []

def asinList(list,char):
    list.append(char)
    print(list)

def asinListDel(list,char):
    list.remove(char)
    print(list)

# def asinListDel(list,char):
#     list.remove(char)
#     print(list)

cow = animals("cow", 100)
# cow.print_i()
# leon = animals("leon", 100)
makaka = animals("makaka", 100)
# piople = animals("piople", 100)
# rostic = animals("rostic", 100)
# asinList(list,cow)

def changeList(animals, sign):
    if(sign == "добавить"):
        asinList(list,animals)
    if(sign == "удалить"):
        asinListDel(list,animals)
    if (sign == "изменить"):
        asinListDel(list, animals)

changeList(makaka,"добавить")
changeList(cow,"добавить")
changeList(cow,"удалить")