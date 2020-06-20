g2:log(5+x);
dg2:diff(g2,x);
f:exp(x)-x-5;
g3:x-f/diff(f,x);
dg3:diff(g3,x);
plot2d([abs(dg2),abs(dg3)],[x,-5,5],[y,0,1]);
plot2d([g2,g3,1.9368],[x,0,20],[y,0,20]);
plot2d([g2,g3,1.9368],[x,1.85,2],[y,1.92,1.95]);