#WAP to check whether the number is armstrong or not(Ex:153=1^3+5^3+3^3=3+125+27=153)
arm=0
n=int(input("Enter the number:"))
temp=n
while(n>0):
    rem=n%10
    arm=arm+rem*rem*rem
    n=n//10
print("The addition of the number is:",arm)
if(arm==temp):
    print("The number is armstrong")
else:
    print("The number is not an armstrong")
