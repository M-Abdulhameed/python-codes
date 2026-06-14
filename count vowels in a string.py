a=input("Enter a word:")
vowels="aeiouAEIOU"
count=0
for i in a:
    if i in vowels:
        count = count +1
 
print(f'{count} vowels in {a}')


    
