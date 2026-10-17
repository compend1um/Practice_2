from source.quadrature.monte_carlo import monte_carlo
print(monte_carlo(lambda x: x**2 - 4, 2, 3, 10**(-3), 2, 220000))