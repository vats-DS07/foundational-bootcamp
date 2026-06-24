#9/6/26
# student management system

# name = input("Enter Student Name: ")
# roll_no = input("Enter Roll Number: ")
# age = int(input("Enter Age: "))
# program = input("Enter Program: ")
# cgpa = float(input("Enter CGPA: "))
# completed_courses = int(input("Enter Number of Completed Courses: "))

# remaining_courses = 40 - completed_courses
# completion_percentage = (completed_courses / 40) * 100

# print("\n========== STUDENT REPORT ==========")
# print(f"Name: {name}")
# print(f"Roll Number: {roll_no}")
# print(f"Age: {age}")
# print(f"Program: {program}")
# print(f"CGPA: {cgpa}")
# print(f"Completed Courses: {completed_courses}")
# print(f"Remaining Courses: {remaining_courses}")
# print(f"Degree Completion: {completion_percentage}%") 


# Personal Expense Tracker

# budget = float(input("Enter Monthly Budget: "))

# food = float(input("Food Expense: "))
# travel = float(input("Travel Expense: "))
# internet = float(input("Internet Bill: "))
# entertainment = float(input("Entertainment Expense: "))
# misc = float(input("Miscellaneous Expense: "))

# total = food + travel + internet + entertainment + misc
# balance = budget - total
# spent = (total / budget) * 100

# print("\n================Expense Report==============")
# print("Total Expense =", total)
# print("Remaining Balance =", balance)
# print("Percentage Spent =", spent)

# if spent > 80:
#     print("Warning! Spending exceeds 80% of budget.")


# Digital Shopping Cart

# products = []
# quantities = []
# prices = []

# for i in range(5):
#     product = input("Enter Product Name: ")
#     quantity = int(input("Enter Quantity: "))
#     price = float(input("Enter Price: "))

#     products.append(product)
#     quantities.append(quantity)
#     prices.append(price)

# print("\n-------- BILL -------")

# grand_total = 0

# for i in range(5):
#     item_total = quantities[i] * prices[i]
#     grand_total = grand_total + item_total

#     print(products[i], quantities[i], "x", prices[i], "=", item_total)

# gst = grand_total * 0.18
# final_bill = grand_total + gst

# print("\nSubtotal :", grand_total)
# print("GST (18%) :", gst)
# print("Final Bill :", final_bill)

# if grand_total > 50000:
#     discount = final_bill * 0.10
# elif grand_total > 25000:
#     discount = final_bill * 0.05
# else:
#     discount = 0

# final_bill = final_bill - discount

# print("Discount :", discount)
# print("Amount Payable :", final_bill) 


# University Admission Eligibility Checker

# try:
#     name = input("Enter Student Name: ")

#     age = int(input("Enter Age: "))
#     percentage = float(input("Enter Class 12 Percentage: "))
#     exam_score = float(input("Enter Entrance Exam Score: "))
#     category = input("Enter Category (General/OBC/SC/ST): ")

#     if age <= 0:
#         print("Invalid Age")
#     elif percentage < 0 or percentage > 100:
#         print("Invalid Percentage")
#     elif exam_score < 0 or exam_score > 100:
#         print("Invalid Exam Score")

#     else:
#         if percentage >= 60 and exam_score >= 50:
#             eligibility = "Eligible"
#         else:
#             eligibility = "Not Eligible"

#         average = (percentage + exam_score) / 2

#         if average >= 90:
#             grade = "A"
#         elif average >= 80:
#             grade = "B"
#         elif average >= 70:
#             grade = "C"
#         else:
#             grade = "D"

#         if average >= 90:
#             scholarship = "50% Scholarship"
#         elif average >= 80:
#             scholarship = "25% Scholarship"
#         else:
#             scholarship = "No Scholarship"

#         if category.upper() in ["SC", "ST"] and eligibility == "Eligible":
#             scholarship = scholarship + " + Category Benefit"

#         print("\n===== ADMISSION REPORT =====")
#         print("Name:", name)
#         print("Age:", age)
#         print("Class 12 Percentage:", percentage)
#         print("Entrance Exam Score:", exam_score)
#         print("Category:", category)
#         print("Average Score:", average)
#         print("Eligibility:", eligibility)
#         print("Admission Grade:", grade)
#         print("Scholarship Status:", scholarship)

# except ValueError:
#     print("Please enter valid numeric values.")








# 10/6/26


# Task-1: Unit Converter

# print("1. Kilometer to Meter")
# print("2. Liter to Milliliter")
# print("3. Meter to Centimeter")
# print("4. Kilogram to Gram")

