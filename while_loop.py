
# i = int(input("Enter the number : "))
# while i<= 10:
#     i += 2
#     print(f"{i}")


num = int(input("Enter number : "))
temp= num 
reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 +digit
    num = num // 10

if temp == reverse :
    print("palindrome Number ")
else :
    print("not Palindrome")
