# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 14:43:12 2016

@author: Jally
"""
#Overall Comment: Very good methods and calculation! There are certain ways to improve the efficiency of the code, if you
#interest, you can find them. I have use 'Comment' in front of my comment, you can have a look and if any misunderstanding 
#happened, please let me know. One more suggestion for you, can you refer to the example format that professor has shown 
#in the lesson to keep the same format as others so that it is easy to read. Excellent Job Anyway!
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  8 23:48:11 2016
@author: Jally
"""

def max(a,b):
    '''
  1. This function, max(a,b),takes two numbers as arguments and returns the largest of them
  
  Parameters:
  a,b - two numbers been taken
  
  returns:
  a number who is bigger between a and b
    '''
    if a>=b:  #compare a with b, if a is not smaller than b then return a
        return a 
    else:
        return b# if a is smaller than b, return b
max(3,4)
        

def max_of_three(a,b,c):
    '''
    2.This function,max_of_three(a,b,c),takes three numbers as arguments and returns the largest of them
    
    Parameters:    
    a,b,c- three numbers been taken
    
    returns:
    a number who is bigger among a b c
    '''
    if a>=b:
        t=a  
    else:
        t=b  #compare a and b, then give maximum of them to t
    if t>=c:
        return t
    else:
        return c #compare t and c,then return the maximum of them
max_of_three(1,2,3)        



def length(list):
    '''
    3.This function,length(list), computes the length of a given list or string
    
    Parameters:
    list- a arbitrary list or string
    
    returns:
    the length of the list
    '''
    a=0 #create a new variable whose initial value is 0
    for num in list: #loop every element in list
        a=a+1 #count the number of list
    return a
length(["hello",2,"cute"])
    

def vowel(a):
    '''
     4.This function,vowel(a), takes a character and returns True if it is a 
     vowel, False otherwise.
     
     Parameters:
     a- an alphebatic character been taken
     
     returns:
     True if a is a vowel, False otherwise
    '''
    vow='aeiou' #create a string contains all vowels
    if a in vow: 
        return True # if a is a charater in vowels return True
    else:
        return False # otherwise return False
vowel('a')




def translate(text):
    '''
     5.This function, tranlate(text), translate a text into "rövarspråket" (Swedish for "robber's language"). 
     That is, double every consonant and place an occurrence of "o"in between
     
     Parameters:
     text- a text or string been taken.
     
     returns:
     a new text or string whose consonant is by consonant-o-consonant
    '''
    text=text.replace(' ','') # cancel the space between two words
    az=''.join(map(chr,range(97,123)))# create a string from a to z
    con='bcdfghjklmnpqrstvwxyz'#create a string contains all consonants
    for num in az: # loop from a to z
        if num in con: #determine whether a letter is consonant
            text=text.replace(num,'%so%s'%(num,num)) #replace every consonant num with num'o'num          
        else:
            continue # if it is not consonant, continue to next loop
    return text
translate('you are so cute')
    

def sum(list):
    '''
     6.This function, sum(list), sums (respectively) all the numbers in a list of numbers
     
     Parameters:
     list- a list of numbers
     
     returns:
     the sum of the list of numbers
    '''
    sum=0 # initate sum as 0
    for num in list:
        sum=sum+num # add each number to sum
    return sum #return the sum
sum([1,2,3,4,5])
    

def multiply(list):
    '''
     6.This function, multiply(list), multiplies (respectively) all the numbers in a list of numbers
     
     Parameters:
     list- a list of numbers
     
     returns:
     the multiply of the list of numbers
    '''
    mu=1  #initate sum
    for num in list:
        mu=mu*num #multiply all the numbers one by one
    return mu
multiply([1,2,3,4])

    

def reverse(string):
    '''
     7.This function, reverse(string), computes the reversal of a string but no space
     
     Parameters:
     string- is a string been taken
     
     returns:
     a new string which is reverse of new string and no space
    '''
    string=string.replace(' ','')#cancel the whitespace
    stri='' #initate an new empty string:stri
    for i in range(1, len(string)+1): #loop from 1 to the length of string
        stri=stri+string[-i] #index evey charater from end to beginnig then create the stirng which is reverse of original one    
    return stri
reverse('you are so cute')


def is_palindrome(word):
    '''
    8.This function, is_palindrome, define a function that recognizes palindromes
    
    Parameters:
    word- a word been taken 
    
    returns:
    True if the word is palindrome, False otherwise
    '''
    for i in range(0,len(word)): #loop from 0 to the length of word
        if word[i]==word[-(i+1)]: #compare the letters of word in symmetric position, if they are same, compare the next
            continue
        else:
            return False #if letters in symmetric position are not same, return false
            break
    return True # compare all the letters in symmetric position and each pair is same, so we return true
