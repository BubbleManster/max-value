from datetime import datetime
start=datetime.now()

f=open("list.txt")
list=f.read()
list=list.split()
max_value=eval(list[0])
for i in list:
    j=eval(i)
    if j > max_value:
        max_value=j
print(max_value)
f.close()

print("Runtime is: ",datetime.now()-start)
