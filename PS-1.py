# EASY QUESTIONS
# Question-1
num1 = int(input("Enter A Number:"))
if num1 == 0:
    print("zero")
elif num1 >= 0:
    print("positive")
else:
   print("negitive")

# Question-2
num= int(input("Enter A Number:"))

if num % 2 == 0:
  print("Even")
else :
  print("Odd")

# Question-3

age =int(input("Enter a number:"))

if age >= 18:
    print(" Age IsEligible To Vote")
else:
    print(" Age IsNot Eligible To Vote")
    
# Question-4

def greatestNumber(num1, num2):
    if num1>num2:
       return num1
    else:
       return num2
print(greatestNumber(10,20))

# Question-5
num=100
if num >= 40 :
 result = "Pass" 
else :
 result = "Fail"
print(result)


# Question-6
num = int(input("Enter A Day:"))
if num == 1:
  print("Monday")
elif num == 2:
  print("Tuesday")
elif num == 3:
  print("Wednesday")
elif num == 4:
  print("Thursday")
elif num == 5:
  print("Friday")
elif num == 6:
  print("Saturday")
elif num == 7:
  print("Sunday")
else:
  print("Invalid")

# Question-8
def monthName(month_number):
    if month_number == 1:
        return "January"
    elif month_number == 2:
        return "February"
    elif month_number == 3:
        return "March"
    elif month_number == 4:
        return "April"
    elif month_number == 5:
        return "May"
    elif month_number == 6:
        return "June"
    elif month_number == 7:
        return "July"
    elif month_number == 8:
        return "August"
    elif month_number == 9:
        return "September"
    elif month_number == 10:
        return "October"
    elif month_number == 11:
        return "November"
    elif month_number == 12:
        return "December"
    else:
        return "Invalid Month Number..!"

month_number = int(input("Enter A Month Number From 1 to 12 : "))
print("Month:", monthName(month_number))



# Medium Questions

#  Question-1
def greatestNumber(num1, num2, num3):
    if num1>num2:
        if num1>num3:
            return num1
        return num3
    elif num2>num3:
        return num2
    return num3
print(greatestNumber(10,20,30))



#  Question-2
def leapYear(year):
    if (year % 400 == 0 and year % 100 != 0 ) or ( year % 4 == 0 ):
            return "Leap Year"
    else:
        return "Not A Leap Year"
print(leapYear(2024))


