# Files are all local to machine. This must be ammended.

# pip install PyPDF2

import PyPDF2
 
#create file object variable
#opening method will be rb
pdffileobj=open('test_cv.pdf','rb')
 
#create reader variable that will read the pdffileobj
pdfreader=PyPDF2.PdfReader(pdffileobj)
 
#This will store the number of pages of this pdf file
x=len(pdfreader.pages)
print("NUMBER OF PAGES " + str(x))
 
#create a variable that will select the selected number of pages
pageobj=pdfreader.pages[x - 1]
 
#(x+1) because python indentation starts with 0.
#create text variable which will store all text datafrom pdf file
text=pageobj.extract_text()
 
#save the extracted data from pdf to a txt file
#we will use file handling here
#dont forget to put r before you put the file path
#go to the file location copy the path by right clicking on the file
#click properties and copy the location path and paste it here.
#put "\\your_txtfilename"
file1=open(r"C:\Users\ggsra\Projects\hack_anthropic\test_cv.txt","a")
file1.writelines(text)