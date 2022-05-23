#
# num = int(input("Type number for collatz sequence - "))
# coll_list = []
# while num > 1:
#     if num % 2 == 0:
#         coll_list.append(num)
#         num = num // 2
#     else:
#         coll_list.append(num)
#         num = num * 3 + 1
#
# print(coll_list)
#
# max_col_elem = 0
#
# for i in range(0, len(coll_list)):
#     if max_col_elem < coll_list[i]:
#         max_col_elem = coll_list[i]
# print("max", max_col_elem)
#
# min_col_elem = max_col_elem
# for i in range(0,len(coll_list)):
#     if min_col_elem > coll_list[i]:
#         min_col_elem = coll_list[i]
# print("min",min_col_elem)