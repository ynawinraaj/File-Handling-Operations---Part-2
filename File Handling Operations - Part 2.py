# open file & read it's content
file=open('sample.txt','r')
print("file in read mode......")
print(file.read())
file.close()

# open file & read it's begining first 8 charecter
file_write=open('sample.txt','w')
file_write.write("file in write mode.....")
file_write.write("RAAJ")
file.close()

#append your name and age
file_appened=open('sample.txt','a')
file_appened.write("file in append mode.....")
file_appened.write("im a student of codingal")
file.close()