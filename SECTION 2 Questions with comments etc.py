#Section 2 Questions 

#Question 1 
"""
C(x) = ax^3 - bx^2 + cx + d

where a, b, c, and d are known coefficients based on historical data analysis.

Define the Cost Function: Implement a function cost(x) that computes the cost C(x) for a given number of units x
"""

def cost(x, a, b, c, d):
    """
    Compute the cost C(x) for a given number of units x.

    Parameters:
    x (float): Number of units.
    a, b, c, d (float): Coefficients for the cost function.

    Returns:
    float: Cost C(x).
    """
    return a * x**3 - b * x**2 + c * x + d

# Example usage:
# Assuming a=1, b=2, c=3, d=4, and x=5
result = cost(5, 1, 2, 3, 4)
print("Cost for x=5:", result)


#Question 2
"""
 Calculate the Gradient: Implement a function cost_gradient(x) that computes the derivative of the cost function, representing the gradient at a given x
"""
import sympy as sp

def cost_gradient(x, a, b, c, d):
    """
    Compute the gradient of the cost function at a given number of units x.

    Parameters:
    x (sympy.Symbol or float): Number of units.
    a, b, c, d (float): Coefficients for the cost function.

    Returns:
    float: Gradient of the cost function at x.
    """
    # Create a symbolic variable
    x_sym = sp.symbols('x')

    # Define the cost function
    cost_function = a * x_sym**3 - b * x_sym**2 + c * x_sym + d

    # Compute the derivative (gradient) with respect to x
    gradient = sp.diff(cost_function, x_sym)

    # Substitute the numerical value of x into the gradient expression
    gradient_value = gradient.subs(x_sym, x)

    return gradient_value

# Example usage:
# Assuming a=1, b=2, c=3, d=4, and x=5
result_gradient = cost_gradient(5, 1, 2, 3, 4)
print("Gradient at x=5:", result_gradient)


#Question 3
"""
Implement Gradient Descent: Write a function gradient_descent(start_x, learning_rate, iterations) 
that uses the gradient descent algorithm to find the value of x that minimizes C(x). 
The function should start from start_x, use a learning_rate to control the step size, 
and perform the optimization for a given number of iterations.

"""

def gradient_descent(start_x, learning_rate, iterations, a, b, c, d):
    """
    Use gradient descent to find the value of x that minimizes the cost function C(x).

    Parameters:
    start_x (float): Initial value of x.
    learning_rate (float): Step size for gradient descent.
    iterations (int): Number of iterations.
    a, b, c, d (float): Coefficients for the cost function.

    Returns:
    float: The optimized value of x.
    """
    current_x = start_x

    for _ in range(iterations):
        # Compute the gradient at the current_x
        gradient = cost_gradient(current_x, a, b, c, d)

        # Update x using the gradient descent formula
        current_x = current_x - learning_rate * gradient

    return current_x

# Example usage:
# Assuming a=1, b=2, c=3, d=4, learning_rate=0.1, and start_x=0
optimized_x = gradient_descent(0, 0.1, 100, 1, 2, 3, 4)
print("Optimized value of x:", optimized_x)


#Question 4
"""
Test Your Implementation: Use the coefficients a=0.01, b=1.2, c=5, and d=100. 
Start with an initial guess start_x = 10, a learning rate of 0.01, and run the gradient descent for 1000 iterations.
"""
# Given coefficients
a = 0.01
b = 1.2
c = 5
d = 100

# Initial guess and parameters
start_x = 10
learning_rate = 0.01
iterations = 1000

# Test the gradient_descent function
optimized_x = gradient_descent(start_x, learning_rate, iterations, a, b, c, d)
print("Optimized value of x:", optimized_x)


