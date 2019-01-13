#import files from the web address
#! this sign runs the command interface supporting curl
#curl enables curl that can download files
#https://raw.githubusercontent.com/..... is the address for the data file to import
# -o tells curl write data to a file
#poem1.txt name curl will give the file
#Opening a Local File in read mode
#poem_file = open('poem1.txt', 'r') 
#Read mode 'r'
#MODE	Description
#'r'	read only mode
#'w'	write - overwrites file with same name
#'r+'	read and write mode
#'a'	opens for appending to end of file
#................................................................
# first let open the file
open_file=open('mine.txt','r')
print(open_file)#It gives the detail of file.

# Now let read the file
file_content=open_file.read()
print(file_content)

#Read a number of Characters
open_file=open('mine.txt','r')
specified_characters=open_file.read(35)
print(specified_characters)

#Read with string methods
open_file=open('mine.txt','r')
specified_characters=open_file.read(35).upper()
print(specified_characters)

open_file=open('mine.txt','r')
specified_characters=open_file.read(35).title()
print(specified_characters)

open_file=open('mine.txt','r')
specified_characters=open_file.read(35).lower()
print(specified_characters)

open_file=open('mine.txt','r')
specified_characters=open_file.read(35).upper()
print(specified_characters.isalpha())

open_file=open('mine.txt','r')
specified_characters=open_file.read(35).upper()
print(specified_characters[6:34])

#Readlines() method we can use .readlines to read an entire text file as a list.

open_file=open('mine.txt','r')
specified_characters=open_file.readlines()
print(specified_characters)
for line in specified_characters:
     print(line)
#Readlines() list returns remove newline from the list
open_file=open('mine.txt','r')
specified_characters=open_file.readlines()
print(specified_characters)
count=0
for line in specified_characters:
     specified_characters=line[:-1]
     count=count+1
print(specified_characters)
for line in specified_characters:
     print(line)
#Use close() method to free resources as .read() method consume memory or take space in memory that will remain same if you do not close it
open_file.close()
#this is different from previous method readlines() as it is readline()
#readline method read one line at a time and return a string
open_file=open('mine.txt','r')
line1=open_file.readline()
line2=open_file.readline()
line3=open_file.readline()
print(line1+line2+line3)
print(open_file.readline())
open_it=open_file.readline()
while open_it:
      print(open_it[:-1].upper())
      open_it=open_file.readline()
#readline() with strip() method
#it will by default remove all space
#use strip() method with arguments to remove any character in the paragraph
open_file=open('mine.txt','r')
open_it=open_file.readline().strip('a')
print("Strip method................................................................")
while open_it:
      print(open_it)
      open_it=open_file.readline().strip('a')
schools = open("check.txt", "r")  
name = schools.readline().strip('*\n')

while name:
    if name.startswith("M"):
        print(name)
    else:
        pass
    name = schools.readline().strip('*\n')

