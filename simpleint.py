#WAP to Calculate a simple interest (Accept the principal amount from user, Number of years from user but don't accept the rate of interest from user)

principal=int(input("Enter the Principal amount:"))#Accept principal amount from user
year=int(input("Enter the number of year:")) #Accept number of year from user
rate=5.0 
simpleinterest= (principal*year*rate)/100 #Apply the simple Interest formula
print("The Simple Interest is:",simpleinterest)
