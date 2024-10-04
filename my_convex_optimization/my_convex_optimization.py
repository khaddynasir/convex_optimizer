import numpy as np
from bisection_method import find_root_bisection
from gradient_descent import gradient_descent
from simplex_solver import solve_linear_problem
from scipy.optimize import brentq  # Import Brent's method

# Define the function and its derivative
f = lambda x: (x - 1) ** 4 + x ** 2
f_prime = lambda x: 4 * (x - 1) ** 3 + 2 * x

# Run Bisection method
print("Finding root using bisection method:")
root_bisection = find_root_bisection(f_prime, -2, 3)
print(f"Bisection Root: {root_bisection}")

# Use Brent's method as a replacement for Newton-Raphson
print("\nFinding root using Brent's method:")
root_brent = brentq(f_prime, 0, 1)
print(f"Brent's Method Root: {root_brent}")

# Run Gradient Descent
print("\nFinding minimum using Gradient Descent:")
x_min = gradient_descent(f, f_prime, start=-1, learning_rate=0.01)
print(f"Gradient Descent Minimum: {x_min}, f(x_min): {f(x_min)}")

# Define matrix for Simplex method
A = np.array([[2, 1], [-4, 5], [1, -2]])
b = np.array([10, 8, 3])
c = np.array([-1, -2])

# Run Simplex method
print("\nSolving linear optimization problem using Simplex method:")
optimal_value, optimal_arg = solve_linear_problem(A, b, c)
print(f"Optimal value: {optimal_value}, Optimal arguments: {optimal_arg}")