# Create a file with the append flag. If the file does not exist, it will be created. 
# Otherwise, new data will be added to the existing file without removing the previous content

f = open("test.txt", 'a')
f.write("New Line\n")
f.close()
