# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 19:22:25 2016

@author: Jally
"""


'''Question 1'''
def fibonacci (n):
    '''
    The function,fibonacci(n), calculates nth the term of the Fibonacci sequence

    parameters:
    n- a number represents nth term of fibonacci sequence
    
    returns
    the number of nth fibonacci sequence
    '''
    if n==1 or n==2:
        return 1  #set the end of recursion 
    else:
        return fibonacci(n-1)+fibonacci(n-2)#use recursion function to caculate fibonacci(n)


def index_first(n):
    '''
    The function, index_first(n), caculates the index of the first term in the 
    Fibonacci sequence to contain n digits
    
    parameters:
    n- the number of digits
    
    return
    a number that is the index of the first term in the Fibonacci sequence to contain n digits
    '''
    i=1
    j=1 #initialize two numbers of the adjacent Fibonacci sequence 
    k=1 #initialize the index of fibonacci sequence with 1
    while True: # create a loop always runnings until break
        if len(list(map(int, str(i))))==n: #as long as the number of digits is n, break the loop           
            break
        else:
            k=k+1 #every loop the index need to plus 1
            t=i
            i=j
            j=j+t #every loop i and j need to move to the next
    return k
print('the first number with 100 digits appears in %d th postion'%index_first(100))

 
 
 
 
'''Question 2'''
import os
os.chdir('/Users/Jally/GitHub/Zhang_Yichen_python')
def main():
    '''
    the function is that By starting at the top of the triangle below and moving 
to adjacent numbers on the row below, and we need to find the maximum total from 
top to bottom of the triangle in file"triangle.txt"
    '''
    tri=open("triangle.txt","r").read() #read the file as string
    tri=tri.split('\n')#split the string into list at every '\n'
    i=0 #initialize the index of column
    sum=int(tri[0]) #initialize the sum as first number
    for j in range(1,len(tri)): #cteate a loop from top to bottom
        temp=tri[j].split() #switch every row into list of numbers
        if int(temp[i])>int(temp[i+1]):  
            sum=sum+int(temp[i])
        else:
            sum=sum+int(temp[i+1])
            i=i+1   # compare the adjacent number, add the bigger one to sum and give the column number to index i   
    print('the maximum total is %d from top to bottom'%sum)
main()
    
    
    
    
    
'''Quesiton 3'''   
def collatz(n):
    '''
    the function, collatz(n),calculates the length of the Collatz chain for a given integer
    
    parameters:
    n- a given integer
    
    return
    the length of collatz chain
    '''
    i=1 #initialize length of collatz chain
    while n!=1: #keep running until n=1
        if n%2==0:
            n=n/2#if n is even, n=n/2
        else:
            n=3*n+1#if n is odd, n=3*n+1
        i=i+1 # count the length of chain
    return i
    
def main():
    '''
    to caculate which starting number, under one thousand, produces the longest chain
    '''    
    t=collatz(1)#initalize the biggest number as collatz(1)
    j=1 # initalize the index of biggest number of collatz()
    for i in range(1,1000): 
        if t<collatz(i):
            t=collatz(i) # caculate the collatz(n) from 1 to 1000, if whose collatz is bigger than t, the biggest for now, value it to t
            j=i # remember this number
        else:
            continue
    print('the number %d has longest chain with chain length: %d'%(j,t))
main()






'''Quesiton 4'''   
from decimal import *
getcontext().prec = 2000 #in order to get longer decimal part
def recur_cycle(value):
    '''
    the function, recur_cycle(value),calculates the length of the recurring cycle for a given integer 
    in the decimal representation of the unit fractions 1/value.
    
    parameters:
    value- is a arbitary number
    
    returns
    the length of recurring cycle
    '''
    tem = Decimal(1)/Decimal(value) #get the decimal representation with long decimal part
    deci=list(str(tem)) #trasfer the decimal to a list for convenient of later comparison
    if len(deci)<999:
        return 0 # if its decimal is finite, the length of recursion cycle is 0
    else:
        n=1 #initialize the length of cycle is 1
        while True:    
            if deci[10]==deci[10+n]: #compare value from 10th term because some cycles are not start from beginning, so we define the start from 10th value, if some value is same as the start, turn into next comparison 
                z=1 # z is a determine tool, if n is cycle length z=1, otherwise z=0
                for i in range(0,n):
                    if deci[10+i]==deci[10+n+i]:# as long as one value is the same as the start, then compare the every values in corresponding postions
                        continue
                    else:
                        z=0 # as long as one-pair values are not same, n is not cycle length
                        break
                if z==1:
                    return n # if it meet the request, return the cycle length n
                else:
                    n=n+1 # if n is not cycle length, set n=n=1 and go on the loop
                    continue
            else:
                n=n+1
                continue
            
def main():
    '''
    Use the function, recur_cycle(), to find the value of d < 500 for which 1/d 
    contains the longest recurring cycle in its decimal fraction part
    '''
    value=2
    max=recur_cycle(2)#initialize the max of cycle from value=2
    for i in range(3,500):#input the value from 3 to 499 
        if recur_cycle(i)>max:
            max=recur_cycle(i) # if length of its cycle is longer than max, for now, value it to max
            value=i # and remeber its value
        else:
            continue            
    print('the number %d have the longest recurring cycle with cycle length: %d'%(value,max))#max is the maximum length of recursion cycle and 'value' is its corresponding value
main()





'''
Question 5
In England the currency is made up of pound, £, and pence, p, and there are 
eight coins in general circulation: 1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p)
then,calculates how many different ways £2 can be made using any number of coins
'''
cash = [1,2,5,10,20,50,100,200] #all the currency
def coinExchangeRecursion(n, m):
     '''
     the function,coinExchangeRecursion(n,m),calculate the total ways to charge a money
     
     parameters:
     n- the total count of money
     m- the index of cash corresponding to 8 different coins
     
     return
     the total ways to change a money
     '''
     if n == 0:
         return 1 #n=0 means the money have been exactly changed, it is one end condition
     if n < 0 or m == 0:
         return 0 #that means money cannot by changed exactly through this way, it is the other end condition
     return coinExchangeRecursion(n,m-1)+coinExchangeRecursion(n-cash[m-1],m) #there are two direction of money change, one is not using current coin and directly pass current type, the other is using current coin
	
def main():
	N = 200
	count = coinExchangeRecursion(N,8) #input 8 different coins and N=200 to count the possible outcomes' number
	print('We have %d ways to change the money'%count)
	
main()






'''Question 6'''								
from math import sqrt

def Isprime(n,k):
     '''
     the function, Isprime(n,k), checks whether n is prime given the scope of divisor [1,k]
     
     parameters:
     n- a number waiting to be checked whether is prime or not
     k- a number giving the divisor's scope
     
     returns:
     1- if n is prime
     0- if n is not prime
     '''
     if k == 1:# the end condition of recursion
    		return 1
     if n%k ==0:# if n could be divided by k, n is not prime
    		return 0
     else:
    		return Isprime(n,k-1)# the recursion body

def main():
     '''
     the main function is to input a number and then check it if it's prime
     '''
     number = eval(input('Please input a POSITIVE INTEGER:'))#input a number		
     K = int(sqrt(number)) #prime test divisor can only up to square root of n
     if Isprime(number,K) == 1:
         print ('%d is a prime number!' %number)  
     else:
         print('%d is NOT a prime number!' %number)	   		
main()






'''Quesiton 7'''   
def sort(list):
    '''
    the function, sort(list), accepts a list of strings and uses recursion to 
    return a sorted list. Each step should at most modify two elements of the list.

    parameters:
    list- a list of strings
    
    return
    a list of sorted strings
    '''
    tem=list[0]#initialize a temporary string which represents biggest string later
    for i in range(1,len(list)):
        if list[i]>tem:
            tem=list[i]# read the strings one by one and give the biggest one to tem
        else:
            continue
    list.remove(tem)# remove the biggest one from list
    if list==[]:
        return [tem]# recursion end condition: if only one string left, return this one-string list
    else:
        return sort(list)+[tem]# new list will be re-sorted from small to big according to the ASCII code
sort(['you','are','good','person'])







'''Quesiton 8'''   
def result1(x,n):
    '''
    the function, result1, caculates the function f(x)=3.95*（x-x**2）through n times recursion
    
    parameters:
    x- a number in [0,1] as input
    n- the times of recursion 
    '''
    if n==1:
        return 3.95*(x-x**2) #the end of recursion，also is the first time to cacalute the result
    else:
        return result1(result1(x,1),n-1) # then take the value from last caculation into the next caculation
print('the result(.9,100) of function f(x)=3.95*（x-x**2）is %f' %result1(.9,100))
#the result1 is  0.3078187619897856

def result2(x,n):
    '''
    the function, result1, caculates the function f(x)=3.95*x*(1-x）through n times recursion
    
    parameters:
    x- a number in [0,1] as input
    n- the times of recursion 
    '''
    if n==1:
        return 3.95*x*(1-x) #the end of recursion，also is the first time to cacalute the result
    else:
        return result2(result2(x,1),n-1) # then take the value from last caculation into the next caculation
print('the result(.9,100) of function f(x)=3.95*x*(1-x) is %f' %result2(.9,100)) 
#the result2 is 0.9230225584410336

def result3(x,n):
    '''
    the function, result1, caculates the function f(x)=3.95*x-3.95*(x**2) through n times recursion
    
    parameters:
    x- a number in [0,1] as input
    n- the times of recursion 
    '''
    if n==1:
        return 3.95*x-3.95*(x**2) #the end of recursion，also is the first time to cacalute the result
    else:
        return result3(result3(x,1),n-1) # then take the value from last caculation into the next caculation
print('the result(.9,100) of function f(x)=3.95*x-3.95*(x**2) is %f'%result3(.9,100)) 
# the result3 is 0.28783086903250865
'''
the results of three functions are distinct, because there is a limit of decimal places. 
The default of decimal is 16 places. Therefore, during the 100 times iteration, the value has changed a lot.
Through the different functions aftering some times, every time the inputs of 
three functions are different. So the final results are distinct
'''