from source.quadrature.monte_carlo import monte_carlo
print(monte_carlo(lambda x: x**2 - 4, 2, 10, 10**(-5), 42, 220000))