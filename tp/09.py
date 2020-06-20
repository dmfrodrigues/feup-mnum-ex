import math

def func(x):
    return (math.sin(x))**2

def enquadramento_passo_constante(f, guess, h):
    right = (f(guess-h) > f(guess))
    if right: l, m, r = guess      , guess + h, guess + 2*h
    else    : l, m, r = guess - 2*h, guess - h, guess
    fr, fm, fl = f(r), f(m), f(l)
    while min([fr, fm, fl]) != fm:
        if right: l, m, r, fl, fm, fr = m  , r, r+h, fm    , fr, f(r+h)
        else    : l, m, r, fl, fm, fr = l-h, l, m  , f(l-h), fl, fm
    return (l, r)

def enquadramento_passo_variavel(f, guess, h):
    right = (f(guess-h) > f(guess))
    if right: l, m, r = guess    , guess + h, guess+3*h
    else    : l, m, r = guess-3*h, guess-h  , guess
    fl, fm, fr = f(l), f(m), f(r)
    while min([fl, fm, fr]) != fm:
        print(l, r, r-l)
        h *= 2
        if right: l, m, r, fl, fm, fr = m    , r, r + h, fm    , fr, f(r+h)
        else    : l, m, r, fl, fm, fr = l - h, l, m    , f(l-h), fl, fm
    return (l, r)

def reducao_intervalar_tercos(f, a, b, err):
    while b-a > err:
        c , d  = a + (b-a)/3, a + (b-a)*2/3
        fc, fd = f(c)       , f(d)
        if fc < fd: b = d
        else      : a = c
    return (a, b)

B = (math.sqrt(5)-1)/2
B2 = B*B
def reducao_intervalar_aurea(f, a, b, err):
    c , d  = a + (b-a)*B2, b - (b-a)*B2
    fc, fd = f(c)       , f(d)
    while b-a > err:
        if fc < fd:
            b = d
            d, fd = c, fc
            c = a + (b-a)*B2
            fc = f(c)
        else:
            a = c
            c, fc = d, fd
            d = b - (b-a)*B2
            fd = f(d)
    return (a, b)

def ajuste_quadrica(f, l, r):
    x1, x2, x3 = l, (l+r)/2, r
    f1, f2, f3 = f(x1), f(x2), f(x3)
    h = (r-l)/2
    return x2-h*(f1-f3)/(2*(f1-2*f2+f3))

guess = 4
h = 0.1

err = 0.001

l, r = enquadramento_passo_constante(func, guess, h)
l, r = enquadramento_passo_variavel(func, guess, h)
print(l, r)
#l, r = reducao_intervalar_tercos(func, l, r, err)
l, r = reducao_intervalar_aurea (func, l, r, err)
m = ajuste_quadrica(func, l, r)
print(m)
print(m - math.pi)
