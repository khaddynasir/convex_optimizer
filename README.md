# Welcome to My Convex Optimization
***

## Task
<p>This project tackles the problem of finding the minimum of a convex function, solving optimization problems, and exploring various root-finding algorithms. The goal is to implement several numerical methods to efficiently solve optimization and root-finding tasks, such as the Bisection Method, Gradient Descent, and Brent's Method, alongside using the Simplex algorithm for linear programming problems.</p>

<p>The challenge lies in ensuring the methods converge to the correct solution, especially in cases like the Newton-Raphson method, which can diverge if the initial guess or function behavior is unsuitable. Proper handling of derivative functions and linear constraints is also essential for accurate results in optimization tasks.</p>

## Description
<p>The problem has been solved by implementing a series of mathematical methods that address different aspects of convex optimization and root-finding. Specifically, we:</p>

<ul>
    <li><code>Bisection Method</code>: A robust method for finding the root of a function in a given interval by repeatedly dividing the interval in half and selecting the subinterval where the sign of the function changes.</li>
    <li><code>Brent's Method</code>: A more efficient combination of the Bisection method, secant method, and inverse quadratic interpolation to find roots, ensuring both stability and speed.</li>
    <li><code>Gradient Descent</code>: Used to find the minimum of a convex function by iteratively moving in the direction of the negative gradient with a specified learning rate.</li>
    <li><code>Simplex Method</code>: Solves linear programming problems by iterating over vertices of the feasible region (polytope) and finding the optimal solution for the objective function.</li>
</ul>

<p>The solution uses Python's numerical libraries such as <code>numpy</code> and <code>scipy</code> for efficient computation and optimization routines. The code is modular, allowing each method to be tested and verified independently.</p>

## Installation
<p>To install and run the project, you need to have Python installed along with the necessary libraries.</p>

<p>To install the required dependencies, run the following command:</p>

<pre>
<code>pip install numpy scipy matplotlib</code>
</pre>

<p>No additional build steps are required; the Python files can be run directly in the terminal or integrated into larger projects.</p>

## Usage
<p>After installing the required libraries, you can execute the project by running <code>my_convex_optimization.py</code>. This file ties together the various algorithms and tests their correctness. You can simply run it using the Python interpreter.</p>

<pre>
<code>python my_convex_optimization.py</code>
</pre>

<p>This will execute the following operations:</p>

<ul>
    <li>Find the root of the derivative of the function using the Bisection method.</li>
    <li>Find the root of the derivative of the function using Brent's method.</li>
    <li>Minimize the function using Gradient Descent.</li>
    <li>Solve the linear optimization problem using the Simplex method.</li>
</ul>

<p>Each method will print its results to the console, including the root found, minimum value, and the optimal solution for the linear programming problem.</p>

### The Core Team


<span><i>Made at <a href='https://qwasar.io'>Qwasar SV -- Software Engineering School</a></i></span>
<span><img alt='Qwasar SV -- Software Engineering School's Logo' src='https://storage.googleapis.com/qwasar-public/qwasar-logo_50x50.png' width='20px' /></span>
