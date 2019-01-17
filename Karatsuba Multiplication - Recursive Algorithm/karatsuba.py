# -*- coding: utf-8 -*-
"""
Created on Mon Aug 27 20:52:59 2018

@author: Shashwat Kathuria
"""
# input1 = 3141592653589793238462643383279502884197169399375105820974944592
# input2 = 2718281828459045235360287471352662497757247093699959574966967627
# expectedResult = 8539734222673567065463550869546574495034888535765114961879601127067743044893204848617875072216249073013374895871952806582723184
def main():

    # Prompting user for input numbers
    x = input("Enter first number : ")
    y = input("Enter second number : ")

    # Calling karatsuba multiplication function on the inputs
    result = karatsuba(x, y)

    # Printing the result (multiplication of the numbers)
    print("The multiplication  of the two numbers is : " + str(result))

def karatsuba(x,y):
    """Karatsuba Algorithm function to compute the multiplication of two numbers. Input x,y are the
       numbers to be multiplied."""

    # x = a x 10**power + b
    # y = c x 10**power + d
    # x * y = (a x 10**power + b) x (c x 10**power + d) =  ac * 10**(2*power) + (ad+bc) * 10**(power) + bd
    # where ad + bc = [(a + b) * (c + d)] - ac - bd

    # Base case
    if len(str(x)) == 1 or len(str(y)) == 1:
        return x * y

    else:

        # Converting into power format plus an offset term as shown above
        maxNoOfDigits = max(len(str(x)),len(str(y)))
        power = maxNoOfDigits // 2

        # Computing coefficients
        a = x // 10 ** (power)
        b = x % 10 ** (power)
        c = y // 10 ** (power)
        d = y % 10 ** (power)

        # Recursively calling to compute the required terms
        bd = karatsuba(b, d)
        aPlusb_cPlusd = karatsuba( (a + b), (c + d) )
        ac = karatsuba(a, c)

        # Returning the result
        return (ac * 10**(2*power)) + ((aPlusb_cPlusd - ac - bd) * 10**(power)) + (bd)

if __name__ == "__main__":
    main()
