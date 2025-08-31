# Program to count number of Lines in this File 
# Opening a File
file = open('coding.txt', 'r')
Counter = 0

# Reading from File
Content = file.read()
# Splitting Content into Lines and storing in a List
Colist = Content.split("\n")

for i in Colist:
    if i:
        Counter += 1

print("This is the number of lines in the file")
print(Counter)