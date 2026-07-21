# def x(func):
    
#     def inner(*args):
        
#         func(*args)
#         func(args)
#         func(args)

#     return inner




# @x
# def Hello(a):
#     print(a)
    


# Hello(84)



# def decorator(func):

#     def inner(*args, **kwargs):

#         print("Before")

#         func(*args,**kwargs)

#         print("After")

#     return inner


# @decorator
# def add(a, b):
#     print(a + b)


# add(5,a = 2)

# def hello(name, age):
#     print(name, age)


# x = {
#     "name": "Ivan",
#     "ag": 18
# }

# hello(*x)

# def kalsuletor(*args):
    
#     return sum(args)
    
# print(kalsuletor(1,2,3,4,5,6,7,8,9,10))




# def show_users(**kwargs):
    
#     for len in kwargs:
#         print(kwargs[len])
    

# x = {
#     "name": "Ivan",
#     "age": 18,
#     "city":"Kyiv"
    
# }
# show_users(**x)



# def dekorator(func):
    
#     def inner(*args, **kwergs):
        
#         print("Function started")
    
#         func(*args, **kwergs)

#         print("Function ended")

#     return inner

# @dekorator
# def hello(name):
#     print(f"Hello {name}")


# hello("Ivan Kuthmich")


def my_print(*args):
    
    
    char = len(args) -1
    
    for lan in args:
        print(lan,end="")
        if char != 0 and char >-1:
            print("|",end="")
            char -= 1



my_print(10,20,"Hello")








# def create_student(name, age, city):
#     print(name, age, city)


# student = {
#     "name": "Ivan",
#     "age": 18,
#     "city": "Kyiv"
# }
# create_student(**student)



















