import cmath
print("the first value is the x squared value second value is the x value and the third value is the constant ")
a=int(input("enter the first value "))
b=int(input("enter the second value "))
c=int(input("enter the constant value "))
if a==0:
    print('that is not a quadratic equation')
if b and c ==0:
    print("please enter a valid eqution")
else:
    product=4*a*c
    subtraction=b**2-product
    if subtraction<=0:
       subtraction=+2*subtraction
    if subtraction<=0:
        print("The equation that you provided has a negative roots ")
    else:
        square_root=cmath.sqrt(subtraction)
        if b>=0:
          numerator_a=b+square_root
          numerator_b=b-square_root
        else:
          numerator_a=-b+square_root
          numerator_b=-b-square_root
        print("The roots of the equation" ,a, "x^2 + " ,b, "x +" ,c, "are" + "1." , numerator_a/2*a , "2." ,numerator_b/2*a)
        print (-2**2)