# choice = int(input("Enter your choice: "))

# print("\n========== Conversion Result ==========")

# if choice == 1:
#     km = float(input("Enter kilometers: "))
#     meter = km * 1000
#     cm = km * 100000
#     print("Thousand Meters =", meter)
#     print("Hundred Centimeters =", cm)

# elif choice == 2:
#     liter = float(input("Enter liters: "))
#     ml = liter * 1000
#     ml = liter * 1000000
#     print("Thousand Milliliters =", ml)
#     print("Million Milliliters =", ml)

# elif choice == 3:
#     meter = float(input("Enter meters: "))
#     cm = meter * 100
#     mm = meter * 1000
#     print("Thousand Centimeters =", cm)
#     print("Thousand Millimeters =", mm)

# elif choice == 4:
#     kg = float(input("Enter kilograms: "))
#     g = kg * 1000
#     milligrams = kg * 1000000
#     print("Thousand Grams =", g)
#     print("Million Milligrams =", milligrams)

# else:
#     print("Invalid Choice")




# ASSIGNMENT-1
# Task-2: Check whether a number is positive, negative or zero

# num = int(input("Enter a number: "))

# if num > 0:
#     print("The number is positive.")

# elif num < 0:
#     print("The number is negative.")

# else:
#     print("The number is zero.")




# Task-3: Leap Year Checker

# year = int(input("Enter a year: "))

# if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#     print(year, "is a leap year.")
# else:
#     print(year, "is not a leap year.")




# Task-4: simple atm program

# pin = int(input("Enter your 4-digit PIN: "))

# if pin == 1234:
#     print("PIN accepted. Access granted.")

#     amount = float(input("Enter amount to withdraw: "))

#     if amount <= 5000:
#         print("Dispensing amount")
#     else:
#         print("Amount exceeds limit")

# else:
#     print("Invalid PIN. Access denied.")



#ASSIGNMENT-2
# Task-5: Temperature advisor program

# temp = float(input("Enter the current temperature in Celsius: "))

# if temp < 0:
#     print("Wear a heavy coat. ")

# elif temp >0 and temp <= 15:
#     print("Wear a jacket. ")

# elif temp > 16 and temp <= 30:
#     print("Comfortable weather. ")

# else :
#     print("Wear light clothing and stay hydrated. ")




# Task-6: loan eligibility checker

# Income = float(input("Enter your monthly income: "))
# Emi = float(input("Enter your existing EMI amount: "))

# if Income >= 30000 and Emi <= 0.4 * Income:
#     print("Eligible for the loan.")

# elif Income < 30000:
#     print("Income too low.")

# elif Emi > 0.4*Income:
#     print("High Debt Burden.")




# Task-7: Build a number guessing Hint program

# guess = int(input("Guess a number between 1 and 50: "))
# secret_number = 42

# if guess < secret_number:
#      print("Too low !")
#      print("You are :", secret_number - guess, "away from the number.")

# elif guess > secret_number:
#      print("Too high !")
#      print("You are :", guess - secret_number, "away from the number.")

# else:
#      print("Congratulations! You guessed the number.")



#ASSIGNMENT-3
# Task-8: Classify a student's performance based on their marks

# marks = float(input("Enter your marks: "))

# if marks >= 40 and marks <= 100:
#     print("Pass")

#     if marks >= 90:
#         print("Distinction")

#     elif marks >= 75:
#         print("First division")

#     elif marks >= 60:
#         print("Second division")

#     else:
#         print("Third division")

# else:
#     print("Fail")




# Task-9: Job application scanner

# age = int(input("Enter your age: "))

# if age >= 21 and age <= 40:
#     degree = input("state your degree : ")

#     if degree == "B.Tech" or degree == "MCA":
#         cgpa = float(input("Enter your CGPA: "))

#         if cgpa >= 7.0:
#             print("Congratulations! You are eligible for the job.")

#         else:
#             print("Sorry, your CGPA does not meet the requirement.")

#     else:
#         print("Sorry, your degree does not meet the requirement.")

# else:
#     print("Sorry, your age does not meet the requirement.")




# Task-10: build a e-commerce discount calculator

# total_amount = float(input("Enter the total amount: "))

# if total_amount > 5000:
#     discount = total_amount * 0.15
#     print("You get a 15% discount of", discount)
#     premium_member = input("Are you a premium member? (yes/no): ")

#     if premium_member == "yes":
#         additional_discount = total_amount * 0.05
#         print("As a premium member, you get an additional 5% discount of", additional_discount)
#         print("Total discount:", discount + additional_discount)

