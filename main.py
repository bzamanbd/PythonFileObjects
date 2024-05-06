# f = open('myNewFile.txt', 'w') 
# f.write("I am learning python \n")
# f.write("I am learning fast api")
# f.close()

f = open('myNewFile.txt', 'r')
line1 = f.readline()
line2 = f.readline()
f.close()

print(line1,line2)

import os
print(os.getcwd())