is_palindrome('radar')
 
       
        
def is_member(x,a):
    '''
    9.This function, is_member(x,a), takes a value (i.e. a number, string, etc) 
    x and a list of values a, and returns True if xis a member of a,False otherwise.
    
    Parameters:
    x- a value(i.e. a number, string, etc)
    a- a list of values
    
    returns:
    True if x is a member of a, False otherwise
    '''
    for i in range(0,len(a)):#loop from 0 to the length of list
        if x==a[i]:#iterate every value of a to see if one of them is equal to x
            return True
        else:
            continue
    return False # after a loop, none is equal to x,return false
is_member('cute',["hello",'cute',2]) 
     
     

def overlapping(list1,list2):
    '''
     10.This function, overlapping(list1,list2), takes two lists and returns 
     True if they have at least one member in common, False otherwise.
     
     Parameters:
     list1, list2 - two list been input
     
     returns:
     True if list1 and list2 have overlap, False otherwise
    '''
    for i in range(0,len(list1)): #Comment: This is equal to range(len(list1))
        for j in range(0,len(list2)):
            if list1[i]==list2[j]: # two nested for-loops to compare each value between list1 and list2
                return True # as long as one pair is same,means they have overlap and return true
            else:
                continue
    return False # compare all the values in list1 with list2's, no overlap,return false
overlapping(["hello",1,2],[3,4,"hello"])
#Comment: You can improve this code with in. For i in range(len(list1)): if list1[i] in list2: return True

def generate_n_chars(n,c):
    '''
     11.This function, generate_n_chars(n,c), takes an integer n and a character 
     and returns a string, n characters long, consisting only of c
     
     Parameters:
     n- an integer been taken
     c-a character been taken
     
     returns:
     a string with n characters long, consisting only of c
    '''
    z=''#create a new empty string
    for i in range(0,n):
        z=z+c #repeat n times to add character to new string
    return z #return the new string
generate_n_chars(4,'s')
    
    
def histogram(list):
    '''
     12.This function, histogram(list), takes a list of integers and prints a histogram to the screen
     
     Parameters:
     list- a list of integers been taken
     
     Returns:
     a string of a series of "*" whose number represent each number of list
    '''
    for i in range(0,len(list)):
        print('*'*list[i],end=' ') #check the values of list one by one and output ‘*’multiply value, end=' 'means no return but space after every print
histogram([3,2,5])  
      

def max_in_list(list):
    '''
     13.This function, max_in_list(list), takes a list of numbers and returns the largest one
     
     Parameters:
     list- a list of numbers been taken
     
     Returns:
     a number who is the maximum of the list of numbers
    '''
    t=list[0] #initate t as list[0]
    for i in range(1,len(list)):
        if t<=list[i]: 
            t=list[i] #compare the t with next number, if next number is bigger, then value it to t 
        else:
            continue
    return t
max_in_list([1,5,6,3])
    
    
def count_len(list):
    '''
     14.This function, count_len(list), maps a list of words into a list of 
     integers representing the lengths of the correponding words
     
     Parameters:
     list- a list of words been taken
     
     Returns:
     a list of number in which each number represents the length of the coresponding word in list
    '''
    lenth=[] # create a empty list
    for i in range(0,len(list)):
        lenth.append(len(list[i]))# count the number of every word then add them to the list lenth
    return lenth
count_len(["hello","world","cute"])    
    
        

def find_longest_word(list):
    '''
    15.This function, find_longest_word(list), takes a list of words and 
    returns the length of the longest one
    
    Parameters:
    list- a list of word been taken
    
    Returns:
    a number which represents the longest length in list
    '''
    t=len(list[0]) #initate t with the length of list[0]
    for i in range(1,len(list)):
        if t<=len(list[i]):
             t=len(list[i])# check the rest words one by one, if the length of them is bigger than t, them value it with its length
        else:
             continue
    return t
find_longest_word(["cute","hello","importance"])

    

def filter_long_words(list,n):
    '''
    16.This function, filter_long_words(list,n), takes a list of words and an 
    integer n and returns the list of words that are longer than n.
    
    Parameters:
    list- a list of words been taken
    n- a threshold of words' length
    
    Returns:
    a list of words whose length are longer than n
    '''
    new=[] #create a new empty list
    for i in range(0,len(list)):
        if len(list[i])> n:
            new.append(list[i]) #check the words of list one by one, if length of them is longer than threshold,then add them to the new list
        else:
            continue
    return new
filter_long_words(["importance","python","hello","word"],5)
        
