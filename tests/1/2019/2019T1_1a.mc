f:exp(x)-x-11;
plot2d(f,[x,-15,5],[y,-10,10]);
float(subst([x = -12],f));
float(subst([x = -10],f));
float(subst([x = 2],f));
float(subst([x = 3],f));
