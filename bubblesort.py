
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
    
    # OUTPUT : [[1, 4, 3], [-5, 20, 30], [10, 11, 12]]
#              [[-5, 20, 30], [1, 4, 3], [10, 11, 12]]