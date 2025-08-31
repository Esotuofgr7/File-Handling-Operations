# Open the File in Read mode 
file_read = open('coding.txt')
print("File in Read Mode -")
print(file_read.read())
file_read.close()

# Open the File in Write Mode 
file_write = open('coding.txt', 'w')
# Write in the File
file_write.write("File in Write Mode....")
file_write.write("Hi! I am Penguin. I am 1 year old")
file_write.close()

# Open the File in Append Mode
file_apppend = open('coding.txt', 'a')
# Append in the File
file_apppend.write("\n File in Append Mode")
file_apppend.write("Hi! I am Penguin. I am 1 year old")
file_apppend.close()