'''
Given a  number int_input, find the product of all the digits

'''
NUM = int(input())
I = 1
while I<abs(NUM):
   A = NUM%10
   I = A*I
   NUM = NUM//10
   
print(I)    

