import re
import numpy
import string

file_location="P:\PCAOB Staff\Interns\zhangy1\\test\\test.txt"
file_location = string.replace(file_location, "\\", '/')
file=open(file_location,'r')

sum=0
for line in file:
	line=line.strip()
	numbers=re.findall("[0-9]+",line)
	for i in numbers:
		sum=sum + int(i)
		

		
		
		
		
		
print sum
	
