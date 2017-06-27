import time
import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
from pandas import ExcelWriter
import re
import os
import string


s = raw_input('Input the file location ->')
s2 = raw_input('Input the file name ->')
s3 = raw_input('Input the save file name ->')

start_time = time.time()#For the main file path, one needs to make sure they are forward slashes
s = string.replace(s, "\\", '/')

# Combining the main folder location and the xlsx file that has the list of ciks
main_location = s + '/' + s2 # Combining the temporary csv files for the different results with the folder location
result_company_info = s + '/result_company_info.csv'
result_filing = s + '/result_filing.csv'
result_wrong = s + '/result_wrong.csv'
results = s + '/' + s3



#Function for saving exsisting and non exsisting files
def savingout(save,dataframe):	
  if not os.path.isfile(save):		
    dataframe.to_csv(save, index=False)	
  else: 		
    dataframe.to_csv(save,mode = 'a',header=False, index=False)
    
    
#Function for looking through lines of html, fininding the matching regular expression, and then returing the matching line
def filterPick(lines, regex):    
  matches = map(re.compile(regex).search, lines)    
  return [m.group(1) for m in matches if m]

	#Pandas reading in the main list of firmnames
in_file = pd.read_excel(main_location)
firmname = in_file['firmname'].tolist()
#Empty dataframes where different reuslts will be stored
wrong_df = pd.DataFrame()
results_df2 = pd.DataFrame()
results2_df = pd.DataFrame()
# Loop keeps track of how many 500 iterations have passed# Time2 keeps track of how many iterations have happenned
loop = 1
time2 = 0
with requests.Session() as s:    
  s.get('https://www.sec.gov/')
  
for i in firmname
    time2=time2+1
    header="https://www.sec.gov/cgi-bin/browse-edgar?company="
    footer="&owner=exclude&action=getcompany"
    ur1= header + str(i) + footer
    r=s.get(ur1)
    soup=bs(r.content,'html.parser')
    no_firmname=soup.find(text=re.compile("No matching companies"))
    if no_firmname == u'No matching companies.':
          wrong = no_firmname.encode('ascii','ignore')
          columns={'Wrong':wrong,'Firmname':i}
          df=pd.DataFrame(columns,index=[0])
          wrong_df=wrong_df.append(df)
          print "\n Ooops there isn't %s" %(i)
          progress = round(float(time2)/len(firmname)*100)
          print "\n %d Percent Done" %(progress)
          if time2>=500 *loop:
              print "Saving Results"
              loop=1+loop
              savingout(result_company_info,result2_df)
              savingout(result_filing, results_df2)
              savingout(result_wrong, wrong)
  
    
    
    
    
    
    
    
    



  
  
  
  
  
  
  
  
  
  
  
