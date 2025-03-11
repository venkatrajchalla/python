    # Q - 1
    
def add(a,b):
    return a + b 
print(add(5,10))   

# Q -2

def convert_secs(min):
    return  min * 60
print(convert_secs(2))    


# Q - 3

def increment(num):
    return num + 1
print(increment(5))

 # Q-4
def age_in_days(year):
    return year * 365
print(age_in_days(10))
 
#  Q - 5
def power(vol, curr):
    return vol * curr
print(power(50,5))

#  Q-6
def string(a):
    return "something" + str(a)
print(string("somethig...!"))
  
#  Q-7
def check(a,b):
    return a == 10 or b == 10 or a + b == 10
print(check(5,5))
print(check(5,1))

#  Q-8
def check_length(str1,str2):
    return len(str1) == len(str2)
print(check_length("Venkat", "Raj"))

# Q-9
def greet(name):
    return f"Hello, {name}!"
print(greet("Suraji"))

# Q-10

def ph_number(num):
    if len(num) != 10 or any(number < 0 or number > 9 for number in num):
        return "Invalid Input"
    return f"({num[0]}{num[1]}{num[2]}{num[3]}{num[4]}{num[5]}-{num[6]}{num[7]}{num[8]}{num[9]})"
print(ph_number([1,1,1,1,1,1,1,1,1,1]))
    
    #   Q - 11
def sorting_length(array):
    temp =  len(array)
    for i in range(temp):
        for j in range(0, temp-i-1):
            if len(array[j]) > len(array[j+1]):
                array[j],array[j + 1] = array[j + 1], array[j]
    return array
print(sorting_length(["V", "en","kat","Raj","Venkat Raj"]))               
     




        #   Q-12
def find_largest_nums(array):
        largest_nums = []
        for sub_array in array:
            largest = sub_array[0]
            for num in sub_array:
                if num > largest:
                    largest = num
            largest_nums.append(largest)
        return largest_nums
print(find_largest_nums([[4,2,3,1],[1,2,3,4],[1,9,0,2]]))

        #  Q - 13
        
def second_largest(array):
    if len(array) < 2:
        return "Atleast 2 elements are required to determine"
    largest = second = float('-inf')
    for num in array :
        if num > largest :
            second = largest
            largest = num
        elif num > second and second != largest:
            second = num
    return second if second != float('-inf')else None
print(second_largest([10,50,20,30,40,60]))
print(second_largest([10,10,10,10]))            
    
    
           # Q - 14
           
           
def remove_dups(array):
    result = []
    for item in array:
        exists = False
        for res_item in result:
            if res_item == item: 
                exists = True
                break
        if not exists:
            result.append(item)
    return result
print(remove_dups([1,2,0,0,1,3]))
print(remove_dups(["Hi","Hlo","Hi", "Oyee..!","Hi"])) 

        #  Q - 15
        
def find_unique_number(array):
    for i in range(len(array)):
        count = 0
        for j in range(len(array)):
            if array[i] == array[j]:
             count += 1
        if count == 1:
            return array[i]
    return None     #---> it return None if it doesn't find any unique number  
print(find_unique_number([8,8,8,8,9,10,10,10,]))     
        
                                     
        
        