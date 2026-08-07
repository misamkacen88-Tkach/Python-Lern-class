from decimal import Decimal, getcontext
import math
# print('python', 'for', sep=',', end='.\n')
# print('backend')

# print('hello','my','liked','development',sep=';')

# x = '\n'
# for i in range(10):
#     x += '\n\n\n\n\n\n\n\n\n\n\n\n\n\n'

# print("\nButwrite cod dont liked.Madye you could ", end=x)
# print('n')


# help("keywords")

# s1 = "first"
# s2 = "second"

# s1, s2 = s2, s1

# print((1245**13 + 20**5**3 - 40)*400)
# a = int(input("a: "))
# b = int(input("b: "))
# c = int(input("c: "))

houer = 60

# time_mins = 90
# start_hoer = 0
# start_mins = 0


# time_all = (time_mins // houer + start_hoer) % 24
# time_mins = (time_mins % houer + start_mins) % houer

# print(time_all, time_mins)

# min = 61
# sec = 0
# dey = 50

# minbefor = min * dey
# secdefor = sec * dey

# sec = secdefor % houer
# min = minbefor % houer + secdefor // houer
# huer = minbefor // houer

# print(min, end=' ')
# print(sec,end=' ')
# print(huer)

# a = 20.01219512195122
# b = 40.02777777777778
# c = 87.1

# print((a**3 + b**(1/2))/c)
# y = 4443.765
# x = (abs(y))

# o = x*10**3
# o = int(o)
# o = o % 10

# print(o)




# husband = round(float(20000.50) * 100)
# wife = round(float(30000.75) * 100)

# total_cents = husband + wife

# vacation = int(total_cents * 0.10)
# food = int(total_cents * 0.30)
# utilities = int(total_cents * 0.05)
# leisure = int(total_cents * 0.15)

# savings = total_cents - (vacation + food + utilities + leisure)

# x = vacation % 100
# print(x)
# print(f"Отпуск: {vacation // 100} руб. {vacation % 100} коп.")
# # print(f"Пропитание и еда: {food // 100} руб. {food % 100} коп.")
# # print(f"Коммунальные платежи: {utilities // 100} руб. {utilities % 100} коп.")
# # print(f"Досуг: {leisure // 100} руб. {leisure % 100} коп.")
# # print(f"Накопления: {savings // 100} руб. {savings % 100} коп.")
# from decimal import Decimal
# import time

# a, b, x = 0.1, 0.2, 0.3
# start1 = time.time()
# for _ in range(1_000_000):
#     x += x * a - b

# float_time = time.time() - start1

# a, b, x = Decimal("0.1"), Decimal("0.2"), Decimal("0.3")
# start = time.time()
# for _ in range(1_000_000):
#     x += x * a - b

# decimal_time = time.time() - start

# print(round(decimal_time / float_time, 3))

# x = float(input())
# y = float(input())
# b = float(input())


# x = math.ceil(x)
# y = math.ceil(y)
# b = math.ceil(b)

# print(f"Ширина: {x} \nДавжина: {y}\nВисота: {b}")

# n1, n2, n3, n4 = [int(i) for i in input().split('.')]
# x = [n1,n2,n3,n4]

# count = 0
# count0 = 0
# count255 = 0



# for i in x:
    
#     if i <=255 and i >=0:
#         count += 1
#         if i == 255:
#             count255 += 1
#         elif i == 0:
#             count0 += 1
#     else:
#         print(False)
      
# if count == 4 and count0 !=4 and count255 != 4:
#     print(True)
# else :
#     print(False)



# x = input().split(' ')

# coutn = None
# coutn1 = 999999

# for i, valiu in enumerate(x):
    
#     y = x[i]
    
#     if len(y) <= coutn1:
        
#         coutn = x[i]
#         coutn1 = len(y)
    
# print(coutn)

# x = None
# y = '13426ybb35h3h4'

# if x :
#     print('0')
# if y :
#     print('1')

# command = "console"
# flag = "-f"
# argument = "hello"

# match command, flag:
#     case "print" | "write" | "say", "console":
#         print(argument)
#     case "decorate", _:
#         print(flag, argument)
#     case _:
# #         print("error")

# x = {"привет": "Привет!", "как дела?": "все классно!", "Пока": "до скорой встречи!"}

# try: 
    
#  print(x[input("\n<Базарчик>\n=>").lower()])
 
# except:
    
#     print("хз я даун")


# match input().lower:
#     case "Привет":
#         print('Привет медвет АХХХАХАХАХАХАХХАХАХАХ!!!!!!!!!!!!')





# for i in range((x := int(input()))):
#     for j in range(x,0 +i,-1):
        
