n=int(input("enter the number"))
original=n
reverse=0

while n>0:
    digit=n%10
    reverse=reverse*10+digit
    n=n//10

if reverse==original:
    print("number is palindrome")
else :
    print("number is not palindrome")