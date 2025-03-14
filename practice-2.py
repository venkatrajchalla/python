#   Q - 16 
# Create a function that takes two strings as arguments and returns the number of times the first string (the single character) is found in the second string.
# Example:

# charCount("c", "Chamber of secrets") ➞ 1

def char_count(char, string):
    count = 0
    for c in string:
        if c == char:
            count += 1
    return count

result = char_count("a", "venkat raj challa")
print(result) 

# Q - 17
# create a function that takes a string and returns the number (count) of vowels contained within it.
# EXAMPLE :
# countVowels("Celebration")-->5

def count_vowels(string):
    vowels = "aeiouAEIOU"
    count = 0
    for char in string:
        for vowel in vowels:
            if char == vowel:
                count += 1
                break  
    return count

result = count_vowels("virat kohli")
print(result)  



# Q-18
# Given a string, create a function to reverse the case. All lower-cased letters should be upper-cased, and vice versa.
# Example:
# reverseCase("Happy Birthday") ➞ "hAPPY bIRTHDAY"


def reverse_case(s):
    result = ""  
    uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lowercase = "abcdefghijklmnopqrstuvwxyz"
    
    for char in s: 
        if char in uppercase:  
            index = uppercase.index(char)
            result += lowercase[index] 
        elif char in lowercase:  
            index = lowercase.index(char)
            result += uppercase[index] 
        else:
            result += char  
    return result  
print(reverse_case("EnJoYy PaNdAgOo")) 

# Q-19
# Take one integer n, loop till n and pass each value to a function, create a function that takes one integer parameter, and multiply with 2 in every integer.
			
# 			Input:      n=5
# 			Output:   2 4 6 8 10

# 			Explanation:  Loop start with 1 go till 5 bcoz n=5
# 					1 x 2 =2, 2 x 2=4, 3 x 2=6 …..etc 


def multiply_by_two(num):
    return num * 2

n = int(input("Enter a number: "))  

for i in range(1, n + 1): 
    print(multiply_by_two(i), end=" ")  
    
    # Q-20
    # Create Function that will take one parameter and return type of the data.
			
	# 		Input:       500
	# 		Output:     Integer

	# 		Input:       Coding
	# 		Output:    String
 
def get_data_type(value):
    if type(value) == int:
        return "Integer"
    elif type(value) == float:
        return "Float"
    elif type(value) == str:
        return "String"
    elif type(value) == bool:
        return "Boolean"
    elif type(value) == list:
        return "List"
    elif type(value) == tuple:
        return "Tuple"
    elif type(value) == dict:
        return "Dictionary"
    elif type(value) == set:
        return "Set"
    else:
        return "Unknown"
    
print(get_data_type(500))      # Output: Integer
print(get_data_type("Coding")) # Output: String
print(get_data_type(1.43))     # Output: Float
print(get_data_type(True))     # Output: Boolean

# Q-21
#  Program to find greatest of three numbers(using ternary operator).

			# Input:  4 8 2
			# Output: 8 is greatest
  
def greatest_number(num1, num2, num3):
    if num1>num2:
        if num1>num3:
            return num1
        return num3
    elif num2>num3:
        return num2
    return num3
print(greatest_number(10,20,30))

# Q-22
#  C Program to find factorial of number.
		
			# Input: n=5
			# Output: 120

			# Explanation: 5 x 4 x 3 x 2 x 1 = 120
   
def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers."
    
    fact = 1
    for i in range(1, n + 1):
        fact *= i 
    return fact  
n = int(input("Enter a number: "))

print("Factorial of", n, "is", factorial(n))

 
# Q-23
#  C Program to arrange numbers in ascending order
			# Input: [2,3,1,5,4]
			# Output: [1,2,3,4,5]

		    #     Sort the Array using loop only(you can not use predefined function).


arr = [5, 3, 1, 4, 2]
n = len(arr)  

for i in range(n - 1):  
    for j in range(n - i - 1):  
        if arr[j] > arr[j + 1]:  
            temp = arr[j]
            arr[j] = arr[j + 1]
            arr[j + 1] = temp

print("Sorted array:", arr)

#Q- 24
# Print Patter using loop.

			# 1
			# 1 2
			# 1 2 3
			# 1 2 3 4
  			# 1 2 3 4 5
def print_pattern(n):
    for i in range(1, n + 1):  
        for j in range(1, i + 1):  
            print(j, end=" ")  
        print() 
