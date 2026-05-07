
# simple example of function 
# def lavya():
#     print("hello my name is lavya")
# lavya()

# parameterized function in python 

# def ram(name):
#     print("my name is ",name)

# ram("mohan")



# return type of function in python 
# def add(num1,num2):
#     num3 = num1+num2
#     return num3
# result = add(10,20)
# print(result)



# def acx():
#     print("Hello world")
# acx()


# def square(n):
#     return n*n
# print(square(4))


# def check_even_odd(n):
#     return "Even" if n % 2==0 else "Odd"

# result = check_even_odd(4)
# print(result)

# def greet_name(name):
#     print("hello,",name)

#     greet_name("lavya")
# # greet_name("surya")


# # def find_max(a,b):
# #     return a if a > b else b
# # print(find_max(50,9))


# def greet_name(name):
#     print("Hello ",name)
# greet_name("Lavya")



# def check_even_odd(n):
#     return "Even" if n % 2==0 else"odd"

# def square(n):
#     return n*n
# print(square(4))

# def name():
#     print("hello world")
# #     name()
# def factorial(n):
#     fact = 1
#     for i in range(1, n+1):
#         fact *= i
#     return fact

# print(factorial(5))
# def is_palindrome(s):
#     return s == s[::-1]
# print(is_palindrome("Madam"))

# def sum_list(lst):
#     return sum(lst)
# print(sum_list([1,2,3,4]))


# def count_vowels(s):
#     vowels="aeiouAEIOU"
#     count=0
#     for ch in s:
#         count +=1
#         return count
#     print(count_vowels("Hello"))


# def even_list(lst):
#     return[x for x in lst if x%2==0]
# print(even_list([1,2,3,4,5,6]))

# def fibbonaci(n):
#     a,b=0,1
#     for n in range(n):
#         print(a,end="")
#         a,b=b,a+b
#         fibbonaci(6)

# def total_sum(*args):
#     return sum(args)
# print(total_sum(1,2,3,4))

# def sort_list(lst):
#     for i in range(len(lst)):
#         if lst[i]>lst[j]:
#             lst[i],lst[i]=lst[j],lst[i]
#             return lst
#         print(sort_list([5,2,9,1]))


# def frequency(lst):
#     frequency={}
#     for item in lst:
#         frequency[item]=frequency.get(item,0)+1
#         return frequency
#     print(frequency([1,2,2,3,3,3]))

# def is_prime(n):
#     if n<2:
#         return False
#     for i in range(2,n):
#         if n%i==0:
#             return True
#         print(is_prime(7))
    

# def reverse_string(s):
#     return[::-1]
# print(reverse_string("python"))

# def largest(lst):
#     return max(lst)

# def remove_dublicates(lst):
#     return list(set(lst))
# print(remove_dublicates([1,2,2,3,3,3,3,4,4,4,4]))


# def word_count(s):
#     return len(s.split())
# print(word_count("I love python programing"))

# def is_armstrong(n):
#     power=len(str(n))
#     total=sum(int(d)**power for d in str(n))
#     return total==n
# print(is_armstrong(153))
