f:exp(x)-x-5;
plot2d(f,[x,-6,3],[y,-4,4]);
float(subst([x = -6],f));
float(subst([x = -4],f));
float(subst([x = +1],f));
float(subst([x = +3],f));
