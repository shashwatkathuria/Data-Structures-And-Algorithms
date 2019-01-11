# -*- coding: utf-8 -*-
"""
Created on Mon Aug 27 20:52:59 2018

@author: Shashwat Kathuria
"""
# input1 = 3141592653589793238462643383279502884197169399375105820974944592
# input2 = 2718281828459045235360287471352662497757247093699959574966967627
# expectedResult = 8539734222673567065463550869546574495034888535765114961879601127067743044893204848617875072216249073013374895871952806582723184
def main():
    x = input("Enter first number : ")
    y = input("Enter second number : ")

    result = karatsuba(x, y)

    print("The multiplication  of the two numbers is : " + str(result))

def karatsuba(x,y):
    if len(str(x)) == 1 or len(str(y)) == 1:
        return x*y
    else:
        m = max(len(str(x)),len(str(y)))
        m2 = m // 2

        a = x // 10**(m2)
        b = x % 10**(m2)
        c = y // 10**(m2)
        d = y % 10**(m2)

        z0 = karatsuba(b,d)
        z1 = karatsuba((a+b),(c+d))
        z2 = karatsuba(a,c)

        return (z2 * 10**(2*m2)) + ((z1 - z2 - z0) * 10**(m2)) + (z0)

if __name__ == "__main__":
    main()
