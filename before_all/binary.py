import sys
# x = int(input("Numer: "))

# binar = bin(x)
# print(binar)

# hexs = hex(x)
# print(hexs)

# octs = oct(x)
# print(octs)

# print(a)
# print(hex(a))
# print(int(octs, 8))


# def base6_to_base16(number_str):
#     # Шаг 1: Переводим из 6-чной системы в десятичную int()
#     decimal_number = int(number_str, 6)
    
#     # Шаг 2: Переводим из десятичной в 16-чную hex() 
#     # [2:] убирает технический префикс '0x', а .upper() делает буквы заглавными
#     hex_number = hex(decimal_number).upper()
    
#     return hex_number

# # Входное число
# input_number = "1124"
# result = base6_to_base16(input_number)

# print(result)





# def contwertor(res,sistem):
#     if res == 0:
#         return "0"
#     if res == 0:
#         return "0"
#     if res == 0:
#         return "0"
    
#     result = ""
#     while res > 0:
#         remainder = res % sistem   
#         result = str(remainder) + result 
#         res = res // sistem         
        
#     return result
        
    
    
# a = int(input())

# x = contwertor(a,8)
# print(x)





# res0 = a % 8 
# res1 = a // 8 

# res2 = res1 % 8
# res3 = res2 // 8

# res4 = res3 % 8
# res5 = res4 // 8

# print(res0,res2,res4)








# x = int(input()) * 8
# y = (f"{-2**(x - 1), 2**(x -1)-1}")




# def xor(x,y):
    
#     # x = bin(x)
#     # y = bin(y)
    
#     x = (x ^ y)
#     return x
    
    
    
# plain = xor(127,47)
# print(plain)
# plain = xor(plain,2)
# print(plain)





print(5 % 3 == 2 or 10 < 5 and 5 < 20)

















