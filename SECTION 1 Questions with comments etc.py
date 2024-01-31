#Part 1 compulsory questions 

#Question 1 
""""
Write a Python function relative_error(true_value, approx_value) that 
takes two arguments: true_value (the exact value) and approx_value (the approximate value),
and returns the relative error.
"""

def relative_error(true_value, approx_value):
    """
    Calculate the relative error between true_value and approx_value.

    Parameters:
    true_value (float): The exact value.
    approx_value (float): The approximate value.

    Returns:
    float: The relative error.
    """
    # Ensure that true_value is not zero to avoid division by zero
    if true_value == 0:
        raise ValueError("true_value cannot be zero for relative error calculation.")
    
    # Calculate the relative error
    error = abs(true_value - approx_value) / abs(true_value)

    return error

# Example usage:
true_value = 10.0
approx_value = 9.5

error = relative_error(true_value, approx_value)
print(f"Relative Error: {error}")



#Question 2
"""
Given a system of linear equations represented 
by a matrix A and a vector b, write a Python function using NumPy to find the vector x such that Ax = b. 
Test your function with a 3x3 matrix and a 3x1 vector.

"""
import numpy as np

def solve_linear_system(A, b):
    """
    Solve the linear system Ax = b using NumPy.

    Parameters:
    A (numpy.ndarray): Coefficient matrix.
    b (numpy.ndarray): Right-hand side vector.

    Returns:
    numpy.ndarray: Solution vector x.
    """
    # Use numpy.linalg.solve to find the solution
    x = np.linalg.solve(A, b)
    
    return x

# Example usage:
A = np.array([[-1, 1, 1],
              [1,  -1, 1],
              [1,  1, -1]])

b = np.array([1, 2, 3])

# Solve the system
solution = solve_linear_system(A, b)

print("Coefficient Matrix A:")
print(A)

print("\nRight-hand side Vector b:")
print(b)

print("\nSolution Vector x:")
print(solution)


#Question 3
"""
Implement the bisection method for finding roots of a continuous function. 
Your Python function bisection_method(func, a, b, tolerance) should take a function func, an interval [a, b], and a tolerance value, 
and return the root of the function within the given interval and tolerance.
"""


def bisection_method(func, a, b, tolerance):
    """
    Find the root of a continuous function within the interval [a, b] using the bisection method.

    Parameters:
    func (callable): The continuous function for which the root is to be found.
    a (float): Left endpoint of the interval.
    b (float): Right endpoint of the interval.
    tolerance (float): Tolerance value for stopping the iteration.

    Returns:
    float: The approximate root of the function within the given interval and tolerance.
    """
    if func(a) * func(b) > 0:
        raise ValueError("The function values at the interval endpoints must have opposite signs.")

    while (b - a) / 2 > tolerance:
        c = (a + b) / 2
        if func(c) == 0:
            return c
        elif func(c) * func(a) < 0:
            b = c
        else:
            a = c

    return (a + b) / 2

# Example usage:
def quadratic_function(x):
    return x**2 - 4

# Find the root of the quadratic function within the interval [0, 3] with tolerance 0.0001
root = bisection_method(quadratic_function, 0, 3, 0.0001)
print("Approximate Root:", root)

#Question 4
"""
Write a Python function euler_method(func, y0, x0, h, n) to solve the first-order ODE dy/dx = func(y, x) using Euler's method. 
The function should take the differential equation func, initial condition y0 at x0, step size h, and number of steps n, 
and return the approximate value of y at x0 + n*h. 
"""
def euler_method(func, y0, x0, h, n):
    """
    Solve the first-order ODE dy/dx = func(y, x) using Euler's method.

    Parameters:
    func (callable): The function representing the ODE dy/dx = func(y, x).
    y0 (float): Initial condition for y at x0.
    x0 (float): Initial value of x.
    h (float): Step size.
    n (int): Number of steps.

    Returns:
    float: Approximate value of y at x0 + n*h.
    """
    y = y0
    x = x0

    for _ in range(n):
        y += h * func(y, x)
        x += h

    return y

# Example usage:
def ode_func(y, x):
    return x * y

# Solve the ODE dy/dx = x * y with initial condition y(0) = 1, step size h = 0.1, and number of steps n = 10
result = euler_method(ode_func, 1, 0, 0.1, 10)
print("Approximate value of y at x0 + n*h:", result)

