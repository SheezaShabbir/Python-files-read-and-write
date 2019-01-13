new_file=open("writing.txt","w")
#print(new_file)
new_file.write("This is my new file and checking it while it is right or not.")
open_file=open("writing.txt","r")
#print(open_file.read())
#seek(0) to move the pointer to the begining of the file so the previous and next change both could be read
#As we add new text the pointer has moved to the end of line so if we read it there will be nothing
#So to move pointer to the start we use this method
new_file=open("writing.txt","w+")
new_text=new_file.read()
print(new_text)
new_file.write("..............This is new line .......")
new_file.seek(0)
new_text=new_file.read()
print(new_text)
new_file.seek(4)
new_text=new_file.read()
print(new_text)
new_file.seek(0)
new_text=new_file.read()
print(new_text[4:0])

#file.seek(offset, whence)
#whence mode	description
#0	points to the beginning of the file
#1	points to the current location
#2	points to the end of the file & offset is always 0
new_file.seek(0,2)
new_file.write("**********************************")
new_file.seek(0,0)
checking=new_file.read()
print(checking)
new_file.seek(0,0)
new_file.write("**********************************OOOOOOOOOOOOOOOOOOOOOOOOOOO")
new_file.seek(0,0)
checking=new_file.read()
print(checking)

#open a file in a writable mode
#open a file in a writing mode, with: 'w', 'w+', 'r+', 'a', 'a+'
#MODE	Description
#'r'	read only mode
#'w'	write - overwrites file with same name
#'w+'	write and read mode - overwrites file with same name
#'r+'	read and write mode (no overwrite)
#'a'	opens for appending to end of file (no overwrite)
#'a+'	opens for appending to end of file (no overwrite) plus read
#warning: 'w' and 'w+' modes will create a new file or overwrite existing files (deleting all file contents)
def logger(log):
    log_entry = input("enter log item (enter to quit): ")
    count = 0

    while log_entry:
        count += 1
        log.write(str(count) + ": " + log_entry + "\n")
        log_entry = input("enter log item (enter to quit): ")
        
    return count
    
# [ ] review and run example: makes a blank file  (initialize/reset)

log_file = open('log_file.txt', 'w+')
log_file.close()
# [ ] review and run example - opens the log_file before passing to logger() function call, below
# allows for calls below to run several times appending to the end of log_file

log_file = open('log_file.txt', 'a+')
# [ ] review and run example - calls the above logger() function
# what happens running the cell above (a+) again before running this cell again? 
# what happens if log_file.seek(0) is run before an append?

logger(log_file)    

log_file.seek(0)
log_text = log_file.read()

print()
print(log_text)
log_file.close()

# [ ] review and run example - create a file with initial count of 0
count_file = open("count_file.txt", "w+")

count_file.write("Count is: 0")
count_file.seek(0)
print(count_file.readline().strip())

count_file.close()
# [ ] review and run example - can rerun this cell
count_file = open("count_file.txt", "r+")

count_file.seek(0)
count_line = count_file.readline().strip()
print("BEFORE\n" + count_line)

# get the int character(s) after the colon and space, cast and increment
count = int(count_line[10:])+1

# write the incremented value to the file - overwrite before value
count_file.seek(10)
count_file.write(str(count))

count_file.seek(0)
print("\nAFTER\n" + count_file.readline().strip())

count_file.close()
# [ ]  review funtion code for inc_count() funtion that reads file and updates the count
# the file always has 1 line that is The count is: N, where N is an integer
def inc_count(cnt_file):
    cnt_file.seek(0,0)
    cnt_line = cnt_file.readline().strip()
    cnt = int(cnt_line[10:])+1
    cnt_file.seek(10,0)
    cnt_file.write(str(cnt))
    return cnt
# [ ] review and run example with call to function: inc_count() - **Run cell multiple times**
# opens file/prints initial value
count_file = open("count_file.txt", "r+")

count_file.seek(0)
count_line = count_file.readline().strip()
print("BEFORE\n" + count_line)

# call inc_count() to increase the count 5 times
for i in range(5):
    count = inc_count(count_file)
    count_file.seek(0)
    print("\nAFTER inc_count() call", i+1, "\n" + count_file.readline().strip())

count_file.close()
