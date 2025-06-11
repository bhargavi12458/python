f=open("c:\\users\\MICLAB\\desktop\\demo.txt",'r')
print("the file pointer is at byte:",f.tell())
content=f.read();
print("after reading ,the file pointer is at:",f.tell())
