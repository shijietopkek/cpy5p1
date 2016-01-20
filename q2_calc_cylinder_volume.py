# q2_calc_cylinder_volume.py

# get input
Radius = float(input("Enter Radius of cylinder (cm): "))
Length = float(input("Enter Length of cylinder (cm): "))

from math import pi

# determine volume
Volume = Radius*Radius*Length* pi

# output result
print("Volume of cylinder (cm^3)=", Volume)
