A :matrix([4.5,-1,-1,1],[-1,4.5,1,-1],[-1,2,4.5,-1],[2,-1,-1,4.5]);
A_:abs(A);
s :map(lambda([r],[lsum(x,x,r)]),A_);
d :s-[A_[1][1],A_[2][2],A_[3][3],A_[4][4]];