'''program to add febinocci series'''
a=-1
b=1
n=int(input())
sum=0
for i in range(1,n+1):
     c=a+b
     print(c)
     sum=sum+c
     a=b
     b=c
     print(sum)


10
0
0
1
1
1
2
2
4
3
7
5
12
8
20
13
33
21
54
34
88
