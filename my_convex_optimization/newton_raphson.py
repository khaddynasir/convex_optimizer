def find_root_newton_raphson(f, f_deriv, x0, tol=0.001, max_iter=1000, damping=0.1):
    x = x0
    for _ in range(max_iter):
        fx = f(x)
        if abs(fx) < tol:
            return x
        fdx = f_deriv(x)
        if fdx == 0:
            raise ValueError("Zero derivative encountered, stopping iteration.")
        x -= damping * (fx / fdx)  # Apply reduced damping factor
    return x