print_pattern(5)

# Q-25
#  25. C Program to Calculate the Power of a Number(using loop only).

			# Input: n=5, p=3
			# Output: 5 ^ 3 = 125
			# Explanation: 5 x 5 x 5 = 125

# Input values
n = 5
p = 3

result = 1
for _ in range(p):
    result *= n  
print(f"{n} ^ {p} = {result}")


#  Q-26
#  26. Program to Check Whether a Number is Prime or Not
# 			Input: 9
# 			Output: 9 is not a prime no

# 			Input: 7
# 			Output : 7 is a prime no

def is_prime(num):
    """Function to check if a number is prime."""
    if num < 2:  
        return False   

    for i in range(2, int(num ** 0.5) + 1):  
        if num % i == 0:
            return False 
    return True  
num = int(input("Enter a number: "))

if is_prime(num):
    print(f"{num} is a prime number")
else:
    print(f"{num} is not a prime number")
    
    #  Q - 27
    #   Program to find LCM of two numbers using while loop

	# 		Input: 15 50
	# 		Output: Lcm of 15 and 50 is 150.

def find_lcm(a, b):
    if a > b:
        greater = a
    else:
        greater = b

    while True:
        if (greater % a == 0) and (greater % b == 0): 
            return greater  
        greater += 1  
a, b = 15, 50
print(f"LCM of {a} and {b} is {find_lcm(a, b)}")

#  Q-28
#  Program to Display Characters from A to Z Using Loop with count.

# 			Output: A1 B2 C3 D4 E5 F6 ……. Z26 

def display_alphabet_with_count():
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" 

    for i in range(26):  
        print(alphabet[i] + str(i + 1), end=" ") 
display_alphabet_with_count()

# Q -29
# Program to find a missing number

# 			Input:  n=5(length of array), arr= [5,3,1,4]
# 			Output: 2 is missing

# 		Using loop only(you can not use predefined function)
# Input: length of array and the given numbers
n = 10
arr = [1, 2, 3, 4 , 5, 6, 7 ,8 ,9]

for i in range(1, n + 1):  
    found = False  
    
    for j in range(len(arr)):  
        if arr[j] == i:
            found = True
            break  
    
    if not found:
        print(f"{i} is missing")
        break  

    # Q-30
    #  Program to count vowels and consonants in a given String.
	# 		Input: i am ram
def count_vowels_consonants(string):
    vowel_count = 0
    consonant_count = 0
    vowels = "aeiouAEIOU"
    for char in string:
        if char != " ": 
            is_vowel = False  
            for v in vowels:
                if char == v:
                    is_vowel = True
                    break
            
            if is_vowel:
                vowel_count += 1
            else:
                consonant_count += 1
    return vowel_count, consonant_count
string = "i am ram"
vowels, consonants = count_vowels_consonants(string)
print(f"Vowels: {vowels}, Consonants: {consonants}")

# Q - 31
#  program to insert  the elements of an array for specific index.

# 			Input: [1,2,3,4,5,7,8,9,10] , index=5
# 			Output: [1,2,3,4,5,6,78,9,10]


def insert_at_index(arr, index, element):
    new_arr = [0] * (len(arr) + 1)  
    
    for i in range(len(arr) + 1):  
        if i < index:
            new_arr[i] = arr[i]  
        elif i == index:
            new_arr[i] = element
        else:
            new_arr[i] = arr[i - 1] 
            
    return new_arr 
result = insert_at_index([1, 2, 3, 4, 6, 7, 8, 9, 10], 4, 5)
print(result)

# Q-32
# 32. Reverse a number using while Loop

# 			Input: 123
# 			Output: 321
def reverse_number(n):
    reversed_num = 0  

    while n > 0:
        digit = n % 10
        reversed_num = reversed_num * 10 + digit  
        n = n // 10  
    
    return reversed_num 

num = 123
result = reverse_number(num)
print(result)

# Q-33
#   Count occurrence of number:
			# Input: [1,6,3,1,5,9,7,2,1,9,3,7,8,9,10] , no find=7
			# Output: 7 present 2 times.
   
def count_occurrences(arr, num):
    count = 0  
    for i in arr: 
        if i == num:
            count += 1 
    return count 
result = count_occurrences([1, 2, 3, 4, 3, 5, 3, 8, 3, 9, 10], 3)
print(f"Given number is present {result} times.")
   













	

