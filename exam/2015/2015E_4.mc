ga:0.5*sqrt(exp(x));
gb:exp(x)/(4*x);
gc:(-0.5)*sqrt(exp(x));
dga:diff(ga,x);
dgb:diff(gb,x);
dgc:diff(gc,x);
plot2d([abs(dga),abs(dgb),abs(dgc)],[x,-2,6],[y,0,1]);
