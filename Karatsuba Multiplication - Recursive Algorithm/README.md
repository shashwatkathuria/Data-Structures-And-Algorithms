# KARATSUBA'S RECURSIVE MULTIPLICATION ALGORITHM
---------------------------------------------------
INSTRUCTIONS TO RUN THE PROGRAM
---------------------------------------------------

The following command must be executed to run the program:

        python karatsuba.py

---------------------------------------------------
ALGORITHM
---------------------------------------------------

In Karatsuba's Algorithm, two numbers are multiplied recursively in such
a way that it is more efficient than the naive O(n ^ 2) approach. The
multiplication of each term requires 3 computations rather than 4 as in
the naive iterative approach. Some multiplications are used to reduce the
calculation as shown in the following lines:

    x = a x 10^power + b
    y = c x 10^power + d
    x * y = (a x 10^power + b) x (c x 10^power + d) =  ac * 10^(2 * power) + (ad + bc) * 10^(power) + bd
    where  ad + bc = [(a + b) * (c + d)] - ac - bd
           power = max number of digits of any of the two numbers divided by 2 and converted to integer

The run time complexity of this algorithm is O( n ^ log3(base2) ) according to the Master's Theorem.

-----------------------------------------------------
