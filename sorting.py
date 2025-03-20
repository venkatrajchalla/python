# 1. binary search algorithm

# list = [ 2,91,-32,68,334,-222,22 ]
# def binary_search(input_list,search_elem):
#     low = 0 
#     high = len(input_list)-1
#     while low <= high:
#         mid = (low+high)//2
#         if input_list[mid] == search_elem:
#             return mid
#         elif input_list[mid]<search_elem:
#             low = mid+1
#         else input_list[mid]>search_elem:

# 2.unoptimized bubblesort for ascending order

# for  j in range(len(list)-1):        

#   for i in range (len(list)-1):
#     if list[i]>list[i+1]:
#         list[i],list[i+1] = list[i+1],list[i]
#   print(list)

# 3.unoptimized bubblesort for ascending order

# for  j in range(len(list)-1):        

#   for i in range (len(list)-1):
#     if list[i]< list[i+1]:
#         list[i],list[i+1] = list[i+1],list[i]
#   print(list)

# list =["2","91","-32","68","334","-222","22"]
# for  j in range(len(list)-1):        

#     for i in range (len(list)-1):
#       if len(list[i])> len (list[i+1]):
#         list[i],list[i+1] = list[i+1],list[i]
#     print(list)
# def bubble_sort(list):

#  for  j in range(len(list)-1):   
#     flag = False     

#     for i in range (len(list)-1):
#      if list[i]>list[i+1]:
#         flag =True
#         list[i],list[i+1] = list[i+1],list[i]
#     if not flag:
#      break
# print(list([2,91,-32,68,334,-222,22]))
list = [[1,4,3],[10,11,12],[-5,20,30]]

for j in range(len(list) - 1):   
    flag = False     
    for i in range (len(list) -1 - j):
        if list[i][0] > list[i+1][0]:
          flag =True
          list[i],list[i+1] = list[i+1],list[i]
    if not flag:
       break
    print(list)