# if total_amount <= 5000:
#     discount = total_amount * 0.05
#     print("You get a 5% discount of", discount)




# Task-11: Common grading systems in india

# choice = int(input("1. Percentage\n2. CGPA\nEnter Choice: "))

# if choice == 1:
#     percentage = float(input("Enter Percentage: "))

#     if percentage >= 90:
#         print("Grade: A+")
#     elif percentage >= 80:
#         print("Grade: A")
#     elif percentage >= 70:
#         print("Grade: B+")
#     elif percentage >= 60:
#         print("Grade: B")
#     elif percentage >= 50:
#         print("Grade: C")
#     else:
#         print("Grade: F")

# elif choice == 2:
#     cgpa = float(input("Enter CGPA: "))

#     if cgpa >= 9:
#         print("Grade: A+")
#     elif cgpa >= 8:
#         print("Grade: A")
#     elif cgpa >= 7:
#         print("Grade: B+")
#     elif cgpa >= 6:
#         print("Grade: B")
#     elif cgpa >= 5:
#         print("Grade: C")
#     else:
#         print("Grade: F")

# else:   
#     print("Invalid Choice")




#15/6/26
#assignment-1

#task-1: find maximum among two numbers

# num1 = float(input("Enter the first number : "))
# num2 = float(input("Enter the second number : "))

# if num1 > num2:
#     print(num1, "is greater than", num2)
# else:
#     print(num2, "is greater than", num1)




#task-2: that inputs a number(N) and adds 7 to N if N is odd, else add 4.

# N = int(input("Enter a number : "))

# if N % 2 == 0:
#     result = N + 4
#     print("The result after adding 4 is :", result)
# else:
#     result = N + 7
#     print("The result after adding 7 is :", result)




#task-3: to create a simple number guessing game.

# secret_number = 47 

# guess = int(input("Guess a number between 1 and 100 \n :     "))

# if guess == secret_number:
#     print("Congratulations! You guessed the correct number.")

# else:
#     print("Sorry, that's not the correct number. The secret number was", secret_number)




# task-4 : nesting (use of nesting if else statements)

# number = 5
# if number >= 0:
#     if number == 0:
#         if number == 0:
#             print("The number is zero.")
#     else:
#         print("The number is positive.")
# else:
#     print("The number is negative.")




# task-5 : that takes a number as an input and prints whether it is positive, negative, or zero.if the number is poositive, check if it is even or odd and print the result.

# number = int(input("enter the number : "))

# if number > 0 :
#     print("the number is positive")
#     if number % 2 == 0:
#         print("the number is even")
#     else:
#         print("the number is odd")
# elif number < 0:
#     print("the number is negative")
# else:
#     print("the number is zero")




# task-6 : that takes 3 numbers as input and prints the largest number among them.

# num1 = float(input("Enter the first number : "))
# num2 = float(input("Enter the second number : "))
# num3 = float(input("Enter the third number : "))

# if num1 >= num2 and num1 >= num3:
#     print(num1, "is the largest number.")
# elif num2 >= num1 and num2 >= num3:
#     print(num2, "is the largest number.")
# else:
#     print(num3, "is the largest number.")




# task-7 : that calculates the grade of a student based on their exam score.

# marks = float(input("Enter your marks : "))

# if marks >=90 and marks <= 100:
#     print("A grade")

# elif marks >= 89 and marks <=80:
#     print("B grade")

# elif marks >=79 and marks <=70:
#     print("C grade")




#task-8 : make the table.

# for i in range(1, 11):
#     for j in range(1,11):
#         print(i * j, end="\t")
#     print()




# task-9 : that uses for loop to iterate over a list of numbers and print each number square

# numbers = [1, 2, 3, 4, 5]

# for num in numbers:
#     if num % 2 == 0:
#         print(num * num)
#     else:
#         print(num * num)




#task-10 sum of all odd number between 1 to 50

# sum = 0
# num = 1

# while num <= 50:
#     if num % 2 != 0:
#         sum = sum + num
#     num = num + 1

# print("Sum of odd numbers =", sum)




#task-11 print all number from 1-50 except 7 multiples using continue to skip 7 multiples.

# for num in range(1,51):
#     if num % 7 == 0:
#         continue
#     print(num)




# task-12

# import random

# num = 0
# count = 0

# while num <= 7:
#     num = random.randint(1, 10)
#     print(num)
#     count = count + 1

# print("Total numbers generated =", count) 




# task-13

#if we want to retreive both key and value in dictionary then what we have to use.  




# task-14 : recursion

