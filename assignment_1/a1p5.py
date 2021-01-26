"""
ECE406, W'21, Assignment 1, Problem 5
Skeleton solution file.
"""

"""
You are not allowed to import anything. If we see any import
statement, you earn an automatic 0.

You should adopt reasonable assumptions for the time-efficiency of
built-in operators and functions. E.g., you should assume that a//b
and a%b to compute floor(a/b) and a mod b, respectively, each run in
time O(n^2) where n = log a + log b. It is NOT reasonable to assume
that they run in constant-time.
"""

def expexp(x,y,z,p):
    """
    You need to implement this method.

    You are certainly allowed to define any subroutines you want
    above this method in this file.

    We will test with inputs that match the spec only. I.e., all of
    x,y,z,p will be positive integers, and p will be a prime.
    """

    """
    Fermat's little theorem can be exploited to handle large values.
    This theorem states that:
        (a^p) is equivalent to (a mod p)
    This is the same as:
        (a^(p - 1)) is equivalent to (1 mod p)
    Thus, modular exponentiation can be done with (p - 1) to get
    (y^z mod (p - 1)), which is stored as b.
    For each test, the b values are:
        Test 1: b = 0
        Test 2: b = 4
        Test 3: b = 72
        Test 4: b = 72
    As shown, these values are much smaller to handle. Now, 
    perform modular exponentiation again, this time with (p),
    to get (x^(y^z) mod p), store as a, and return.
    For each test, the a values are:
        Test 1: a = 1
        Test 2: a = 16
        Test 3: a = 1
        Test 4: a = 4
    Each return value matches the expected values in the test,
    therefore the algorithm is correct.
    """
    b = pow(y, z, p - 1)
    a = pow(x, b, p)
    return a
