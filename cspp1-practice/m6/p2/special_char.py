'''
Replace all the special characters(!, @, #, $, %, ^, &, *) in a given string with a space.
example : ab!@#cd is the input, the output is ab   cd
Output has three spaces, which are to be replaced with these special characters
'''
def main():
    '''
    Read string from the input, store it in variable str_input.
    '''
str_input = input()
X=0
Y=0
Z=0
j=0
A=[a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z]
B=[A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z]
C=['!','@','#','$','%','^','&','*','(',')','+']
I=("")
for char in str_input:
    print(char)
while(X<len(char)):
     if char[j]==A[X] or char[j]==B[Y]:
        X=X+1
        Y=Y+1
        j=j+1
        print(char)
   if char[j]==C[Z]:
      char[Z]=I
      print(char)
   
 
print(char)
    
