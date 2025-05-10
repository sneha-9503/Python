#WAP to reverse the given number by user
Example: n=123  output=321
rev=0
n=int(input("Enter the Number:"))
while(n>0):
    rem=n%10
    rev=rev*10+rem
    n=n//10
    print(rev)
print("The Reverse number is:",rev)
