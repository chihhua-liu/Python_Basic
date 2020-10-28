# demo70   __iter__(self) and __next__(self) for 遞迴 ex: for
#
# class Object70(object):
#     def __init__(self, limit):    建構式
#         print("object init")
#         self.limit = limit
#         self.counter = 0
#
#     def __iter__(self):   #遞迴時呼叫，不然類別實例無法使用迴圈
#         print("start to iterate")
#         return self
#
#     def __next__(self):   # 每一次遞迴呼叫一次
#         # print("iterate")
#         if self.counter < self.limit:
#             self.counter += 1
#             return self.counter
#         else:
#             raise StopIteration()
#
#
# obj1 = Object70(30)
# print(type(obj1))
# # for i in obj1:
# #     print(i)
# print([i for i in obj1])