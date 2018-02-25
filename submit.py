#Run this script at the end when you are ready to submit your homework to the autograder.

import hw_parsing  # imports your hw_parsing module
import requests

submissionFile=open('hw_parsing.py','r')
postData=hw_parsing.yourSubmission()


with open('token','a+') as tokenFile:
	token=tokenFile.read();

if len(token)<6:
	with open('token','w') as tokenFile:
		tokenResponse=requests.post("https://script.google.com/macros/s/AKfycbxKmFUGdc3iQtn4s_Hng1aOzpuY7JU3Cyo9upIMGk_2V9BJO1U/exec",data={'requestingToken':1,'email':postData["email"]});
		token=tokenResponse.text;
		tokenFile.write(token)

postData["token"]=token
postData["submission"]=submissionFile.read()
subResponse=requests.post("https://script.google.com/macros/s/AKfycbxKmFUGdc3iQtn4s_Hng1aOzpuY7JU3Cyo9upIMGk_2V9BJO1U/exec",data=postData)
responseFile=open('submissionResponse.txt','wb')
responseFile.write(subResponse.text.encode('utf8'))
print(subResponse.text)
