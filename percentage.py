#WAP to accept percentage from user and make a decision whether he got O grade,first class,second class or failed
percentage = float(input("Enter your percentage: "))
if (percentage >= 80):
    print("You got O grade")
elif (percentage >= 60):
    print("You got First Class")
elif (percentage >= 40):
    print("You got Second Class")
else:
    print("You have failed.")
