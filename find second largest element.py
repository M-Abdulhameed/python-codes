a=[5,2,3,6,4,4]
first=a[0]
second=0

for i in a:
    if i>first:
        second=first
        first=i
    elif i!=first:
        if i > second and second !=first:
            second = i

print(second)