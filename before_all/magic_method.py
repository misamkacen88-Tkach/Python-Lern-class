# class Student:

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
    
#     def __str__(self):
#         return (f"Student:\nName: {self.name}\nAge: {self.age}")

# student = Student("Gey", 19)
# print(student)

# ==	__eq__
# !=	__ne__ (или not __eq__)
# <	__lt__
# >	__gt__
# <=	__le__
# >=	__ge__
class Inventory:

    def __init__(self):
        self.items = [
            "Sword",
            "Shield",
            "Potion"
        ]
        
    def __getitem__(self, x ):
        print(f"Python asks for index {x}")

        return  self.items[x]
       

invent = Inventory()

# # for item in invent:
# #     print(item)

# iterator = iter(invent)

# while True:
#     try:
#         item = next(iterator)
#         print(item)
#     except StopIteration:
#         break

# class Playlist:

#     def __init__(self):
#         self.songs = [
#             "Song 1",
#             "Song 2",
#             "Song 3"
#         ]
    
#     def __iter__(self):
#         return iter(self.songs)

# music = Playlist()

# for song in music:
#     print(song)


class Inventory:

    def __init__(self):
        self.items = [
            {"name":"Aword","price":100},
            {[11,'name', '500']:"yhield","price":50},
            {"name":"Potio","price":200}
        ]

    def sort(self, key, reverses = False):
        self.items.sort(key=key, reverse=reverses)
    
    def __iter__(self):
        return iter(self.items)
    
    
invent = Inventory()

invent.sort(key=lambda x: x["name"], reverses=True)
for inv in invent:
    print(inv)
   