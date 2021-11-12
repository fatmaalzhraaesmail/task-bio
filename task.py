'''
problem 1
___________________________________

x=int(input("Enter Ur Number : "))
for i in range(x):
    for j in range(i,x):
        print(" ",end=" ")
    for j in range(i+1) :
        print("*",end=" ")
    print()
'''
import itertools
from heapq import merge

'''

problem 2
_________________________________

x=input("Enter Ur Statment : ")
new_statment=" "
Vowels=['i','o','u','a','e']
for chara in x:
    if chara not in Vowels:
        new_statment+=chara
    else :
        continue
print(new_statment)


'''
'''
problem 3
_________________________________

statment=input("Enter Ur Statment : ")
letter=input("Enter Letter : ")
List1=[]

print(statment)
for i in range(len((statment))):
    if statment[i]==letter:

       List1.append(i)
    else:
        continue

print(List1)

'''
'''
problem 4
_________________________________

number=int(input("Enter Ur number : "))
res=[]
Lists=[]

for i in range(number):
     x=i+1

     for z in range(x):
         z+=1
         multi=z*x
         Lists.append(multi)
     res.append(Lists)
     Lists=[]

print(res)
'''



'''
problem 5
_________________________________
import webbrowser
from random import choice
links=["https://www.google.com","https://www.youtube.com","https://www.twitter.com","https://www.w3school.com"]
webbrowser.open(choice(links))

'''

'''
problem 6
_________________________________

s1=input("Enter s1 : ")
s2=input("Enter s2 : ")
x=int(len(s1)/2)
s3=s1[:x:]
s3=
s3+s2
s3=s3+s1[x:]
print(s3)


'''

'''

problem 7
_________________________________

list1=["a","b","c"]
list2=["a","b","c"]
newlist=[]
for i in list1:
    for j in list2:
        newlist.append(i+' '+j)
print(newlist)
or
____

n=int(input("Enter num : "))
str=input("Enter Statment : ")
print( list(list(itertools.product(str, repeat=n))))
---
or 
def merge(input):
  ans = []
  for x in input:
    ans.append(x[0]+x[1])
  return ans
n=int(input("Enter num : "))
str=input("Enter Statment : ")
res=list(itertools.product(str, repeat=n))
print(merge(res))
'''
'''
problem 8
_________________________________

statment=input("Enter Statment : ")
char_cntr=0
digit_cntr=0
symbol_cntr=0
for x in statment:
    if x.isalpha():
        char_cntr+=1
    elif x.isdigit():
        digit_cntr+=1
    else:
        symbol_cntr+=1
print("Chars = ",char_cntr ,"\n","Digits = ",digit_cntr,"\n","Symbols = ",symbol_cntr)


'''

'''
problem 9
_________________________________

s1=input("s1 : ")
s2=input("s2 : ")
temp = True
for chara in s1:
    if chara in s2:
        continue
    else:
        temp=False
print(temp)

'''
'''
problem 10
_________________________________

str=input("Enter Ur String : ")
char_dic=dict()
for x in str:
    cout_num=str.count(x)
    char_dic[x]=cout_num
print(char_dic)


'''
