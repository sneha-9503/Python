#WAP to check whether the number is palindrome number or not inputnum=232 rev=232 if both are equal then it is palindrome
rev=0
num=int(input("Enter the number:"))                           
temp=num
while(num>0):
    rem=num%10
    rev=rev*10+rem
    num=num//10
    print(rev)
print("The Reverse number is",rev)
if(rev==temp):
    print("The number is palindrome")
else:
    print("The number is not palindrome")
