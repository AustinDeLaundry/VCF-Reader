#Made by Austin DeLauney 
#This program has been tested on Android VCF cards, which are version 2.1 of the VCF file format
#More information on the formats @ http://en.wikipedia.org/wiki/VCard

print("Hello!, This program translates you .VCF file into a readable, and printable file!")
print("Please give me the path of your file so I can open it and give you something pretty!")
vcf_file = input("File path: ")
new_file_save = input("Save path: ") + "/Contacts.txt"

f = open(vcf_file, 'r')
s = open(new_file_save, 'a')
f_contents = f.readlines()

contacts = []
new_contact = ""

for line in f_contents:
	line = line.strip() #Strips the line
	
	if(line[:3] == "FN:"): #Get's name and adds it
		new_contact += ("Name: " + line[3:] + "\n")
	elif(line[:4] == "ORG:"): #Adds Organization
		new_contact += ("Organization: " + line[4:] + "\n")
		#print(new_contact)
	elif(line[:6] == "TITLE:"): #Adds title
		new_contact += ("Title: " + line[6:] + "\n")
	#Adds phone numbers
	elif(line[:9] == "TEL;CELL:"):
		#print("HELLO!")
		new_contact += ("Cell: " + line[9:] + "\n")
	elif(line[:9] == "TEL;HOME:"):
		new_contact += ("Home: " + line[9:] + "\n")
	elif(line[:9] == "TEL;WORK:"):
		new_contact += ("Work: " + line[9:] + "\n")
	#Adds addresses
	elif(line[:9] == "ADR;HOME:"):
		new_contact += ("Home address: " + line[9:].replace(';', '').strip() + "\n")
	elif(line[:9] == "ADR;WORK"):
		new_contact += ("Work address: " + line[9:].replace(';', '').strip() + "\n")
	#Adds emails
	elif(line[:12] == "EMAIL;HOME:"):
		new_contact += ("Personal email: " + line[12:] + "\n")
	elif(line[:12] == "EMAIL;WORK:"):
		new_contact += "Work email: " + line[12:] + "\n"
	#Ends the contact information, appends it to list and creates a new contact
	elif(line == "END:VCARD"):
		contacts.append(new_contact + "\n")
		new_contact = ""

f.close()

#Prints contact information
for contact in contacts:
	s.write(contact)

s.close()

