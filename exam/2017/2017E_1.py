from math import sqrt
def f(x): return (x-9)**2+x**4
def enq_passo_variavel(f, x, h):
    fx, fxh = f(x), f(x+h)
    to_right = (fxh < fx)
    if to_right: a, b, c = x, x+h/3, x+h
    else       : a, b, c = x-h, x-h/3, x
    fa, fb, fc = f(a), f(b), f(c)
    while fb != min([fa, fb, fc]):
        h *= 2
        if to_right: a, b, c, fa, fb, fc = b, c, c+h, fb, fc, f(c+h)
        else       : a, b, c, fa, fb, fc = a-h, a, b, f(a-h), fa, fb
    return (a, c)
B = (sqrt(5)-1)/2
def pesquisa_aurea(f, a, b, err):
    c, d = b-B*(b-a), a+B*(b-a)
    fc, fd = f(c), f(d)
    while b-a >= err:
        if fc <= fd: b, d, c = d, c, d-B*(d-a); fc, fd = f(c), fc
        else       : a, c, d = c, d, c+B*(b-c); fc, fd = fd, f(d)
    return (a, b)
def ajuste_quadratico(f, a, b):
    x2 = (a+b)/2
    f1, f2, f3 = f(a), f(x2), f(b)
    return x2+(b-a)*(f1-f3)/(f3-2*f2+f1)
x, h = 0, 0.001
a, b = enq_passo_variavel(f, x, h)
print("Limites do intervalo: %.5f %.5f"%(a, b))
a, b = pesquisa_aurea(f, a, b, 1e-10)
print("Limites do intervalo reduzido: %.15f %.15f"%(a, b))
sol = ajuste_quadratico(f, a, b)
print("Minimo: %.15f"%sol)
