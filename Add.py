program to add 1 to n odd numbers
n=int(input('enter the number'))
sum=0
for i in range(1,n+1):
    i%2==1
    sum=sum+i
    print(sum,end=" ")

 enter the number20
1 3 6 10 15 21 28 36 45 55 66 78 91 105 120 136 153 171 190 210




#program to add 1to n even numbers
n=int(input('enter the number'))
sum=0
for i in range(1,n+2):
     if i%2==0:
      sum=sum+i
      print(sum,end=" ")


enter the number10
2 6 12 20 30
