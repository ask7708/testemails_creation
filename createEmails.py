
"""Prompts users for inputs may have to change in different version of python"""
fileName = raw_input("Enter file name: ")
emailUsed = raw_input("Enter email to be used(ex. sampletest NOT sampletest@gmail.com): ")
domainName = raw_input("Enter domain name to be used(ex. gmail, yahoo, aol, etc.): ")

"""Calculate the number of dots to insert"""
numberOfDots = len(emailUsed)

file = open(fileName+".txt", "w")

"""Takes string name writes to the file each email"""
for i in range(1, numberOfDots):

    addEmail = emailUsed[:i]+"."+emailUsed[i:]

    for j in range(i+2, numberOfDots*2-(i+1), 2):


        addEmail = (addEmail[:j]+"."+addEmail[j:])
        file.write(addEmail+"@"+domainName+".com"+"\n")
        print (addEmail)

file.close()

