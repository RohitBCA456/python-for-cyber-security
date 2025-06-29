# num = int(input("Enter a number : "))

# def count_down(number):
#     while number > 0:
#         print(number)
#         number = number-1

# count_down(num)

# num = int(input("Enter a number : "))

# def sum_of_squares(num):
#     sum = 0
#     for i in range(1, num+1):
#         sum = sum + i**2
#         i = i+1 
#         print(sum)
        
# sum_of_squares(num)

num = int(input("Enter the number : "))

def sum_of_multiples_with_for(n):
    sum = 0
    for i in range(1, n+1):
        if i % 3 == 0 and i % 5 == 0:
            sum = sum + i**2
        else:
            continue
    return sum

print(sum_of_multiples_with_for(num))