# def factorial(n):
#     if n == 1:
#         return 1
#     else:
#         return n * factorial(n-1)
    
#     print("factorial of 5 :", factorial(5)) 




# task-15 convert celsius to fahrenheit

# def celsius_to_farhenheit (c):
#     return (c * 9/5) + 32
# print(celsius_to_farhenheit (0))




# take a list and do it multplicative reverse and print the outcome.




# task-16  program to detect palidrome text.

# text = input("Enter a text: ")

# if text == text[::-1]:
#     print("Palindrome")
# else:
#     print("Not a Palindrome")




#task-17 Fibonnaci Series

# n = int(input("Enter the numbers : "))

# a = 0
# b = 1

# for i in range(n):
#     print(a, end=" ")
#     c = a + b
#     a = b
#     b = c     





#17/6/26



#task-1 library fine calculator

# n = int(input("Enter number of students: "))

# total = 0
# highest = 0

# for i in range(n):
#     print("\nStudent", i + 1)

#     name = input("Enter student name: ")
#     days = int(input("Enter days late: "))

#     if days <= 5:
#         fine = days * 5
#     elif days <= 10:
#         fine = days * 10
#     else:
#         fine = days * 20

#     print("Name:", name)
#     print("Fine:", fine)

#     total = total + fine

#     if fine > highest:
#         highest = fine

# average = total / n

# print("\nTotal Fine Collected =", total)
# print("Highest Fine =", highest)
# print("Average Fine =", average)





#rough work
# numbers = [10, 20, 30, 40, 50]

# for num in numbers:
#     print(num)


# a=[1,2]
# b=[4,5]

# for i in a:
#     for j in b:
#         print(a,b)



# for i in [10,20]:
#     for j in [11,20]:
#         print(i,j)



# for i in range(1,5):
#     for j in range(1, 11):
#         print(i, "x", j, "=", i * j)
#     print()




# for i in range(1, 4):
#     for j in range(1, 4):
#             continue
#     print(i,j)


# b=[5,12,7,18,3,20]

# for i in b:   
#       print(b,if b > 10)



# res=listmany val for row in mat




# num = int(input("Enter a number: "))

# for i in range(1, 11):
#     if i == 5:
#         continue
#     print(num, "x", i, "=", num * i)



# for i in range(1, 6):
#     for j in range(1, i + 1):
#         print("*", end=" ")
#     print()






# 18/6/26




#task-2 student perfomance analyser

# def student_report(name, marks):
#     print("\n----- Student Report -----")
#     print("Name :", name)
#     print("Marks:", marks)

# def add_bonus(marks):
#     marks = marks + 5
#     print("Inside Function Marks:", marks)

# def sum_marks(n):
#     if n == 1:
#         return 1
#     return n + sum_marks(n - 1)

# def square(x):
#     return x * x

# def cube(x):
#     return x * x * x

# def apply_operation(func, value):
#     return func(value)

# name = input("Enter Student Name: ")
# marks = int(input("Enter Marks: "))

# student_report(name, marks)

# add_bonus(marks)
# print("Outside Function Marks:", marks)

# n = int(input("Enter a number for recursive sum: "))
# print("Recursive Sum =", sum_marks(n))

# print("\nChoose Operation")
# print("1. Square")
# print("2. Cube")
    
# choice = int(input("Enter Choice: "))
# num = int(input("Enter Number: "))

# if choice == 1:
#     operation = square
# elif choice == 2:
#     operation = cube
# else:
#     print("Invalid Choice")
#     exit()

# result = apply_operation(operation, num)
# print("Result =", result)





#task-2 secret number guessing game 

# secret_number = 47

# try:
#     guess = int(input("Guess a number between 1 and 100\n: "))

#     if guess == secret_number:
#         print("Congratulations! You guessed the correct number.")

#     else:
#         print("Sorry, that's not the correct number.")
#         print("The secret number was", secret_number)

# except ValueError:
#     print("Invalid input! Please enter only numbers.")
    




#22/6/26

#task-1 movie ticket booking with valid constructor

# class Ticket:
#     def __init__(self, movie_name, available_seats, requested_seats):
#         self.movie_name = movie_name
#         self.available_seats = available_seats
#         self.requested_seats = requested_seats

#         print(f"\nMovie: {self.movie_name}")

#         if requested_seats <= available_seats:
#             self.available_seats -= requested_seats
#             print("Booking Confirmed!")
#             print("Requested Seats:", requested_seats)
#             print("Seats Left:", self.available_seats)
#         else:
#             print("Sorry! Requested seats are not available.")

