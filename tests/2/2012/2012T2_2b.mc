A:matrix([4.8,-1.0,-1.0,1.0],[-1.0,4.8,1.0,-1.0],
         [-1.0,2.0,4.8,-1.0],[2.0,-1.0,-1.0,4.8]);
A_:abs(A);
s:2*matrix([A_[1][1]],[A_[2][2]],[A_[3][3]],[A_[4][4]])
  -map(lambda([r],[lsum(x,x,r)]),A_);