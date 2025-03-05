#   Q.1 - Find the sum of odd digits in a given number

num = int(input("Enter any number:"))
sum_odd = 0

while num > 0:
    digit = num % 10
    if digit % 2 == 1:
      sum_odd += digit
    num = num // 10
print(sum_odd)                 

#  Q.2 - Print all the Armstrong numbers in given range

for num in range(1,101):
    temp = num
    power = 0
    n = temp
    
    while n > 0:
        power += 1
        n //= 10
    n = temp
    armstrong_sum = 0
    while n > 0:
        digit = n % 10
        armstrong_sum += digit ** power
        n //= 10
    
    if num == armstrong_sum:
        print(num)        
        
        
#  Q.3- Find the smallest prime digit  in a given number

num = int(input("Enter any number:"))
smallest_prime = 10
while num > 0:
    digit = num  % 10 
    if digit in { 2,3,5,7,}:
        smallest_prime = min(smallest_prime, digit)
    num //= 10
if smallest_prime == 10:
    print("not found")
else:
    print("smallest prime digit:" ,smallest_prime)            