# t1 = Ticket("Avengers", 100, 4)
# t2 = Ticket("Pushpa 2", 20, 25)
# t3 = Ticket("Interstellar", 50, 10)




#task -2 simulating a simple inventory  

# class Product:

#     def __init__(self, id, name, price, quantity):
#         self.id = id
#         self.name = name
#         self.price = price
#         self.quantity = quantity

#     def total_value(self):
#         return self.price * self.quantity


# data = [
#     (1, "Laptop", 50000, 2),
#     (2, "Mouse", 500, 5),
#     (3, "Keyboard", 1200, 3)
# ]

# products = []

# for i in data:
#     p = Product(i[0], i[1], i[2], i[3])
#     products.append(p)

# grand_total = 0

# for p in products:
#     print("ID:", p.id)
#     print("Name:", p.name)
#     print("Total Value:", p.total_value())
#     print()

#     grand_total = grand_total + p.total_value()

# print("Total Inventory Value =", grand_total)



#23/6/26

#Task- Class Methods and Static Methods


# class Employee:
#     company = "KRM Corp"      # class variable
#     _count = 0                # protected class variable

#     def __init__(self, name, dept):
#         self.name = name
#         self.dept = dept
#         Employee._count += 1

#     @classmethod
#     def get_count(cls):
#         return f"{cls.company} has {cls._count} employees"

#     @staticmethod
#     def validate_dept(dept):
#         valid = ["CSE", "ECE", "MBA", "MCA"]
#         return dept in valid

# e1 = Employee("Alice", "CSE")
# e2 = Employee("Bob", "ECE")

# print(Employee.get_count())

# print(Employee.validate_dept("CSE"))




#Task- Secure student record

# class Student:
#     count = 0

#     def __init__(self, roll_no, marks, grade):
#         self.__roll_no = roll_no
#         self._grade = grade
#         self.marks = marks
#         Student.count += 1

#     @property
#     def gpa(self):
#         avg = sum(self.__marks) / len(self.__marks)
#         return avg / 10

#     @property
#     def marks(self):
#         return self.__marks

#     @marks.setter
#     def marks(self, value):
#         for m in value:
#             if m < 0 or m > 100:
#                 raise ValueError("Marks must be between 0 and 100")
#         self.__marks = value

#     @classmethod
#     def count_students(cls):
#         return cls.count


# s1 = Student(1, [80, 90, 85], "A")
# s2 = Student(2, [70, 75, 80], "B")

# print("Student 1 GPA:", s1.gpa)
# print("Student 2 GPA:", s2.gpa)
# print("Total Students:", Student.count_students())




#Task- Library book manager

# class Book:

#     def __init__(self, isbn, title, author, copies):
#         self.__isbn = isbn         
#         self._title = title         
#         self._author = author       
#         self.__copies = copies      

#     @property
#     def available(self):
#         return self.__copies

#     def checkout(self, n):
#         if n > self.__copies:
#             raise ValueError("Not enough copies available")
#         self.__copies -= n

#     def return_book(self, n):
#         if n <= 0:
#             raise ValueError("Invalid number of books")
#         self.__copies += n


# b1 = Book("97812345", "Python Basics", "Rahul Sharma", 10)

# print("Available Copies:", b1.available)

# b1.checkout(3)
# print("After Checkout:", b1.available)

# b1.return_book(2)
# print("After Return:", b1.available)



#task- ATM machine simulator

class Account:

    def __init__(self, owner, pin, balance):
        self._owner = owner          # protected
        self.__pin = pin             # private
        self.__balance = balance     # private
        self.__login = False

    def authenticate(self, pin):
        if pin == self.__pin:
            self.__login = True
            print("Login Successful")
        else:
            print("Wrong PIN")

    @property
    def balance(self):
        return self.__balance

    def deposit(self, amount):
        if self.__login:
            self.__balance = self.__balance + amount
            print("Amount Deposited")
        else:
            print("Please login first")

    def withdraw(self, amount):
        if self.__login:

            if amount > 20000:
                print("Maximum withdrawal is 20000")
                return

            if amount > self.__balance:
                print("Insufficient Balance")
                return

            self.__balance = self.__balance - amount
            print("Amount Withdrawn")

        else:
            print("Please login first")

    def mini_statement(self):
        if self.__login:
            print("Owner :", self._owner)
            print("Balance :", self.__balance)
        else:
            print("Please login first")

a1 = Account("Vats", 1234, 50000)

a1.authenticate(1234)

a1.deposit(5000)
a1.withdraw(10000)

print("Current Balance:", a1.balance)

a1.mini_statement()