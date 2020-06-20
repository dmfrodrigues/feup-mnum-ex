g1:exp(x)-5;
g2:log(5+x);
dg1:diff(g1,x);
dg2:diff(g2,x);
plot2d([abs(dg1),abs(dg2)],[x,-10,5],[y,0,1]);
