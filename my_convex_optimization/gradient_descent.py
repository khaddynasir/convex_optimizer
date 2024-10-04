def gradient_descent(f, f_prime, start, learning_rate=0.1, tol=0.001, max_iter=1000):
    x = start
    for i in range(max_iter):
        grad = f_prime(x)
        x_new = x - learning_rate * grad
        if abs(x_new - x) < tol:
            break
        x = x_new
    return x