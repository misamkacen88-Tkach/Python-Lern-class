
# class Students:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
    
#     def __str__(self):
#         return f"{self.name}, {self.age}"
    
#     def __repr__(self):
#         return self.__str__()




# students = [Students("Ivan", 18),Students("Andrei", 18),Students("Anna", 18)]

# students.sort(key=lambda x: (x.age, x.name))



# print(students)


def generator():
    print("Start")

    yield 1

    print("Middle")

    yield 2

    print("End")


g = generator()

next(g)
next(g)


def test():
    x = 10
    print("A", x)

    yield x

    x += 5
    print("B", x)

    yield x


g = test()

print(next(g))
print(next(g))



def countdown():

    for i in range(5, 0, -1):
        yield i