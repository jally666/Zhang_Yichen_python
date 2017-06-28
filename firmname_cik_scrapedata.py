
import time
import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
from pandas import ExcelWriter
import re
import os
import string

#User enters the file location information
s = raw_input('Input the file location ->')
s2 = raw_input('Input the file name ->')
s3 = raw_input('Input the save file name ->')


#Start a timer for how long it takes to run the code
start_time = time.time()
#For the main file path, one needs to make sure they are forward slashes
s = string.replace(s, "\\", '/')

# Combining the main folder location and the xlsx file that has the list of ciks
main_location = s + '/' + s2
# Combining the temporary csv files for the different results with the folder location
result_company_info = s + '/result_company_info.csv'
result_filing = s + '/result_filing.csv'
result_wrong = s + '/result_wrong.csv'
results = s + '/' + s3


#Pandas reading in the main list of firmnames
in_file = pd.read_excel(main_location)
issuer = in_file['issuer'].tolist()
issuer = [str(issuer[x]) for x in range(len(issuer))]  # transfer from unicode to ascii

#Empty dataframes where different reuslts will be stored
wrong_df = pd.DataFrame()
results_df = pd.DataFrame()

# Loop keeps track of how many 500 iterations have passed
# Time2 keeps track of how many iterations have happenned

loop = 1
time2 = 0
with requests.Session() as s:
    s.get('https://www.sec.gov/')
	
#Start of the loop, i is the issuer for each row in the 'issuer' list
for i in issuer:
	time2 = time2 + 1
	start=0
	while True: 
		CIK=[]
		COMPANY=[]
		#Main sec header which never changes
		header = 'https://www.sec.gov/cgi-bin/browse-edgar?company='
		middle = '&owner=include&match=contains&start='
		footer ='&count=40&hidefilings=0'
		#create url to parse through sec header + issuer + fotter
		url = header + str(i) + middle + str(start)+ footer
		#r here is the url that we quieried
		r = s.get(url)
		#soup is an html tree where we took the content of r and put it in the html tree. IF you look up a given link, it should be the same html tree that you would see on that page
		soup = bs(r.content,'html.parser')
		#First think is to check if the issuer is a real company, thus we search the soup for the phase
		no_issuer =soup.find(text=re.compile("No matching companies"))
		if no_issuer==u'No matching companies.':
			break
		else:
			matches = soup.find(text=re.compile("Companies with names matching"))
			if pd.isnull(matches):
				try:
					r_cik=soup.find("div",{"id":"contentDiv"}).find("span",{"class":"companyName"}).find('a').string.strip().encode('ascii','ignore')
					r_company=soup.find("div",{"id":"contentDiv"}).find("span",{"class":"companyName"}).contents[0].encode('ascii','ignore')
					
					CIK.append(r_cik)
					COMPANY.append(r_company)
				except:
					pass
			else:
				try:
					table = soup.find_all('table')
					rows=table[0].find_all('tr')
					for tr in rows[1:]:
						cols=tr.find_all('td')
						r_cik=cols[0].find('a').string.strip().encode('ascii','ignore')
						r_company=cols[1].contents[0].string.strip().encode('ascii','ignore')
						CIK.append(r_cik)
						COMPANY.append(r_company)
					
				except:
					pass
					
			columns={'CIK':CIK,'COMPANY':COMPANY,'issuer':i}
			df=pd.DataFrame(columns)
			results_df=results_df.append(df)
			start = start + 40
			
writer = ExcelWriter(results)
results_df.to_excel(writer,'Possible Companies',index=False)
writer.save()
		
			
		
		
		
		
		
		
		
	
	
	


	
