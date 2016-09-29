# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 19:30:54 2016

@author: Jally
"""

import pandas as pd
import matplotlib.pyplot as plt
from pandas import Series
import numpy
import math

def histogram_outlier(data,tit):
    '''
    the function, histogram_outlier() is to test for severe outliers that could 
    hide the true shape of the distribution, separate that part of the data, 
    and plot histograms for both segments of the distribution.
    
    Parameter:
    data: a series of data
    tit: the title of this data
    
    output:
    no return, but histograms of segments of data and one box plot of whole data
    '''
    # delete all the NAN data
    for i in range(len(data)):
        if math.isnan(data[i]):
            data.drop[data[i]] 
    
    # separate the outliers
    stati = data.describe()# obtain the simple location statistics
    upper = stati.ix[6,0]+(stati.ix[6,0]-stati.ix[4,0])*1.5#caculate outliers up threshold
    lower = stati.ix[4,0]-(stati.ix[6,0]-stati.ix[4,0])*1.5# caculate outliers down threshold
    outlierup=[] #initialize a list to store upper outliers 
    outlierdown=[] #initialize a list to store lower outliers 
    norm=[] #initialize a list to store main part of data 
    up=1
    low=1# initalize a key to determine if there is outliers
    for i in range(0,len(data)):
        if float(data[i])> upper:
            outlierup.append(float(data[i]))  # if data are beyond the upper threshold, store them in outlierup      
        elif float(data[i])<lower:
            outlierdown.append(float(data[i]))# if data are lower than the lower threshold, store them in outlierdown
        else:        
            norm.append(float(data[i]))# if data are between the two thresholds, store them in norm
    outlierup=Series(outlierup) 
    norm=Series(norm)
    outlierdown=Series(outlierdown)# transfer these three lists into pandas' series  
    if len(outlierup)==0:
        print('there is no upper outliers for %s' %tit) # if outlierup is empty, there is no upper outliers and value up with 0
        up=0
    if len(outlierdown)==0:
        print('there is no lower outliers for %s' %tit)# if outlierdown is empty, there is no lower outliers and value low with 0
        low=0
    
    # calculate the optimal bin width and draw historgram
    stat=norm.describe() # obtain the simple location statistics of main part data
    iqr=stat.ix[6,0]-stat.ix[4,0]# caculate the IQR
    h=2*iqr/(len(norm)**(1/3))#use freedom-diaconis rule to caculate the optimal bin width

    if h==0:
        bin=int(2*(len(norm)**(1/3)))+1#if h=0 means it cannot draw histogram with freedom-diaconis, so we need to change to rice rule 
    else:
        bin=round((max(norm)-min(norm))/h)# caculate the optimal bins number

    plt.figure()
    plt.hist(norm, bins=bin) #draw the histogram with optimal bins number
    plt.title("Main Part Histogram of %s" %tit)
    plt.xlabel("Value")
    plt.ylabel("Frequency")
    plt.show()
   
    # if there are upper outlier's data, draw upper outlier histogram
    if up==1:
        statup=outlierup.describe()# obtain the simple location statistics of upper outliers
        iqr=statup.ix[6,0]-statup.ix[4,0] #caculate the IQR
        h=2*iqr/(len(outlierup)**(1/3))#use freedom-diaconis rule to caculate the optimal bin width
        
        if h==0:
            bin=int(2*(len(outlierup)**(1/3)))+1#if h=0 means it cannot draw histogram with freedom-diaconis, so we need to change to rice rule        
        else:
            bin=round((max(outlierup)-min(outlierup))/h)# caculate the optimal bins number
        
        plt.figure()
        plt.hist(outlierup, bins=bin)#draw the histogram with optimal bins numbe
        plt.title("Upper Outlier Histogram of %s" %tit)
        plt.xlabel("Value")
        plt.ylabel("Frequency")
        plt.show()
    
    # if there are lower outlier's data, draw lower outlier histogram
    if low==1: 
        statdown=outlierdown.describe()# obtain the simple location statistics of lower outliers
        iqr=statdown.ix[6,0]-statdown.ix[4,0]#caculate the IQR
        h=2*iqr/(len(outlierdown)**(1/3))#use freedom-diaconis rule to caculate the optimal bin width

        if h==0:#if h=0 means it cannot draw histogram with freedom-diaconis rule
            bin=int(2*(len(outlierdown)**(1/3)))+1
        else:
            bin=int((max(outlierdown)-min(outlierdown))/h+1)# caculate the optimal bins number
        
        plt.figure()
        plt.hist(outlierdown, bins=bin)#draw the histogram with optimal bins number
        plt.title("Lower Outlier Histogram of %s" %tit)
        plt.xlabel("Value")
        plt.ylabel("Frequency")
        plt.show()
      
    #draw box plot
    plt.figure()
    plt.boxplot(data)# draw the box plot of whole data
    plt.title("%s box plot" %tit)
    plt.show()
    
def main1():
    '''
    this main1() function is to read the diamond pricing dataset and then draw 
    histograms and box plot
    '''
    data_index='https://vincentarelbundock.github.io/Rdatasets/csv/Ecdat/Diamond.csv'
    diamond=pd.read_csv(data_index)# read the data set from website
    title=diamond.head(0)# value the 'title' with the header of 'diamond' data set
    
    carat=diamond.ix[:,1] # value the 'carat' with diamond's carat data
    price=diamond.ix[:,5] # value the 'price' with diamond's price data
    
  
    histogram_outlier(carat,title.columns[1])#draw the histograms about carat data set
    histogram_outlier(price,title.columns[5])#draw the histograms about price data set
    
def main2():
    '''
    this main1() function is to read the Abalone dataset and then draw histograms and box plot
    '''
    data_index='http://archive.ics.uci.edu/ml/machine-learning-databases/abalone/abalone.data'
    abalone=pd.read_csv(data_index,header=None,names=['sex','length','diameter','height','whole weight',\
    'shucked weight','viscera weight','shell weight','rings'])# read the Abalone dataset and then add the column names to them
    title=abalone.head(0)# value the 'title' with the header of 'abalone' data set
    
    for i in range(0,len(title.columns)): #read the abalone dataset column by column
        if type(abalone.ix[1,i])==numpy.float64 or type(abalone.ix[1,i])==numpy.int64: # if it is number type, draw the histograms of this series
            histogram_outlier(abalone.ix[:,i],title.columns[i])
        
def main3():
    '''
    this main1() function is to read the Census-Income (KDD) Data set and then draw histograms and box plot
    '''
    kdd=pd.read_csv('/Users/Jally/Github/Zhang_Yichen_python/census-income.data ',\
    header=None,names=['age','class of worker','industry code','occupation code',\
    'education','adjusted gross income','wage per hour','enrolled in edu inst last wk','marital status',\
    'major industry code','major occupation code','mace','hispanic origin',\
    'sex','member of a labor union','reason for unemployment','full or part time employment stat',\
    'capital gains','capital losses','divdends from stocks','federal income tax liability',\
    'tax filer status','region of previous residence','state of previous residence',\
    'detailed household and family stat','detailed household summary in household',\
    'instance weight','migration code-change in msa','migration code-change in reg',\
    'migration code-move within reg','live in this house 1 year ago','migration prev res in sunbelt',\
    'num persons worked for employer','family members under 18','total person earnings',\
    'country of birth mother','country of birth self',\
    'citizenship','total person income','own business or self employed','taxable income amount',\
    'veterans benefits','weeks worked in year'])
    title=kdd.head(0)
    
    for i in range(0,len(title.columns)):
        if type(kdd.ix[1,i])==numpy.float64 or type(kdd.ix[1,i])==numpy.int64 : # if it is number type, draw the histograms of this series
            histogram_outlier(kdd.ix[:,i],title.columns[i])
    
# check           
main1()
main2()
main3()