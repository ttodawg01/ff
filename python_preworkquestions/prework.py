#question 1 Write a function to print "hello_USERNAME!" USERNAME is the input of the function. 
# The first line of the code has been defined as below. def hello_name(user_name):

def hello_name(user_name):
    input("What is your name? ")
if "user_name":
    print("Hello_USERNAME!")





#question2 Write a python function, first_odds that prints
#  the odd numbers from 1-100 and returns nothing def first_odds():


start, end = 0, 99
for num in range(start, end + 1):
    if num % 2 != 0:
        print(num, end = " ")



#question3 Please write a Python function, max_num_in_list to return the max number of a given list. 
# The first line of the code has been defined as below. def max_num_in_list(a_list):

max_num_in_list = [1,2,5,10]
print("\nLargest element is:", max(max_num_in_list))


#Question 4
#Write a function to return if the given year is a leap year. A leap year is divisible by 4, 
# but not divisible by 100 unless it is also divisible by 400. 
#The return should be boolean Type (true/false). def is_leap_year(a_year):

def is_leap_year():
    print(2012 % 4)
    if 2012 % 4 == 0:
        print(True)
    if 2012 % 100 == 0:
        print(True)
print(is_leap_year())



#Question 5

#Write a function to check to see if all numbers in the list 
#are consecutive numbers. For example, [2,3,4,5,6,7] are consecutive numbers,
 #but [1,2,4,5] are not consecutive numbers. The return 
 #should be boolean Type. def is_consecutive(a_list):

def is_consecutive():
    list=[2,3,5,6,7]
    if list % 