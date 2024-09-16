import sympy as sp

# Definindo a variável e a função
x = sp.Symbol('x')
func = sp.sin(x)

# Calculando a integral
integral = sp.integrate(func, x)

# Exibindo o resultado
print(f"A integral de sin(x) é: {integral}")
