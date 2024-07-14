# 4/3*22/7r**3 = formula
radius =float(input("Enter the radius of sphere:"))
volume = (4 / 3) * 3.1415 * (radius ** 3)
print("Volume of sphere is:", volume)
print(type(volume))

#Operators Precedence
# () ,**,/ // % ,*,+,-,bitwise shift opeators, comperision , 
a= 3+2**4/2*5-8//2
print(a)
 #tyecasting
a = 4
b = 5
c = 1
a_str = str(a)
b_str = str(b)
c_str = str(c)

final_string = a_str + b_str + c_str
final_int = int(final_string)
print("final int:", final_int, type(final_int))