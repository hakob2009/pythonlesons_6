#  գումարում

# def minus(a, b):
#     return a + b
#
#
# print(minus(18, 67))

# հանում

# def plus(a, b):
#     return  a - b
#
#
# print(plus(84, 26))

# բազմապատկում

# def multiple(num1, num2):
#     return num1 * num2
#
#
# print(multiple(12, 2))

# քոլաթսի հաջորդականություն

# def func_coll(num):
#     coll_list = []
#     while num > 1:
#         if num % 2 == 0:
#             coll_list.append(num)
#             num = num // 2
#         else:
#             coll_list.append(num)
#             num = num * 3 + 1
#     return coll_list
# print(func_coll(15))


# def division(num1, num2):
#     if type(num1) == int and type(num2) == int:
#         return num1 // num2
#     elif type(num1) == float and type(num2) == float:
#         return num1 / num2
#     else:
#         return "type error"
#
#
# print(division(16, 4))
# print(type(12) == int)


def test_fun(start, end, odd_list, even_list):
    for i in range(start, end):
        if i % 2 == 0:
            even_list.append(i)
        else:
            odd_list.append(i)

    print(odd_list)
    print(even_list)

odd_list = []
even_list = []

print(test_fun(12, 133, odd_list, even_list))
