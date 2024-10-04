def find_root_bisection(f, a, b, tol=0.001):
    if f(a) * f(b) >= 0:
        raise ValueError("Bisection method requires the function to change signs over the interval.")
    while (b - a) / 2.0 > tol:
        midpoint = (a + b) / 2.0
        if f(midpoint) == 0:
            return midpoint
        elif f(a) * f(midpoint) < 0:
            b = midpoint
        else:
            a = midpoint
    return (a + b) / 2.0