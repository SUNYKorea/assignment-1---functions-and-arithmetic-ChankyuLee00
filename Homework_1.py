# Name: Chankyu Lee
# SBUID: 112980557

# Remove the ellipses (...) when writing your solutions.

# ---------------------------- Exercise I ---------------------------------------
# ----------------- Convert Fahrenheit to Celsius -------------------------------
# TODO: Complete the implementation of fahrenheit2celsius () and what_to_wear(). 

def fahrenheit2celsius(fahrenheit): 
   F_temp= float(input("Input the Fahrenheit: "))
   C_temp= (F_temp - 32) * 5/9

   print("Fahrenheit is converted to celsius:")
   print(C_temp)
   #print("{F_temp} is same as {C_temp}") 

def what_to_wear(celsius):
   Temp_input= float(input("What's the current temperature in Celsius?:"))

   if Temp_input < -10:
       print("puffy jacket")
   elif -10<Temp_input<0:
       print("Scarf") 
   elif 0< Temp_input <10:
       print("Sweater")
   elif 10<Temp_input<20:
       print("Light jacket")
   elif Temp_input>20:
       print("T-Shirt")





# ---------------------------- Exercise II --------------------------------------
# ----------------- Area and perimeter of a triangle  ---------------------------
# TODO: Fill the functions shoelace_triangle_area, euclidean_distance and
# compute_triangle_perimeter from scratch  

def shoelace_triangle_area(x1, y1, x2, y2, x3, y3):
    ...

def euclidean_distance(x1, y1, x2, y2):
    ...

def compute_triangle_perimeter(x1, y1, x2, y2, x3, y3):
    ...


# ---------------------------- Exercise III -------------------------------------
# ----------------- Compute the area of a regular polygon -----------------------
# TODO: Fill the functions deg2rad, apothem  and polygon_area 


def deg2rad(deg):
    ...

def apothem(number_sides, length_side):
   ...

def polygon_area(number_sides, length_side):
   ...


# ---------------------------- Test -------------------------------------
# The following lines are for testing purposes, and will not be part of
# your grade. You may freely modify the following codes.

# Exercise 1 test
fahrenheit = 40
what_to_wear(fahrenheit2celsius(fahrenheit))

# Exercise 2 test
x1, x2, x3, y1, y2, y3 = -4, -5, 3, -4, 5, -3 # declaration of the vertices of the triangle
area = shoelace_triangle_area(x1, y1, x2, y2, x3, y3)
perimeter = compute_triangle_perimeter(x1, y1, x2, y2, x3, y3)
print("The area of the triangle is : " + str(area) + " , its perimeter is : " + str(perimeter) )

# Exercise 3 test
number_sides = 5
length_side = 4
print ("The area of the polygon is : " + str(polygon_area(number_sides, length_side)))

