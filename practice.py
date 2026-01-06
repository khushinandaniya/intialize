# n = int(input("Enter a number: "))
# sum = 0

# for i in range(1,n+1):
#     sum = sum+i

# print("sum of first " , n," number is" , sum)


# for i in range(2,51,2):
#     print(i, end=" ")



# def square(n):
#     return n*n

# num = int(input("Enter a number: "))
# result = square(num)
# print("The square of", num, "is", result)


# def prime(n):
#     if n<=1:
#         return False
#     else:
#         for i in range(2,int(n*0.5)+1):
#             if n%i==0:
#                 return False
#         return True
    

# num = int(input("Enter a number: "))
# if prime(num):
#     print(num, "is a prime number")
# else:
#     print(num, "is not a prime number")


# count =0
# for i in range(1,101):
#     if(i%3==0):
#         count = count + 1

# print("Total numbers divisible by 3 between 1 and 100 are:", count)


def even_odd(*args):
    E = 0
    O = 0
    for i in args :
        if(i%2 == 0):
            E = E + 1
        else:
            O = O + 1
    
    print("Even numbers:", E)
    print("Odd numbers:", O)

even_odd(23,98,43,77,66,42,47,99,31)

print("changes made from github")


    



