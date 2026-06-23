a=input("enter a string ")
result=''
for i in range (0,len(a),2):
    b=a[i]
    c=int(a[i+1])
    for j in range(c):
        result = result+b
print(result)


        