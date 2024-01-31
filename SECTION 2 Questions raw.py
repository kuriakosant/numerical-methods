#Section 2 

#Question 1
def cost(x, a, b, c, d):
    return a * x**3 - b * x**2 + c * x + d

# Example usage:
# Assuming a=1, b=2, c=3, d=4, and x=5
result = cost(5, 1, 2, 3, 4)
print("Cost for x=5:", result)

#Question 2
import sympy as sp
def cost_gradient(x, a, b, c, d):
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
def gradient_descent(start_x, learning_rate, iterations, a, b, c, d):
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




