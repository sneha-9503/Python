#WAP to get the area of the circle.
def area_circle(radius):
    pi=3.14159
    return pi*radius*radius
r=int(input("Enter the radius of the circle:"))
res=area_circle(r)
print(f"The Area of a circle is{res}")
