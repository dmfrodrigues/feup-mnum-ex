from math import log, exp
def iterate(x, g):
    i = 0
    while True:
        x_prev = x; x = g(x); i += 1
        if(abs((x-x_prev)/x)) < 1e-10: break
    return (x, i)
def g2(x): return log(5.0+x)
def g3(x): return ((x-1.0)*exp(x)+5.0)/(exp(x)-1.0)
guess1, guess2 = 1.9, 20.0
s2_1 = iterate(guess1, g2); s2_2 = iterate(guess2, g2)
s3_1 = iterate(guess1, g3); s3_2 = iterate(guess2, g3)
print("x1 = %.10f"%iterate(-5,g3)[0])
print("x2 = %.10f"%s2_1[0])
print("Guess = \t%.5f\t%.5f"%(guess1, guess2))
print("Formula 2: \t%d\t%d"%(s2_1[1], s2_2[1]))
print("Formula 3: \t%d\t%d"%(s3_1[1], s3_2[1]))