from scipy.optimize import linprog

def solve_linear_problem(A, b, c):
    res = linprog(c, A_ub=A, b_ub=b, method='simplex')
    return res.fun, res.x