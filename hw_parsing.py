# Homework Parsing Template Code
#
# This file will begin by creating a string called userGuideText using the pdfminer library.
# This string userGuideText will be saved into a separate file userGuideText.txt to speed up your subsequent testing.
#
# Your assignment is to programmatically analyze the userGuideText string using regular expressions to find all the unique SCPI Query Commands.
# Once you find all the query commands, you should pass them as a single long queryString to pass to our virtual E3631A system.
# queryString should be a single string that has all the queries concatenated (joined) together with the appropriate terminators.
#
# When you have a final answer, you can submit your assignment to the autograder by running the submit.py script

##################################################################
### HELPER CODE TO IMPORT PDFMINER LIBRARY AND PRODUCE TEXT STRING
##################################################################
from pdf import pdfminerToText
import re
import requests

try:
	with open('userGuideText.txt','r', encoding='utf-8') as f1: userGuideText=f1.read()
except:
	userGuideText=pdfminerToText.convert("E3631-90002.pdf")
	with open('userGuideText.txt','w', encoding='utf-8') as f2: f2.write(userGuideText)

##################################################################
### YOUR CODE TO FIND & CONCATENATE ALL SCPI QUERIES GOES HERE
##################################################################
email= "jason_webster@brown.edu"

#Grabs all lines that start with some type of command (including nodes)
results = re.findall('^\**[A-Z]{3,}[A-Za-z\[\]:]*[?]', userGuideText, re.MULTILINE)
print(len(results))
count = 0;
queryString = ''
for i in range(len(results)):
	#This part gets all full queries that come immediately after their set commands
	if (results[i].endswith('?')):
		count += 1
		command = results[i]
		#remove optional nodes
		command = re.sub('\[:[A-Za-z]*\]', '', command)
		#remove parameters
		command = re.sub('<[A-Za-z0-9]+>', '', command)
		print('comm: ' + command)
		queryString = queryString + command + '\n'
	#This part gets queries that are broken up into multiple parts
print(count)

#queryString='???' # UPDATE THIS LINE TO INCLUDE YOUR CONCATENATE SERIES OF QUERY COMMANDS AS ONE LONG STRING
##################################################################
### HELPER CODE TO SAVE YOUR ANSWER and THE RESPONSE YOU RECEIVE
##################################################################
with open('queryString.txt','w') as f3:
    test=f3.write(queryString)

response=requests.get('https://script.google.com/macros/s/AKfycbxKmFUGdc3iQtn4s_Hng1aOzpuY7JU3Cyo9upIMGk_2V9BJO1U/exec',params={'queryString':queryString}).text
with open('response.txt','w') as f4:
    test=f4.write(response)
print(response)
##################################################################
### DO NOT CHANGE THE FOLLOWING - Used in submission process
##################################################################
def yourSubmission():
	return {'email':email,'hw':'parsing','queryString':queryString,'response':response}

	"""		if ((results[i][0] == '[') | (results[i][0] == ':')):
				j = 0
				#go back and get the parent
				while ((results[i-j][0] == '[') | (results[i-j][0] == '\n') | (results[i-j][0] == ':')):
					j = j + 1
				command = results[i-j][0:len(results[i-j])-1] + results[i]
			else:
				command = results[i] """