#         print(j,end=' ')
    
#     print()

    
    
    
    
    
    
# for j in range(5,0,-1):
#     print(j, end=' ')
   
# print()  
# for j in range(5,1,-1):
#     print(j, end=' ')

# print()
# for j in range(5,2,-1):
#     print(j, end=' ')
    
# print()
# for j in range(5,3,-1):
#     print(j, end=' ')
    
# print()
# for j in range(5,4,-1):
#     print(j, end=' ')
     
    

# if str.isdigit(x := input()):
#     print(int(x)*3)
# else:
#     print("No number 1")



# try:
#     print(int(x)*3)
# except:
#     print("еблан 2")


# x ="backend"

# for i in range(len(x)):
#     print(x[i] * (i+1))

# s = "backend"
# print(s[-1:0:-1])

# x = 'abcd'
# print(f"{(x[1]*4)}\n{x[-2:] + '!'}\n{x[0:-3]}\n{x + x[-1::-1]}\n{x[1::2]}\n{x[::2]}")


# print(ord('a'))
# print(chr(97))

# key = int(input())
# shifrotext = ''
# plantext = [shifrotext + i for i in chr(ord(input().split('.')) + key)]

# print(plantext)



# s = input()
# step = int(input())


# res = "".join(
#     chr((ord(char) - ord("a") + step) % 26 + ord("a")) for char in s
# )

# print(res)

# res = "".join(chr((ord(char) - ord("a") - step) % 26 + ord("a")) for char in res)
# print(res)



# s = input()

# max_char = ""
# max_count = 0

# current_char = ""
# current_count = 0

# for char in s:
#     if char == current_char:
#         current_count += 1
#     else:
#         current_char = char
#         current_count = 1


#     if current_count >= max_count:
#         max_count = current_count
#         max_char = current_char

# print(max_char)
# print(max_count)






# print( len(input().split()))





















# КОРТЕЖИ:
# man = ('Mishel',23,'Programer')
# name,age,profession = man

# print(name)




# a, *b = 1,2,3,4,5,6
# c, *_ = 2,3,4,5,6
# print(type(a)) # 1
# print(type(b))
# print(_)



# perents = (
#             ('Mam1',1980,('Gey','Parf','Max')),
#             ('Mam2',1993,('Gey','Parfan','Max')),
#             ('Mam3',1976,('Gey','Parfenenko','Max')),)


# for perent in perents:
    
#     name, age, cildrens = perent
#     print(f"\n\nName mamka : {name},\nAge : {age},\nChildrens : ")
#     for i in cildrens:
#         print(i,end=', ')


# new_list = [int(input()) for i in range(int(input()))]



# new_list = [int(i) for i in input().split(' ') ]

# x = 1
# for i in new_list:
    
#     x *= i
#     print(x)



# for i,j in enumerate(new_list):
#     if i != 0:
#         print(j + new_list[i-1], end=' ')

# new_list = sorted(set(new_list))

# print(new_list[-2])


# count =0


# for i,j in enumerate(new_list):
    
#     x = True
   
#     while x:
#         if len(new_list) != 1 and new_list[i] == 0 :
             
#             new_list.pop(i)
#             count +=1
            
#         else:
            
#             x = False
 
# for i in range(count):
#     new_list.append(0)

# print( new_list)


# new_list = [int(i) for i in input().split(' ') ]

# for i,j in enumerate(new_list):
    
#      x = True
   
#      while x:
#         if new_list[i] % 2 != 0 :
#             print(j)
#             new_list.pop(i)
            
            
#         else:
            
#             x = False
    


# print(*new_list)

# print(
#     len(
#         {
#             i.replace('b','d',1) if i.startswith('b') else i.replace('c','') 
#             for i in ['aa','bbb','cccc', 'bacbac'] if len(i) > 2
#         }
#     )
# )

# x = {'x':1, 'y': 2}
# print(len(x))

# x = {1,1,1,1,2,0,0,0,1}

# print(len(set(x)))

# a = {1, 2, 3, 4 ,5, -5, -4, -3, -2, -1, 0}
# # x = 0

# # for i in a:
# #     x += i**2
    
# # print(x)

# required = {'a','b'}


# optional = {'c','d'}

# user_data = set(input().split())

# print(required.issubset(user_data) and user_data <=(required | optional) )


# print(1 in a)


# s = [i for i in input().split()]
# s.sort()
# x = {}

# for i in s:
    
#         x.setdefault(i,0)
#         x[i] +=1
       
# for key,value in x.items():
#     print(f"{key} {value}") 

# x = {1,2}
# y = (1,2)
# print(type(x))
# print(type(y))
# x = frozenset(x)
# print(type(x))


















