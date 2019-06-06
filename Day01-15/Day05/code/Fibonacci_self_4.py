#coding=utf-8

# arr = []
# arr.append(1)
# arr.append(1)
# count = 2
# for i in range(1,10000):
#     if i == arr[count-1] + arr[count-2]:
#         arr.append(i)
#         count = count + 1
#
# print arr

a = 0
b = 1
for _ in range(20):
    a,b = b,a+b
    print a,

