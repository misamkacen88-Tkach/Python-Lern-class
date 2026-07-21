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





for i in range((x := int(input()))):
    for j in range(x,0 +i,-1):
        
        print(j,end=' ')
    
    print()

    
    
    
    
    
    
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
     
    






















