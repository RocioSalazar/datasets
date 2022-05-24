import matplotlib.pyplot as plt


def f(x, y):
    return x/y


def runge_kutta(x, y, n, h):

    print('\n--------SOLUCIÓN--------')
    print('')
    print('x(n)\ty(n)\ty(n+1)')
    print('-------------------------')
    ejex = [x]
    ejey = [y]
    for i in range(n):
        k1 = f(x, y)
        k2 = f(x + h/2, y + k1 * h/2)
        k3 = f(x + h/2, y + k2 * h/2)
        k4 = f(x + h, y + k3 * h)
        yi = y+1/6*(k1+2*k2+2*k3+k4)*h
        print('%.4f\t%.4f\t%.4f' % (x, y, yi))
        print('-------------------------')
        y = yi
        x = x+h

        ejex.append(x)
        ejey.append(y)

    plt.plot(ejex, ejey)
    plt.scatter(ejex, ejey)
    plt.title('Runge-Kutta')
    plt.show()

# Inputs
print('Ingrese los valores iniciales')
x = float(input('valor inicial de x = '))
y = float(input('valor inicial de y = '))

print('Ingrese el número de iteraciones:')
n = int(input('Número de iteraciones = '))

runge_kutta(x, y, n, 0.1)

# runge_kutta(1, 3, 4, 0.1)