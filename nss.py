# 1) Write a program in Python to display the cube of the number upto given an integer. Go to the editor
# n = int(input())
# for i in range(1, n + 1):
#    print("Number is :", i, "and cube of the", i, "is :", i**3 )

# 2) Print list in reverse order using a loop
# n = input().split()
# print(sorted(n, reverse = True))

# 3)Find the factorial of a given number
# n = int(input())
# fct = 1
# for i in range(2, n + 1):
#     fct *= i
# print(fct)

# 4) Calculate the sum of all numbers from 1 to a given number
# n = int(input())
# sum = 0
# for i in range(1, n+1):
#     sum += i
# print(sum)

# 5) Given an integer x, return true if x is palindrome integer.
# n = int(input())
# num_1=n
# pal = 0
# while(n!=0):
#     digit = n%10
#     pal = pal*10 + digit
#     n=int(n/10)
# if(pal==num_1):
#     print("true")
# else:
#     print("false")



# 1) Write a program to use for loop to print the following reverse number pattern
# n = int(input())
# for i in range(n):
#     for j in range(n-i):
#         print(n-i-j,end=" ")
#     print()

# 2) Write a program to use for loop to print the following number pattern
# n = int(input())
# for i in range(n+1):
#     for j in range(i):
#         print(i,end=" ")
#     print()

# 1) get_discount
# print((lambda a, b: a - (a * b/100))(1500, 50))
# print((lambda a, b: a - (a * b/100))(89, 20))
# print((lambda a, b: a - (a * b/100))(100, 75))

# 2) sum_numbers
# print((lambda a: a*(a+1)/2)(5))
# print((lambda a: a*(a+1)/2)(1))
# print((lambda a: a*(a+1)/2)(12))

# 3) is_triplet
# print((lambda a, b, c: "true" if ((a**2 + b**2) == c**2) else "false")(3, 4, 5))
# print((lambda a, b, c: "true" if ((a**2 + b**2) == c**2) else "false")(5, 12, 13))
# print((lambda a, b, c: "true" if ((a**2 + b**2) == c**2) else "false")(1, 2, 3))




